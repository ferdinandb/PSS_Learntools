from learntools.core import *
import pandas as pd
import numpy as np


investments = pd.DataFrame(0, index=['Anna', 'Tim', 'Kim', 'Jordan'], columns=['AAPL', 'MSFT', 'GOOGL'])
investments2 = investments.copy()
investments2['GOOGL'] = 4
investments3 = investments2.copy()
investments3.loc['Kim'] = 8
investments4 = investments3.copy()
investments4['AAPL'].loc['Tim'] = 10
investments5 = investments4.copy()
investments5['MSFT'].loc[['Anna', 'Jordan']] = 3

price_data1 = pd.read_csv('./data/company-prices.csv')
price_data2 = price_data1.copy()
price_data2['Date'] = pd.to_datetime(price_data2['Date'])
price_data3 = price_data2.copy()
price_data3 = price_data3.set_index('Date')
price_data4 = price_data3.copy()
price_data4 = price_data4 / 100

returns = pd.DataFrame(np.nan,
                       index=price_data4.index[1:],  # disregard the first index entry
                       columns=price_data4.columns)  # use all column if the original df
returns2 = returns.copy()
for company in price_data4.columns:
    t = price_data4[company].iloc[1:].values
    tm1 = price_data4[company].iloc[:-1].values
    returns2[company] = (t - tm1) / tm1



class Q1(EqualityCheckProblem):
    _var = 'investments'
    _expected = investments
    _hint = "Search the pandas [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas." \
            "DataFrame.html) and check the available parameters for DataFrame. You will need the first three: " \
            "`data`, `index`, and `columns`."
    _solution = CS("""investments = pd.DataFrame(data=0,  # the keyword argument data is not necessary
                           index=['Anna', 'Tim', 'Kim', 'Jordan'], 
                           columns=['AAPL', 'MSFT', 'GOOGL'])""")


class Q2(EqualityCheckProblem):
    _var = 'investments'
    _expected = investments2
    _hint = "You can solve the question in one line of code. Select the column " \
            "`GOOGL` and set it equal to 4. That's it."
    _solution = CS("investments['GOOGL'] = 4")


class Q3(EqualityCheckProblem):
    _var = 'investments'
    _expected = investments3
    _hint = "Bear in mind that the DataFrame `investments` uses index values `['Anna', 'Tim', 'Kim', 'Jordan']` " \
            "rather than index positions (0, 1, 2, 3). Hence, you have to use `.loc['Kim']` to access the specific row."
    _solution = CS("investments.loc['Kim'] = 8")


class Q4(EqualityCheckProblem):
    _var = 'investments'
    _expected = investments4
    _hint = "Let's solve the easier bit first: selecting the column. If you have the column, you can select the row. " \
            "The resulting cell is what we have to change. Doing both steps is simply a combination of the two " \
            "previous exercises."
    _solution = CS("investments['AAPL'].loc['Tim'] = 10")


class Q5(EqualityCheckProblem):
    _var = 'investments'
    _expected = investments5
    _hint = "Check the [pandas documentation for `.loc[]`](https://pandas.pydata.org/pandas-docs/stable/reference/" \
            "api/pandas.DataFrame.loc.html). What inputs are allowed?"
    _solution = CS("investments['MSFT'].loc[['Anna', 'Jordan']] = 3")


class Q6(EqualityCheckProblem):
    _var = 'price_data'
    _expected = price_data1
    _hint = "This is a very simple CSV file. You won't have to consider anything when reading it."
    _solution = CS("price_data = pd.read_csv('./data/company-prices.csv')")


class Q7(EqualityCheckProblem):
    _var = 'price_data'
    _expected = price_data1
    _hint = ""
    _solution = CS("price_data.head(10)")


class Q8(EqualityCheckProblem):
    _var = 'price_data'
    _expected = price_data2
    _hint = "Read the documentation carefully. You will have to use `pd.to_datetime()` and pass 'the object to " \
            "convert' as the first and only argument. The object to convert is the column `Date`."
    _solution = CS("price_data['Date'] = pd.to_datetime(price_data['Date'])")


class Q9(EqualityCheckProblem):
    _var = 'price_data_alt'
    _expected = price_data2
    _hint = "Read the documentation carefully. The method `.astype()` is chained after the DataFrame (in our case" \
            "`price_data`). The first and only argument has to be a dictionary with the column name and the desired " \
            "dtype `datetime64[ns]`."
    _solution = CS("price_data_alt = price_data.astype({'Date': 'datetime64[ns]'})")


class Q10(EqualityCheckProblem):
    _var = 'price_data'
    _expected = price_data3
    _hint = "Have a look at the documentation. What methods sets an index?"
    _solution = CS("price_data = price_data.set_index('Date')")


class Q11(EqualityCheckProblem):
    _var = ''
    _expected = None
    _hint = "We select only one column of the DataFrame, making it a Series. Have a look " \
            "at the [documentation](https://pandas.pydata.org/docs/reference/api/pandas." \
            "Series.to_csv.html) for more details. As you can see, the index is saved " \
            "by default."
    _solution = CS("price_data['BP'].to_csv('./data/prices-BP.csv')")


class Q12(EqualityCheckProblem):
    _var = ''
    _expected = None
    _hint = "The ModuleNotFoundError indicates that a required module/package/library is not installed (the " \
            "three words can be used interchangeably). If you find the documentation of the missing package, you " \
            "should also find the installation instructions."
    _solution = CS("""price_data.to_excel('./data/company-prices.xlsx', sheet_name='PriceData')

'''
The ModuleNotFoundError indicates that a required module/package/library is not installed (the 
three words can be used interchangeably). Before being able to export the DataFrame to an Excel
file, you have to install the package 'openpyxl'.

Go to PyCharm and select the tab 'Terminal' at the bottom left of the screen. Your Jupyter Lab
application should be running. You can open a second Terminal window by clicking on the small '+'
icon next to 'Terminal: [Local x]'.

The documentation of openpyxl describes how to install the missing package:
https://openpyxl.readthedocs.io/en/stable/#installation

Simply run the following pip command in your Terminal: pip install openpyxl
'''""")


class Q13(EqualityCheckProblem):
    _var = 'price_data'
    _expected = price_data4
    _hint = "Simply divide the entire DataFrame by 100. Remember to assign your changes back to `price_data`."
    _solution = CS("price_data = price_data / 100")


class Q14(EqualityCheckProblem):
    _var = 'sample'
    _expected = price_data4.iloc[2:5]
    _hint = "The index starts at zero, i.e. the third row has index `2`. The upper boundary of the range is " \
            "exclusive. What index position do we have to choose then?"
    _solution = CS("sample = price_data.iloc[2:5]")


class Q15(EqualityCheckProblem):
    _var = 'sample'
    _expected = price_data4.iloc[-7:]
    _hint = "Make sure to not set an ending value. Use `.iloc[n:]` instead, with `n` being the number of entries that " \
            "you want to display."
    _solution = CS("sample = price_data.iloc[-7:]")


class Q16(EqualityCheckProblem):
    _var = 'returns'
    _expected = returns
    _hint = "You can solve this question in no more than three lines of code. You get the index using " \
            "`price_data.index` and the columns using `price_data.columns`. Bear in mind that we have to " \
            "remove the first row of the `price_data` index."
    _solution = CS("""returns = pd.DataFrame(np.nan, 
                       index=price_data.index[1:],  # disregard the first index entry
                       columns=price_data.columns)  # use all column if the original df""")


class Q17(EqualityCheckProblem):
    _var = 'returns'
    _expected = returns2
    _hint = "Don't forget to convert the Series to values using `.values`."
    _solution = CS("""for company in price_data.columns:
    # Helper variables to store the price Series at different times
    t = price_data[company].iloc[1:].values
    tm1 = price_data[company].iloc[:-1].values
    
    # Have a look: both Series have a length of 260 rows; mission accomplished!
    print(len(t), len(tm1))

    # Do the math and assign the return to the corresponding column in our DataFrame
    returns[company] = (t - tm1) / tm1""")


class Q18(EqualityCheckProblem):
    _vars = ['bp_min', 'bp_max']
    _expected = [returns2['BP'].min(), returns2['BP'].max()]
    _hint = "Have a look at the pandas documentation."
    _solution = CS("""bp_min = returns['BP'].min()
bp_max = returns['BP'].max()""")





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
    Q15,
    Q16,
    Q17,
    Q18,
])
__all__ = list(qvars)
