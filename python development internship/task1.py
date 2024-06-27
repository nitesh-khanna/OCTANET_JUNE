class CardHolders():
    def __init__(self, name, cardNum, pin, balance):
        self.name=name
        self.cardNum=cardNum
        self.pin=pin
        self.balance=balance
    
    def getName(self):
        return self.name
    def getCardNum(self):
        return self.cardNum
    def getPin(self):
        return self.pin
    def getBalance(self):
        return self.balance
    
    def deposit(self):
        try:
            amount=int(input('enter amount to be deposited: '))
            self.balance+=amount
            print(f'{amount} has been deposited into your account')
        except:
            print('invalid input')
    
    def withdraw(self):
        try:
            amount=int(input('enter amount to be withdrawn: '))
            if(amount>self.balance):
                print('insufficient balance')
            else:
                self.balance-=amount
                print(f'{amount} has been withdrawn from your account')
        except:
            print('invalid input')
    def transfer(self):
        while True:
            try:
                card_number=input("enter receiver's card number: ")
                acc_match=[holder for holder in CardHolders_list if holder.cardNum==card_number]
                if(len(acc_match)>0):
                    break
                else:
                    print('Card number not recognised. Please  try again.')
            except:
                print('Card number not recognised. Please  try again.')
        amount=int(input('enter amount to be transferred: '))
        if(self.balance>=amount):
            self.balance-=amount
            acc_match[0].balance+=amount
            print(f'{amount} has been transferred to card number {acc_match[0].cardNum}')
        else:
            print('Insufficient balance')

current_user=CardHolders('','','','')
CardHolders_list=[]
CardHolders_list.append(CardHolders('Jack','987654321012345',4382,10000))
CardHolders_list.append(CardHolders('Mohan','123456789012345',6163,15000))
CardHolders_list.append(CardHolders('Tom','132464576897012',5544,9000))
CardHolders_list.append(CardHolders('Harry','907867546324138',3090,19000))
while True:
    try:
        card_number=input('enter your card number: ')
        acc_match=[holder for holder in CardHolders_list if holder.cardNum==card_number]
        if(len(acc_match)>0):
            current_user=acc_match[0]
            break
        else:
            print('Card number not recognised. Please  try again.')
    except:
        print('Card number not recognised. Please  try again.')

while True:
    try:
        pin=int(input('enter your pin: '))
        if(current_user.getPin()==pin):
            break
        else:
            print('Incorrect pin. Please  try again.')
    except:
        print('Invalid pin. Please  try again.')

print('Welcome',current_user.name,'!')
while True:
    print()
    print('''Choose one of the following:
        1. Deposit
        2. Withdrawal
        3. Transfer
        4. Balance
        5. Exit''')
    print()
    try:
        choice=int(input('enter your choice: '))
        if(choice==1):
            current_user.deposit()
        elif(choice==2):
            current_user.withdraw()
        elif(choice==3):
            current_user.transfer()
        elif(choice==4):
            print('Your current balance is',current_user.getBalance())
        elif(choice==5):
            break
        else:
            print('invalid choice')
    except:
        print('invalid choice')
