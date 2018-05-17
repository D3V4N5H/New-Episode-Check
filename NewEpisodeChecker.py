uid='' # Enter your email here
pwd='' # Enter Amazon Prime password here
from selenium import webdriver
browser=webdriver.Firefox()
browser.implicitly_wait(2) # seconds
browser.get('https://www.primevideo.com')

#SIGN IN - checks if needed and automates it
signIn=browser.find_element_by_css_selector('.av-nav-link-with-droplist > span:nth-child(1) > a:nth-child(1)')
if signIn:
    signIn.click()
    email=browser.find_element_by_css_selector('#ap_email')
    password=browser.find_element_by_css_selector('#ap_password')
    submit = browser.find_element_by_css_selector('#signInSubmit')
    email.send_keys(uid)
    password.send_keys(pwd)
    submit.click()

#Find the 'Deception'
deception=browser.find_element_by_css_selector('div.a-section:nth-child(19) > div:nth-child(1) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(4) > span:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)')
deception.click()

#Check for new episode by evaluating total
title=browser.find_element_by_css_selector('span.av-secondary:nth-child(1)')
total=int(title.text.strip('(').strip(')'))
print('\n\nTotal episodes are %s' % total)
newEpReleased1 = False
if int(total)>10:
    newEpReleased1 = True

#Check for new episode by value of Progress bars
progressBars=browser.find_elements_by_class_name('av-progress-bar')
newEpReleased2=False
for bar in progressBars:
    if bar.get_attribute('aria-valuenow')!='100':
        newEpReleased2=True

if newEpReleased1==False or newEpReleased2==False:
    print('''\nNo new episodes :'(  Umm... check again later?''')
    browser.quit()
else:
    print('Hooray!')
