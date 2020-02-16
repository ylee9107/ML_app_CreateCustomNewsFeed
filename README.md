# ML App to Create a Custom Newsfeed

## Introduction:

Reading is an excellent way to fill in any knowledge gap. It is even better if there is a way to enchance this experience whereby to quickly get a customised newsfeed tailored to the reader's interests. This project/app aims to help frequent readers such as myself to find even more to read or rather, to satisfy curiousities on certain topics. It can be seen as beneficial to have what you want to read without going through the hassle of digging for it. 

Hopefully by the end of this project, a system can be built that is able to understand a tailored taste in news and be able to send them directly to the user.

## Breakdown of the Project:
- Making a supervised training set with the Pocket App.
- Utilising the Pocket API to obtain stories.
- Making use of the Embedly API to extract story bodies.
- Basics of NLP (Natural Language Processing)
- Classifiers such as SVM (Support Vector Machines)
- IFTTT will be integrated with RSS feeds and Google Sheets.
- Setup a system for a daily personal newsletters

## Dataset:

The dataset for this project was obtained directly from websites of personal interests. The notebook also describes in detail on how to create the dataset.

## To run the ‘main.py’ file:

Open command line and navigate to the folder/directory. then type in " python grab_news” as an example. This app runs every 480 mins.

## Required Libraries:

1. Pandas
2. Numpy
3. Sklearn
4. Pickle
5. JSON
6. Requests
7. Schedule
8. Time
9. gspread
10. oauth2client.service_account
11. BeautifulSoup
12. OS
13. urllib

These files will require a Secret Key or API Key from IFTTT to run. Please ensure that the KEY ('IFTTT API KEY') is saved in a folder called 'IFTTT API key', notice the capitalised letters between the key and the folder. The entire folder should be saved in the same directory as the files. 

Or, You can copy your key into the file already included.

It should also be noted that:
- A redirect url is required: use your Twitter Account, save it into the .txt file included.
- A Pocket API key (consumer key) is required. 

## Set up IFTTT service:

IFTTT - If This Then That, is a free service that allows for connection with a huge number of services with a series of triggers and actions. Using this service requires signing up for an account at www.ifttt.com. 

## Installing Pocket Chrome Extension for this project:

Setup and example of usage:
	1	Open Chrome, and add Pocket app in the Extensions.
	2	Open any link of interest.
	3	Click on the Pocket extension icon, once red, it means the article or link have been saved.

To begin constructing the supervised dataset:
	1	As you go through your day, read your articles.
	2	Tag 'y' for interesting ones, and tag 'n' for non-interesting ones.
	3	Note: it is better to have lots (100s) of articles to make the model better.

Retreive the save stories:
	1	Go to: https://getpocket.com/developer/apps/new
	2	Click on 'Create a New App' in the top left corner of the webpage.
	3	Input the details and get the API KEY.
	4	Be sure to click on all the Permissions (allows for adding, changing and retrieving)
	5	Once done, click to submit.
	6	Click on 'My Apps' in the top left corner fo the webpage and you will see the custom applications.

## Summary:

From this project, I have gained more experience in dealing with text data from webpages or rather news articles, utilising APIs such as BoilerPipe, to extract the required information. This was also used to create a dataset for both training and testing. From these text data, I also utilised some basics of NLP such as transforming the corpus into bag-of-words, removal of stop words that brought no important content to the data, and finally, stemming and lemmatisation of the text data. The model used in this project to classify articles of interest and non-interest was SVM where the theory was also covered. This project have also improved my experience with using IFTTT integration to gather more data from the websites that consist of news articles. Lastly, the project was concluded with a python script can that be run in the background to send a personalised news feed to your email.
