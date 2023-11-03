from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

def download_pdf(driver, topic):
    driver.get('https://www.lotsawahouse.org/topics/'+topic+'/')

    driver.implicitly_wait(3)

    driver.execute_script("window.scrollTo(0, 400)")


    # click pdf link so url will be active
    pdf_link = driver.find_element(By.LINK_TEXT, 'PDF')

    pdf_link.click()

    time.sleep(10)

    # download pdf from active url
    url = 'https://www.lotsawahouse.org/Cgi/make-ebook-cgi.pl?lang=english&path=topics%2F'+topic+'&format=PDF&do=download'

    response = requests.get(url)

    with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/lotsawahouse/topic-pdfs/'+topic+'.pdf', 'wb') as f:
        f.write(response.content)

# window to webpage
driver = webdriver.Chrome()

topic_list = []
remaining = []

with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/lotsawahouse/topic-list.txt', 'r') as f:
    for line in f:
        topic = line.lower().replace(' ', '-').replace('&', '').replace('--', '-').replace('\'', '')
        topic = topic.replace('ā','a').replace('ḍ', 'd').replace('é', 'e').replace('ī','i').replace('ṃ','m').replace('ṇ', 'n').replace('ñ','n').replace('ö', 'o').replace('ś', 'sh').replace('ṣ','sh').replace('ü', 'u').replace('ū', 'u')
        topic_list.append(topic)

for topic in topic_list:
    try:
        download_pdf(driver, topic)
    except:
        remaining.append(topic)

driver.close()

with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/lotsawahouse/remaining-topics.txt', 'w') as f:
    f.writelines(remaining)