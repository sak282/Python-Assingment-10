def Table(no):

    for i in range(1,11):
        print(no*i)
    

def main():
    print("enter number:")
    value=int(input())

    ret=Table(value)
    print("Table of the no is :",ret)


if __name__=="__main__":
    main()






