import requests
import json


def parse(r):
    for product in json.loads(r.content)['Data']['Prs']:
        if float(product['price']) != 0.0 and float(product['map_lat']) != 0.0\
                and float(product['map_lon']) != 0.0:
            txt_file.write(f"  Product id: {product['product_id']}, price: {product['price']}GEL, "
                           f" latitude: {product['map_lat']} longtitude: {product['map_lon']} \n")


txt_file = open('myhome.txt', 'w')
r1 = requests.get('https://www.myhome.ge/ka/search?Page=1&Ajax=1')
r2 = requests.get('https://www.myhome.ge/ka/search?Page=2&Ajax=1')
r3 = requests.get('https://www.myhome.ge/ka/search?Page=3&Ajax=1')
r4 = requests.get('https://www.myhome.ge/ka/search?Page=4&Ajax=1')
r5 = requests.get('https://www.myhome.ge/ka/search?Page=5&Ajax=1')
r6 = requests.get('https://www.myhome.ge/ka/search?Page=6&Ajax=1')
r7 = requests.get('https://www.myhome.ge/ka/search?Page=7&Ajax=1')
parse(r1)
parse(r2)
parse(r3)
parse(r4)
parse(r5)
parse(r6)
parse(r7)
