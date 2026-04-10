

# Input values
basic_salary = 20000

# Allowances
hra = 0.20 * basic_salary
da = 0.10 * basic_salary

# Deduction
tax = 0.05 * basic_salary

# Net Salary Calculation
net_salary = basic_salary + hra + da - tax

# Output
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Tax:", tax)
print("Net Salary:", net_salary)
