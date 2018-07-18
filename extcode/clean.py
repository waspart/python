import os,re

txt_path = 'txts/'
save_path = 'res/'

for i in list(range(len(os.listdir(txt_path)))):
    txt_name = 'page' + repr(i) + '.txt'
    # print(txt_name + ': ')
    with open(txt_path + txt_name, 'r+') as fread, \
         open(save_path + txt_name, 'a+') as fwrite:
        # print(fread.read())
        txt_read = fread.read()

        # txt_read = re.sub('\n+', ' ', txt_read)
        txt_read = re.sub(' +', ' ', txt_read)
        clean = txt_read.split('\n')

        for item in clean:
            if item != '':
                fwrite.write(item + '\n')

    print(txt_name + '\t done!!!!')

