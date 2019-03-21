import requests
import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://money.cnn.com/data/markets/'
page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name = [] #name list

for name_box in soup.findAll('span', attrs={'class':'column stock-name'}): #find instances of stock name
		
	name.append(name_box.text) #attach name to lists
	#print name_box.text
print name
		
price = [] #price list
for price_box in soup.findAll('span', attrs={'class':'column stock-price'}): 
	price.append(price_box.text)
print price
import csv	
stock = {}	 #combine lists
for na, pr in zip(name, price):
	stock[na] = pr
print stock

#write csv of lists 
with open('index.csv', 'a') as f:
	for na, pr in stock.items():
		f.write("%s,%s\n"%(na, pr))