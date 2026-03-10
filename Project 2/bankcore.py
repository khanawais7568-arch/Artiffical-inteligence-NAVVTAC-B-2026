# banking_app/bankcore.py

# Branch ID
branch_id = 2057

# List to store user info: [customer_id, name, password]
users_info = []

# Function to create account
def create_account(name, password):
    user_number = len(users_info) + 1
    customer_id = f"{branch_id}-{user_number}"
    
    users_info.append([customer_id, name, password])
    print(f"\nAccount created successfully! Your Customer ID: {customer_id}")
    return customer_id

# Function to login
def login(customer_id, password):
    for user in users_info:
        if user[0] == customer_id and user[2] == password:
            print(f"\nLogin successful! Welcome {user[1]}")
            return True
    print("\nInvalid login")
    return False