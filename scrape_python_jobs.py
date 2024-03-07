import re
import requests
from bs4 import BeautifulSoup

def sanitize_title(sequence):
    seen = set()
    new_list = [word for word in sequence if not (word in seen or seen.add(word))]
   
    if '\n' in new_list:
        new_list.remove('\n')
    if 'New' in new_list:
        new_list.remove('New')

    return " ".join(new_list)


def scrape_data():

    url = "https://www.python.org/jobs/"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

   
    jobs_list = soup.find(class_="list-recent-jobs")
    
    jobs = jobs_list.find_all("li")
    
    scrapped_jobs = [
        {
            "title": sanitize_title(re.findall(r"\S+|\n", job.find("h2", class_="listing-company").span.text)),
            "link": f'https://www.python.org{job.find("h2", class_="listing-company").a["href"]}',
            "date": job.find("span", class_="listing-posted").time.text
        }
        for job in jobs
        ]

    return scrapped_jobs

