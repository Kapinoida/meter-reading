from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyinputplus as pyip

#url = 'https://einfo.gflesch.com/einfo//aem.aspx?ac=2976643-9556'
url = pyip.inputStr(prompt='Enter URL: ')
jonesurl = 'http://censored/machine_status.html'
busurl = 'http://censored/machine_status.html'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

jones = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
jones.get(jonesurl)

jonesCount = jones.find_elements_by_xpath('//h2')[4].text
jonesCount = jonesCount[-7:]
jones.close()


bus = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
bus.get(busurl)

busCount = bus.find_elements_by_xpath('//h2')[4].text
busCount = busCount[-7:]
bus.close()

browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe', options=chrome_options)
browser.get(url)

jonesInput = browser.find_element_by_id('newReading_181467')
jonesInput.send_keys(Keys.SPACE)
browser.find_element_by_id('newReading').send_keys(jonesCount)
browser.find_element_by_xpath('//button[text()="OK"]').click()
browser.implicitly_wait(2)

busInput = browser.find_element_by_id('newReading_181464')
busInput.send_keys(Keys.SPACE)
browser.find_element_by_id('newReading').send_keys(busCount)
browser.find_element_by_xpath('//button[text()="OK"]').click()

browser.find_element_by_id('btnSubmit2').click()
