print("*****CALCULATOR*****")
A=float(input("Enter number 1:"))
B=float(input("Enter number 2:"))

print("Select any below operations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice=input("Enter your operation:")
def calculator():
    if (choice == '1'):
        op=A+B
        return op
    elif (choice == '2'):
        op=A-B
        return op
    elif (choice == '3'):
        op=A*B
        return op
    elif(choice == '4'):
        if (A==0):
            return "Zero cannot be divided"
        else:
            op=A/B
            return op
    else:
        if (A is None or B is None):
            return "Kndly type numbers"
        else:
            return ValueError
        
if __name__=='__main__':
    result=calculator()
    print("The Answer is:",result)

    