from learntools.core import *



class Q1(EqualityCheckProblem):
    index_constituents = {'dax30': ['Adidas', 'BMW', 'SAP'], 'ftse100': ['Burberry', 'Unilever']}

    _vars = ['dax30', 'ftse100']
    _expected = [index_constituents['dax30'], index_constituents['ftse100']]
    _hint = "Brackets are used to define a list. Make sure to put the strings in quotation marks."
    _solution = CS("""dax30 = ['Adidas', 'BMW', 'SAP']
ftse100 = ['Burberry', 'Unilever']

'''
Our list of constituents is likely to change over time. Tuples are immutable 
and would not allow us to add/remove constituents. Lists, however, are mutable 
and allow us to reflect the changes.
'''
""")


class Q2(EqualityCheckProblem):
    index_constituents = {'dax30': ['Adidas', 'BMW', 'SAP'], 'ftse100': ['Burberry', 'Unilever']}

    _var = 'index_constituents'
    _expected = index_constituents
    _hint = "Use curley brackets to define a dictionary."
    _solution = CS("""index_constituents = {
    'ftse100': ftse100,
    'dax30': dax30
}""")


class Q3(EqualityCheckProblem):
    index_constituents = {'dax30': ['Adidas', 'BMW', 'SAP'],
                          'ftse100': ['Burberry', 'Unilever'],
                          's&p500': ['Microsoft', 'Apple', 'Amazon', 'Alphabet']}

    _var = 'index_constituents'
    _expected = index_constituents
    _hint = "Add a new element by defining a new key of the dictionary."
    _solution = CS("index_constituents['s&p500'] = ['Microsoft', 'Apple', 'Amazon', 'Alphabet']")


class Q4(EqualityCheckProblem):
    index_constituents = {'dax30': ['Adidas', 'BMW', 'SAP'],
                          'ftse100': ['Burberry', 'Unilever'],
                          's&p500': ['Microsoft', 'Apple', 'Amazon', 'Alphabet']}

    _var = 'num_constituents'
    _expected = len(index_constituents['s&p500'])
    _hint = "Use the `len()` function to find the number of items."
    _solution = CS("num_constituents = len(index_constituents['s&p500'])")


class Q5(EqualityCheckProblem):
    index_constituents = {'dax30': ['Adidas', 'BMW', 'SAP'],
                          'ftse100': ['Burberry', 'Unilever'],
                          's&p500': ['Microsoft', 'Apple', 'Amazon', 'Alphabet']}

    _vars = ['answer_using_variable', 'answer_using_dict']
    _expected = [index_constituents['dax30'][2], index_constituents['dax30'][2]]
    _hint = "Use brackets to access the n-th element of a list."
    _solution = CS("""answer_using_variable = dax30[2]
print(answer_using_variable)

answer_using_dict = index_constituents['dax30'][2]
print(answer_using_dict)""")


class Q6(EqualityCheckProblem):
    index_constituents = {'dax30': ['Adidas', 'BMW', 'SAP'],
                          'ftse100': ['Burberry', 'Unilever', 'Royal Dutch Shell', 'Lloyds Banking Group'],
                          's&p500': ['Microsoft', 'Apple', 'Amazon', 'Alphabet']}

    _var = 'index_constituents'
    _expected = index_constituents
    _hint = "Use the `extend()` command rather than `append()`."
    _solution = CS("index_constituents['ftse100'].extend(['Royal Dutch Shell', 'Lloyds Banking Group'])")


class Q7(EqualityCheckProblem):
    index_constituents = {'dax30': ['Adidas', 'BMW', 'SAP'],
                          'ftse100': ['Burberry', 'Unilever', 'Royal Dutch Shell', 'Lloyds Banking Group'],
                          's&p500': ['Microsoft', 'Apple', 'Amazon', 'Alphabet']}

    _var = 'subsample'
    _expected = index_constituents['ftse100'][0:2]
    _hint = "You can use the `a:b` operator to get more than one item. Remember that we start counting " \
            "at zero and that the index of b is excluded, i.e., the entry with that index won't show up."
    _solution = CS("subsample = index_constituents['ftse100'][0:2]")


class Q8(EqualityCheckProblem):
    companies = ['Microsoft', 'Apple', 'Amazon', 'Alphabet', 'Berkshire Hathaway Inc.', 'Johnson & Johnson', 'Visa']
    remove_companies = ['Berkshire Hathaway Inc.', 'Visa']

    _vars = ['companies', 'remove_companies']
    _expected = [companies, remove_companies]
    _hint = "The company names are already prepared and displayed in quotation marks; just add brackets around it."
    _solution = CS("""companies = ['Microsoft', 'Apple', 'Amazon', 'Alphabet', 'Berkshire Hathaway Inc.', 'Johnson & Johnson', 'Visa']
remove_companies = ['Berkshire Hathaway Inc.', 'Visa']""")


class Q9(EqualityCheckProblem):
    companies = ['Microsoft', 'Apple', 'Amazon', 'Alphabet', 'Berkshire Hathaway Inc.', 'Johnson & Johnson', 'Visa']

    _var = 'company'
    _expected = companies[-1]
    _hint = "Combine two conditions with `or` and skip the current iteration with the `continue` statement. " \
            "Strings behave like lists, i.e., you can get individual letters using brackets."
    _solution = CS("""for company in companies:
    if company in remove_companies or company[0] == 'M':
        continue
    print(company)""")


class Q10(EqualityCheckProblem):
    _var = 'companies_file'
    _expected = './data/companies.txt'
    _hint = "You have to use the `with` statement to open the file. Use a for loop to iterate over the " \
            "companies. Finally, use an if condition in combination with `continue` to skip the current iteration."
    _solution = CS("""companies_file = './data/companies.txt'

with open(companies_file, 'w', encoding='utf-8') as file:
    for company in companies:
        if company in remove_companies or company[0] == 'M':
            continue
        file.write(f'{company}\\n')

with open(companies_file, 'w', encoding='utf-8') as file:
    file.writelines([f'{company}\\n' for company in companies if company not in remove_companies and company[0] != 'M'])""")


class Q11(EqualityCheckProblem):
    _var = 'data'
    _expected = """Apple
Amazon
Alphabet
Johnson & Johnson
"""
    _hint = "Use the `with` statement to open the file and save the data with `file.read()`."
    _solution = CS("""with open(companies_file, 'r', encoding='utf-8') as file:
    data = file.read()""")


class Q12(EqualityCheckProblem):
    _var = 'data'
    _expected = """Apple
Amazon
Alphabet
Johnson & Johnson
Intel
"""
    _hint = "First, open the file and append the new line. Second, read the same file and print the lines."
    _solution = CS("""def add_company(file, new_entry):
    \"""Appends a new_entry to file and returns a list of the items in the file\"""
    
    with open(file, 'a+', encoding='utf-8') as f:
        f.write(new_entry + '\\n')
    
    with open(file, 'r', encoding='utf-8') as f:
        print(f.read())""")


class Q13(EqualityCheckProblem):
    _var = 'even_nums'
    _expected = [num for num in range(20, 31) if num % 2 == 0]
    _hint = "You should be able to solve the exercise without a hint."
    _solution = CS("even_nums = [num for num in range(20, 31) if num % 2 == 0]")


class Q14(EqualityCheckProblem):
    _var = 'num_constituents'
    _expected = {'dax30': 3, 'ftse100': 4, 's&p500': 4}
    _hint = "You should be able to solve the exercise without a hint."
    _solution = CS("num_constituents = {name: len(index_constituents[name]) for name in index_constituents}")


class Q15(EqualityCheckProblem):
    _hint = "You may want to use a list containing your friend's names and a dictionary to store their investments. " \
            "This way, you can solve the first bit in two lines of code. The two functions `process_order()` and " \
            "`print_account_balance()` are just a combination of if conditions and one for loop to print all the " \
            "account balances."
    _solution = CS('''# First, import the randint() function (this should be done at the top of the page)
from random import randint

# Then, we set up all the necessary variables
friends = ['A', 'B', 'C', 'D']
investments = {f: randint(0, 10) for f in friends}


def process_order(friend, order):
    """
    Processes an order and either adds or removes a given number of shares
    from an investment account
    
     - friend: the name of the account holder
     - order: the relative change of the order
    """
    # We want to access investments inside the function. Your example may work without
    # this line of code because Python allows you to use external/global variables. Be
    # careful, however, and explicitly state which variables you want to access from 
    # outside the function (that is considered best-practice)
    global investments
    
    if friend not in investments:
        # Let's first check if a given person is listed in the order book
        print(f'Error: There is no customer {friend} in the order book.')
        return False  # end the function and just return
        # You could also create a new entry in the order book rather than raising an error
    
    # Load the investment holdings
    investment = investments[friend]
    
    # We have to do some quality checks first
    if (investment + order) < 0:
        print('Error: You cannot have a negative balance. Check your order.')
        return False  # end the function and just return
        
    # Everything seems ok; let's process the order
    investments[friend] = investment + order
    
    # Our success message should be fancy; we differentiate between share/shares (singular/plural)
    if order == 1:
        s_label = 'share'  # this is the only singular case
    else:
        s_label = 'shares'  # both 0 shares or anything >1 is plural 
    
    # And we differentiate between selling and buying
    if order < 0:
        o_label = 'sold'
    else:
        o_label = 'bought'
    
    # This is how we put everything together
    print('Order complete:', o_label, abs(order), s_label, f'on behalf of {friend}')

    
def print_account_balance():
    """
    Prints the account balance and adds the suffix 'share/shares' depending
    on the number of shares
    """
    global investments
    
    # We loop over the investments and output one person after another
    for i in investments:
        # Our label share/shares has to be singular or plural
        if i == 1:
            label = 'share'  # this is the only singular case
        else:
            label = 'shares'  # both 0 shares or anything >1 is plural 
        
        # You can probably tell by now that I am a big fan of the f-strings. Feel 
        # free to use a different syntax.
        print(f'{i} holds {investments[i]} {label}')
    
    print('\\n')  # the additional line break makes it easier to read



# Bevore we start, let's check the order book
print_account_balance()

# First order
process_order('B', -7)

# Second order
process_order('E', 10)

# Third and last order for today
process_order('D', 1)

# This is our ending balance
print_account_balance()''')



qvars = bind_exercises(globals(), [
    Q1,
    Q2,
    Q3,
    Q4,
    Q5,
    Q6,
    Q7,
    Q8,
    Q9,
    Q10,
    Q11,
    Q12,
    Q13,
    Q14,
    Q15
])
__all__ = list(qvars)
