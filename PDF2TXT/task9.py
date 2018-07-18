from aip import AipOcr

app_id = '11073460'
api_key = 'qaL43FdLsGUjLNxgzvcpXLwP'
secret_key = '3Crcl3VHrSMC1yIIBS75wyjTGZco9BwS'

client = AipOcr(app_id, api_key, secret_key)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('img2.png')
ret = client.basicGeneral(image)

print(type(ret))
print(ret)

dict_lst = ret['words_result']
print(type(dict_lst))
print(dict_lst)

for d in dict_lst:
    s_part = d['words']
    f = open('tnb.txt', 'a+')
    f.write(s_part)
    f.close()

print('\n done!!!!!!!!!!!')

