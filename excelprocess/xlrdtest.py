import xlrd

# 慢支.xlsx 特殊处理
# 乳腺疾病

workbook = xlrd.open_workbook(u'xlsxs/肿瘤的治疗与康复.xls')
sheet_names = workbook.sheet_names()
# print(len(sheet_names))
for sheet_name in sheet_names[:1]:
    # print(sheet_name)
    sheet2 = workbook.sheet_by_name(sheet_name)
    # print(sheet2.row_values(0))
    # print(sheet2.row_len(1))
    print(sheet2.nrows)

    count = 0
    for i in list(range(1, sheet2.nrows)):
        # print(len(sheet2.row_values(i)))
        row_val = sheet2.row_values(i)

        if row_val[1].strip() == '' and row_val[0].strip() == '':
            continue
            # print('lineNo =', i, row_val[0].strip().split('\n')[0])

        if row_val[1].strip() == '':
            print(row_val[0].strip().split('\n')[0], 'lineNo =', i)
            count += 1

    print(count)
    # print(sheet2.row_values(46))
    # dat = sheet2.row_values(46)[0].replace(' ', '')
    # print(dat.replace('\n', '').strip())
    # print(sheet2.row_values(46)[1].replace('\n', '').strip())


        # if len(sheet2.row_values(i)) != 2:
        #     print(sheet2.row_values(i))
        # print(sheet2.row_values(i))
        # print(type(sheet2.row_values(i)[0]))

# print(int(sheet2.row_values(271)[0]))
#
# str = ''
# print(str.__eq__(''))