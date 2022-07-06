'''This module is used to return the books that were borrowed. It asks the user's first name, creates a file,
and adds the details of the books that were borrowed. Additionally it asks the user if they had returned the books after 10 days.
If the user had returned the books after 10 days, a fine is generated and added to the file. A bill is printed at the end of this
process.'''

import ListSplit
import DateTime

def returnBook():
    #Taking the first name of the lender as input
    lender_name=input("Enter name your first name: ")
    print()
    
    #Try method to catch if the user inputs wrong name
    try:
        #Creating a borrow file with the lender's first name
        borrow="Borrow-"+lender_name+".txt"
        
        #Opening the borrow file and reading the information 
        f = open(borrow,"r") 
        lines=f.readlines()
        lines=[borrow.strip("Rs.") for borrow in lines]

        #Opening the borrow file again to read the information and store it in a variable
        f = open(borrow,"r")
        data=f.read()
        
    #Except when the user inputs wrong name
    except:
        print("Incorrect Borrower Name Found. Please Enter again!\n")
        #Call the returnBook function
        returnBook()

    #Creating a return file
    r="Return-"+lender_name+".txt"
    #Opening the file in write mode to write the lender's first name and the date and time of return
    f = open(r,"w")
    f.write("\n\n\t\t\tISLINGTON LIBRARY\n")
    f.write("\t\t\tReturn Details\n")
    f.write("\t\t Returned By: "+ lender_name+"\n")
    f.write("\t\tDate: " + DateTime.getDate()+"    Time:"+ DateTime.getTime()+"\n\n")
    f.write("S.N. \t\t Bookname \t\tAuthorname\t\t Cost \n\n" )

    #Assigning fine, total as 0.0, count as 0 and loop as True 
    fine = 0.0
    total = 0.0
    loop= True
    count =0

    #Writing the details of the books returned in the returned file
    for i in range(len(ListSplit.bookname)):    
        if ListSplit.bookname[i] in data:
            count+=1
            f = open(r,"a") 
            f.write(str(count)+".\t\t"+ListSplit.bookname[i]+"\t\t"+ListSplit.authorname[i]+"\t\tRs."+ListSplit.cost[i]+"\n")

            #Increasing the quantity of the book returned by 1
            ListSplit.quantity[i]=int(ListSplit.quantity[i])+1
            #Adding the total costs of the books being returned
            total= total + float(ListSplit.cost[i])
            
    
    while loop==True:
        #Askning the user if the book was returned after 10 days
        print("Have you returned after 10 days??")
        late=input("PRESS Y for Yes and N for No\n")
        print()

        #If the input is y or Y 
        if(late.upper()=="Y"):
            
            #Taking input of the number of days
            day=int(input("By how many days was the book returned late?\n"))
            print()

            #Multiplying the number of days by 5
            fine=5*day
            break

        #If the input is n or N
        elif(late.upper()=="N"):
            #end the while loop
            break
        
        #If the input is neither Y or N
        else:
            print("Please enter Y or N\n")

    #Updating the total by adding fine to the total        
    total=total+fine
    print("Fine: "+"Rs."+str(fine))
    print("Final Total: "+ "Rs."+str(total))
    print()

    #Appending the return file with fine and total
    f = open(r,"a")
    f.write("\t\t\t\t\t\t\t  Fine: Rs. "+ str(fine)+"\n")
    f.write("\t\t\t\t\t\t\t Total: Rs. "+ str(total))
    f.close()

    #Printing the return file as a bill
    f = open(r,"r")
    return_=f.read()
    print(return_)

    #Updating the stock file after the return process is complete   
    f = open("Stock.txt","w")
    for i in range(len(ListSplit.bookname)):
        f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"Rs."+ListSplit.cost[i]+"\n")
    f.close()
    
