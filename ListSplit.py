'''This module is used to split the list in stock file and store them in a
seperate list for each item respectively'''

def listSplit():
    #declaring global variables for bookname, authorname, quantity and cost
    global bookname
    global authorname
    global quantity
    global cost
    
    #declaring empty lists for bookname, authorname, quantity and cost
    bookname=[]
    authorname=[]
    quantity=[]
    cost=[]

    #opening the stock file in read mode and storing in file variable
    file = open("stock.txt","r")
    
    #storing the values of file.readlines in lines variable
    lines = file.readlines()

    #Using for loop to strip the new line in x, and storing it in lines 
    lines =[x.strip("\n") for x in lines]

    #Using for loop till range length of lines
    for i in range(len(lines)):
        #assigning index as 0
        index =0
        
        #Using for loop till lines[i] and using .split function to split the lines where there is a ","
        for a in lines[i].split(','):
            
            #Appending bookname, authorname, quantity and cost by using their index
            if(index==0):
                bookname.append(a)
            elif(index==1):
                authorname.append(a)
            elif(index==2):
                quantity.append(a)
            elif(index==3):
                cost.append(a.strip("Rs."))
            #incrementing index by 1    
            index+=1    
