import requests

from parser import Parser, ParserOptions

options = ParserOptions()
parser = Parser(options)

url = "https://lorem-rss.herokuapp.com/feed"
response = requests.get(url)

parser.parse_string(response.content)
