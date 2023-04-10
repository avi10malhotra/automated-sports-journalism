from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# define the search parameter constants
GOOGLE_SEARCH_URL = 'https://www.google.com/search?q='
PREFIX_QUERY = 'fifa+world+cup+qatar+2022tm+'
LANGUAGE_CONFIG = '&hl=en'

with open('matches.txt', 'r') as file:
    matches = [line.strip().replace(' ', '+') for line in file]

# initialise the webdriver
driver = webdriver.Chrome()

for match in matches:
    # navigate to the match page
    driver.get(GOOGLE_SEARCH_URL + PREFIX_QUERY + match + LANGUAGE_CONFIG)

    # wait for the search results to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g')))

    # find the "More about this game" link and click on it
    driver.implicitly_wait(10)
    more_link = driver.find_element(By.XPATH, "//div[@aria-label='More about this game']")
    more_link.click()

    # find the "TIMELINE" tab and click on it
    driver.implicitly_wait(10)
    timeline_tab = driver.find_element(By.XPATH, '//li[@data-tab_type="SOCCER_TIMELINE"]')
    timeline_tab.click()

    # store all the score updates and commentary
    driver.implicitly_wait(10)
    updates = driver.find_elements(By.CLASS_NAME, "imso_gf__gf-itm")

    # format the commentaries for storage
    commentaries = [updates[i].text.replace('\n', '\t') for i in range(len(updates))]

    # write the commentary data to a file
    with open(f'match_commentary/{match}.csv', 'w') as f:
        f.write('\n'.join(commentaries))
    f.close()

driver.quit()