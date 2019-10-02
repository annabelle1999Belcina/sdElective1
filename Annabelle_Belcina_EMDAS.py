while True:                 #infinite 
    Input = input("Enter equation: ")
    equation = []                       # Storage for the whole equation.
    digit = ''                  #Storage for the digits as one number.
    for i in Input:                 #Scanning every element inputed. 
        if i >= '0' and i <= '9' or i=='.':           #checking if the input is number and is a digit or is it in decimal form.
            digit += i                  #if digit, store digits into one string(operations are not included).
        elif digit:                     # if the string storage(digit) has a stored number,
            equation.append( digit )        #add the digit to the equation storage.    
            equation.append( i )        #if the input is an operation and not digit, add directly to the equation storage.
            digit = ""              #make the digit empty.
    if digit:                   # if digit storage has a number after loop ended,
      equation.append(digit)        #add digit to the equation storage. 
    print(equation)     
    for i in equation:         ##Scanning every element inside the equation storage.

        #to solve the equation, it should follow the EMDAS rule.
        #to follow, check the operations in order. (^,*,/,+,-).
        #check and execute first the exponent(^) until subtraction(-).
              
#for Exponent:
      if "^" in equation:               #check ^ represents the power to which a given number is to be raised by the number next to ^.
        power = equation.index("^")
        equation[power-1]=float(equation[power-1]) ** float(equation[power+1])
        del equation[power]
        del equation[power]
        print(equation)           #show the updated equation.

#for Multiplication:
      if "*" in equation:               #Check the operation.
        times = equation.index("*")         #look the index number of the operation.
        equation[times-1]= float(equation[times-1])* float(equation[times+1])     #to execute the operation with its specified numbers only.
                                                                      #use float so that it can also solve numbers w/ decimal point.
        del equation[times]             #To delete the operation.
        del equation[times]             #To delete the number next to the operation.
        print(equation)

#For Division:
      if "/"in equation:
        devide = equation.index("/")
        equation[devide-1]= float(equation[devide-1])/ float(equation[devide+1])   #replace the equation[devide-1] with its answer.
        del equation[devide]
        del equation[devide]
        print(equation)

#For Addition:
      if "+" in equation:
        add = equation.index("+")
        equation[add-1]= float(equation[add-1])+ float(equation[add+1])
        del equation[add]
        del equation[add]
        print(equation)

#for Subtraction:
      if "-" in equation:
        sub = equation.index("-")
        equation[sub-1]= float(equation[sub-1])- float(equation[sub+1])
        del equation[sub]
        del equation[sub]
      print(equation,"\n")
    print(Input,"=",equation[0],"\n")           #Display the whole equation with an answer.

    
