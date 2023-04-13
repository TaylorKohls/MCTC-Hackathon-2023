# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:40:13 2023

@author: Owner
"""

income = []
income_names = []
income_display = []
income_total = 0

expenses = []
expense_names = []
expense_display = []
expense_total = 0

checker = ''

income_source_number=int(input('how many monthly income sources? '))

while income_source_number >= 10:
    checker = input('This is the number of income sources, not the total amount of money you spend per month.  Are you sure? (Y or N)')
    if (checker == 'Y') or (checker =='y'):
        break
    else:
        income_source_number=int(input('how many monthly income sources? '))

for i in range(income_source_number):
    n = input('name the income source: ')
    income_names.append(n)
    j = float(input('how much per month? $'))
    income.append(j)
    income_total += j
    income_display.append(str(n + ' : $' + str(j)))
    print (n + ' : $' + str(j))

expense_number=int(input('how many expenses monthly? '))

while expense_number >= 10:
    checker = input('This is the number of expenses you have, not the amount of money you spend monthly.  Are you sure? (Y or N)')
    if (checker == 'Y') or (checker =='y'):
        break
    else:
        expense_number=int(input('how many monthly expense? '))

for k in range(expense_number):
    m = input('name the expense: ')
    expense_names.append(m)
    l = float(input('how much per month? $'))
    expenses.append(l)
    expense_total += l
    expense_display.append(str(m + ' : $' + str(l)))
    print (m + ' : $' + str(l))
    
monthly_balance = income_total - expense_total

print('montly income')
for i in income_display:
    print(i)

print('monthly expenses')
for i in expense_display:
    print(i)
    
print ('monthly income = $' + str(income_total))
print ('monthly expenses = $' + str(expense_total))
print ('monthly balence = $' + str(monthly_balance))