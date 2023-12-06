# BULLDOG JOB SCRAPER
def scrape_bulldog_job(soup):
    jobs = []
    for job in soup.find_all(class_='shadow-jobitem'):
        name = job.select('h3')[0].text.strip()
        link = job['href']
        salary = job.select('div')[14].text.strip() or 'Salary not provided'
        company_name = job.select('div')[5].string
        workplace = job.select('div')[8].span.string
        
        jobs.append((name, link, salary, company_name, workplace))
        
    return jobs