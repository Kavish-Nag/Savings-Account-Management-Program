dict={}
Lst=[]
while True:
    print("","1. Open Savings account.","\n","2. Deposit Money.","\n","3. Withdraw Money.","\n","4. Display User ","\n","5. Exit")
    ch=int(input("Enter choice:"))
    min_amt=2000
    if(ch==1):
        print("Open savings account.")
        n=(input("Name of account holder:"))
        DOB=(input("Date of birth(DD/MM/YY):"))
        job=(input("Occupation:"))
        cn=int(input("Contact no.:"))
        ad=(input("Address:"))
        L1=[DOB,job,cn,ad,0]
        Lst.extend(L1)
        dict[n]=[L1]
        print("Account opened successfully")

    elif(ch==2):
        print("Deposit Money","\n","Login")
        user=(input("Enter Name:"))
        if user not in dict:
            print("User not found")
        else:
            amt=int(input("Amount to be deposited:"))
            s=amt+Lst[4]
            Lst[4]=s
            print("Amount deposited successfully!","\n","Current balance:",Lst[4])
            print(Lst)

    elif(ch==3):
        print("Withdraw Money","\n","Login")
        user=(input("Enter Name:"))
        if user not in dict:
            print("User not found")
        else:
            amt=int(input("Amount to be withdrawn:"))
            if(amt>L[4]):
                print("Not sufficient Balance")
            else:
                d=Lst[4]-amt
                Lst[4]=d
                print("Withdrawn successfully!","\n","Current balance:",Lst[4])
                print(Lst)

    elif(ch==4):
        user=(input("Enter Name:"))
        
        if user not in dict:
            print("User not found:")
        else:
            print("User Profile")
            print("Name:",n,"\t","DOB:",DOB,"\n","Occupation:",job,"\n","Contact number:",cn,"\n","Address:",ad,"\n","Account Blance:",Lst[4])
    else:
        exit()
