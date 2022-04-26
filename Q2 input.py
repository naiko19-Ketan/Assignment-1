total_income=int(input('Enter your Gross income: '))
no_of_dependents=int(input('Enter number of dependents: '))
standard_deduction=10000
dependent_deduction=3000
taxable_income= total_income - standard_deduction - (dependent_deduction*(no_of_dependents))
tax=(taxable_income*20)/100
print('Your annual income tax is',tax)
