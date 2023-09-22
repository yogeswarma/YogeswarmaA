def isleapyear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False


year = int(input("enter a year to find leap year or not :"))

if isleapyear(year):
  print(' this year {} is a leap year.'.format(year))
else:
  print('this year {} is not a leap year.'.format(year))
