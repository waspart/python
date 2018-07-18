import os

_path = 'image'
if not os.path.isdir(_path):
    os.mkdir(_path)
    print("创建成功")
# else:
#     print("没有")
#     os.mkdir(_path)
