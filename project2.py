#####
# Author: Rachel Lee
# Assignment: Project 2
# Date: 6/24/2020
#####

import sys

# Read in file (e.g. CSV) with 6 entry data separated by ';' -> return dict key-paired by first entry (e.g. entry[0])
class Data_Read:

    def __init__(self, file_name):
        self.file_name = file_name
    
    def read_data(self):
        file_dict = {}
        try:
            file = open(self.file_name, 'r')
            for line in file:
                entry = line.rstrip('\n').split(';')
                # print(f"Entry : {entry}")
                tmp_map = {}
                tmp_map["first_name"] = entry[1]
                tmp_map["last_name"] = entry[2]
                tmp_map["password"] = entry[3]
                tmp_map["balance_checking"] = entry[4]
                tmp_map["balance_savings"] = entry[5]
                file_dict[entry[0]] = tmp_map
            file.close()
        except IOError:
            print(f"Error opening the file: {self.file_name}. Check if file exists or file path.")
            sys.exit()
        return file_dict

# Set account information into dictionary key-paired by account_id
# Inherit Data_Read class to read in files -> return dict
class Account_Set(Data_Read):

    def __init__(self, file_name):
        self.file_name = file_name
        # enable inheritance to Data_Read class to access class methods
        Data_Read.__init__(self, file_name=self.file_name)

# Functional actions for accounts
# Functions are set as class methods for objects to use for Account functionality
class Account_Action:

    def __init__(self):
        self.existing_accounts = {}
    # def __init__(self, bank_database, account):
    #     self.bank_database = bank_database
    #     self.account = account
    
    # reads in 2 dict params -> dict
    def add_customer(self, existing_accounts, new_accounts):
        self.existing_accounts = existing_accounts
        self.existing_accounts.update(new_accounts)
        return self.existing_accounts

    def withdraw_checking(self, existing_accounts, account_id, amount):
        self.existing_accounts = existing_accounts
        account_id = str(account_id)
        if account_id in existing_accounts:
            print(f"\n\nAccount {account_id} exists, withdrowing {amount}..")
            orig_amount = int(existing_accounts[account_id]['balance_checking'])
            new_amount = str(orig_amount - amount)
            print(f"NEW AMOUNT : {new_amount}\n")
            existing_accounts[account_id]['balance_checking'] = new_amount
            print(f"Account '{account_id}' updated values : ")
            print(existing_accounts[account_id])
            print("\n")
            # print(self.existing_accounts)
        else:
            print(f"\nError! Check account id entered. \nAccount {account_id} does not exist.\n")
        return self.existing_accounts

    def withdraw_savings(self, existing_accounts, account_id, amount):
        self.existing_accounts = existing_accounts
        account_id = str(account_id)
        if account_id in existing_accounts:
            print(f"\n\nAccount {account_id} exists, withdrowing {amount}..")
            orig_amount = int(existing_accounts[account_id]['balance_savings'])
            new_amount = str(orig_amount - amount)
            print(f"NEW AMOUNT : {new_amount}\n")
            existing_accounts[account_id]['balance_savings'] = new_amount
            print(f"Account '{account_id}' updated values : ")
            print(existing_accounts[account_id])
            print("\n")
            # print(self.existing_accounts)
        else:
            print(f"\nError! Check account id entered. \nAccount {account_id} does not exist.\n")
        return self.existing_accounts

    def deposit_checking(self, existing_accounts, account_id, amount):
        self.existing_accounts = existing_accounts
        account_id = str(account_id)
        if account_id in existing_accounts:
            print(f"\n\nAccount {account_id} exists, depositing {amount}..")
            orig_amount = int(existing_accounts[account_id]['balance_checking'])
            new_amount = str(orig_amount + amount)
            print(f"NEW AMOUNT : {new_amount}\n")
            existing_accounts[account_id]['balance_checking'] = new_amount
            print(f"Account '{account_id}' updated values : ")
            print(existing_accounts[account_id])
            print("\n")
            # print(self.existing_accounts)
        else:
            print(f"\nError! Check account id entered. \nAccount {account_id} does not exist.\n")
        return self.existing_accounts

    def deposit_savings(self, existing_accounts, account_id, amount):
        self.existing_accounts = existing_accounts
        account_id = str(account_id)
        if account_id in existing_accounts:
            print(f"\n\nAccount {account_id} exists, depositing {amount}..")
            orig_amount = int(existing_accounts[account_id]['balance_savings'])
            new_amount = str(orig_amount + amount)
            print(f"NEW AMOUNT : {new_amount}\n")
            existing_accounts[account_id]['balance_savings'] = new_amount
            print(f"Account '{account_id}' updated values : ")
            print(existing_accounts[account_id])
            print("\n")
            # print(self.existing_accounts)
        else:
            print(f"\nError! Check account id entered. \nAccount {account_id} does not exist.\n")
        return self.existing_accounts

    def transfer_to_checking(self, existing_accounts, account_id, amount):
        self.existing_accounts = existing_accounts
        account_id = str(account_id)
        if account_id in existing_accounts:
            print(f"\n\nAccount {account_id} exists, transferring {amount} from 'savings' to 'checking'..")
            checking_amt = int(existing_accounts[account_id]['balance_checking'])
            savings_amt = int(existing_accounts[account_id]['balance_savings'])
            new_checking_amt = str(checking_amt + amount)
            new_savings_amt = str(savings_amt - amount)
            print(f"NEW CHECKING AMOUNT : {new_checking_amt}\n")
            print(f"NEW SAVINGS AMOUNT : {new_savings_amt}\n")
            existing_accounts[account_id]['balance_checking'] = new_checking_amt
            existing_accounts[account_id]['balance_savings'] = new_savings_amt
            print(f"Account '{account_id}' updated values : ")
            print(existing_accounts[account_id])
            print("\n")
            # print(self.existing_accounts)
        else:
            print(f"\nError! Check account id entered. \nAccount {account_id} does not exist.\n")
        return self.existing_accounts

    def transfer_to_savings(self, existing_accounts, account_id, amount):
        self.existing_accounts = existing_accounts
        account_id = str(account_id)
        if account_id in existing_accounts:
            print(f"\n\nAccount {account_id} exists, transferring {amount} from 'checking' to 'savings'..")
            checking_amt = int(existing_accounts[account_id]['balance_checking'])
            savings_amt = int(existing_accounts[account_id]['balance_savings'])
            new_checking_amt = str(checking_amt - amount)
            new_savings_amt = str(savings_amt + amount)
            print(f"NEW CHECKING AMOUNT : {new_checking_amt}\n")
            print(f"NEW SAVINGS AMOUNT : {new_savings_amt}\n")
            existing_accounts[account_id]['balance_checking'] = new_checking_amt
            existing_accounts[account_id]['balance_savings'] = new_savings_amt
            print(f"Account '{account_id}' updated values : ")
            print(existing_accounts[account_id])
            print("\n")
            # print(self.existing_accounts)
        else:
            print(f"\nError! Check account id entered. \nAccount {account_id} does not exist.\n")
        return self.existing_accounts

    def trans_from_checking_ext(self, existing_accounts, account_id, amount, ext_id, ext_acct_type):
        self.existing_accounts = existing_accounts
        account_id = str(account_id)
        ext_id = str(ext_id)
        if ext_acct_type == 'checking':
            account_type = 'balance_checking'
        elif ext_acct_type == 'savings':
            account_type = 'balance_savings'
        else:
            print("Invalid account type!")

        if (account_id in existing_accounts):
            print(f"\n\nAccount {account_id} and {ext_id} exist.")
            print(f"Transferring {amount} from 'checking account' Account_ID: '{account_id}'  to '{ext_acct_type} account' Account_ID: '{ext_id}' ..")
            checking_amt = int(existing_accounts[account_id]['balance_checking'])
            ext_amt = int(existing_accounts[ext_id][account_type])
            print(f"CHECKING AMT : {checking_amt}")
            print(f"EXT AMT : {ext_amt}")
            new_checking_amt = str(checking_amt - amount)
            new_ext_amt = str(ext_amt + amount)
            print(f"\nNEW CHECKING AMOUNT : {new_checking_amt}")
            print(f"NEW EXT AMOUNT : {new_ext_amt}\n")
            existing_accounts[account_id]['balance_checking'] = new_checking_amt
            existing_accounts[ext_id][account_type] = new_ext_amt
            print(f"Account '{account_id}' updated values : ")
            print(existing_accounts[account_id])
            print("\n")
            print(f"Account '{ext_id}' updated values : ")
            print(existing_accounts[ext_id])
            print("\n")
            print(self.existing_accounts)
        else:
            print(f"\nError! Check account id entered. \nAccount {account_id} does not exist.\n")
        return self.existing_accounts

    def trans_from_savings_ext(self, existing_accounts, account_id, amount, ext_id, ext_acct_type):
        self.existing_accounts = existing_accounts
        account_id = str(account_id)
        ext_id = str(ext_id)
        if ext_acct_type == 'checking':
            account_type = 'balance_checking'
        elif ext_acct_type == 'savings':
            account_type = 'balance_savings'
        else:
            print("Invalid account type!")

        if (account_id in existing_accounts):
            print(f"\n\nAccount {account_id} and {ext_id} exist.")
            print(f"Transferring {amount} from 'savings account' Account_ID: '{account_id}'  to '{ext_acct_type} account' Account_ID: '{ext_id}' ..")
            checking_amt = int(existing_accounts[account_id]['balance_savings'])
            ext_amt = int(existing_accounts[ext_id][account_type])
            print(f"SAVINGS AMT : {checking_amt}")
            print(f"EXT AMT : {ext_amt}")
            new_checking_amt = str(checking_amt - amount)
            new_ext_amt = str(ext_amt + amount)
            print(f"\nNEW SAVINGS AMOUNT : {new_checking_amt}")
            print(f"NEW EXT AMOUNT : {new_ext_amt}\n")
            existing_accounts[account_id]['balance_savings'] = new_checking_amt
            existing_accounts[ext_id][account_type] = new_ext_amt
            print(f"Account '{account_id}' updated values : ")
            print(existing_accounts[account_id])
            print("\n")
            print(f"Account '{ext_id}' updated values : ")
            print(existing_accounts[ext_id])
            print("\n")
            print(self.existing_accounts)
        else:
            print(f"\nError! Check account id entered. \nAccount {account_id} does not exist.\n")
        return self.existing_accounts



    @classmethod
    def login(cls):
        print("user login")

# All customers account info and accessible manipulation of customer data
class Bank_Database(Account_Action):

    def __init__(self):
        self.database = {}
        Account_Action.__init__(self)

    # get bank accounts information
    def get_accounts(self):
        return self.database

    # set bank accounts information
    def set_accounts(self, customer_accounts):
        self.database = customer_accounts

    # bank = property(fget=get_accounts, fset=set_accounts)

    # method to add a dict of accounts to existing account database
    def add_accounts(self, new_accounts):
        tmp_database = {}
        for key, val in new_accounts.items():
            if key not in self.database:
                print(f"Account '{key}' does not exist, added to bank account database.")
                # print(f"Values {val} added.")
                tmp_database[key] = val
            else:
                print(f"Account '{key}' is a duplicate account.")
                # print(f"{key} : {val} exists.")    

        self.database.update(tmp_database)
        # print(self.database)
        # print(self.database.keys())
        return self.database
        


# Interactive console for Bank setup and transactions
def main():
    print("\n")
    print("===========================================================")
    print("============== Welcome to our Banking System ==============")
    print("===========================================================")
    print("\n")

    # Prompt_1
    prompt_1 = int(input("Enter option... \n- '1' to Continue. \n- '2' to Exit. \nEnter: "))
    
    # Prompt_1 - Option 1
    if prompt_1 == 1:
        print("\n")
        file1 = input("Enter file name to import list of accounts: ")  
    # Prompt_1 - Option 2
    elif prompt_1 == 2:
        sys.exit("Exiting system... ")
    else:
        print("Input is invalid. Please try again.\n")

        # while loop to count input attempts for prompt_1
        counter_1 = 0
        while counter_1 < 2:
            prompt_1 = int(input("Enter option... \n- '1' to Continue. \n- '2' to Exit. \nEnter: "))

            # Prompt_1 - Option 1
            if prompt_1 == 1:
                print("\n")
                file1 = input("Enter file name to import list of accounts: ")
                break
            # Prompt_1 - Option 2
            elif prompt_1 == 2:
                sys.exit("\nExiting system... ")
                break
            else:
                print("\nInput is invalid. Please try again.\n")
                counter_1 += 1
        else: 
            sys.exit("\nToo many attempts. Exiting system... ")
    
    # Set bank for Prompt_1 - Option 1
    accounts1 = Account_Set(file1).read_data()
    Bank = Bank_Database()
    Bank.set_accounts(accounts1)
    print(Bank.get_accounts())

    print("\n")
    print("\n")
    print("===========================================================")
    print("============== Welcome to our Banking System ==============")
    print("===========================================================")
    print("\n")
    
    # Prompt_2
    prompt_2 = int(input("Enter option... \n- '1' to Get list of existing bank accounts. \n- '2' to Add new list of accounts to existing bank accounts. \n- '3' to Withdraw, Deposit, or Transfer. \n- '4' to Exit. \nEnter: "))
    # Prompt_2 - Option 1
    if prompt_2 == 1:
        # Run : Prompt_2 - Option 1
        accounts = Bank.get_accounts()
        print("\n")
        print("Current existing bank accounts listed below : ")
        for key, val in accounts.items():
            first = accounts[key]['first_name']
            last = accounts[key]['last_name']
            print(f"Account ID: {key}, Account Holder: {last.capitalize()}, {first.capitalize()}")
    # Prompt_2 - Option 2
    elif prompt_2 == 2:
        print("\n")
        print("===========================================================")
        print("=== Add new list of accounts to existing bank accounts ====")
        print("===========================================================")
        print("\n")
        print("Would you like to enter a new customer or add a list of accounts to the existing bank?")
        question_2 = int(input("Enter option... \n- '1' to Add a new customer \n- '2' to Add a list of accounts to existing Bank database. \n- Enter: "))
        print("\n")

        # Prompt_2 - Option 2 -> Option 1
        if question_2 == 1:
            print("Adding a new customer... \nPlease make sure to have customer info in a .csv file and enter file name.")
            file2 = input("Enter file name: ")
            accounts2 = Account_Set(file2).read_data()
            Bank.add_customer(accounts1, accounts2)
        # Prompt_2 - Option 2 -> Option 2
        elif question_2 == 2:
            print("Adding list of accounts to existing Bank. Specify file in .csv format.")
            file2 = input("Enter file name: ")
            accounts2 = Account_Set(file2).read_data()
            Bank.add_accounts(accounts2)
        else:
            print("\nInput is invalid. Please try again.\n")
            
            # while loop to count input attempts for question_2
            counter_3 = 0
            while counter_3 < 2:
                print("Would you like to enter a new customer or add a list of accounts to the existing bank?")
                question_2 = int(input("Enter option... \n- '1' to Add a new customer \n- '2' to Add a list of accounts to existing Bank database. \n- Enter: "))
                if question_2 == 1:
                    print("Adding a new customer... \nPlease make sure to have customer info in a .csv file and enter file name.")
                    file2 = input("Enter file name: ")
                    accounts2 = Account_Set(file2).read_data()
                    Bank.add_customer(accounts1, accounts2)
                    break
                elif question_2 == 2:
                    print("Adding list of accounts to existing Bank. Specify file in .csv format.")
                    file2 = input("Enter file name: ")
                    accounts2 = Account_Set(file2).read_data()
                    Bank.add_accounts(accounts2)
                    break
                else:
                    print("\nInput is invalid. Please try again.\n")
                    counter_3 += 1
            else: 
                sys.exit("\nToo many attempts. Exiting system... ")
        
        # Run : Prompt_2 - Option 2
        print("\n")
        print("Account(s) have been added. List of all accounts in Bank below: ")
        print(Bank.get_accounts())

    # Prompt_2 - Option 3
    elif prompt_2 == 3:      
        print("\n")
        print("===========================================================")
        print("========== Withdraw, Deposit, or Transfer Money ===========")
        print("===========================================================")
        print("\n")
        print("Would you like to Withdraw, Deposit, or Transfer money?")
        question_3 = int(input("Enter option... \n- '1' to Withdraw. \n- '2' to Deposit. \n- '3' to Transfer. \n- Enter: "))
        print("\n")

        # Prompt_2 - Option 3 -> Option 1
        if question_3 == 1:
            print("Withdrawing money... \nPlease enter Account ID, Account Type (checking/savings), and Amount to Withdraw.")
            account_num = int(input("Enter Account ID: "))
            account_type = input("Enter Account Type: ")
            amount = int(input("Enter Withdrawal Amount: "))
            existing_accounts = Bank.get_accounts()
            
            # check account type input
            if account_type == 'checking':
                Bank.withdraw_checking(existing_accounts, account_num, amount)
                existing_accounts = Bank.get_accounts()
            elif account_type == 'savings':
                Bank.withdraw_savings(existing_accounts, account_num, amount)
                existing_accounts = Bank.get_accounts()
            else:
                sys.exit("\nInput is invalid. Exiting system... ")

        # Prompt_2 - Option 3 -> Option 2
        elif question_3 == 2:
            print("Depositing money... \nPlease enter Account ID, Account Type (checking/savings), and Amount to Deposit.")
            account_num = int(input("Enter Account ID: "))
            account_type = input("Enter Account Type: ")
            amount = int(input("Enter Deposit Amount: "))
            existing_accounts = Bank.get_accounts()
            
            # check account type input
            if account_type == 'checking':
                Bank.deposit_checking(existing_accounts, account_num, amount)
                existing_accounts = Bank.get_accounts()
            elif account_type == 'savings':
                Bank.deposit_savings(existing_accounts, account_num, amount)
                existing_accounts = Bank.get_accounts()
            else:
                sys.exit("\nInput is invalid. Exiting system... ")

        # Prompt_2 - Option 3 -> Option 3
        elif question_3 == 3:
            print("Transfer to internal or external account?")
            option_type = input("Enter option (internal/external): ")
            
            if option_type == 'internal':
                print("Transferring money between internal accounts... \nPlease enter Account ID, Account Type transferring to - (checking/savings), and Amount to Transfer.")
                account_num = int(input("Enter Account ID: "))
                account_type = input("Enter Account Type: ")
                amount = int(input("Enter Deposit Amount: "))
                existing_accounts = Bank.get_accounts()
                
                # check account type input
                if account_type == 'checking':
                    Bank.transfer_to_checking(existing_accounts, account_num, amount)
                    existing_accounts = Bank.get_accounts()
                elif account_type == 'savings':
                    Bank.transfer_to_savings(existing_accounts, account_num, amount)
                    existing_accounts = Bank.get_accounts()
                else:
                    sys.exit("\nInput is invalid. Exiting system... ")

            elif option_type == 'external':
                print("Transferring money between external accounts... \nPlease enter Account IDs, Account Type transferring to - (checking/savings), and Amount to Transfer.")
                id_from = int(input("Enter Account ID transferring FROM: "))
                type_from = input("Enter Account Type: ")
                id_to = int(input("Enter Account ID transferring TO: "))
                type_to = input("Enter Account Type: ")
                amount = int(input("Enter Deposit Amount: "))
                existing_accounts = Bank.get_accounts()
                
                # check account type input
                if type_from == 'checking':
                    Bank.trans_from_checking_ext(existing_accounts, id_from, amount, id_to, type_to)
                    existing_accounts = Bank.get_accounts()
                elif type_from == 'savings':
                    Bank.trans_from_savings_ext(existing_accounts, id_from, amount, id_to, type_to)
                    existing_accounts = Bank.get_accounts()
                else:
                    sys.exit("\nInput is invalid. Exiting system... ")
            else:
                    sys.exit("\nInput is invalid. Exiting system... ")
        else:
            print("\nInput is invalid. Please try again.\n")

            # while loop to count input attempts for question_3
            counter_4 = 0
            while counter_4 < 2:
                print("\n")
                print("===========================================================")
                print("========== Withdraw, Deposit, or Transfer Money ===========")
                print("===========================================================")
                print("\n")
                print("Would you like to Withdraw, Deposit, or Transfer money?")
                question_3 = int(input("Enter option... \n- '1' to Withdraw. \n- '2' to Deposit. \n- '3' to Transfer. \n- Enter: "))
                print("\n")

                # Prompt_2 - Option 3 -> Option 1
                if question_3 == 1:
                    print("Withdrawing money... \nPlease enter Account ID, Account Type (checking/savings), and Amount to Withdraw.")
                    account_num = int(input("Enter Account ID: "))
                    account_type = input("Enter Account Type: ")
                    amount = int(input("Enter Withdrawal Amount: "))
                    existing_accounts = Bank.get_accounts()
                    
                    # check account type input
                    if account_type == 'checking':
                        Bank.withdraw_checking(existing_accounts, account_num, amount)
                        existing_accounts = Bank.get_accounts()
                    elif account_type == 'savings':
                        Bank.withdraw_savings(existing_accounts, account_num, amount)
                        existing_accounts = Bank.get_accounts()
                    else:
                        sys.exit("\nInput is invalid. Exiting system... ")

                    break #break out of while loop prompt_2/counter_4

                # Prompt_2 - Option 3 -> Option 2
                elif question_3 == 2:
                    print("Depositing money... \nPlease enter Account ID, Account Type (checking/savings), and Amount to Deposit.")
                    account_num = int(input("Enter Account ID: "))
                    account_type = input("Enter Account Type: ")
                    amount = int(input("Enter Deposit Amount: "))
                    existing_accounts = Bank.get_accounts()
                    
                    # check account type input
                    if account_type == 'checking':
                        Bank.deposit_checking(existing_accounts, account_num, amount)
                        existing_accounts = Bank.get_accounts()
                    elif account_type == 'savings':
                        Bank.deposit_savings(existing_accounts, account_num, amount)
                        existing_accounts = Bank.get_accounts()
                    else:
                        sys.exit("\nInput is invalid. Exiting system... ")

                    break #break out of while loop prompt_2/counter_4

                # Prompt_2 - Option 3 -> Option 3
                elif question_3 == 3:
                    print("Transfer to internal or external account?")
                    option_type = input("Enter option (internal/external): ")
                    
                    if option_type == 'internal':
                        print("Transferring money between internal accounts... \nPlease enter Account ID, Account Type transferring to - (checking/savings), and Amount to Transfer.")
                        account_num = int(input("Enter Account ID: "))
                        account_type = input("Enter Account Type: ")
                        amount = int(input("Enter Deposit Amount: "))
                        existing_accounts = Bank.get_accounts()
                        
                        # check account type input
                        if account_type == 'checking':
                            Bank.transfer_to_checking(existing_accounts, account_num, amount)
                            existing_accounts = Bank.get_accounts()
                        elif account_type == 'savings':
                            Bank.transfer_to_savings(existing_accounts, account_num, amount)
                            existing_accounts = Bank.get_accounts()
                        else:
                            sys.exit("\nInput is invalid. Exiting system... ")
                        

                    elif option_type == 'external':
                        print("Transferring money between external accounts... \nPlease enter Account IDs, Account Type transferring to - (checking/savings), and Amount to Transfer.")
                        id_from = int(input("Enter Account ID transferring FROM: "))
                        type_from = input("Enter Account Type: ")
                        id_to = int(input("Enter Account ID transferring TO: "))
                        type_to = input("Enter Account Type: ")
                        amount = int(input("Enter Deposit Amount: "))
                        existing_accounts = Bank.get_accounts()
                        
                        # check account type input
                        if type_from == 'checking':
                            Bank.trans_from_checking_ext(existing_accounts, id_from, amount, id_to, type_to)
                            existing_accounts = Bank.get_accounts()
                        elif type_from == 'savings':
                            Bank.trans_from_savings_ext(existing_accounts, id_from, amount, id_to, type_to)
                            existing_accounts = Bank.get_accounts()
                        else:
                            sys.exit("\nInput is invalid. Exiting system... ")
                    else:
                        sys.exit("\nInput is invalid. Exiting system... ")
                
                else:
                    counter_4 += 1
                # break #break out of while loop prompt_2/counter_4

    # Prompt_2 - Option 4
    elif prompt_2 == 4:
        sys.exit("\nExiting system... ")
    else:
        print("\nInput is invalid. Please try again.\n")
        
        # while loop to count input attempts for prompt_2
        counter_2 = 0
        while counter_2 < 2:
            prompt_2 = int(input("Enter option... \n- '1' to Get list of existing bank accounts. \n- '2' to Add new list of accounts to existing bank accounts. \n- '3' to Withdraw, Deposit, or Transfer. \n- '4' to Exit. \nEnter: "))
            # Prompt_2 - Option 1           
            if prompt_2 == 1:
                accounts = Bank.get_accounts()
                for key, val in accounts.items():
                    first = accounts[key]['first_name']
                    last = accounts[key]['last_name']
                    print(f"Account ID: {key}, Account Holder: {last.capitalize()}, {first.capitalize()}")
                break #break out of while loop prompt_2/counter_2
            # Prompt_2 - Option 2
            elif prompt_2 == 2:
                print("\n")
                print("===========================================================")
                print("=== Add new list of accounts to existing bank accounts ====")
                print("===========================================================")
                print("\n")
                print("Would you like to enter a new customer or add a list of accounts to the existing bank?")
                question_2 = int(input("Enter option... \n- '1' to Add a new customer \n- '2' to Add a list of accounts to existing Bank database. \n- Enter: "))
                print("\n")

                # Prompt_2 - Option 2 -> Option 1
                if question_2 == 1:
                    print("Adding a new customer... \nPlease make sure to have customer info in a .csv file and enter file name.")
                    file2 = input("Enter file name: ")
                    accounts2 = Account_Set(file2).read_data()
                    Bank.add_customer(accounts1, accounts2)
                # Prompt_2 - Option 2 -> Option 2
                elif question_2 == 2:
                    print("Adding list of accounts to existing Bank. Specify file in .csv format.")
                    file2 = input("Enter file name: ")
                    accounts2 = Account_Set(file2).read_data()
                    Bank.add_accounts(accounts2)
                else:
                    print("\nInput is invalid. Please try again.\n")
                    
                    # while loop to count input attempts for question_2
                    counter_3 = 0
                    while counter_3 < 2:
                        print("Would you like to enter a new customer or add a list of accounts to the existing bank?")
                        question_2 = int(input("Enter option... \n- '1' to Add a new customer \n- '2' to Add a list of accounts to existing Bank database. \n- Enter: "))
                        if question_2 == 1:
                            print("Adding a new customer... \nPlease make sure to have customer info in a .csv file and enter file name.")
                            file2 = input("Enter file name: ")
                            accounts2 = Account_Set(file2).read_data()
                            Bank.add_customer(accounts1, accounts2)
                            break #break out of while loop question_2/counter_3
                        elif question_2 == 2:
                            print("Adding list of accounts to existing Bank. Specify file in .csv format.")
                            file2 = input("Enter file name: ")
                            accounts2 = Account_Set(file2).read_data()
                            Bank.add_accounts(accounts2)
                            break #break out of while loop question_2/counter_3
                        else:
                            print("\nInput is invalid. Please try again.\n")
                            counter_3 += 1
                    else: 
                        sys.exit("\nToo many attempts. Exiting system... ")
                
                # Run : Prompt_2 - Option 2
                print("\n")
                print("Account(s) have been added. List of all accounts in Bank below: ")
                print(Bank.get_accounts())
                break #break out of while loop prompt_2/counter_2

            # Prompt_2 - Option 3
            elif prompt_2 == 3:
                print("\n")
                print("===========================================================")
                print("========== Withdraw, Deposit, or Transfer Money ===========")
                print("===========================================================")
                print("\n")
                print("Would you like to Withdraw, Deposit, or Transfer money?")
                question_3 = int(input("Enter option... \n- '1' to Withdraw. \n- '2' to Deposit. \n- '3' to Transfer. \n- Enter: "))
                print("\n")

                # Prompt_2 - Option 3 -> Option 1
                if question_3 == 1:
                    print("Withdrawing money... \nPlease enter Account ID, Account Type (checking/savings), and Amount to Withdraw.")
                    account_num = input("Enter Account ID: ")
                    account_type = input("Enter Account Type: ")
                    amount = input("Enter Withdrawal Amount: ")
                    existing_accounts = Bank.get_accounts()
                    
                    # check account type input
                    if account_type == 'checking':
                        Bank.withdraw_checking(existing_accounts, account_num, amount)
                        existing_accounts = Bank.get_accounts()
                    elif account_type == 'savings':
                        Bank.withdraw_savings(existing_accounts, account_num, amount)
                        existing_accounts = Bank.get_accounts()
                    else:
                        sys.exit("\nInput is invalid. Exiting system... ")

                # Prompt_2 - Option 3 -> Option 2
                elif question_3 == 2:
                    print("Depositing money... \nPlease enter Account ID, Account Type (checking/savings), and Amount to Deposit.")
                    account_num = input("Enter Account ID: ")
                    account_type = input("Enter Account Type: ")
                    amount = input("Enter Deposit Amount: ")
                    existing_accounts = Bank.get_accounts()
                    
                    # check account type input
                    if account_type == 'checking':
                        Bank.deposit_checking(existing_accounts, account_num, amount)
                        existing_accounts = Bank.get_accounts()
                    elif account_type == 'savings':
                        Bank.deposit_savings(existing_accounts, account_num, amount)
                        existing_accounts = Bank.get_accounts()
                    else:
                        sys.exit("\nInput is invalid. Exiting system... ")

                # Prompt_2 - Option 3 -> Option 3
                elif question_3 == 3:
                    print("Transfer to internal or external account?")
                    option_type = input("Enter option (internal/external): ")
                    
                    if option_type == 'internal':
                        print("Transferring money between internal accounts... \nPlease enter Account ID, Account Type transferring to - (checking/savings), and Amount to Transfer.")
                        account_num = input("Enter Account ID: ")
                        account_type = input("Enter Account Type: ")
                        amount = input("Enter Deposit Amount: ")
                        existing_accounts = Bank.get_accounts()
                        
                        # check account type input
                        if account_type == 'checking':
                            Bank.transfer_to_checking(existing_accounts, account_num, amount)
                            existing_accounts = Bank.get_accounts()
                        elif account_type == 'savings':
                            Bank.transfer_to_savings(existing_accounts, account_num, amount)
                            existing_accounts = Bank.get_accounts()
                        else:
                            sys.exit("\nInput is invalid. Exiting system... ")

                    elif option_type == 'external':
                        print("Transferring money between external accounts... \nPlease enter Account IDs, Account Type transferring to - (checking/savings), and Amount to Transfer.")
                        id_from = input("Enter Account ID transferring FROM: ")
                        type_from = input("Enter Account Type: ")
                        id_to = input("Enter Account ID transferring TO: ")
                        type_to = input("Enter Account Type: ")
                        amount = input("Enter Deposit Amount: ")
                        existing_accounts = Bank.get_accounts()
                        
                        # check account type input
                        if type_from == 'checking':
                            Bank.trans_from_checking_ext(existing_accounts, id_from, amount, id_to, type_to)
                            existing_accounts = Bank.get_accounts()
                        elif type_from == 'savings':
                            Bank.trans_from_savings_ext(existing_accounts, id_from, amount, id_to, type_to)
                            existing_accounts = Bank.get_accounts()
                        else:
                            sys.exit("\nInput is invalid. Exiting system... ")
                    else:
                            sys.exit("\nInput is invalid. Exiting system... ")
                else:
                    print("\nInput is invalid. Please try again.\n")

                # while loop to count input attempts for question_3
                counter_4 = 0
                while counter_4 < 2:
                    print("\n")
                    print("===========================================================")
                    print("========== Withdraw, Deposit, or Transfer Money ===========")
                    print("===========================================================")
                    print("\n")
                    print("Would you like to Withdraw, Deposit, or Transfer money?")
                    question_3 = int(input("Enter option... \n- '1' to Withdraw. \n- '2' to Deposit. \n- '3' to Transfer. \n- Enter: "))
                    print("\n")

                    # Prompt_2 - Option 3 -> Option 1
                    if question_3 == 1:
                        print("Withdrawing money... \nPlease enter Account ID, Account Type (checking/savings), and Amount to Withdraw.")
                        account_num = input("Enter Account ID: ")
                        account_type = input("Enter Account Type: ")
                        amount = input("Enter Withdrawal Amount: ")
                        existing_accounts = Bank.get_accounts()
                        
                        # check account type input
                        if account_type == 'checking':
                            Bank.withdraw_checking(existing_accounts, account_num, amount)
                            existing_accounts = Bank.get_accounts()
                        elif account_type == 'savings':
                            Bank.withdraw_savings(existing_accounts, account_num, amount)
                            existing_accounts = Bank.get_accounts()
                        else:
                            sys.exit("\nInput is invalid. Exiting system... ")

                        break #break out of while loop prompt_2/counter_4

                    # Prompt_2 - Option 3 -> Option 2
                    elif question_3 == 2:
                        print("Depositing money... \nPlease enter Account ID, Account Type (checking/savings), and Amount to Deposit.")
                        account_num = input("Enter Account ID: ")
                        account_type = input("Enter Account Type: ")
                        amount = input("Enter Deposit Amount: ")
                        existing_accounts = Bank.get_accounts()
                        
                        # check account type input
                        if account_type == 'checking':
                            Bank.deposit_checking(existing_accounts, account_num, amount)
                            existing_accounts = Bank.get_accounts()
                        elif account_type == 'savings':
                            Bank.deposit_savings(existing_accounts, account_num, amount)
                            existing_accounts = Bank.get_accounts()
                        else:
                            sys.exit("\nInput is invalid. Exiting system... ")

                        break #break out of while loop prompt_2/counter_4

                    # Prompt_2 - Option 3 -> Option 3
                    elif question_3 == 3:
                        print("Transfer to internal or external account?")
                        option_type = input("Enter option (internal/external): ")
                        
                        if option_type == 'internal':
                            print("Transferring money between internal accounts... \nPlease enter Account ID, Account Type transferring to - (checking/savings), and Amount to Transfer.")
                            account_num = input("Enter Account ID: ")
                            account_type = input("Enter Account Type: ")
                            amount = input("Enter Deposit Amount: ")
                            existing_accounts = Bank.get_accounts()
                            
                            # check account type input
                            if account_type == 'checking':
                                Bank.transfer_to_checking(existing_accounts, account_num, amount)
                                existing_accounts = Bank.get_accounts()
                            elif account_type == 'savings':
                                Bank.transfer_to_savings(existing_accounts, account_num, amount)
                                existing_accounts = Bank.get_accounts()
                            else:
                                sys.exit("\nInput is invalid. Exiting system... ")
                            
                            # break #break out of while loop prompt_2/counter_4

                        elif option_type == 'external':
                            print("Transferring money between external accounts... \nPlease enter Account IDs, Account Type transferring to - (checking/savings), and Amount to Transfer.")
                            id_from = input("Enter Account ID transferring FROM: ")
                            type_from = input("Enter Account Type: ")
                            id_to = input("Enter Account ID transferring TO: ")
                            type_to = input("Enter Account Type: ")
                            amount = input("Enter Deposit Amount: ")
                            existing_accounts = Bank.get_accounts()
                            
                            # check account type input
                            if type_from == 'checking':
                                Bank.trans_from_checking_ext(existing_accounts, id_from, amount, id_to, type_to)
                                existing_accounts = Bank.get_accounts()
                            elif type_from == 'savings':
                                Bank.trans_from_savings_ext(existing_accounts, id_from, amount, id_to, type_to)
                                existing_accounts = Bank.get_accounts()
                            else:
                                sys.exit("\nInput is invalid. Exiting system... ")
                            
                            # break #break out of while loop prompt_2/counter_4
                                
                        else:
                                sys.exit("\nInput is invalid. Exiting system... ")
                    
                        break #break out of while loop prompt_2/counter_4

                    break #break out of while loop prompt_2/counter_2

                # Run : Prompt_2 - Option 2
                print("\n")
                print("Account Action completed. List of all accounts and balance in Bank below: ")
                print(Bank.get_accounts())
                break #break out of while loop prompt_2/counter_4

            # Prompt_2 - Option 4
            elif prompt_2 == 4:
                sys.exit("Exiting system... ")
                break
            else:
                print("\nInput is invalid. Please try again.\n")
                counter_2 += 1
        else: 
            sys.exit("\nToo many attempts. Exiting system... ")

    # accounts2 = Account_Set("bank2.csv").read_data()



    
    print("\n\n\n")

main()



# ################ TEST CODE ################
# ###### - Individual Functionality - #######
# ###########################################
# ''' set 1st and 2nd accounts '''
# accounts1 = Account_Set("bank.csv").read_data()
# accounts2 = Account_Set("bank2.csv").read_data()
# # print(accounts1)
# # print(accounts2)
# # print('\n\n')

# ''' set a Bank object/database for list of all accounts '''
# Bank = Bank_Database()
# Bank.set_accounts(accounts1)
# # print(Bank.get_accounts())
# # print(Bank.get_accounts().keys())
# # print('\n\n')

# ''' add 2nd accounts to 1st accounts and store in Bank database '''
# Bank.add_accounts(accounts2)
# # print(Bank.get_accounts())
# # print(Bank.get_accounts().keys())
# # print('\n\n')

# ''' validate attempt to re-add accounts already added are avoided '''
# print(Bank.add_accounts(accounts2))
# # print(Bank.get_accounts())
# # print(Bank.get_accounts().keys())
# # print('\n\n')

# ''' retrieve all bank account info from Bank database '''
# existing_accounts = Bank.get_accounts()
# # print("Existing accounts : ", existing_accounts)
# # print("Account Keys : ", existing_accounts.keys())
# # print('\n\n')

# ''' BEGIN Separate Test for Bank_Database class and add_accounts method '''
# # customers = Bank.add_accounts(accounts2)
# # print("\n\nCUSTOMERS : \n", customers)
# # # print(customers.keys())
# # # print(type(Bank))
# # # print(type(customers))

# # Bank = Bank_Database(customers)
# # customers2 = Bank.add_accounts(accounts2)
# # print(customers2)
# ''' END of Seperate Test '''

# ''' set new test object for new accounts '''
# new_account = Account_Set("bank3.csv").read_data()
# # print(new_account)
# print(new_account.keys())
# print('\n\n')

# ''' Test add_customer method of Bank_Database class'''
# Bank.add_customer(existing_accounts, new_account)
# print(Bank.get_accounts())
# print(Bank.get_accounts().keys())

# ''' Test withdraw_checking method of Account_Action class'''
# # existing_accounts = Bank.get_accounts()
# # Bank.withdraw_checking(existing_accounts, 20005, 1000)
# # print(Bank.get_accounts())

# ''' Test withdraw_savings method of Account_Action class'''
# # existing_accounts = Bank.get_accounts()
# # Bank.withdraw_savings(existing_accounts, 20005, 3000)
# # print(Bank.get_accounts())

# ''' Test deposit_checking method of Account_Action class'''
# # existing_accounts = Bank.get_accounts()
# # Bank.deposit_checking(existing_accounts, 20005, 500)
# # print(Bank.get_accounts())

# ''' Test deposit_savings method of Account_Action class'''
# # existing_accounts = Bank.get_accounts()
# # Bank.deposit_savings(existing_accounts, 20005, 7000)
# # print(Bank.get_accounts())

# ''' Test transfer_to_checking method of Account_Action class'''
# # existing_accounts = Bank.get_accounts()
# # Bank.transfer_to_checking(existing_accounts, 20005, 500)
# # print(Bank.get_accounts())

# ''' Test transfer_to_savings method of Account_Action class'''
# # existing_accounts = Bank.get_accounts()
# # Bank.transfer_to_savings(existing_accounts, 20005, 500)
# # print(Bank.get_accounts())

# ''' Test non-existent account '''
# # existing_accounts = Bank.get_accounts()
# # Bank.transfer_to_savings(existing_accounts, 20025, 500)
# # print(Bank.get_accounts())

# ''' Test trans_from_checking_ext method of Account_Action class'''
# # existing_accounts = Bank.get_accounts()
# # Bank.trans_from_checking_ext(existing_accounts, 20005, 500, 20001, 'savings')
# # print(Bank.get_accounts())

# ''' Test trans_from_savings_ext method of Account_Action class'''
# # existing_accounts = Bank.get_accounts()
# # Bank.trans_from_savings_ext(existing_accounts, 20005, 500, 20001, 'checking')
# # print(Bank.get_accounts())