import json
# THE PROTOCOL SCRAPER
def scrape_the_protocol(soup):
    baseUrl = 'https://theprotocol.it'
    jobs = []
    for job in soup.find_all(class_='mainWrapper_mmgl643'):
        name = job.select('h2')[0].string
        link = f"{baseUrl}{job.parent['href']}"
        salary =  job.find(class_='textWrapper_t3j9udu').text.strip() if job.find(class_='textWrapper_t3j9udu') else 'Salary not provided'
        company_name = job.find(class_='rootClass_rpqnjlt').string
        workplace = job.find_all(class_='rootClass_rpqnjlt')[2].string

        jobs.append((name, link, salary, company_name, workplace))
        
    return jobs