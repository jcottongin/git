import requests
import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://finance.yahoo.com/most-active'
page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name = [] #name list

for name_box in soup.findAll('a', attrs={'class':'Fw(600)'}): #find instances of stock name
		
	name.append(name_box.text) #attach name to lists
	print name_box.text
#print name
		
price = [] #price list
for price_box in soup.findAll('td', attrs={'class':'Va(m) Fz(s) Ta(end) Pstart(20px) Fw(600)'}): 
	price.append(price_box.text)
#print price
import csv	
stock = {}	 #combine lists
for na, pr in zip(name, price):
	stock[na] = pr
print stock

#write csv of lists 
with open('index.csv', 'a') as f:
	for na, pr in stock.items():
		f.write("%s,%s\n"%(na, pr))