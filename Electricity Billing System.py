import random
import datetime as dt
import pickle
V='y'
yes=['y','yes','Yes','YES','Y']
no=['n','NO','no','No','N']
user_accounts=[]
transactions=[]
def db_creation():
    f1=open('account.dat','wb')
    user_accounts=[]
    pickle.dump(user_accounts,f1)
    f1.close()
    f2=open('transactions.dat','wb')
    transactions=[]
    pickle.dump(transactions,f2)
    f2.close()
def db_load():
    f3=open('account.dat','rb')
    a=pickle.load(f3)
    f3.close()
    f4=open('transactions.dat','rb')
    b=pickle.load(f4)
    f4.close()
    return a,b
def db_save(a,b):
    f5=open('account.dat','wb')
    pickle.dump(a,f5)
    f5.close()
    f6=open('transactions.dat','wb')
    pickle.dump(b,f6)
    f6.close()
    
while True:
    print('\nStartup\n')
    b=input("Is this the first time running this program?(Y/N):- ")
    if b=='y'or b=='Y':
        db_creation()
        break
    elif b=='n'or b=='N':
        user_accounts, transactions=db_load()
        break
    else:
        print('Enter a valid input')
    print('\n\n\n')
    
while V=='YES' or "yes" or 'Yes' or 'y' or 'Y':
    print('************************WELCOME TO ELECTRICITY BILLING SYSTEM************************')
    print("1.ACCOUNT SETTINGS")
    print("2.TRANSACTION")
    print("3.VIEW CUSTOMER DETAILS")
    
    print('5.EXIT')
    choice2=(input('ENTER YOUR CHOICE'))
    if choice2=='1':
        print('1.NEW CUSTOMER')
        print('2.DELETE EXISTING ACCOUNT')
        choice12=(input('ENTER YOUR CHOICE:'))
        if choice12=='1':
            while True:
                fl=0
                accountno=random.randrange(1000000,9999999,10)
                for i in user_accounts:
                    if i[0]==accountno:
                        fl=1
                        break
                if fl==1:
                    continue
                else:
                    break
            print("your accountno is",accountno)
            boxid=input("enter your mete box ID:")
            bankname=input('Enter your BANK NAME  :')
            bankbranch=input('Enter your BANK BRANCH  :')
            name=input('Enter your name  :')
            address=input('Enter your address  :')
            areacode=(input('Enter your area PIN CODE  :'))
            phoneno=(input('Enter your PHONE NUMBER  :'))
            email=input('Enter your email  :')
            info2=(accountno,bankname,bankbranch,name,address,areacode,phoneno,email,boxid)
            user_accounts.append(info2)
            print('Account Created')
        elif choice12=='2':
            acc=input("ENTER YOUR ACCOUNT NUMBER:")
            fl=0
            for i in user_accounts:
                    if i[0]==acc:
                        fl=1
                        break
            if fl==0:
                print('No account found')
                continue
            else:
                for i in transactions:
                    if i[0]==acc:
                        index=transactions.index(i)
                        delete=transactions.pop(index)
                for i in user_accounts:
                    if i[0]==acc:
                        index=user_accounts.index(i)
                        delete=user_accounts.pop(index)
            print("ACCOUNT",acc," IS SUCCESFULLY DELETED")
        else:
            print('Enter a valid choice')
    elif choice2=='2':
        acc=int(input('Enter your account number  :'))
        fl=0
        for i in user_accounts:
            if i[0]==acc:
                fl=1
                break
        if fl==0:
            print('No account Found')
            continue
        else:
            unit=random.randint(0,101)
            print('Dear customer, you have used ',unit,'units of electricity.')
            print('One unit of curent is 150 ruppees')
            toda=dt.date.today()
            totamt=150*unit
            GST=(15/100)*totamt
            totalamt=totamt+GST
            print('Pleae payup ',totalamt,'rupees inclding GST')
            p=input("Please Enter YES to transact(If already paid,then please answer 'paid' then please call customer care:###########)")
            if p=="YES"or 'Yes'or'yes'or'y'or 'Y':
                print("Transaction successful")
                print("You have paid the bill")
            elif p.lower=='paid':
                print('The above payment will be checked for correction by Gov.')
            else:
                print('plz pay the bill sooner')
            info3=(acc,unit,toda,totamt,GST,totalamt,p)
            transactions.append(info3)
            print('Thank you for your service.') 
    elif choice2=='3':
        accountno=int(input('Enter your account number  :'))
        z=(0,)
        for i in user_accounts:
            if i[0]==acc:
                fl=1
                row=i
                break
        if fl==0:
            print('No account Found')
            continue
        else:
            print(" Account Number: ", row[0])
            print("bankname:",row[1])
            print("bankbranch:",row[2])
            print("Person name:",row[3])
            print("Your meter device ID=",row[8])
            print("Residential address:",row[4])
            print("area code:",row[5])
            print("phone number:",row[6])
            print("email:",row[7])
            fl=0
            print('\n\tTransaction details.')
            for i in transactions:
                if i[0]==row[0]:
                    fl=1
                    row=(i)
                    break
            if fl==0:
                print('No transaction found')
            else:
                if row[6].lower()=='y'or'yes' :
                    print(" Unit : ",row[1])
                    print(" paid on:",row[2])
                    print("amount  paid without GST:",row[3])
                    print("GST=",row[4])
                    print("amount paid including GST:",row[5])
            
    elif choice2=='5':
        print("THANK  YOU!!!!  VISIT AGAIN!!!!")
        break
    else:
        print('Enter a valid choice!')
    db_save(user_accounts,transactions)
print('Thank you for using the system')