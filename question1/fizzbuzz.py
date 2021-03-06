def increment(i):
   return i + 1


def printNum(i):
   print(i)


def check_multiple_of_3(i):
   isMultiple = 0
   if (i % 3 == 0):
      isMultiple = 1
      return isMultiple
   else:
      #nothing
      return isMultiple 


def check_multiple_of_5(i):
   isMultiple = 0
   if (i % 3 == 0):
      isMultiple = 1
      return isMultiple
   else:
      #nothing
      return isMultiple



num = 0

while num <= 100:
   printNum(num)
   num = increment(num)
