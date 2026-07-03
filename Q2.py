def Summation(no):
    sum=0

    for i in range(1,no+1):
        sum=sum+i
    return sum    

    

def main():
    print("enter number:")
    value=int(input())

    ret=Summation(value)
    print("sum  of the first n natural no is :",ret)


if __name__=="__main__":
    main()






