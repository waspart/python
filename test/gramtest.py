from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, string

def cleanInput(input):
	input = re.sub('\n+', ' ', input)
	input = re.sub(' +', ' ', input)
	input = bytes(input, 'utf-8')
	input = input.decode('ascii', 'ignore')
	cleanIn = []
	input = input.split(' ')
	for item in input:
		item = item.strip(string.punctuation)
		if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
			cleanIn.append(item)
	return cleanIn

def ngrams(input, n):
	input = cleanInput(input)
	output = []
	for i in list(range(len(input) - n + 1)):
		output.append(input[i : i + n])
	return output

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html, 'html.parser')
cont = bsObj.find('div', {'id':'mw-content-text'}).get_text()
ngrams = ngrams(cont, 2)
print(ngrams)
print('count is: ' + repr(len(ngrams)))