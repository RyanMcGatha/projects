class BudgetBot:
    def __init__(self, start_balance):
        self.start_balance = start_balance
        self.transactions = {
            'deposits': {
                'categorys': {}
            },
            'withdraws': {
                'categorys': {}
            }
        }

    def current_balance(self):
        deposits_sum = sum(sum(cat) for cat in self.transactions['deposits']['categorys'].values())
        withdraws_sum = sum(sum(cat) for cat in self.transactions['withdraws']['categorys'].values())
        return self.start_balance + deposits_sum - withdraws_sum

    def list_transactions(self):
        trans_type = input('Deposits or withdraws? ')
        key = True
        while key:
            if trans_type == 'deposits':
                self.list_categories('deposits')
            elif trans_type == 'withdraws':
                self.list_categories('withdraws')
            else:
                print('Invalid input. Please enter "deposits" or "withdraws".')
                break

    def list_categories(self, trans_type):
        ls_cats = self.transactions[trans_type]['categorys']
        print(ls_cats)
        cat_select = input('Please select a category or type "exit" to leave: ')
        if cat_select in ls_cats:
            print('Category: ', cat_select, ' selected!')
            usr_exit = input('Enter "exit" to leave: ')
            if usr_exit == 'exit':
                key = False
            else:
                print('ERROR')
        else:
            print('ERROR')

    def new_transaction(self):
        key = True
        while key:
            trans_type = input('Deposits or withdraws? Enter "exit" to leave. ')
            if trans_type == 'deposits':
                self.new_category('deposits')
            elif trans_type == 'withdraws':
                self.new_category('withdraws')
            elif trans_type == 'exit':
                key = False
            else:
                print('Invalid input. Please enter "deposits", "withdraws", or "exit".')

    def new_category(self, trans_type):
        new_cat = input(f'Would you like to create a new {trans_type} category? ')
        if new_cat == 'yes':
            usr_cat_name = input('Enter new category name: ')
            usr_depo_cats = self.transactions[trans_type]['categorys']
            usr_depo_cats[usr_cat_name] = []
            print('New category:', usr_cat_name, 'created!')
        elif new_cat == 'no':
            self.list_categories(trans_type)
        elif new_cat == 'exit':
            key = False
        else:
            print('Invalid input. Please enter "yes", "no", or "exit".')

def main():
    print('Hello Welcome to Budget Bot 9000')
    print('--------------------------------')
    start_balance = float(input('Please enter your starting balance: '))
    budget_bot = BudgetBot(start_balance)

    while True:
        print('1. Check Balance')
        print('2. Show Recent Transactions')
        print('3. Add Transaction')
        print('4. Quit')
        usr_option = int(input('What would you like to do? (Enter 1 - 4): '))

        if usr_option == 1:
            print('Current Balance:', budget_bot.current_balance())
        elif usr_option == 2:
            budget_bot.list_transactions()
        elif usr_option == 3:
            budget_bot.new_transaction()
        elif usr_option == 4:
            print('Goodbye.')
            break
        else:
            print('Please enter a number 1 - 4')

if __name__ == "__main__":
    main()
