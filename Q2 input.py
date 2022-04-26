total_income=int(input())
no_of_dependents=int(input())
standard_deduction=10000
taxable_income= total_income - 10000 - (3000*(no_of_dependents))
tax=(taxable_income*20)/100
print(tax)
