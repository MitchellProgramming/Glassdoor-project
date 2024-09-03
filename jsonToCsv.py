#This line of code converts all of the files into csv
from bs4 import BeautifulSoup
import pandas as pd
import json
import os
def jsonToCsv(fileName):
    with open(fileName) as inputfile:
        jsonDict=json.load(inputfile)['reviews']
        print(len(jsonDict))
        dataFrame=pd.json_normalize(jsonDict)[["employer.shortName","reviewDateTime","summary","ratingOverall","ratingWorkLifeBalance","ratingCultureAndValues","ratingCareerOpportunities","ratingCompensationAndBenefits","ratingSeniorLeadership","jobTitle.text","location.name","lengthOfEmployment","pros","cons","reviewId"]]
    return dataFrame
folderLocation="scrapfly-scrapers/glassdoor-scraper/fortune500json"
listOfFiles=os.listdir(folderLocation)
listOfDataFrames = []
for x in listOfFiles:
    listOfDataFrames.append(jsonToCsv(folderLocation+"/"+x))
    print(x)
concatPandas=pd.concat(listOfDataFrames)
print("Before drop duplicates",len(concatPandas))
concatPandas=concatPandas.drop_duplicates("reviewId")
print("After drop duplicates",len(concatPandas))

concatPandas.to_csv('fortuneTopTen.csv')
