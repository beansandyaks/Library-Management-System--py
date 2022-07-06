''' This module is used to borrow books. It asks user to input their name, creates a text file with the first name
and adds the details of the book entered along with the date and time. It lets the user multiple borrow books
according to the book id'''
import DateTime
import ListSplit

def borrowBook():
    success=False
    while(True):
        fname=input("Enter your first name: ")
        print()
        #Checking if the input is aplhabets
        if fname.isalpha():
            break
        print("please input alphabet from A-Z")
        
    while(True):
        lname=input("Enter your last name: ")
        print()
        #Checking if the input is alphabets
        if lname.isalpha():
            break
        print("Please input alphabet from A-Z")

    #Creating a borrow text file        
    borrow="Borrow-"+fname+".txt"
    #Opening the text file on write mode to include the first and last names and the date and time of borrow in the file
    f = open(borrow,"w")
    f.write("\n\n\t\t\tISLINGTON LIBRARY\n")
    f.write("\t\t\tBorrow Details\n")
    f.write("\t\tBorrowed By: "+ fname+" "+lname+"\n")
    f.write("\t\tDate: " + DateTime.getDate()+"    Time:"+ DateTime.getTime()+"\n\n")
    f.write("S.N. \t\t Bookname \t\tAuthorname\t\t Cost \n\n" )

    #Assigning sum_a, sum_b, total, n as 0
    sum_a=0.0
    sum_b=0.0
    total=0.0
    n=0

    while success==False:
        print("\t---------------------------------------------------------------------------------------------------")
        print("\tBookID \t\t BOOK NAME \t\tAUTHORNAME \t\tQUANTITY \t\t  COST")
        print("\t---------------------------------------------------------------------------------------------------")
        print()
        
        #Displaying the details of available books 
        for i in range(len(ListSplit.bookname)):
            print("\t "+str(i+1)+"\t\t"+ListSplit.bookname[i]+"\t\t"+ListSplit.authorname[i]+"\t\t  "+str(ListSplit.quantity[i])+"\t\t\tRs."+ ListSplit.cost[i])
            print()

        #Try to catch any value error
        try:   
            a= int(input("Enter the BookID of the book you wish to borrow [1-8]:  "))
            n=a
            print()
            
            #Try to catch any index error
            try:
                
                #If condition to check if the quantity of selected book if more than 0
                if(int(ListSplit.quantity[a-1])>0):
                    #Displaying the book is available and the name of the book borrowed
                    print("\t---------------------------------------------------------------------------------------------------")
                    print("\t\t\t\t\t\tTHE BOOK IS AVAILABLE !!")
                    print()
                    print("\t\t\t\t\t\tYou have borrowed "+ListSplit.bookname[a-1])
                    print("\t---------------------------------------------------------------------------------------------------")
                    print()

                    #Opening borrow file in append mode
                    f = open(borrow,"a")
                    
                    #Writing the details of book borrowed
                    f.write("1. \t\t"+ ListSplit.bookname[a-1]+"\t\t"+ListSplit.authorname[a-1]+"\t\tRs."+ListSplit.cost[a-1]+"\n")

                    #Adding the cost of the book to sum_a variable
                    sum_a = float(ListSplit.cost[a-1])
            
                    #Decreasing the quantity of the book borrowed by 1
                    ListSplit.quantity[a-1]=int(ListSplit.quantity[a-1])-1

                    #Opening the Stock file to update the information after borrow
                    f = open("Stock.txt","w")
                    for i in range(len(ListSplit.bookname)):
                        f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"Rs."+ListSplit.cost[i]+"\n")

                    '''For borrowing multiple books'''
                        
                    loop=True
                    count=1
                    while loop==True:
                        #Taking input Y or N from the user
                        choice=str(input("Do you want to borrow more books? [Y/N]: "))
                        print()

                        #If the user input is Y
                        if(choice.upper()=="Y"):
                            print("\t---------------------------------------------------------------------------------------------------")
                            print("\tBookID \t\t BOOK NAME \t\tAUTHORNAME \t\tQUANTITY \t\t  COST")
                            print("\t---------------------------------------------------------------------------------------------------")
                            print()

                            #Displaying all the available books using for loop
                            for i in range(len(ListSplit.bookname)):
                                print("\t "+str(i+1)+"\t\t"+ListSplit.bookname[i]+"\t\t"+ListSplit.authorname[i]+"\t\t  "+str(ListSplit.quantity[i])+"\t\t\tRs."+ ListSplit.cost[i])    
                                print()                        

                            #Storing the choice of the user in b variable
                            b= int(input("Enter the BookID of the book you wish to borrow [1-8]:  "))
                            print()

                            #Comparing n and b
                            if(n == b):
                                print("You have already borrowed this book!\n")
                                
                            else:
                                #Checking if the quantity of the book chosen is more than 0
                                if(int(ListSplit.quantity[b-1])>0):
                                    #Increasing count by 1
                                    count+=1
                                    print("\t---------------------------------------------------------------------------------------------------")
                                    print("\t\t\t\t\t\tTHE BOOK IS AVAILABLE !!\n")
                                    print()
                                    print("\t\t\t\t\t\tYou have borrowed "+ListSplit.bookname[b-1])
                                    print("\t---------------------------------------------------------------------------------------------------\n")
            
                                    #Opening the borrow file to append the details of the book borrowed    
                                    f = open(borrow,"a") 
                                    f.write(str(count) +". \t\t"+ ListSplit.bookname[b-1]+"\t\t"+ListSplit.authorname[b-1]+"\t\tRs."+ListSplit.cost[b-1]+"\n")
                                    sum_b+=float(ListSplit.cost[b-1])

                                    #Decreasing the quantity of book borrowed by 1
                                    ListSplit.quantity[b-1]=int(ListSplit.quantity[b-1])-1

                                    #Opening the Stock file to update the information after borrow    
                                    f = open("Stock.txt","w") 
                                    for i in range(len(ListSplit.bookname)):
                                        f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"Rs."+ListSplit.cost[i]+"\n")
                                        success=False
                                #When the quantity of the book is not more than 0            
                                else:
                                    print("Book is not available\n")
                                    loop=False
                                    break
                                
                            #Storing the value in b to n    
                            n=b   
                        #If the choice is N
                        elif (choice.upper()=="N"):
                          
                            loop=False
                            success=True
                            f = open(borrow,"a")
                            total = sum_a + sum_b
                            f.write("\n\t\t\t\t\t\t\t Total: Rs. "+ str(total))

                            f = open(borrow,"r")
                            read=f.read()
                            print(read)

                            print("\n\n\n\t---------------------------------------------------------------------------------------------------")
                            print("\t\t\t\t\tThank you for borrowing books from us!\n")
                            print("\t\t\t\t\tPlease return the book within 10 days. \n\n\t\t\tYou will be fined Rs. 5 per day if you fail to return in time.")
                            print("\t---------------------------------------------------------------------------------------------------\n\n")

                        #When the choice is neither Y or N    
                        else:
                            print("PLEASE ENTER Y or N\n")
                #When the quantity of the book selected is not more than 0 
                else:
                    print("Book is not available\n")
                    borrowBook()
                    success=False
            #When index error is found
            except IndexError:
                print("You have input invalid number. Please choose BookID acording to the book you wish to borrow.")
                print()
        #When value error is found
        except ValueError:
            print()
            print("Please choose numbers between between 1-8")
            print()
