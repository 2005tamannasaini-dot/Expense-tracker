# Expense Tracker Project

expense_bill = []
print("Welcome ! Our Expense Tracker.😊")

while True:
    print("\n 📜_____MENU____")
    print("1. ADD EXPENSE.")
    print("2. SHOW EXPENSE. ")
    print("3. TOTAL EXPENSE ")
    print("4. EXIT.")

    choice = input("Enter your choice:")

# 1. ADD EXPENSE:
    if (choice == "1"):
        date = input("Enter Expense Date:")
        item_name = input("Add Name Of items:")        
        amount = float(input("Enter The Amount:"))

        expense = {
            "date": date,
            "item_name": item_name,
            "amount": amount
        }

        expense_bill.append(expense)
        print("\n Added to your expenses.✅")

# 2. SHOW EXPENSE:
    elif (choice == "2"):
        print("\n📉 Your Spending History:")

        if len(expense_bill) == 0:
            print("🚫 Your expense list is empty!")

        else:
            print("\n _____See Your Expense_____")
            for item in expense_bill:
                print(f"  {item['date']} ➡️  {item['item_name']}, {item['amount']}")  
                  
    # 3. TOTAL EXPENSE:
    elif (choice == "3"):
        total = 0
        for item in expense_bill:
            total += item["amount"]

        print("Your Total Expense:",total) 

    # 4. EXIT:
    elif (choice == "4"):
        print("👋 Goodbye! Thank You For Using Our System.....!!! ")
        break
    else:
        print("❌ Invalid Choice! PLEASE Try Again.")              

