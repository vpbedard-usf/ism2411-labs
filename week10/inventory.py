#1. The thing that most suprtised me was how the lists were counted.
#Going from 0 makes sense, but it messes with me!
#2. Cataloging prices in my last job, a list would have helped.
#I can see what the last thing we bought was so I could have added it to an invoice. 
#Exercise1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))
#Exercise2
print(inventory[0])
print(inventory[-1])
middle = len(inventory)//2
print(inventory[middle])
#Exercise3
print(inventory[0:3])
print(inventory[-2:])
print(inventory[::2])
#exercise4
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
#exercise5
coords = (40.7128, -74.0060)
try:
    coords[0]=99
except TypeError:
    print("Tuples are useful for coordinates because they do not change. If they were to change, that would be bad.")
print(coords)
#exercise6
sales6 = [100, 250, 75, 480, 200]
total=sum(sales6)
print(f"Total: ${total:,.2f}")
avg=sum(sales6)/len(sales6)
print(f"Average: ${avg:,.2f}")
best=int(max(sales6))
print(f"Best: ${best:,.2f}")
worst=min(sales6)
print(f"Worst: ${worst:,.2f}")
#exercise7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted=[]
for price in prices:
    discounted.append(price-price*.1)
print(prices)
roundedlist=[round(discount, 2) for discount in discounted]
print(roundedlist)
#exercise8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales=[]
for sale in sales:
    if sale>300:
        high_sales.append(sale)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: ${sum(high_sales)/len(high_sales):,.2f}")