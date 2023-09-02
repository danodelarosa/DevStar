import requests
from bs4 import BeautifulSoup
from datetime import datetime

class JobResult:
    def __init__(self, date_posted, description, company, salary, expiration_date):
        self.date_posted = date_posted
        self.description = description
        self.company = company
        self.salary = salary
        self.expiration_date = expiration_date

def scrape_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    with open("indexm.html", "w", encoding="utf-8") as f:
        for line in soup:
            f.write(str(line))
    job_results = []

    for job in soup.find_all("div", class_="job-card__container"):
        date_posted = datetime.strptime(job.find("span", class_="posting-date").text, "%b %d, %Y")
        description = job.find("div", class_="job-card__description").text
        company = job.find("div", class_="job-card__company").text
        salary = job.find("div", class_="job-card__salary").text
        expiration_date = datetime.strptime(job.find("span", class_="posting-expiration-date").text, "%b %d, %Y")

        job_result = JobResult(date_posted, description, company, salary, expiration_date)
        job_results.append(job_result)

    return job_results

def main():
    url = "https://www.linkedin.com/jobs/search/?keywords=python&location=United%20States"

    print("hola1")
    job_results = scrape_jobs(url)
    
    print("hola2")
    for job_result in job_results:
        print(job_result)
    print("hola3")
if __name__ == "__main__":
    main()
