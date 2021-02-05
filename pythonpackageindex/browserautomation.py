"""automated browser signup"""
# install selenium
# pypi selenium >> driver chrome >> download latest release window 32 bit


from selenium import webdriver
import config

# this class contain popular browser

# class Chrome

# in this pc version 88 is supported not 89
browser = webdriver.Chrome()
browser.get("http://github.com")

# we cant find id of sign in button
sign_link = browser.find_element_by_link_text("Sign in")
sign_link.click()

# label username have id login field

username_box = browser.find_element_by_id("login_field")
# filling this box with new usename
username_box.send_keys(config.email)

password_box = browser.find_element_by_id("password")
password_box.send_keys(config.password)

password_box.submit()

# its page_source return html content of webpage
# this assert we can varify something or else throw exception
assert "AzharUddinSheikh" browser.page_source 

# more specific way lets get inside the class first and read it 
profile_link = browser.find_elements_by_class_name("user-profile-link")

# now we need inner html of this link
label = profile_link.get_attribute("innerHTML")    
assert "AzharUddinSheikh" in label

# imp waits and page objects are most encourage 


# each code run open new browser 
browser.quit()