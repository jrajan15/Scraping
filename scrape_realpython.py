import requests
from bs4 import BeautifulSoup
job = input("What job do you want? \n")
location = input("Where? \n")
print()

url = 'https://www.monster.com/jobs/search/?q=' + job + '&where=' + location
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    link = job_elem.find('a')['href']
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
    print(f"Apply here: " + link + "\n")
    
##python_jobs = results.find_all('h2',
##                               string = lambda text: 'senior' in text.lower())
##
##for p_job in python_jobs:
##    link = p_job.find('a')['href']
##    print(p_job.text.strip())
##    print("Apply here: " + link)
##    print()
    
    
    
