import sys
import mymodule

# sys.path.append('D:/xx/PythonSERVER/python31/Code')  # 提供搜索路径
print(__name__)  # 此处打印主模块的名称：__main__
mymodule.say_hello()
print('Version', mymodule.version)
print('Model Name', mymodule.model_name())

for i in sys.argv:
    print("arg ", i)
print('path:', sys.path)

# 导入特定的成员,注意下面的path没有sys前缀

from sys import path

print('path:', path)
