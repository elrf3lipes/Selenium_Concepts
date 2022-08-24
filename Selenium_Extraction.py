from selenium import webdriver  # importing webdriver from selenium
from selenium.webdriver.support.ui import Select # tacle dropdown menus
import pandas as pd # store data into a data frame, 'pd' is a short for Panda
import time

website = 'https://www.adamchoi.co.uk/overs/detailed'  # defined website
path = '/Users/ramonsaldanha/Downloads/chromedriver'  # defined path where Chrome driver is
driver = webdriver.Chrome(path)   # created a driver
driver.get(website)  # open a Chrome driver window

# to build xPat: //tagName[@AttributeName="Value"]
# label = tag, analytics-event="All matches"
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')  # *use different quotes than the xpath
all_matches_button.click() # click on this button

dropdown = Select(driver.find_element_by_id('country')) # this is used for dropdowns
dropdown.select_by_visible_text('Brazil')

time.sleep(3) # we want the execution of the code to wait 3 seconds here

matches = driver.find_elements_by_tag_name('tr')

# create lists to segregate data

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text)
    home = match.find_element_by_xpath('./td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)

# driver.quit()

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team}) # to create a data frame using dictionary
df.to_csv('football_data.csv', index=False) # to export the data to a .csv file
print(df)