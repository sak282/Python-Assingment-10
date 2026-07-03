def Oddnum(no):
    

    for i in range(1,no+1):
        if i%2!=0:
            print(i)  

    

def main():
    print("enter number:")
    value=int(input())

    ret=Oddnum(value)
    


if __name__=="__main__":
    main()






