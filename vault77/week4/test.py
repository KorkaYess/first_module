string = 'Alise is 21 years old'

def no_digits(string):
   result = []
   #result = ''.join([i for i in string if not i.isdigit()])
   for char in string:
       if not char.isdigit():
           result.append(char)
   result = ''.join(result)
   return result

print(no_digits(string))

assert no_digits(string) == 'Alise is  years old'