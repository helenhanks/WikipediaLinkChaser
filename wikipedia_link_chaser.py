from selenium import webdriver
import time

chrome_driver_path = 'ChromeDriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)
#driver.minimize_window()

# Open Wikipedia Main Page
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find hyperlink to article of the day and click on it
first_link = driver.find_element_by_css_selector("#mp-tfa p a")
print(first_link.text)

# Navigate to link
driver.get(first_link.get_attribute('href'))

# Create word list
word_list = []
repeated_word = False

for i in range(1,31):

    if repeated_word:      
        break
    # Find all hyperlinks in main text of article
    links = driver.find_elements_by_css_selector("div.mw-parser-output p a")
    for link in links:
        
        # Exclude any links that are not actual English words
        if len(link.text)==0:
            pass
        elif link.text[0] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            pass
        elif '[' in link.text:
            pass
        elif '/' in link.text:
            pass
        elif 'English' in link.text:
            pass
        elif 'Latin' in link.text:
            pass
        elif 'Greek' in link.text:
            pass
        elif 'spelling' in link.text:
            pass
        elif 'listen' in link.text:
            pass
        else:
            print(str(i) + ". " + link.text)
            if link.text in word_list:
                repeated_word = True
                print("Repeat detected, end of chain.")
            word_list.append(link.text)
            driver.get(link.get_attribute('href'))
            break
    time.sleep(1)
       
# Close tab
# driver.close()

#Close whole browser
driver.quit()
