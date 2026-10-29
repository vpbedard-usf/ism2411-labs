#1.The first bug I spotted was the missing colon on line 10.
#I found it in the traceback.
#It shows that I ran the script before anything else, it is just my perferred way of diagnosing.
#2.It looks at the tier first.
#Once it determines the tier, it calculates the price, price*discount.
#It returns the final price.
#I am not sure what this is asking, but someone can use it without reading the code, and if they do read the code, it is easy for a human to understand.
#3.I did not use AI, I just followed the teacher. The only AI I used was the part where it was assigned.
#It did not really help aid my understanding, I learned better from just doing it myself.

#exercise1
def calculate_tax(price, rate):
    return price*rate

tax1=calculate_tax(100, .07)
tax2=calculate_tax(250, .08)

print(f"Tax for $100 at 7%: ${tax1:,.2f}")
print(f"Tax for $250 at 8%: ${tax2:,.2f}")
print(f"Another tax: ${calculate_tax(150, 0.05):,.2f}")

#exercise2
def apply_discount(price, tier):
    if tier == "gold":
        return price*.85
    elif tier == "silver":
        return price*.9
    elif tier == "bronze":
        return price*.95
    else:
        return price

price = 200
tiers = ["gold","silver","bronze","none"]

for tier in tiers:
    print(f"Tier: {tier}: Price: ${apply_discount(price, tier)}")

#exercise3
discounted=apply_discount(200, "gold")
tax=calculate_tax(discounted, 0.07)
after_tax=discounted+tax
print(f"After gold discount: ${discounted:,.2f}")
print(f"After tax: ${after_tax:,.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', .07):,.2f}")

#exercise4
orders = [(200, "gold"),(150,"silver"),(80, "bronze"),(500,"none")]
for price, tier in orders:
    total = final_price(price, tier, .07)
    print(f"Price: ${price:,.2f}, Tier: {tier}, Final: ${total:,.2f}")

#exercise6
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here?
print(double_it()) # what prints here?
print(x)           # has x changed?
#it will return 100.
#it will return double 999, not 100. 
#it will return 100, it has not changed.
#the x is GLOBAL, the x inside the finction is LOCAL. Not the same x. You can use 'global' to get the value outside the function.