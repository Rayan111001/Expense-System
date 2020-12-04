#Expenses code by Rayan Miah and Jacob Artis
class Expenses():
    #constructor
    def __init__(self,description,category,amount):
        self.description = description
        self.category = category
        self.amount = amount
        
    #getters
    def getDescription(self):
        return self.description
    
    def getCategory(self):
        return self.category
    
    def getAmount(self):
        return self.amount
    
    #setters
    def setDescription(self,description):
        self.description = description
    
    def setCategory(self,category):
        self.category = category
    
    def setAmount(self,amount):
        self.amount = amount
        
    def __str__(self):
        return(f"Description: {self.description}\nCategory: {self.category}\nAmount: {self.amount:.2f}")

class List():
    def __init__(self):
        self.expense = []
    
    def getExpenses (self):
        return self.expense
    
    def addExpense():
        print ("To add an expense please give the folowing information")
        newDesc = input("Add a small description of the new expense: ")
        newCategory = input("Add a category for the new expense: ")
        newAmount = input("Give the amount of the new expense: ")  
        
    

def main():
    #Main code to run
    menu()
    
def menu():
    #Menu options
    #3 options analysis, edit and exit
    while True:
        print("""Menu:
                1. Analysis mode
                2. Edit mode
                3. Exit\n""")
        choice = input("Select an option:")
        
        if choice == "1":
            analysis()
            
        if choice == "2":
            editPage()
            
        if choice == "3":
            exit()
    
def analysis():
    #Print category totals, average and totals
    
    
    

    

def deleteExpense():
    print("no")
    
def editPage():
    #Add expense, delete items and exit
    while True:
        print("""Menu:
            1. Add expense
            2. Delete expense
            3. Exit\n""")
        editChoice = input("Select an option:")
        
        if editChoice == "1":
            addExpense()
        
        if editChoice == "2":
            deleteExpense()
            
        if editChoice == "3":
            menu()

if __name__ == "__main__":
    #Runs the program
    main()
    
