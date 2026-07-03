def Evennum(no):
    

    for i in range(1,no+1):
        if i%2==0:
            print(i)  

    

def main():
    print("enter number:")
    value=int(input())

    ret=Evennum(value)
    


if __name__=="__main__":
    main()






