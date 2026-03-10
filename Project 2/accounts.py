balance_record = []

# Check balance
def check_balance(customer_id):
    for record in balance_record:
        if record[0] == customer_id:
            return record[1]
    return 0

# Deposit money
def deposit(customer_id, amount):
    for record in balance_record:
        if record[0] == customer_id:
            record[1] += amount
            print(f"\nDeposited {amount}. New Balance: {record[1]}")
            return
    # If account not in balance_record, add it
    balance_record.append([customer_id, amount])
    print(f"\nDeposited {amount}. New Balance: {amount}")

# Withdraw money
def withdraw(customer_id, amount):
    for record in balance_record:
        if record[0] == customer_id:
            if record[1] >= amount:
                record[1] -= amount
                print(f"\nWithdrawn {amount}. Remaining Balance: {record[1]}")
            else:
                print("\nInsufficient balance")
            return
    print("\nNo balance record found. Deposit first!")