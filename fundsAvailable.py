bankAccountAmount = int(input("How much money in the bank: $"))

income = int(input("What is your income: $"))

rent = int(input("What is the rent: $"))

essentialExpenses = int(input("How much is the essential expenses: $"))

moneyAvailable = bankAccountAmount + income - rent - essentialExpenses

print("The money available is $%d" % moneyAvailable)
#Can also use str() to wrap an integer and convert it into a string 


### create a program that will convert celsius to farenheit
