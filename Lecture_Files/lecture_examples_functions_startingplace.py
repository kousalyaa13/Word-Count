#examples for lecture on functions
#MD_tax_rate = 0.06
#item_price = 19.99
#MD_sales_tax = item_price * MD_tax_rate
#print(f"The sales tax on ${item_price} is ${MD_sales_tax:.2f}")

#making this a function
#default the roundoff to a False
def calculate_tax(tax_rate, price, roundoff = False):
    """
    returns the sales tax amount, 
    defaults to unrounded,
    given a tax rate and price, 
    and True/False whether to round or not,
    and also prints it out nicely
    """
    sales_tax = price * tax_rate
    if roundoff:
        sales_tax = round(sales_tax, 2)
    print(f"The sales tax on ${price} is ${sales_tax:.2f}")
    return sales_tax

results = calculate_tax(0.06, 100, True)
print(results)
results = calculate_tax(0.08775, 100, True)
print(results)
results = calculate_tax(0.08775, 100, False)
print(results)
results = calculate_tax(0.06, 19.99, True)
print(results)

results = calculate_tax(0.06, roundoff = True, price = 19.99) #this is fine if it is named
print(results)

results = calculate_tax(0.6, 19.99) #testing the default
print(results)


# a docstring should display:
# what your function does,
# description of arguments,
# and how to use it