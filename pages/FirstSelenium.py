from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\c\\90\\chromedriver.exe')
# driver.get("https://bikroy.com/en")
# # driver.execute_script("window.scrollTo(0, 1600);")
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(3)
#
# element = driver.find_element_by_xpath("//div[contains(text(),'Copyright © Saltside Technologies')]")
# assert element.text == 'Copyright © Saltside Technologies'
# print(element.text)
# # print(driver.title)
# # driver.execute_script("scrollBy(0,-500);")
#
# elementpost = driver.find_element_by_xpath("//p[contains(text(),'Post your ad on Bikroy.com')]")
# assert elementpost.text == 'Post your ad on Bikroy.com'
# print(elementpost.text)

# Task2
driver.get("https://bikroy.com/en/ads/dhaka")
driver.find_element_by_xpath(
    "//body/div[@id='app-container']/div[@id='app-wrapper']/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[2]").click()
driver.find_element_by_xpath("//li[@id='price_asc']").click()
# driver.find_element_by_xpath("//iframe[@id='google_ads_iframe_/134461134/bikroy_desktop_serp_leaderboard_0']").click()
driver.get("https://bikroy.com/en/ads/cantonment-13/laptops")
driver.find_element_by_xpath("//h2[contains(text(),'Lenovo Ideapad Slim 3i')]").click()
driver.execute_script("window.scrollTo(0, 500);")
elementpost = driver.find_element_by_xpath("//p[contains(text(),'Lenovo Ideapad slim 3i')]")
assert elementpost.text == 'Lenovo Ideapad slim 3i'
print(elementpost.text)
#
# driver.find_element_by_xpath(
#     "//body/div[@id='app-container']/div[@id='app-wrapper']/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
# elementcall = driver.find_element_by_xpath(
#     "//body/div[@id='app-container']/div[@id='app-wrapper']/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/div[2]/div[2]/div[1]").click()
# assert elementcall.text == '01743447107'
# print(elementcall.text)
