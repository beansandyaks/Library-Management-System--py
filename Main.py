'''This module is has a main menu which offers options from 1-4 for users and performs a specific task 1-4 is entered.
If the input is not between 1-4, a message appears'''

import ListSplit
import DateTime
import Borrow
import Return

#Creating main function
def main():
    print("\t\t===========================================================")
    print("\t\t******************* ISLINGTON LIBRARY *********************")
    print("\t\t===========================================================\n")
    print(" WELCOME TO ISLINGTON LIBRARY\n")
    #Run while loop until true
    while(True):
        print("----------------------------------------------")
        print("\t\tLIBRARY MENU")
        print("----------------------------------------------")
        print("PRESS: 1 To Display Available Books  \n")
        print("PRESS: 2 To Issue Book\n")
        print("PRESS: 3 To Submit Book\n")
        print("PRESS: 4 To Exit\n\n")
    
        try:
        #Store the input from user in a local vairable n        
            n = int(input("Choose a command [1-4] :  "))
            print()
            #If the input is 1
            if(n==1):
                ListSplit.listSplit()
                print("\tBOOKID \t\t BOOK NAME \t\t AUTHORNAME \t\tQUANTITY \tCOST")
                print()

                #Using for loop to dislpay the details of available books
                for i in range(len(ListSplit.bookname)):    
                    print("\t"+str(i+1)+"\t\t"+ListSplit.bookname[i]+"\t\t"+ListSplit.authorname[i]+"\t\t  "+str(ListSplit.quantity[i])+"\t\tRs."+ ListSplit.cost[i])

                print("\nYou can borrow the books for maximum 10 days. Please make sure to return the book in time otherwise fine will be charged.\n")

            #If the input is 2
            elif(n==2):
                ListSplit.listSplit()
                Borrow.borrowBook()
                
            #If the input is 3     
            elif(n==3):
                ListSplit.listSplit()
                Return.returnBook()
                
            #If the input is 4    
            elif(n==4):
                print("Thank you for visiting Islington Library")
                break
            
            #If the input is not 1,2,3 and 4
            else:
                print("\nChoice out of bounds. Please enter a valid choice from 1 to 4 \n")
                
        #If input is not integer        
        except ValueError:
            print("\nPlease Input Numbers from 1 to 4\n")
            
#Calling the main function
main()            
            
