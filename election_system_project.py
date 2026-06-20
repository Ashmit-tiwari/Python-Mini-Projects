print("=== WELCOME TO ELECTION SYSTEM ===")

# --- USER REGISTRATION ---
name = input("Enter your name: ")
voter_id = input("Enter your Voter ID: ")
age = int(input("Enter your age: "))

print("\nChecking eligibility...\n")

# --- ELIGIBILITY CHECK ---
if age >= 18:
    print("✅ You are eligible to vote!")
    
    print("\nHello", name)
    print("Voter ID:", voter_id)

    # --- VOTING SYSTEM ---
    print("\n=== VOTING MENU ===")
    print("1. BJP")
    print("2. Congress")
    print("3. AAP")
    print("4. CJP")

    choice = input("Enter the number of your party choice: ")

    if choice == "1":
        print("You voted for BJP 🟠")
    elif choice == "2":
        print("You voted for Congress 🟢")
    elif choice == "3":
        print("You voted for AAP 🔵")
    elif choice == "4":
        print("You voted for CJP 🟣")
    else:
        print("❌ Invalid choice! Vote not counted.")

else:
    print("❌ Sorry, you are not eligible to vote (Age must be 18+)")