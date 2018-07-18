import urllib.parse

full_url = 'http://www.baidu.com/nn/342'
part_url = '/nn/32'

print(urllib.parse.urljoin(full_url, part_url))