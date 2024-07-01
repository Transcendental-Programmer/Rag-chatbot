import requests
from bs4 import BeautifulSoup
import time
import json
from unidecode import unidecode
import re

def clean_text(text):
    text = unidecode(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def scrape_brainlox_courses():
    base_url = "https://brainlox.com"
    url = f"{base_url}/courses/category/technical"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    courses = []
    links = []
    div_elements = soup.find_all('div', {'class': 'courses-content'})
    for div in div_elements:
        a_element = div.find('a')
        if a_element:
            href = a_element.get('href')
            if href:
                links.append(f"{base_url}{href}")
    
    print(f"total number of pages: {len(links)}")
    count = 1
    for course_link in links: 
        time.sleep(1)  
        response = requests.get(course_link)
        course_soup = BeautifulSoup(response.content, 'html.parser')
        
        title_header = course_soup.find('div', class_="page-title-content")
        title = title_header.find('h2').text if title_header else "No Title"
        title = clean_text(title)
        
        course_overview_div = course_soup.find('div', class_="courses-overview")
        course_overview = course_overview_div.text if course_overview_div else "No Description"
        course_overview = clean_text(course_overview)

        course_info_details_div = course_soup.find('div', class_="courses-details-info")
        course_info_details = {}
        
        if course_info_details_div is not None:
            lists = course_info_details_div.find_all('li')
            for li in lists:
                key = clean_text(li.find_all('span')[0].text)
                value = clean_text(li.text.replace(key, ''))
                course_info_details[key] = value
        else :
            print("course info mein gadbad ho chuki hai")   
        
        courses.append({
            'title': title,
            'course_overview': course_overview,
            'course_info_details': course_info_details,
            'link': course_link
        })

        print(f" page {count} : done")
        count += 1
    return courses

if __name__ == "__main__":
    courses = scrape_brainlox_courses()
    with open('courses.json', 'w') as f:
        json.dump(courses, f, indent=4)
    print("Data scraped and saved to courses.json.")
