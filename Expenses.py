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
    
    def addExpense(self,newExpense):
        self.expense.append(newExpense)
        
    def __str__(self):
        for x in (self.expense):
            print (x)
        return ("")
    
    def makeExpense(self):
        print ("To add an expense please give the folowing information")
        while True:
            newDesc = input("Add a small description of the new expense: ")
            if newDesc == "":
                print ("please give an input")
            else:
                break

        while True:
            newCategory = input("Add a category for the new expense: ")
            if newCategory == "":
                print ("please give an input")
            else:
                break
            
        while True:
            newAmount = input("Give the amount of the new expense: ")
            try :
                float(newAmount)
                break
            except:
                print("An error occurred (please enter a valid float)")
            
        newExpense = Expenses(newDesc,newCategory,newAmount)
        self.addExpense(newExpense)
        
    def deleteExpense(self):
        while True:
            pos = 0
            for x in self.expense:
                description = x.getDescription()
                category = x.getCategory()
                amount = x.getAmount()
                print (pos,") ",description,":",category,": £",amount)
                pos += 1
            delChoice=input ("Please select which expense to delete (input -1 to exit): ")
            try:
                int(delChoice)
                if (int (delChoice)<pos and int(delChoice)>=-1):                                                                                    
                    break
            except:
                print("Please give an int")
        if (int(delChoice) == -1):
            print("")
        else:
            del self.expense[int(delChoice)]
        
    
    def categoryTotals(self):
        categorySet = set()
        for i in self.expense:
            total = 0
            if i.getCategory() not in categorySet:
                category = i.getCategory()
                categorySet.add(category)
                for n in self.expense:
                    if n.getCategory() == category:
                        total += float(n.getAmount())
                print(f"{category}: £{total:.2f}")
                
    def avgSpend(self):
        total = 0
        count = 0
        for i in self.expense:
            total += float(i.getAmount())
            count += 1
        avg = total / count
        return avg
    
    def totalExpenditure(self):
        total = 0
        for i in self.expense:
            total += float(i.getAmount())
        return total
                    
                    

def main():
    #Main code to run
    global listEx
    listEx = List()
    menu()
    
def menu():
    #Menu options
    #3 options analysis, edit and exit
    while True:
        print("""\nMenu:
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
    print("\nCategory totals:")
    listEx.categoryTotals()
    print("\nAverage spend per item:")
    print(listEx.avgSpend())
    print("\nTotal expenditure:")
    print(listEx.totalExpenditure())
    
    
    
    


    
def editPage():
    #Add expense, delete items and exit
    while True:
        print("""Menu:
            1. Add expense
            2. Delete expense
            3. Exit\n""")
        editChoice = input("Select an option:")
        
        if editChoice == "1":
            listEx.makeExpense()
        
        if editChoice == "2":
            listEx.deleteExpense()

        if editChoice == "3":
            menu()

if __name__ == "__main__":
    #Runs the program
    main()
    
