'''
    This program helps in filling the Requisition Request form in the line 
    of work of all the treasurers associated with the UB GSA Organisation.
    
    Copyright (C) 2020 Mohit Shetty

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import time
from selenium import webdriver

#storing values in list
clubname='CSE GSA'
accountnumber='N/A'
indvfillingform='Mohit Seetharama'
lastname='Shetty'
emailindv='mohitsee@buffalo.edu'
vendorname=['studentname']
vendoraddress=['studentemail']
addressline2=['studentaddress']
city='Buffalo'
state='New York'
zipcode=['Zipcode']
eventdate=['eventdate']
eventlocation=['eventlocation']
noofattendees='N/A'
ConferenceName=['Conference Name\n\n']
attendingPresenting=['attending']
nameofthepresentation=['papername']
goodsservices='N/A'
estimatedcost=['cost in USD']

#XPath URL
clubName='//*[@id="field80472327"]'
accountNumber='//*[@id="field80532466"]'
indvFillForm='//*[@id="field80472090-first"]'
lastName='//*[@id="field80472090-last"]'
email='//*[@id="field80472323"]'
vendor='//*[@id="field80472726"]'
vendorAddress='//*[@id="field80533805"]'
addressLine2='//*[@id="field80533817"]'
City='//*[@id="field80533809"]'
State='//*[@id="field80533947"]'
ZipCode='//*[@id="field80533956"]'
eventDate='//*[@id="field80534032"]'
eventLocation='//*[@id="field80472939"]'
noOFAttendees='//*[@id="field80701496"]'
DescriptionOfEvent='//*[@id="field80472937"]'
DescriptionGoodsServices='//*[@id="field80701508"]'
EstimatedTotalCost='//*[@id="field80473196"]'

#Radio buttons
fundraisingEvent='//*[@id="label80473197"]/div/label[2]'       #for yes=//*[@id="label80473197"]/div/label[1] for no=//*[@id="label80473197"]/div/label[2]
purchaseAdvance='//*[@id="label80473198"]/div/label[2]'			#for yes=//*[@id="label80473198"]/div/label[1] for no=//*[@id="label80473198"]/div/label[2]
Alcohol='//*[@id="label83575968"]/div/label[2]'					#for yes=//*[@id="label83575968"]/div/label[1] for no=//*[@id="label83575968"]/div/label[2]

#Submit button
submit='//*[@id="fsSubmitButton3531348"]'

def sleep():
	time.sleep(3)

browser=webdriver.Chrome()
browser.get('https://www.buffalo.edu/studentlife/who-we-are/departments/engagement/information-for-clubs-and-organizations.html#fsa-requisition-request')

#Implement the while loop in the list
i=0
while i<len(vendorname):
	browser.find_element_by_xpath("//select[@name='field80472118']/option[text()='Graduate Student Association Inc.']").click()
	browser.find_element_by_xpath(clubName).send_keys(clubname)
	browser.find_element_by_xpath(accountNumber).send_keys(accountnumber)
	browser.find_element_by_xpath(indvFillForm).send_keys(indvfillingform)
	browser.find_element_by_xpath(lastName).send_keys(lastname)
	browser.find_element_by_xpath(email).send_keys(emailindv)
	browser.find_element_by_xpath(vendor).send_keys(vendorname[i])
	browser.find_element_by_xpath(vendorAddress).send_keys(vendoraddress[i])
	browser.find_element_by_xpath(addressLine2).send_keys(addressline2[i])
	browser.find_element_by_xpath(City).send_keys(city)
	browser.find_element_by_xpath(State).send_keys(state)
	browser.find_element_by_xpath(ZipCode).send_keys(zipcode[i])
	browser.find_element_by_xpath(eventDate).send_keys(eventdate[i])
	browser.find_element_by_xpath(eventLocation).send_keys(eventlocation[i])
	browser.find_element_by_xpath(noOFAttendees).send_keys(noofattendees)
	browser.find_element_by_xpath(DescriptionOfEvent).send_keys('The name of the Conference'+ConferenceName[i]+'The student '+attendingPresenting[i]+' the Conference\n\n'+'The name of the presentation '+nameofthepresentation[i])
	browser.find_element_by_xpath(DescriptionGoodsServices).send_keys(goodsservices)
	browser.find_element_by_xpath(EstimatedTotalCost).send_keys(estimatedcost[i])
	browser.find_element_by_xpath(fundraisingEvent).click()
	browser.find_element_by_xpath(purchaseAdvance).click()
	browser.find_element_by_xpath(Alcohol).click()

	sleep()
	browser.find_element_by_xpath(submit).click()

	i+=1
	sleep()
	browser.back()
	sleep()

#Quit the browser
browser.quit()
