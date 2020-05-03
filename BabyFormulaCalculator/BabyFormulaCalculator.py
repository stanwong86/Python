import re
import requests

Coupon10 = 3
Coupon5 = 6

Catalog = {
	'Target': [
		{
			'oz': 29.8,
			'price': 36.99
		},
		{
			'oz': 22.5,
			'price': 27.99
		}
	],
	'BJs': [
		{
			'oz': 34,
			'price': 35.99
		}
	]
}

def lowestCoupon(coupon=10):
	lowestItem = {'costPerOz': 9999.0}
	allItems = []
	for store, items in Catalog.items():
		for item in items:
			costPerOz = 1.0 * (item['price'] - coupon) / item['oz']
			print('%s, Cost {%s}, Oz {%s}, CostPerOz {%s}' % (store, item['price'], item['oz'], costPerOz))
			if costPerOz < lowestItem['costPerOz']:
				lowestItem = {
					'costPerOz': costPerOz,
					'store': store,
					'price': item['price'],
					'oz': item['oz'],
					'coupon': '$10'
				}

	for item in allItems:
		print(item)

	print('Lowest Item: %s' % lowestItem)
	return lowestItem

def scrapeCatalog():
	url = "https://www.target.com/p/similac-pro-sensitive-non-gmo-infant-formula-with-iron-powder-29-8oz/-/A-70000004"
	r = requests.get(url)
	m = re.search('Similac Pro-Sensitive Non-GMO Infant Formula with Iron Powder - (.*?)oz', r.text)
	if not m:
		raise Exception('Target 29.8oz size error')
	oz = m.group(1)

	m = re.search('product-price', r.text)
	print(r.text)
	print(m.group())
	if not m:
		raise Exception('Target 29.8oz price error')
	price = m.group(1)
	#<div class="style__PriceFontSize-gob4i1-0 fwkyhU h-text-bold" data-test="product-price">$36.99</div>
	print(oz, price)

#print(lowestCoupon(0))


scrapeCatalog()