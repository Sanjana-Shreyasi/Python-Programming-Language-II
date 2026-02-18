#Class Bank Account
#Q Create a class to represent a bank account. Include attributes like account number, balance, and methods like deposit, withdraw and check balance.

class BankAccount:
    def __init__(self, AccountNumber, Balance):
        self.AccountNumber = AccountNumber
        self.Balance = Balance

    def deposit(self, Amount):
        if Amount > 0:
            self.Balance += Amount
            print(f"${Amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def Withdrawal(self, Amount):
        if Amount > 0:
            if Amount <= self.Balance:
                self.Balance -= Amount
                print(f"Withdrawn ${Amount}. Remaining Balance: ${self.Balance}")
            else:
                print("Insufficient Balance")
        else:
            print("Withdrawal amount must be positive.")

    def Check_Balance(self):
        print(f"Account Number: {self.AccountNumber}")
        print(f"Current Balance: ${self.Balance}")


# Create Account Object
Account = BankAccount("SBI1234", 10000)

while True:
    I = int(input("\nSelect Operation\n1) Deposit\n2) Withdrawal\n3) Check Balance\n4) Exit\n"))

    if I == 1:
        I1 = int(input("Enter amount to deposit: "))
        Account.deposit(I1)

    elif I == 2:
        I2 = int(input("Enter amount to withdraw: "))
        Account.Withdrawal(I2)

    elif I == 3:
        Account.Check_Balance()

    elif I == 4:
        print("Exiting")
        break

    else:
        print("Invalid choice. Please try again.")
