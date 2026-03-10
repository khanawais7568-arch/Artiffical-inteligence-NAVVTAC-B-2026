from bankcore import create_account, login
from accounts import check_balance, deposit, withdraw

def banking_menu(customer_id):
    while True:
        print("\n--- Banking Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Logout")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            balance = check_balance(customer_id)
            print(f"Your Current Balance: {balance}")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            deposit(customer_id, amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            withdraw(customer_id, amount)
        elif choice == "4":
            print("Logged out successfully!")
            break
        else:
            print("Invalid choice. Try again.")

def main():
    print("=== Welcome to ABC Bank ===")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Create an Account")
        print("2. Login to Account")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            customer_id = create_account(name, password)
            print("Note your Customer ID:", customer_id)
            
        elif choice == "2":
            customer_id = input("Enter Customer ID: ")
            password = input("Enter Password: ")
            if login(customer_id, password):
                banking_menu(customer_id)
        elif choice == "3":
            print("Thank you for using ABC Bank!")
            break
        else:
            print("Invalid choice. Try again.")

main()