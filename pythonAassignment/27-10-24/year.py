year = int(input("Enter year: "))

if( year %4 == 0):
  print(year, " is a leap year")
elif (year%4 !=0):
  print(year, " is not a leap year")