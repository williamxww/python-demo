salary = input("pls input your salary:").strip()
salary = int(salary)
products = [
    ["iPhone", 5000],
    ["TV", 2000],
    ["bike", 1000],
    ["coffee", 20]
]
shopping_list = []

while True:
    for p in products:
        print(products.index(p), p[0], p[1])
    choice = input("\033[32;1m what do you want to buy?\033[0m")

    if choice == "exit":
        break
    else:
        choice = int(choice)
        info = products[choice]
        if salary < info[1]:
            print("can NOT afford")
            break
        else:
            salary -= info[1]
            shopping_list.append(info)

print(shopping_list)
