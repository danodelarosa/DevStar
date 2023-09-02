import requests
from bs4 import BeautifulSoup

class JobResult:
    def __init__(self, date_posted, description, company, salary, expiration_date):
        self.date_posted = date_posted
        self.description = description
        self.company = company
        self.salary = salary
        self.expiration_date = expiration_date

def scrape_job_listings(search_term, location):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }

    params = {
        "keywords": search_term,
        "location": location,
    }

    response = requests.get("https://www.linkedin.com/jobs/search/", headers=headers, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    with open("indexm.html", "w", encoding="utf-8") as f:
        for line in soup:
            f.write(str(line))
    job_listings = []
    for job_card in soup.find_all("div", class_name="jobs-search-results__card"):
        date_posted = job_card.find("span", class_name="jobs-search-results__card-result--date").text
        description = job_card.find("div", class_name="jobs-search-results__card-result--description").text
        company = job_card.find("div", class_name="jobs-search-results__card-result--company").text
        salary = job_card.find("span", class_name="jobs-search-results__card-result--salary").text
        expiration_date = job_card.find("span", class_name="jobs-search-results__card-result--expiration").text

        job_listings.append(JobResult(date_posted, description, company, salary, expiration_date))

    return job_listings


if __name__ == "__main__":
    job_listings = scrape_job_listings("Software Engineer", "United States")
    for job_listing in job_listings:
        print(job_listing)
