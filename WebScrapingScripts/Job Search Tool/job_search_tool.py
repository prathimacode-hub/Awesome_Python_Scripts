import requests      
from bs4 import BeautifulSoup   #importing necessary libraries

def extract(page):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
	url = f'https://in.indeed.com/jobs?q=software+developer&l=india&start={page}'
	r = requests.get(url,headers)
	soup = BeautifulSoup(r.content, 'html.parser')
	return soup

def transform(soup):
	divs =  soup.find_all('div', class_ = 'jobsearch-SerpJobCard')
	for item in divs:
		title = item.find('a').text.strip()
		company = item.find('span', class_ = 'company').text.strip()
		try:
			salary = item.find('span',class_ = 'salaryText').text.strip()
		except:
			salary = ''
		summary = item.find('div',class_ = 'summary').text.strip().replace('\n','')

		job = {
		    'title':title,
		    'company':company,
		    'salary':salary,
		    'summary':summary
		}
		joblist.append(job)
	return

joblist = []		
c = extract(0)
transform(c)
for job in joblist:
	print(job,'\n')


