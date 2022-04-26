total_income=int(input())
no_of_dependents=int(input())
standard_deduction=10000
dependent_deduction=3000
taxable_income= total_income - standard_deduction - (dependent_deduction*(no_of_dependents))
tax=(taxable_income*20)/100
print(tax)
