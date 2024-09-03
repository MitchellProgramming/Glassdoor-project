#This line of code converts all of the files into csv
from bs4 import BeautifulSoup
import pandas as pd
import json
import os
def jsonToCsv(fileName):
    with open(fileName) as inputfile:
        jsonDict=json.load(inputfile)['reviews']
        print(len(jsonDict))
        dataFrame=pd.json_normalize(jsonDict)[["employer.shortName","reviewDateTime","summary","ratingOverall","ratingWorkLifeBalance","ratingCultureAndValues","ratingCareerOpportunities","ratingCompensationAndBenefits","ratingSeniorLeadership","ratingDiversityAndInclusion","jobTitle.text","location.name","lengthOfEmployment","pros","cons","reviewId"]]
        return dataFrame
folderLocation= "scrapfly-scrapers/glassdoor-scraper/results"
listOfFiles=os.listdir(folderLocation)
listOfDataFrames = []

sizeOfList=0
iteration=1
numwrong=0
for x in listOfFiles:
    print(folderLocation+"/"+x)
    try:
        variable=jsonToCsv(folderLocation+"/"+x)
        print(sizeOfList+len(variable))
        if sizeOfList+len(variable)<1000000:
            listOfDataFrames.append(variable)
            sizeOfList+=len(variable)
        else:
            sizeOfList=len(variable)
            concatPandas=pd.concat(listOfDataFrames)
            print("Before drop duplicates",len(concatPandas))
            concatPandas=concatPandas.drop_duplicates("reviewId")
            print("After drop duplicates",len(concatPandas))
            concatPandas.to_csv('fortuneTopTen'+str(iteration)+".csv")
            iteration+=1
            listOfDataFrames = []
            listOfDataFrames.append(variable)
    except:
        
        print("file wrong")

concatPandas=pd.concat(listOfDataFrames)
print("Before drop duplicates",len(concatPandas))
concatPandas=concatPandas.drop_duplicates("reviewId")
print("After drop duplicates",len(concatPandas))
concatPandas.to_csv('fortune500'+str(iteration)+".csv")
print(numwrong)
    
