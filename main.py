#EXPENSE TRACKER

expenses=[] #list of expense dictionaries
print("welcome to expense tracker 💸")

while True: 
    print("\n ======MENU======")
    print(" 1. Add Expense")
    print(" 2. View All Expense")
    print(" 3. View Total Spending")
    print(" 4. View Spending by Category")
    print(" 5. Exit")

    choice= int(input("Enter your choice : "))

#1 add expense
    if choice == 1:
       date =input("Enter Date (DD-MM-YYYY): ")
       category = input("Enter category (Food, Travel,Shopping,etc): ")
       description=input("Enter short description: ")
       amount= float(input("Enter Amount (₹): "))
        
       expense = {
           "date":date,
           "category":category,
           "description":description,
           "amount":amount
        }
       expenses.append(expense)
       print("\n✅ Expense added successfully")

#2 view all expenses
    elif choice==2:
        if len(expenses)==0:
            print("\n⚠️ No expense recorded yet. ")
        else:
            print("\n-----------All Expenses-------------")
            i=1
            for e in expenses:
                print(f"{i}. {e['date']} | {e['category']} | {e['description']} | ₹{e['amount']}")
                i+=1
                print("-----------------------------------")

#3 view total spending
    elif choice==3:
        total=0
        for e in expenses:
            total+= e["amount"]
        print("\n💰 Total Spending = ",total)
    
#4 view spending by category
    elif choice==4:
        if len(expenses)==0:
            print("\n No expense recorded yet. ")
        else:
            summary ={}
            for e in expenses:
                cat = e["category"]
                if cat in expenses:
                    summary[cat]+= e["amount"]
                else:
                    summary[cat]=e["amount"]
    
            print("\n Spending By Category: ")
            for cat, amt in summary.items():
                print(f"{cat}: ₹{amt}")

#5 exit
    elif choice == 5:
      print("\n👋 Thanks for using Expense Tracker! Bye!")
      break

    else:
        print("\n❌ Invalid choice. Please try again.")      
 