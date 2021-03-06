def div_by_4(i):
   if (i % 4 == 0):
      return 1
   else:
      return 0

def div_by_100(i):
   if (i % 100 == 0):
      return 1
   else:
      return 0

def div_by_400(i):
   if (i % 400 == 0):
      return 1
   else:
      return 0

def check_input(i):
   if (type(i) == int):
      return 1
   else:
      return 0

def check_leapyear(i):
 is_leapyear = 0
 if (check_input(i) == 1):
  if ((div_by_4(i) == 1) and (div_by_100(i) == 0)):
   is_leapyear = 1
  elif (div_by_400(i) == 1):
   is_leapyear = 1
  else:
   is_leapyear = 0

 return is_leapyear

