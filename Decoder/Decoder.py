import math
def find_answers(x):
    z = x+1
    if z%2 !=0:
        a = 0
    else:
        flaga = True
        for i in range(int(math.log2(z)),0,-1):
            if z%(2**i)==0:
                a = i
                flaga = False
                break
        if flaga:
            a = 0
            
    z = z // (2**a)
    z -=1
    z = z//2
    z +=1
    
    if z%2 !=0:
        b = 0
    else:
        flagb = True
        for i in range(int(math.log2(z)),0,-1):
            if z%(2**i)==0:
                b = i
                flagb = False
                break
        if flagb:
            b = 0
    z +=1
    z = z// (2**b)
    c = (z-1)//2
    
    return a,b,c
    
def translate_to_instruction(triple):
    a,b,c = triple
    Variables = ('X','Z')
    Lables = ('A','B','C','D','E')
    if a==0:
        label = ''
    else:
        label = Lables[(a%5)-1]+str(math.ceil(a/5))
        
    if c==0:
        variable = 'Y'
    else:
        variable = Variables[(c%2)-1]+ str(math.ceil(c/2))
        
    statement = f'[{label}] ' if label!='' else ''
    if b == 0:
        statement += variable+' <- '+variable
    elif b == 1:
        statement += variable+' <- '+variable+' + 1'
    elif b == 2:
        statement += variable+' <- '+variable+' - 1'
    else:
        b -=2
        statement += 'IF '+variable+' != 0 GOTO '+ Lables[(b%5)-1]+str(math.ceil(b/5))
    
    return statement
    

 
x = [int(i) for i in input().split()]
for item in x:
    print(translate_to_instruction(find_answers(item)))