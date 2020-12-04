#Expenses code by Rayan Miah and Jacob Artis

def main():
    #Main code to run
    menu()
    
def menu():
    #Menu options
    #3 options analysis, edit and exit
    print("""Menu:
             1. Analysis mode
             2. Edit mode
             3. Exit""")
    choice = input("Select an option:")
    
    if choice == "1":
        analysis()
        
    if choice == "2":
        editPage()
        
    if choice == "3":
        exit()
    
def analysis():
    print("no")
    #Print items, category totals, average
    #and totals
    
def addExpense():
    print ("To add an expense please give the folowing information")
    newDesc = input("Add a small description of the new expense: ")
    newCategory = input("Add a category for the new expense: ")
    newAmount = input("Give the amount of the new expense: ")

def deleteExpense():
    print("no")
    
def editPage():
    #Add expense, delete items and exit
    while True:
        print("""Menu:
            1. Add expence
            2. Delete expence
            3. Exit""")
        editChoice = input("Select an option:")
        
        if editChoice == "1":
            addExpense()
        
        if editChoice == "2":
            deleteExpense()
        if editChoice == "3":
            break
    
    
if __name__ == "__main__":
    #Runs the program
    main()
    
