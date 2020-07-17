income = int(input())
percent = 0

if income in range(0, 15528):
    percent = 0
elif income in range(15528, 42708):
    percent = 15
elif income in range(42708, 132407):
    percent = 25
elif income >= 132407:
    percent = 28

calculated_tax = round(income * percent / 100)

print('The tax for {} is {}%. That is {} dollars!'.format(income, percent, calculated_tax))