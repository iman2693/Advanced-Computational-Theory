import math

def find_answers(x):
    # Increment the input value by 1
    z = x + 1

    # Check if the incremented value is odd
    if z % 2 != 0:
        a = 0  # Set 'a' to 0 if 'z' is odd
    else:
        flaga = True
        # Find the largest power of 2 that divides 'z'
        for i in range(int(math.log2(z)), 0, -1):
            if z % (2 ** i) == 0:
                a = i  # Set 'a' to the found power
                flaga = False
                break
        if flaga:
            a = 0  # If no power was found, set 'a' to 0
            
    # Perform calculations on 'z' based on the value of 'a'
    z = z // (2 ** a)
    z -= 1
    z = z // 2
    z += 1
    
    # Check if the modified 'z' is odd
    if z % 2 != 0:
        b = 0  # Set 'b' to 0 if 'z' is odd
    else:
        flagb = True
        # Find the largest power of 2 that divides the modified 'z'
        for i in range(int(math.log2(z)), 0, -1):
            if z % (2 ** i) == 0:
                b = i  # Set 'b' to the found power
                flagb = False
                break
        if flagb:
            b = 0  # If no power was found, set 'b' to 0
            
    # Perform further calculations on 'z' based on the value of 'b'
    z += 1
    z = z // (2 ** b)
    c = (z - 1) // 2  # Compute 'c' based on 'z'
    
    return a, b, c  # Return the results as a tuple
    
def translate_to_instruction(triple):
    a, b, c = triple  # Unpack the tuple into variables
    Variables = ('X', 'Z')  # Define variable names
    Labels = ('A', 'B', 'C', 'D', 'E')  # Define label names
    
    # Determine the label based on 'a'
    if a == 0:
        label = ''
    else:
        label = Labels[(a % 5) - 1] + str(math.ceil(a / 5))
        
    # Determine the variable based on 'c'
    if c == 0:
        variable = 'Y'
    else:
        variable = Variables[(c % 2) - 1] + str(math.ceil(c / 2))
        
    # Construct the instruction statement
    statement = f'[{label}] ' if label != '' else ''
    
    # Construct the operation based on 'b'
    if b == 0:
        statement += variable + ' <- ' + variable
    elif b == 1:
        statement += variable + ' <- ' + variable + ' + 1'
    elif b == 2:
        statement += variable + ' <- ' + variable + ' - 1'
    else:
        b -= 2
        statement += 'IF ' + variable + ' != 0 GOTO ' + Labels[(b % 5) - 1] + str(math.ceil(b / 5))
    
    return statement  # Return the constructed instruction

# Read a list of integers from user input
x = [int(i) for i in input().split()]
# Process each item in the input list and print the corresponding instruction
for item in x:
    print(translate_to_instruction(find_answers(item)))
