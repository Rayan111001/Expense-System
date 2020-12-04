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
    
        
    

def main():
    expense1 = Expenses("burger","Food",5)
    print(expense1)
    #Main code to run
    menu()
    
def menu():
    #Menu options
    #3 options analysis, edit and exit
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
    #Print items, category totals, average
    #and totals
    print(no)
    
def editPage():
    #Add expense, delete items and exit
    print(no)
    
if __name__ == "__main__":
    #Runs the program
    main()
    
