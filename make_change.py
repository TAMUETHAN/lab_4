# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Andrew Rigler
#               NAME OF TEAM MEMBER 2
#               NAME OF TEAM MEMBER 3
# Section:      5
# Assignment:   Lab 4 #1 Make Change
# Date:         DAY MONTH YEAR
#

paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))

#Change due is in cents to avoid floating point rounding errors when multiplyting and subtracting
change_change_due_cents = int(paid*100) - int(cost*100)

print(f"You received ${change_change_due_cents/100:.2f} in change. That is...")


quarters = int((change_change_due_cents / 100) // 0.25)
change_change_due_cents -= quarters * 25
if quarters:
    if quarters == 1:
        print(f"{quarters} quarter")
    else:
        print(f"{quarters} quarters")

dimes = int((change_change_due_cents / 100) // 0.10)
change_change_due_cents -= dimes * 10
if dimes:
    if dimes == 1:
        print(f"{dimes} dime")
    else:
        print(f"{dimes} dimes")


nickles = int((change_change_due_cents / 100) // 0.05)
change_change_due_cents -= nickles * 5
if nickles:
    if nickles == 1:
        print(f"{nickles} nickel")
    else:
        print(f"{nickles} nickels")

pennies = change_change_due_cents
change_change_due_cents -= pennies
if pennies:
    if pennies == 1:
        print(f"{pennies} penny")
    else:
        print(f"{pennies} pennies")