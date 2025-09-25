print("Hello! ") 
while True:

    n1= float(input("Please enter the 1st number: "))  
    n2= float(input( "Enter the second number: "))
    op= input("Enter operation (+, -, *, /, **, %) : ") 
    value= None 
    if ( op == '+'): 
        value= n1+n2

    elif (op == '-'):
        value =n1-n2

    elif (op == '*') : 
        value =(n1*n2) 
    elif (op == '/') : 
        if(n2==0):
            print("Error: cannot divide by zero") 
        else: 
            value  = (n1/n2)  
    elif (op == '**') :  
        if(n2==0):
            value = 1
        else: 
            value  =n1**n2
    elif (op == '%') :   
        if(n2==0): 
            print("undefined")   
        else: 
            value =n1%n2 
    else : 
        print("Invalid operation")
    if value is not None:
        print(f"Result: {value:.2f}")   
    keep= input("Do you want to calculate again? (yes/no) :") 
    if (keep.lower() =="no") : 
        break