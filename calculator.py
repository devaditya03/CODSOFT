import os

# Simple unique calculator with emoji menu and result history

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("\n" + "=" * 40)
    print("  🧮  UNIQUE SIMPLE CALCULATOR  🧮")
    print("=" * 40 + "\n")

def print_menu():
    print("Choose an operation:")
    print("  1) ➕  Addition          (a + b)")
    print("  2) ➖  Subtraction       (a - b)")
    print("  3) ✖️  Multiplication    (a × b)")
    print("  4) ➗  Division          (a ÷ b)")
    print("  5) ⏅  Power             (a ^ b)")
    print("  6) 📐  Modulo            (a % b)")
    print()

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ❌ Please enter a valid number.")

def get_operation():
    while True:
        choice = input("Enter your choice (1–6): ").strip()
        if choice in {"1", "2", "3", "4", "5", "6"}:
            return choice
        print("  ❌ Invalid choice. Please enter 1–6.")

def calculate(a, b, choice):
    if choice == "1":
        return a + b, "+"
    elif choice == "2":
        return a - b, "-"
    elif choice == "3":
        return a * b, "*"
    elif choice == "4":
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b, "/"
    elif choice == "5":
        return a ** b, "^"
    elif choice == "6":
        if b == 0:
            raise ValueError("Modulo by zero is not allowed.")
        return a % b, "%"

def main():
    last_result = None

    while True:
        clear_screen()
        print_header()
        print_menu()

        a = get_number("Enter the first number (a): ")
        b = get_number("Enter the second number (b): ")
        choice = get_operation()

        try:
            result, op_symbol = calculate(a, b, choice)
            print(f"\n  ✅ Result: {a} {op_symbol} {b} = {result}\n")

            last_result = result
            print(f"  📜 Last result stored: {last_result}")

        except ValueError as e:
            print(f"\n  ❌ Error: {e}\n")

        cont = input("Do you want to calculate again? (y/n): ").strip().lower()
        if cont != "y":
            print("\n  👋 Thank you for using the Unique Simple Calculator!")
            if last_result is not None:
                print(f"  📜 Your last result was: {last_result}")
            break

if __name__ == "__main__":
    main()
