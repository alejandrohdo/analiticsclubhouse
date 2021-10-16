import requests
from lxml import html
import json
from datetime import datetime
import requests

def save_data_local(data):
    """
    Almacenamos todos log en archivo, para tener como referencia de todo el trazado del proceso de descarga   
    """
    f = open('data-clubhouse.json', 'a')
    f.write('\n' + str(data))
    f.close()
    return
headers = {
    'authority': 'ios.clubhouse.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'es-PE,es-US;q=0.9,es-419;q=0.8,es;q=0.7',
    'cookie': '_ga_LEDBTK5HX4=GS1.1.1632423265.1.0.1632423373.0; _ga_21TVVJ5WKQ=GS1.1.1632423266.1.1.1632423390.0; _ga=GA1.2.966876195.1629760247; _gid=GA1.2.2000824054.1634338702; _gat_UA-169630588-1=1; page_identifier=xLyEo0bd',
}

name_room = 'xLyEo0bd'
response = requests.get('https://ios.clubhouse.com/room/{}'.format(name_room), 
	headers=headers,verify=False)

print ('STATUS_CODE:', response.status_code)
# print ('TEXT:', response.text)

dict_data = {}
xpath_name_club = '//*[@id="identity_container"]/a/span/div/div[2]/div[1]/text()'
xpath_name_room = '//*[@id="identity_container"]/a/span/div/div[3]/div/text()'
xpath_names_stage = "//div[contains(@class, 'flex items-center h-6 -ml-3 sm:-ml-1 max-w-xxs sm:max-w-xs md:max-w-sm')]/div/text()"
xpath_names_audencia = "//div[contains(@class, 'flex items-center h-6 -ml-3 sm:-ml-1 mt-1 max-w-xxs sm:max-w-xs md:max-w-sm text-gray-500')]/div[1]/text()"
xpath_names_speakers = "//div[@class='ml-2'][2]/text()"
tree = html.fromstring(response.text)
dict_data['name_club'] = tree.xpath(xpath_name_club)[0]
dict_data['name_room'] = tree.xpath(xpath_name_room)[0]
dict_data['names_stage'] = tree.xpath(xpath_names_stage)
dict_data['link_room'] = 'https://ios.clubhouse.com/room/{}'.format(name_room)
try:
    dict_data['num_audencia'] = int(tree.xpath(xpath_names_audencia)[0])
except Exception as e:
    print (e)
dict_data['num_speakers'] = int(tree.xpath(xpath_names_speakers)[0])
print ('name club:', json.dumps(dict_data))
save_data_local(json.dumps(dict_data))