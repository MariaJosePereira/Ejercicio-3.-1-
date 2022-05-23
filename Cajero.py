
# Online Python - IDE, Editor, Compiler, Interpreter
"""Ejercico 3"""

credit = 1000

print("\t.:MENU:.")
print("1. Deposit the money into the account: ")
print("2. Withdraw money from the account: ")
print("3. Show available money: ")
print("4. Exit")
opcion = int(input("Choose a menu option: "))

print()

if opcion==1:
    extra = float(input("how much money you want to deposit -> "))
    credit += extra
    print(f"money from the account: {credit}")

elif opcion==2:
    withdraw = float(input("how much money you want to withdraw -> "))
    if withdraw>credit:
        print("Doesn’t have that kind of money")
    else: 
        credit -= withdraw
        print(f"money from the account: {credit}")

elif opcion==3:
    print(f"money from the account: {credit}")

elif opcion==4:
    print("Thanks for trusting Bank of America")
else:
    print("Error,wrong choice of menu")
    
        
        
