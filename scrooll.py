def scroll(number,down,up):
    n=0
    if number < down:
       n= number - down 
       n= up + n
       return n
    if number > up:
       n= number - up  
       n= down + n
       return n
    return n



b=0
for a in range(-8,0):
    b=scroll(a,0,10)
    print(str(b)+ " = " + str(a-0))

for a in range(10,18):
    b=scroll(a,0,10)
    print(str(b)+ " = " + str(a-10))