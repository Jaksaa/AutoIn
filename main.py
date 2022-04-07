import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


EMAIL = ""
PASS = ""
SEARCH = ""

jobs_dict = {}

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com")
driver.implicitly_wait(10)
login = driver.find_element(by=By.XPATH, value=("/html/body/main/section[1]/div/div/form/div[2]/div[1]/input")).send_keys(EMAIL)
time.sleep(1)
password = driver.find_element(by=By.XPATH, value="/html/body/main/section[1]/div/div/form/div[2]/div[2]/input").send_keys(PASS)
time.sleep(1)
submit = driver.find_element(by=By.CLASS_NAME, value="sign-in-form__submit-button").click()
time.sleep(10)
search_bar = driver.find_element(by=By.CLASS_NAME, value=("search-global-typeahead__input.always-show-placeholder")).send_keys(SEARCH, Keys.ENTER)
time.sleep(1)
job_filter = driver.find_element(by=By.CLASS_NAME, value=("artdeco-pill.artdeco-pill--slate.artdeco-pill--choice.artdeco-pill--2.search-reusables__filter-pill-button.search-reusables__filter-pill-button")).click()
time.sleep(5)
element = driver.find_element(by=By.XPATH, value=('//*[@id="compactfooter-copyright"]'))  ## ANY ELEMENT ON THE BOTTOM OF THE PAGE JUST TO SCROLL OVER
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", element)
# actions = ActionChains(driver)
# actions.move_to_element(element).perform()
time.sleep(5)
############ PASS CURRENT PAGE TO BEAUTIFUL SOUP TO SCRAP DATA #####################
website = driver.page_source
soup = BeautifulSoup(website, "lxml")
jobs = soup.select("body > div.application-outlet > div.authentication-outlet > div.job-search-ext > div.jobs-search-two-pane__wrapper > div > section.jobs-search__left-rail > div > div > ul > li.jobs-search-results__list-item.occludable-update.p0.relative.ember-view")
for job in jobs:
    job.find("div.disabled.ember-view.job-card-container__link.job-card-list__title")
    job_title = job.text.strip().split("\n")
    jobs_dict[job_title[0]] = {"link": f"https://www.linkedin.com{job.a['href']}",
                               "company": job_title[5].strip(),
                               "city": job_title[10]
                               }
print(jobs_dict)
# time.sleep(60)
# driver.quit()



