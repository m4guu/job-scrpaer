import json


# THE PROTOCOL SCRAPER
def scrape_the_protocol(soup, job_board):
    baseUrl = "https://theprotocol.it"
    jobs = []
    for job in soup.find_all(class_="mainWrapper_m12z7gd6"):
        # JOB BOARD ID
        job_board_id = job_board["_id"]

        name = job.select("h2")[0].string
        link = f"{baseUrl}{job.parent['href']}"
        salary = scrape_theprotocol_salary(job.find(class_="textWrapper_t3j9udu"))
        company_name = job.find(class_="rootClass_rpqnjlt").string
        workplace = job.find_all(class_="rootClass_rpqnjlt")[2].string

        jobs.append((job_board_id, name, link, salary, company_name, workplace))

    return jobs


# the:protocol SALARY SCRAPER
def scrape_theprotocol_salary(salary_div):
    if salary_div:
        salary_txt = salary_div.text.strip()
        #! ADD LOGIC
        bottom_monthly_range = None
        upper_monthly_range = None
    else:
        salary_txt = "Salary not provided"
        bottom_monthly_range = None
        upper_monthly_range = None

    return salary_txt, bottom_monthly_range, upper_monthly_range
