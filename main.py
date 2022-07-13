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

# Request URL contents using bs4
page = requests.get(URL)
content = BeautifulSoup(page.text, features="lxml")

# All job postings on startup.jobs are organized in a parent <div> element with class="content". Capture this element, drop rest.
target_content_parent_element = content.find_all("div", class_="content")
condition = True

# Build a list of individual job posting <div> elements to logically organize and tackle title,location and link capture.
# Each job posting on the webpage is encapsulated in its own <div> element with a class="postCard".
result = []
for x in target_content_parent_element:
    result.extend(x.find_all("div", class_="postCard"))

# Loop through each individual job posting HTML element, and extract the desired fields: Job Title, Job sublink, Job location
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
    # Instantiate a new Job class instance, job_lite is a lighter object instance containing only 3 fields: Title, sublink and location. Based on this data, the filter algo later on will decide whether or not to traverse to the sublink.
    # The Job class standardizes handling and storage on funemploy servers, because data is coming from numerous sources with very different structures.
    job = Job.make_job_lite(title, location, "https://startup.jobs" + posting_link)
    
    # Temporary sanity-checking, print each of the headers out using built-in job print function.
    Job.print_job_lite(job)
    print("-------------------")
