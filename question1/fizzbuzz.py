def increment(i):
   return i + 1


def print_num(i):
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
   if (i % 5 == 0):
      isMultiple = 1
      return isMultiple
   else:
      #nothing
      return isMultiple



num = 1

while num <= 100:
   is_mult_3 = 0 
   is_mult_5 = 0
   is_mult_3 = check_multiple_of_3(num)
   is_mult_5 = check_multiple_of_5(num)

   if (is_mult_3 == 1 and is_mult_5 == 1):
      print("FizzBuzz")
   elif (is_mult_3 == 1):
      print("Fizz")
   elif (is_mult_5 == 1):
      print("Buzz")
   else:
      print(num)

   num = increment(num)
