month_in_a_year = 12
percentage = 100

principal = int(input("Enter principla:"))

annual_interest = int(input("Enter interest rate: "))

monthly_interest = annual_interest/percentage/month_in_a_year

mortage = principal*monthly_interest*(1+monthly_interest)**annual_interest/(1+monthly_interest)**annual_interest-1
print('Mortage: ', mortage)

