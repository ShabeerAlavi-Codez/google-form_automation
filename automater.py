from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random

service=Service()

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")
# executable_path = 'C:\\Users\\Lenova\\Downloads\\chrome-win64\\chrome-win64\\chrome.exe'
# browser = webdriver.Chrome(executable_path = "C:\\Users\\Lenova\\Downloads\\chromedriver_win32\\chromedriver.exe", options=option)


browser = webdriver.Chrome(service=service, options=option)

# browser.get("https://forms.gle/Jre6RJzeSLbrXSeM6")

# Open the desired URL
browser.get("https://forms.gle/Jre6RJzeSLbrXSeM6")


# Use the following snippets to get elements by their class names
# textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")

email = browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input")
age1 =browser.find_element(By.XPATH,"//*[@id='i9']") #b20
age2 = browser.find_element(By.XPATH,"//*[@id='i12']") #20*40
age3= browser.find_element(By.XPATH,"//*[@id='i15']")
age4= browser.find_element(By.XPATH,"//*[@id='i18']") #60

g1= browser.find_element(By.XPATH,"//*[@id='i27']") #male
g2= browser.find_element(By.XPATH,"//*[@id='i30']") #fmale
g3= browser.find_element(By.XPATH,"//*[@id='i33']") #fm

browser.find_element(By.XPATH,"//*[@id='i33']") #fmale
browser.find_element(By.XPATH,"//*[@id='i33']") #fmale

##EDUCATION
e1=browser.find_element(By.XPATH,"//*[@id='i40']") #SSLC
e2=browser.find_element(By.XPATH,"//*[@id='i43']") #PLUS
e3=browser.find_element(By.XPATH,"//*[@id='i46']") #graduation
e4=browser.find_element(By.XPATH,"//*[@id='i49']") #PG
e5=browser.find_element(By.XPATH,"//*[@id='i52']") #PG ABOVE

#rolr
r1=browser.find_element(By.XPATH,"//*[@id='i59']") #owner
r2=browser.find_element(By.XPATH,"//*[@id='i62']") #manger
r3=browser.find_element(By.XPATH,"//*[@id='i65']") #emp
r4=browser.find_element(By.XPATH,"//*[@id='i68']") #sfemp'

#familiar
fam1=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div")
fam2=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div")
fam3=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div")
fam4=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div")
fam5=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div")
#imp
imp1=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div")
imp2=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div")
imp3=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div")
imp4=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div")
imp5=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div")
#confidence
cof1=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div")
cof2=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div")
cof3=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div")
cof4=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div")
cof5=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div")

#traning
ctr1=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div")
ctr2=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div")
ctr3=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div")
ctr4=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div")
ctr5=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div")
#skill
sk2=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div")
sk3=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div")
sk4=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div")
sk5=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div")
sk1=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div")

s2=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div")
s3=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div")
s4=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div")
s5=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div")
s1=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div")

ims2=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[17]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div")
ims3=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[17]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div")
ims4=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[17]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div")
ims5=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[17]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div")
ims1=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[17]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div")

ms2=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div")
ms3=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div")
ms4=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div")
ms5=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div")
ms1=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div")

submitBtn=browser.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")






# Create a list of radio buttons
arBtn= [age1, age2, age3,age4]
erBtn=[e3, e4, e5,e2]
rrBtn=[r1,r4,r3,r2]
fmBtn =[fam1,fam2,fam3,fam4]
imBtn =[imp1,imp4,imp2,imp3,imp5]
cfBtn =[cof1,cof2,cof3,cof4,cof5]
ctrBtn =[ctr1,ctr2,ctr3,ctr4,ctr5]
skBtn =[sk1,sk2,sk3,sk4,sk5]
sBtn =[s1,s2,s3,s4,s5]
imsBtn =[ims1,ims2,ims3,ims4,ims5]
msBtn =[ms1,ms2,ms3,ms4,ms5]


# Choose a random radio button
ar_radio = random.choice(arBtn)
er_radio =random.choice(erBtn)
rr_radio =random.choice(rrBtn)
fm_radio =random.choice(fmBtn)
imp_radio=random.choice(imBtn)
ct_radio=random.choice(ctrBtn)
cf_radio=random.choice(cfBtn)
sk_radio=random.choice(skBtn)
s_radio=random.choice(sBtn)
ims_radio=random.choice(imsBtn)
ms_radio=random.choice(msBtn)

emailList=[ "devatharshiniramesh@gmail.com"]
# Click on the random radio button
email.send_keys(emailList[0])
#age2.click()
ar_radio.click()
g1.click()


er_radio.click()
rr_radio.click()
fm_radio.click()
imp_radio.click()
cf_radio.click()
ct_radio.click()
sk_radio.click()
s_radio.click()
ims_radio.click()
ms_radio.click()

#submit
submitBtn.click()



# Keep the browser open for 5 minutes (300 seconds)
time.sleep(3)

# Close the browser
browser.quit