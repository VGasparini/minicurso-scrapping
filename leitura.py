import json
from pprint import pprint

path = '/home/vgasparini/Documents/git/scrapy_tecnoblog/noticias/spiders/notices.json'

with open(path) as json_file:
    for line in json_file:
        data = json.loads(line).encode('utf8')

pprint(data)
