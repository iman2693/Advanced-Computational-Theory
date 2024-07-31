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
    maxx = maxz = 0
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
        if Variables[(c%2)-1] == 'X' and math.ceil(c/2)>maxx:
            maxx = math.ceil(c/2)
        if Variables[(c%2)-1] == 'Z' and math.ceil(c/2)>maxz:
            maxz = math.ceil(c/2)
    
    
    #statement = f'[{label}] ' if label!='' else ''
    if b == 0:
        #statement += variable+' <- '+variable
        statement = ('Dummy' , variable , label )
    elif b == 1:
        #statement += variable+' <- '+variable+' + 1'
        statement = ('Increment' , variable , label )
    elif b == 2:
        statement = ('Decrement' , variable , label )
        #statement += variable+' <- '+variable+' - 1'
    else:
        b -=2
        statement = ('GOTO' , variable , label, Lables[(b%5)-1]+str(math.ceil(b/5))  )
        #statement += 'IF '+variable+' != 0 GOTO '+ Lables[(b%5)-1]+str(math.ceil(b/5))
    
    return statement,maxx,maxz,label

I = [int(i) for i in input().split()]
X = [int(i) for i in input().split()]
maxx = maxz = 0
Instructions = {}
Lables = {}
for ind,item in enumerate(I):
    Triple = translate_to_instruction(find_answers(item))
    Instructions[ind] = Triple[0]
    
    
    if Triple[3]!='':
        Lables[Triple[3]]= ind
    if Triple[1]>maxx:
        maxx = Triple[1]
    if Triple[2]>maxz:
        maxz = Triple[2]
    Snap_Dict = {}
    for i in range(1,maxx+1):
        Snap_Dict[f'X{i}'] = 0
        if i<len(X)+1:
            Snap_Dict[f'X{i}'] = X[i-1]
    for i in range(1,maxz+1):
        Snap_Dict[f'Z{i}'] = 0
    Snap_Dict['Y'] = 0

i = 0

while i<=len(Instructions)-1:
    print(i+1,end=' ')
    print(*Snap_Dict.values())
    
    #Switch Case
    if Instructions[i][0] == 'Decrement':
        Snap_Dict[Instructions[i][1]] = max(Snap_Dict[Instructions[i][1]]-1,0)
        i+=1
        
    elif Instructions[i][0] == 'Increment':
        Snap_Dict[Instructions[i][1]] += 1
        i+=1
        
    elif Instructions[i][0] == 'GOTO':
        if Snap_Dict[Instructions[i][1]] !=0:
            if Instructions[i][3] in Lables:
                i = Lables[Instructions[i][3]]
            else:
                i = len(Instructions)
                break
        else:
            i += 1
            
    elif Instructions[i][0] == 'Dummy':
        i+=1