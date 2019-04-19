import requests
import json


def parse(txt_file, r):
    for product in json.loads(r.content)['Data']['Prs']:
        if float(product['price']) != 0.0 and float(product['map_lat']) != 0.0\
                and float(product['map_lon']) != 0.0:
            txt_file.write(f" Product id: {product['product_id']},"
                           f" price: {product['price']}GEL, "
                           f" latitude: {product['map_lat']}"
                           f" longtitude: {product['map_lon']} \n")


pages = {1: requests.get('https://www.myhome.ge/ka/search?Page=1&Ajax=1'),
         2: requests.get('https://www.myhome.ge/ka/search?Page=2&Ajax=1'),
         3: requests.get('https://www.myhome.ge/ka/search?Page=3&Ajax=1'),
         4: requests.get('https://www.myhome.ge/ka/search?Page=4&Ajax=1'),
         5: requests.get('https://www.myhome.ge/ka/search?Page=5&Ajax=1'),
         6: requests.get('https://www.myhome.ge/ka/search?Page=6&Ajax=1'),
         7: requests.get('https://www.myhome.ge/ka/search?Page=7&Ajax=1')}

myhome_txt = open('myhome.txt', 'w')
parse(myhome_txt, pages[1])
parse(myhome_txt, pages[2])
parse(myhome_txt, pages[3])
parse(myhome_txt, pages[4])
parse(myhome_txt, pages[5])
parse(myhome_txt, pages[6])
parse(myhome_txt, pages[7])
