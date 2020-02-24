from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#create a new Firefox session
driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()

#Navigate to the aplication home page
driver.get("https://expertsystem.com/10-text-mining-examples/")

topics = []

"""Після кожного заголовка іти некс поки не зустрінеться новий заговолок зчитуємо текс з тегів p"""

#get the search textbox
field_with_topics = driver.find_elements_by_xpath('//div[@class="l-section-h i-cf"]/h5')
for elem in field_with_topics:
    topics.append(elem.text)

print("topics:\t", topics)



'''#enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

lists = driver.find_elements_by_class_name('g')

#get number of the elements found
print(f"Found {len(lists)} searches:")

i = 0
for listItem in lists:
    print(listItem.get_attribute())
    i += 1
    if(i > 10):
        break'''
driver.quit()