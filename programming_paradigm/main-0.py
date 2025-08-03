import sys
from bank_account import BankAccount

def main():
    """
    Interacts with the BankAccount class through command-line arguments.
    """
    # The starting balance is set here. You can change this for testing.
    account = BankAccount(100.0)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_with_args = sys.argv[1]
    
    # Handle the 'display' command which has no amount
    if command_with_args == "display":
        command = "display"
        amount = None
    else:
        try:
            command, amount_str = command_with_args.split(':')
            amount = float(amount_str)
        except ValueError:
            print("Invalid command format. Use <command>:<amount>.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount for deposit/withdraw.")
        
    # Display the final balance for all operations for clarity
    account.display_balance()

if __name__ == "__main__":
    main()