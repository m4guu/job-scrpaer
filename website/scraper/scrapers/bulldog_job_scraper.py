import re
import math


# BULLDOG JOB SCRAPER
def scrape_bulldog_job(soup, job_board):
    jobs = []

    for job in soup.find_all(class_="shadow-jobitem"):
        # JOB BOARD ID
        job_board_id = job_board["_id"]
        name = job.select("h3")[0].text.strip()
        link = job["href"]
        salary = scrape_bulldogjob_salary(job.select("div")[16].text.strip())
        company_name = job.select("div")[5].string
        workplace = job.select("div")[8].span.string

        jobs.append(
            (
                job_board_id,
                name,
                link,
                salary,
                company_name,
                workplace,
            )
        )

    return jobs


# BULLDOG JOB SALARY SCRAPER
def scrape_bulldogjob_salary(salary_div):
    pattern = re.compile(r"[0-9]{1,3} [0-9]{3} - [0-9]{1,3} [0-9]{3} [A-Z]{3}")

    if pattern.match(salary_div):
        salary_txt = salary_div
        salary = salary_txt.replace("PLN", "").replace(" ", "").split("-")

        bottom_monthly_range = math.floor(int(salary[0]))
        upper_monthly_range = math.floor(int(salary[1]))
    else:
        salary_txt = "Salary not provided"
        bottom_monthly_range = None
        upper_monthly_range = None

    return salary_txt, bottom_monthly_range, upper_monthly_range
