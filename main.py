import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import schedule
import time
from time import sleep
import pickle
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from bs4 import BeautifulSoup
import os
import numpy as np
import urllib


def grab_news():
    currentDirectory = os.getcwd() + '/'

    try:
        # Load in the model and vectoriser:
        vectoriser = pickle.load(open(currentDirectory + 'news_vectoriser_pickle', 'rb'))
        model = pickle.load(open(currentDirectory + 'news_model_pickle', 'wb'))

        # Load the JSON API key:
        JSON_API_KEY = currentDirectory + 'JSON_API_Key.json'

        # Authentication:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_API_Key_path, scope)
        gc = gspread.authorize(credentials)

        # Open the file: NewStories.
        wks = gc.open("NewStories")

        # Format the Worksheet:
        NewStories_worksheet = wks.sheet1

        zipped_list = list(zip(NewStories_worksheet.col_values(2), NewStories_worksheet.col_values(3),
                               NewStories_worksheet.col_values(4)))

        NewStories_worksheet_df = pd.DataFrame(zipped_list, columns=['title', 'urls', 'html'])
        NewStories_worksheet_df.replace('', pd.np.nan, inplace=True)
        NewStories_worksheet_df.dropna(inplace=True)

        # Strip the HTML Tags:
        def extract_text(x):
            soup = BeautifulSoup(x, 'html.parser')
            text = soup.get_text()
            return text

        NewStories_worksheet_df.loc[:, 'text'] = NewStories_worksheet_df['html'].map(extract_text)
        NewStories_worksheet_df.reset_index(drop=True, inplace=True)

        # Apply the Vectoriser: transform the matrix.
        test_matrix = vectoriser.transform(NewStories_worksheet_df['text'])

        # Predict by Passing the 'test_matrix' into the model:
        model_results = pd.DataFrame(model.predict(test_matrix), columns=['wanted'])

        # Join the Output with the Stories themselves for model evaluation:
        model_eval = pd.merge(model_results, NewStories_worksheet_df, left_index=True, right_index=True)

        # Get the top 20 rows:
        model_eval = model_eval.iloc[:20, :]

        # Create the Payload to be sent:
        news_str = ''
        for title_i, url_i in zip(model_eval[model_eval['wanted'] == 'y']['title'],
                                  model_eval[model_eval['wanted'] == 'y']['urls']):
            news_str = news_str + title_i + '\n' + url_i + '\n'

        payload = {"value1": news_str}
        IFTTT_app = 'news_event'

        # Load in the API KEY
        IFTTT_key_folderName = 'IFTTT API key'
        IFTTT_path = os.path.abspath(IFTTT_key_folderName) + '/'

        IFTTT_API_KEY = open(IFTTT_path + "IFTTT API KEY.txt", 'r')

        api_key_string = []
        for i in IFTTT_API_KEY:
            api_key_string.append(str(i))

        request_url = requests.post('https://maker.ifttt.com/trigger/' + IFTTT_app + '/with/key/' + api_key_string,
                                    data=payload)

        # Clean up the Worksheet:
        leng_NewStories_worksheet = len(NewStories_worksheet.col_values(1))
        cell_list = NewStories_worksheet.range('A1:F' + str(leng_NewStories_worksheet))

        for cell in cell_list:
            cell.value = ""

        NewStories_worksheet.update_cells(cell_list)
        print(request_url.text)

    except:
        print('Action Failed')


# Set the Script Run time:
schedule.every(480).minutes.do(grab_news)
while 1:
    schedule.run_pending()
    time.sleep(1)

