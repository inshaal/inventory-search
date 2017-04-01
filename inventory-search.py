#Making an inventory & searching in it.
d={}
while True:
    a=raw_input("Enter the product name : ")
    b=raw_input("Enter the price of that product : ")
    d[a]=b
    c=raw_input("Do you want to add more products? [Y/N] ")
    if c=='Y' or c=='y':
        continue
    else:
        break
print "The inventory has been created!"  #just to inform that the first part of our program has finished working.
while True:
    x=raw_input("Enter the product name you want to search for : ")
    print "The price of that product is : ",d[x]
    y=raw_input("Do you want to search the price of more products? [Y/N] ")
    if y=='Y' or y=='y':
        continue
    else:
        break
print "Program stopped. "
