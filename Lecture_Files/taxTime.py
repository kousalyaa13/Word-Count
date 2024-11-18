#module for functions dealing with taxes

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

# tests
# results = calculate_tax(0.06, 100, True)
# print(results)
# results = calculate_tax(0.08775, 100, True)
# print(results)
# results = calculate_tax(0.08775, 100, False)
# print(results)
# results = calculate_tax(0.06, 19.99, True)
# print(results)

# results = calculate_tax(0.06, roundoff = True, price = 19.99) #this is fine if it is named
# print(results)

# results = calculate_tax(0.6, 19.99) #testing the default
# print(results)


# a docstring should display:
# what your function does,
# description of arguments,
# and how to use it