for i in range(0, 3, 1):
    name = input("pls input your name:")
    name_num = len(name.strip())
    if name_num >= 2:
        break
    elif i < 2:
        print("name size should greater than(equals) 2, last %d chance" % (2 - i))
    else:
        print("you have wasted 3 times")
        exit(0)

age = int(input("pls input your age:"))
if name == "vv":
    print("""
-----------------
|welcome!  %s%s   |
-----------------""" % (name, age))
    print(type(age))
else:
    print("i don't know ", name)
