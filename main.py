# Author: github.com/nthonybruno
# Description: Converts a specific unstructured HTML property tax dataset into a structured CSV file for future analysis and manipulation.

# Dependencies below
import requests
from bs4 import BeautifulSoup
import csv
import Job

# URL contains loosely formatted data on every NJ town's property tax data, over 500 entries that I needed formatted.
URL = "https://startup.jobs/?c=Full-Time"
# Page 2: https://startup.jobs/?c=Full-Time&page=2
# If you go over, page returns "No jobs found. Subscribe below to get notified when we find something for you." So paginate until this is found, then backtrack one.
page = requests.get(URL)
content = BeautifulSoup(page.text, features="lxml")
#content = BeautifulSoup(page.text, 'html.parser')

target_content_parent_element = content.find_all("div", class_="content")
result = []

condition = True

for x in target_content_parent_element:
    result.extend(x.find_all("div", class_="postCard"))

for entry in result:
    title = ""
    location = ""
    posting_link = ""

    title_element = entry.find_all("div", class_="postCard__main")
    for x in title_element:
        title_set = x.find_all("a", class_="postCard__title")
        posting_link = title_set[0].get('href')

    for x in title_set:
        title = str(x.getText())
        break

    location_element = entry.find_all("div", class_="postCard__location")
    for x in location_element:
        location = x.getText().strip()
        
    job = Job.make_job_lite(title, location, "https://startup.jobs" + posting_link)
    Job.print_job_lite(job)
    print("-------------------")