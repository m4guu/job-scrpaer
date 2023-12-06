# PRACUJ PL SCRAPER
def scrape_pracuj_pl(soup):
    jobs = []
    for job in soup.find_all(class_='tiles_c1lzjarj'):
        name = job.select('h2')[0].string
        link = job.select('a')[0]['href']
        salary = job.find(class_='tiles_s1nj37zv').text.strip() if job.find(class_='tiles_s1nj37zv') else 'Salary not provided'
        company_name = job.select('h4')[0].string
        workplace = job.select('h5')[0].string or 'Remote'
        
        jobs.append((name, link, salary, company_name, workplace))
        
    return jobs