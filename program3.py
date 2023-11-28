PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

a=int(input("Enter Number of Pennies: "))
b=int(input("Enter Number of nickels: "))
c=int(input("Enter Number of dimes: "))
d=int(input("Enter Number of quarters: "))

totalcent=(a*PENNY_VALUE)+(b*NICKEL_VALUE)+(c*DIME_VALUE)+(d*QUARTER_VALUE)
print("Total Cents: ",totalcent)

totaldollars=totalcent/PENNIES_IN_DOLLAR
print("Total Dollars: ",totaldollars,"$")

if totaldollars>1:
    print("Sorry, the amount you entered was more than one dollar.")
    
elif totaldollars<1:
    print("Sorry, the amount you entered was less than one dollar.")

else:
    print("Congratulations! The amount you entered was exactly one dollar! You win the game!")