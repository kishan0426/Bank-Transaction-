import tkinter
from tkinter import *



# core = Tk()
# core.geometry("720x480")
# core.title("ATM Application")
#
# l1 = Label(text = "Customer name : ", )
# l1.place(x = 30, y = 20, height = 30, width = 200)
# e1 = Entry(text = "")
# e1.place(x = 200, y = 20, height = 30, width = 50)
# l2 = Label(text = "Customer account no : ")
# l2.place(x = 30, y = 100, height = 30, width = 200)
# e2 = Entry(text = "")
# e2.place(x = 200, y = 100, height = 30, width = 50)
# l3 = Label(text = "Customer account no : ")
# l3.place(x = 30, y = 100, height = 30, width = 200)
# e3 = Entry(text = "")
# e3.place(x = 200, y = 100, height = 30, width = 50)

# core.mainloop()
#import the library
import csv

def makelist():
    """function to make a temporary list from the csv data"""
    accno = list(csv.reader(open("cust_details.csv")))
    tmp = []
    for x in accno:
        tmp.append(x)
    return tmp

def addDetails():
    """Function to add details of the customer"""
    cname = input("Enter the cname: ")
    cname.capitalize()
    acnt_no = int(input("Enter the account number: "))
    acnt_type = input("Enter the type of the account: ")
    acnt_type.upper()
    acnt_amount = int(input("Enter the balance amount: "))
    pin = input("Enter a pin: ")
    row = cname + "," + str(acnt_no) + "," + acnt_type + "," + str(acnt_amount) + "," + str(pin) + "\n"
    file = open('cust_details.csv','a')
    file.write(str(row))
    file.close()
    print('*'*40)
    print("Account has been added successfully!")
    return acnt_amount

def viewCustomer():
    """function to view the details of the customer"""
    file = open("cust_details.csv","r")
    for r in file:
        print(r)

def viewBalance(tmp):
    """function to view the balance of a specific customer"""
    ci = input("Enter your acct no: ")
    r = 0
    for y in tmp:
        if ci in tmp[r][1]:
            print(y)
        r = r + 1
    return tmp


def withDraw(tmp):
    """function to withdraw money from the account"""
    ci = input("Enter your acct no: ")
    cash = int(input("Please enter the amount to be withdrawn: "))
    r = 0
    for x in tmp:
        if ci in tmp[r][1]:
            currbal = int(tmp[r][3])
            global balance
            balance = currbal - cash
            tmp[r][3] = balance
            ind = r
            bal = input("Do you want to print the balance receipt? y/n")
            print('*' * 40)
            if bal.casefold() == 'y':
                print("Balance for the customer {0} is {1}".format(x[0], balance))
                print('*' * 40)
                print("Thanks {0}, for making a transaction! Your updated details below : ".format(x[0]))
                print('*' * 40)
                in_file = open("cust_details.csv","r")
                reader = csv.reader(in_file)
                l = list(reader)
                in_file.close()
                l[r][3] = balance
                nl = open("cust_details.csv",'w',newline='')
                csv_writer = csv.writer(nl)
                csv_writer.writerows(l)
                nl.close()
                for v in tmp[ind]:
                    print(v, end = '|')
                print()
            else:
                pass
        r += 1
    return None

def deposit(tmp):
    """function to deposit money on the account"""
    ci = input("Enter your acct no: ")
    dep = int(input("Enter the amount that should be deposit: "))
    r = 0
    for x in tmp:
        if ci in tmp[r][1]:
            newbalance = int(tmp[r][3]) + dep
            tmp[r][3] = newbalance
            ind = r
            print("Updated balance in your account {1}".format(x[0], newbalance))
            in_file = open("cust_details.csv","r")
            reader = csv.reader(in_file)
            l = list(reader)
            in_file.close()
            l[r][3] = newbalance
            nl = open("cust_details.csv",'w',newline='')
            csv_writer = csv.writer(nl)
            csv_writer.writerows(l)
            nl.close()
            for v in tmp[ind]:
                print(v, end ='|')
            print()
        r += 1
    return newbalance

def ChangePin(tmp):
    ci = input("Enter the acc id: ")
    cp = input("Enter the new password: ")
    confirm = input("Enter the password again to confirm: ")
    assert cp == confirm,"Passwords do not match between 1st and 2nd entry. Exiting!"
    r = 0
    for x in tmp:
        if ci in tmp[r][1]:
            tmp[r][4] = cp
            ind = r
            in_file = open("cust_details.csv","r")
            reader = csv.reader(in_file)
            l = list(reader)
            in_file.close()
            l[r][4] = cp
            nl = open("cust_details.csv",'w',newline='')
            csv_writer = csv.writer(nl)
            csv_writer.writerows(l)
            nl.close()
            for v in tmp[ind]:
                print(v, end ='|')
            print()
        r += 1
    return cp

def clear_csv():
    """function to clean the csv"""
    file = open("cust_details.csv","w+")
    file.close()
    print("Details are erased successfully!")

print("Options available :" + '\n' \
      + "1) Get the new customer details to be stored" + '\n' \
      + "2) Withdraw Amount From specified account" + '\n' \
      + "3) Deposit Amount For specified account" + '\n' \
      + "4) View Balance" + '\n' \
      + "5) Change the Pin" + '\n'
      + "6) View All Customer Details" + '\n'
      + "7) Close" + '\n'
      + "8) Clear the csv")

tmp = makelist()
loop = True

user = str(input("Enter your name as per ID proof: "))
pin = str(input("please enter the pin: "))
while loop == True:
    r = 0
    for x in tmp:
        # print(x)
        if user in tmp[r][0] and pin in tmp[r][4]:
            print("logs ---> {} has logged in currently".format(user))
            # print(tmp[r][0],tmp[r][4])
            option = input("Enter any number option from above: ")
            if option == "1":
                addDetails()
            elif option == "2":
                draw = withDraw(tmp)
            elif option == "3":
                dep = deposit(tmp)
            elif option == "4":
                viewBalance(tmp)
            elif option == "5":
                ChangePin(tmp)
            elif option == "6":
                viewCustomer()
            elif option == "7":
                again = input("Do you want to perform any transaction again? - y/n ")
                if again.casefold() == "y":
                    continue
                else:
                    loop = False
                    print("*** Closing the session ***")
                    break
            elif option == "8":
                clear_csv()
        r += 1

        # else:
        #     print("Incorrect pin")
        #     continue

        # loop = False


        # print("Wrong user or pin entered! Try again")
        # continue










