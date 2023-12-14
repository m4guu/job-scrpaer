import re


# PRACUJ PL SCRAPER
def scrape_pracuj_pl(soup, job_board):
    jobs = []
    for job in soup.find_all(class_="tiles_c1lzjarj"):
        # JOB BOARD ID
        job_board_id = job_board["_id"]

        name = job.select("h2")[0].string
        link = job.select("a")[0]["href"]
        salary = scrape_pracujpl_salary(job.find(class_="tiles_s1nj37zv"))
        company_name = job.select("h4")[0].string
        workplace = job.select("h5")[0].string or "Remote"

        jobs.append((job_board_id, name, link, salary, company_name, workplace))

    return jobs


# PRACUJPL SALARY SCRAPER
def scrape_pracujpl_salary(salary_div):
    # ! pattern = re.compile(r"[0-9]{1,3} [0-9]{3}–[0-9]{1,3} [0-9]{1,3}")

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
