
products={}

def addProduct(product):
    name=input("enter product name: ")
    if name  not in product:
        price=int(input("enter product price: "))
        product[name]=price
        print("product added")


def update(product):
    name=input("enter product name to update: ")
    if name in product:
        newprice=int(input("enter new product price: "))
        product[name]=newprice
        print("product price updated")
    else:
        print("product not found")

def findproduct(product):
    ll=int(input("Enter product lower limit: "))
    ul=int(input("Enter product upper limit: "))
    found = False
    for k,v in product.items():
        if (v>=ll and v<=ul):
            print(f"product {k} is {v}")
            found=True
    if not(found):
        print("product not found")

while True:
    print("1. Add new product")
    print("2. Update product price")
    print("3. Find product")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        addProduct(products)
    if choice == "2":
        update(products)
    if choice == "3":
        findproduct(products)
    if choice == "4":
        exit()

