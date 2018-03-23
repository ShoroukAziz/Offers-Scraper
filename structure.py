import requests
from bs4 import BeautifulSoup
import re
import json

structure = []
url_file = open('urls.txt','r')
for line in url_file:
	site = {}
	data = line.split(',')

	site ['Meta'] ={}

	site['Meta']['Name']= data[0].strip()
	site['Meta']['URL'] = data[1].strip()


	site['OfferContainer'] ={}
	site['OfferContainer']['ParentClass']=""
	site['OfferContainer']['Tag']=""
	site['OfferContainer']['Class']=""





	site ['Attributes'] ={}

	site['Attributes']['ItemName'] ={}
	site['Attributes']['ItemName']['AttributeAvailability']=""	
	site['Attributes']['ItemName']['ParentClass']=""
	site['Attributes']['ItemName']['Tag']=""
	site['Attributes']['ItemName']['Class']=""


	site['Attributes']['ItemImage'] ={}
	site['Attributes']['ItemImage']['AttributeAvailability']=""
	site['Attributes']['ItemImage']['ParentClass']=""
	site['Attributes']['ItemImage']['Class']=""
	site['Attributes']['ItemName']['Tag']="img"

	site['Attributes']['PriceBefore'] ={}
	site['Attributes']['PriceBefore']['AttributeAvailability']=""
	site['Attributes']['PriceBefore']['ParentClass']=""
	site['Attributes']['PriceBefore']['Tag']=""
	site['Attributes']['PriceBefore']['Class']=""

	site['Attributes']['PriceAfter'] ={}
	site['Attributes']['PriceAfter']['AttributeAvailability']=""
	site['Attributes']['PriceAfter']['ParentClass']=""
	site['Attributes']['PriceAfter']['Tag']=""
	site['Attributes']['PriceAfter']['Class']=""

	site['Attributes']['PercentageOff'] ={}
	site['Attributes']['PercentageOff']['AttributeAvailability']=""
	site['Attributes']['PercentageOff']['ParentClass']=""
	site['Attributes']['PercentageOff']['Tag']=""
	site['Attributes']['PercentageOff']['Class']=""


	site['Attributes']['ItemBrand'] ={}
	site['Attributes']['ItemBrand']['AttributeAvailability']=""
	site['Attributes']['ItemBrand']['ParentClass']=""
	site['Attributes']['ItemBrand']['Tag']=""
	site['Attributes']['ItemBrand']['Class']=""

	site['Attributes']['ItemLink'] ={}
	site['Attributes']['ItemLink']['AttributeAvailability']=""
	site['Attributes']['ItemLink']['ParentClass']=""
	site['Attributes']['ItemLink']['Class']=""
	site['Attributes']['ItemName']['Tag']="a"

	site['Attributes']['ItemDescription'] ={}
	site['Attributes']['ItemDescription']['AttributeAvailability']=""
	site['Attributes']['ItemDescription']['ParentClass']=""
	site['Attributes']['ItemDescription']['Tag']=""
	site['Attributes']['ItemDescription']['Class']=""

	structure.append(site)

with open('structure.json', 'w') as fp:
    json.dump(structure, fp)





