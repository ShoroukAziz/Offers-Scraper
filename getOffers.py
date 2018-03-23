import requests
from bs4 import BeautifulSoup
import re
import json

def fill_offer (attr,value):
	global i

	if value['AttributeAvailability'] == "Y":	
		if value['Class'] != "":
			try:
				if attr == 'ItemImage':
					offer[attr] = item.find(value['Tag'],class_= value['Class']).get('src')
				elif attr == 'ItemLink':
					offer[attr] = item.find(value['Tag'],class_= value['Class']).get('href')
				else:
					offer[attr] = item.find(value['Tag'],class_= value['Class']).text.strip()

			except:
				offer[attr]="N/A"
		else:
			try:
				if attr == 'ItemImage':
					offer[attr] = item.find(class_= value['ParentClass']).find(value['Tag']).get('src')
				elif attr == 'ItemLink':
					offer[attr] = item.find(class_= value['ParentClass']).find(value['Tag']).get('href')
				else:
					offer[attr] = item.find(class_= value['ParentClass']).find(value['Tag']).text.strip()
			except:
				offer[attr]="N/A"
	else:
		offer[attr]="N/A"

f = open('structure.json','r')
data = f.read()
sites = json.loads(data)
print(">>>>>>>> list of sites loaded")

for site in sites:
	r=requests.get(site['Meta']['URL'], verify=True)
	print (">>>>>>>> fetching",site['Meta']['URL'],"...")
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	Name = site['Meta']['Name']
	print(">>>>>>>> working on",Name)

	offers = []

	OfferContainerParentClass = site['OfferContainer']['ParentClass']
	OfferContainerTag = site['OfferContainer']['Tag']
	OfferContainerClass = site['OfferContainer']['Class']

	if OfferContainerClass != "":
		
		items = soup.find_all(OfferContainerTag,class_= OfferContainerClass)
	else:
		items = soup.find(class_= OfferContainerParentClass).find_all(OfferContainerTag)

	print(">>>>>>>> found",len(items),"items")

	for item in items:
		attributes = site['Attributes']
		offer = {}
		for attr, value in attributes.items():
			fill_offer(attr,value)
		
		offers.append(offer)

	with open("offers-"+Name+".json", 'w') as fp:
			json.dump(offers, fp)
	print(">>>>>>>> done with",Name)
