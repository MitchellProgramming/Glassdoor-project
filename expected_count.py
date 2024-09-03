import pandas as pd
import json
import os

folderLocation="/Users/andrewkwak/CODE/Web Scrape/scrapfly-scrapers/scrapfly-scrapers/glassdoor-scraper/results"
total = 0

for file_name in os.listdir(folderLocation):
    if file_name.endswith('.json'):
        file_path = folderLocation + '/' + file_name
        with open(file_path) as inputfile:
            myDict=json.load(inputfile)
            total += myDict['filteredReviewsCount']
            print('Company', file_name, 'expected', myDict['filteredReviewsCount'])

print('Total', total)