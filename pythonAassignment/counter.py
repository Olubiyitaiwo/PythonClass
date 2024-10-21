positive_number = 0
negative_number = 0
zero_number = 0


counter = 0

while (counter <= 10):

   number = int(input("Enter number: "))

   if(number < 0):
       negative_number+=1

   elif number > 0:
      positive_number+=1

   else:
      zero_number+=1

   counter+=1

print("Number of negatives: " , negative_number )
print("Positive Number" , positive_number)
print("Zero Number" , zero_number)
