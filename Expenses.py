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
    #Print items, category totals, average
    #and totals
    
def editPage():
    #Add expense, delete items and exit
    
if __name__ = "__main__":
    #Runs the program
    main()
    
