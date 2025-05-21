import uuid
from datetime import datetime

# In-memory user database
users = {}

def create_account():
    name = input("Enter your name: ").strip()
    user_id = str(uuid.uuid4())
    users[user_id] = {
        "name": name,
        "balance": 0.0,
        "transactions": []
    }
    print(f"\n✅ Account created for {name}. Your User ID is:\n{user_id}\n")

def get_user(user_id):
    user = users.get(user_id)
    if not user:
        print("❌ User not found.")
        return None
    return user

def deposit():
    user_id = input("Enter your User ID: ").strip()
    user = get_user(user_id)
    if not user:
        return

    amount = float(input("Enter amount to deposit: "))
    user["balance"] += amount
    user["transactions"].append({
        "type": "DEPOSIT",
        "amount": amount,
        "timestamp": datetime.now().isoformat()
    })
    print(f"✅ Deposited ₹{amount}. New balance: ₹{user['balance']}")

def withdraw():
    user_id = input("Enter your User ID: ").strip()
    user = get_user(user_id)
    if not user:
        return

    amount = float(input("Enter amount to withdraw: "))
    if amount > user["balance"]:
        print("❌ Insufficient balance.")
        return

    user["balance"] -= amount
    user["transactions"].append({
        "type": "WITHDRAW",
        "amount": amount,
        "timestamp": datetime.now().isoformat()
    })
    print(f"✅ Withdrawn ₹{amount}. New balance: ₹{user['balance']}")

def check_balance():
    user_id = input("Enter your User ID: ").strip()
    user = get_user(user_id)
    if user:
        print(f"💰 Current balance for {user['name']}: ₹{user['balance']}")

def view_transactions():
    user_id = input("Enter your User ID: ").strip()
    user = get_user(user_id)
    if not user:
        return

    print(f"📜 Transaction history for {user['name']}:")
    for tx in user["transactions"]:
        print(f"  [{tx['timestamp']}] {tx['type']}: ₹{tx['amount']}")

def menu():
    while True:
        print("\n=== PYTHON BANK CLI ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transactions")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            view_transactions()
        elif choice == '6':
            print("👋 Exiting... Have a nice day!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
