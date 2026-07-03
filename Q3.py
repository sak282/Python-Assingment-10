def Fact(no):
    fact=1

    for i in range(1,no+1):
        fact=fact*i
    return fact 

    

def main():
    print("enter number:")
    value=int(input())

    ret=Fact(value)
    print("Factorzation of num is :",ret)


if __name__=="__main__":
    main()






