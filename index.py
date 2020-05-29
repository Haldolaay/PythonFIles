first = [1,2,3,4]
second = ['a','b','c']
def exchange_with(first, second):
    aReverse = second[::-1]
    bReverse = first[::-1]
    first= aReverse
    second = bReverse
    return(first,second)
   
(first,second)= exchange_with(first,second)
print(' first = ',first, '\n second = ',second)   