print ' question 5-----------------'

theInput = raw_input("Enter an integer: ")
number = int(theInput)
if number%2==0:
   print '\neven number entered '
elif number%2!=0:
    print '\nodd number entered '


print '\n\n\n question 6----------------- '

Prisage = 5
voteage = 18
age2bPresident = 35
retireage = 60

personsage =  input("enter your age: ")
print '\n with reference to your age : '

if personsage<Prisage :
    print '\t\ttoo young to start school'
if personsage >=voteage :
    print '\t\t Remember to vote '
if personsage >=age2bPresident :
    print '\t\tvote for me'
if personsage<age2bPresident :
     print '\t\tyou cant be president '
if personsage >= retireage :
    print '\t\tToo old my friend '



print '\n\n-------------question 7----------'

i=40
while i>0:
    if i%3==0:
       print i
    i-=1


print '\n\n-------------question 8----------'

for i in range(6, 31):
  if i%2!=0 and i%3!=0 and i%5!=0 :
      print i


print '\n\n-------------question 9----------'

n=97  # since 97 is our divisor
while n>0:
  if (79*n)%97==1 :
      print n
  n-=1 

