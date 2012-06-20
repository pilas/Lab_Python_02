import math
answer=0
secondanswer=0
print '-------extra credit question 1--------\n\n'
code = input( ' enter a number you want encrypt \n' )
width = int(math.ceil(math.log(code,10)))
check = int(math.ceil(math.log(code,10)))-1
secret = int(code)
for i in range(width):
    real = secret/10
    remainder = secret%10
    answer= answer + remainder *(10**check)
    secondanswer= ((answer + remainder *(10**check) +7)%10)
    check-=1
    secret = real
print 'encrypted format is : '    
print answer
print ' \n -------extra credit question 2--------\n\n'
print secondanswer
    




    

    


