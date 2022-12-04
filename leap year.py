year = int(input("Enter year to be checked"))
if (year%4 == 0 and year%100 != 0 or year%400 == 0):
    output = str("This year is a leap year.")
    print(output)
elif (year%4 != 0 or year%400 !=  0):
    output = str("This year is not a leap year.")
    print(output)
