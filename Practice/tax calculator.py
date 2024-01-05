"""
calculating tax on the slab basis
slab1 : below 2.5 lakhs : 0% tax
slab2 : between 2.5 and 5 lakhs : 5% tax
slab3 : between 5 and 10 lakhs : 20% tax
slab4 : above 10 lakhs : 30% tax
"""


def calTax(income: float) -> float:
    temp = income
    total_tax = 0

    if temp > 1000000:
        tax_amount = temp - 1000000
        tax = 0.3 * tax_amount
        total_tax += tax
        temp -= tax_amount

    if temp > 500000:
        tax_amount = temp - 500000
        tax = 0.2 * tax_amount
        total_tax += tax
        temp -= tax_amount

    if temp > 250000:
        tax_amount = temp - 250000
        tax = 0.05 * tax_amount
        total_tax += tax

    return total_tax


salary = int(input("Enter your salary: "))
print("Your total tax is: ", calTax(salary))
