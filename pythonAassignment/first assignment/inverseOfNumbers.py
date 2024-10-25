
UserNumber = int(input("Enter a number: "))
first = UserNumber//100

stillcalculating = UserNumber//10

second = stillcalculating%10

calculate = UserNumber%100

third = calculate%10

print(third, second , first)

even = 0

odd = 0

if first%2 == 0: even +=1
else : odd+=1

if second%2 == 0: even +=1
else: odd +=1

if third%2 == 0: even +=1
else : odd +=1


print("Even: ", even)

print("Odd: ", odd)




