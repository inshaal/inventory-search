#Inventory.Updates
d={}
while True:
    a=raw_input("Enter the product name : ")
    b=raw_input("Enter the product price : ")
    d[a]=b
    c=raw_input("Do you want to add more products? [Y/N] ")
    if c=='Y' or c=='y':
        continue
    else:
        break
print "The inventory has been created!"
while True:
    x=raw_input("Enter the product name you want to search for : ")
    print "The price of that product is : ",d[x]
    y=raw_input("Do you want to search price of more products? [Y/N] ")
    if y=='Y' or y=='y':
        continue
    else:
        break
print "Program stopped. "
print "done."
