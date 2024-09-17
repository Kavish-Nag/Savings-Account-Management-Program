

```md
# Savings Account Management Program

This is a simple Python program that simulates the management of savings accounts. Users can open an account, deposit money, withdraw money, and display user information.

## Features

1. **Open Savings Account**: Allows users to open a new savings account by providing personal details such as name, date of birth, occupation, contact number, and address.
2. **Deposit Money**: Users can deposit money into their account.
3. **Withdraw Money**: Users can withdraw money from their account, provided they have sufficient funds.
4. **Display User Information**: Displays a summary of the user's account information, including name, date of birth, occupation, contact number, address, and account balance.
5. **Exit**: Closes the program.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/savings-account-management.git
    ```

2. Navigate to the project directory:
    ```bash
    cd savings-account-management
    ```

3. Run the program:
    ```bash
    python savings_account.py
    ```

4. You'll be presented with the following options:
    ```
    1. Open Savings account.
    2. Deposit Money.
    3. Withdraw Money.
    4. Display User.
    5. Exit
    ```

## Program Details

### 1. Open Savings Account
- The user will be asked to provide the following details:
  - Name
  - Date of Birth (DD/MM/YY)
  - Occupation
  - Contact Number
  - Address
- Once the account is created, an initial balance of 0 will be set.

### 2. Deposit Money
- The user is required to log in with their name.
- Enter the amount to deposit.
- The balance will be updated accordingly.

### 3. Withdraw Money
- The user logs in with their name.
- Enter the amount to withdraw. The program checks if sufficient funds are available before completing the transaction.

### 4. Display User Information
- The user logs in with their name to view their account details, including their name, DOB, occupation, contact number, address, and current balance.

### 5. Exit
- This option will close the program.

## Example Usage

1. **Open an account**:
    ```
    Enter choice: 1
    Name of account holder: John Doe
    Date of birth(DD/MM/YY): 01/01/90
    Occupation: Teacher
    Contact no.: 1234567890
    Address: 123 Main Street
    Account opened successfully
    ```

2. **Deposit money**:
    ```
    Enter choice: 2
    Enter Name: John Doe
    Amount to be deposited: 5000
    Amount deposited successfully! 
    Current balance: 5000
    ```

3. **Withdraw money**:
    ```
    Enter choice: 3
    Enter Name: John Doe
    Amount to be withdrawn: 2000
    Withdrawn successfully! 
    Current balance: 3000
    ```

4. **Display user information**:
    ```
    Enter choice: 4
    Enter Name: John Doe
    User Profile
    Name: John Doe   DOB: 01/01/90
    Occupation: Teacher
    Contact number: 1234567890
    Address: 123 Main Street
    Account Balance: 3000
    ```

## Limitations

- The program currently stores account information in memory, so data will not persist after the program is closed.
- All users share the same data list (`Lst`), so if multiple accounts are opened, the data may not be stored correctly.
- Basic error handling is in place, but the program can be improved for better data management and validation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
