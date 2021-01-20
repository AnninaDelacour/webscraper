from bs4 import BeautifulSoup
import requests
import time

print("Put in a location you don't want to work at: ")
unwanted_location = input('>').capitalize()
print(f"Filtering out {unwanted_location}")
print('')


def find_jobs():
    html_text = requests.get('https://www.jobs.at/j/python?dateFrom=days&radius=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li',
                         class_="c-search-listing-item")
    for index, job in enumerate(jobs):
        published_date = job.find('div', class_="j-u-margin-left-auto--s-down j-u-text-align-right").text
        if 'Heute' in published_date or 'vor' in published_date:
            job_headline = job.find('h2',
                                    class_="c-job-headline j-u-typo-m j-u-font-weight-bold j-u-margin-bottom-3xs").text

            company_name = job.find('p', class_="j-u-margin-bottom-3xs").text
            company_location = job.find('a',
                                        class_="js-locationLink u-text-color-darker-gray j-u-color-black c-job-location-link").text
            work_info_teaser = job.find('p', class_='j-u-margin-bottom-xs j-u-display-none--s-down').text
            work_info = job.div.h2.a['href']

            if unwanted_location not in company_location:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Job Headline: {job_headline.strip()} \n")
                    f.write(f"Company Location: {company_location.strip()} \n")
                    f.write(f"Work Information Teaser: {work_info_teaser} \n")
                    f.write(f"More Information: {work_info} \n")
                    f.write(f"Published: {published_date.strip()} \n")
                print(f"File saved: {index}")

find_jobs()

#if __name__ == '__main__':
    #while True:
        #find_jobs()
        #time_wait = 10
        #print(f"Waiting {time_wait} minutes...")
        #time.sleep(time_wait * 60)