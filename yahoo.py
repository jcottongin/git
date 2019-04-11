#!/usr/bin/env python  
from lxml import html
import requests

page = requests.get('https://finance.yahoo.com/most-active')
tree = html.fromstring(page.content)
#print page.text


name = tree.xpath('//td[@class="Va(m) Fz(s) Ta(start) Px(10px)"]/text()')  #create tree of name lists
#print name

names = [name.text_content() for name in tree.xpath('//td[@class="Va(m) Fz(s) Ta(start) Px(10px)"]')]
#search for names column
print names

price = tree.xpath('//td[@aria-label="Price (Intraday)"]')
#print price
prices = [price.text_content() for price in tree.xpath('//td[@aria-label="Price (Intraday)"]')]
#print prices
#search for prices column


stock = {}
for na, pr in zip(names, prices):   #na is name pr is price 
	stock[na] = pr
print stock
#zip lists

import csv
import sys   #ascii code fix
reload(sys)
sys.setdefaultencoding('utf-8') #ascii code fix

with open('stock.csv', 'a') as f:  #open stock.csv and write name and price
	for na, pr in stock.items():
		f.write("%s,$%s\n"%(na, pr))
