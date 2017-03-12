# -*- coding: UTF-8 -*-
# 为了支持中文，增加以上代码
# python默认源码路径再根上，因此要用完整路径。
# 将模块com.bow.class_demo.Animal中的类
from com.bow.class_demo.Animal import Animal


class Person(Animal):
    gender = "M"

    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age)
        self.gender = gender

    def tell_detail(self):
        print("name=%s,age=%d,gender=%s" % (self.name, self.age, self.gender))

    # 重载
    def tell_name(self):
        print("name=" + self.name)


if __name__ == "__main__":
    p = Person("xww", 12, "male")
    p.tell_name()
    p.tell_detail()
