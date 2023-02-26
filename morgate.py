#*******************************GRAPHIC USER INTERFACE*******************
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class App_Window(QMainWindow):
    def __init__(self):
        super(App_Window, self).__init__()
        self.setGeometry(300,300, 600, 600)
        self.setWindowTitle('Budget Organizer')
        add_user()
        self.initUI()
        self.show()

    def initUI(self):
    #*************************BUTTONS**********************************
        # create sign up button
    def add_user(self):
        sign_up = QtWidgets.QPushButton(self)
        sign_up.setText('Create Account')
        sign_up.clicked.connect()


        Username = QtWidgets.QtWidgets.QLineEdit(self)
        Username.setObjectName('User Name')
            
        label = QtWidgets.QLabel(Username)
        label.move(50, 50)

        #*************************LABELS*************************************
        
        #label.setText('Trial')
        #
        

            
def AppBox():
# creating main window
    Budget_app = QApplication(sys.argv)
    Budget_win = App_Window()
    
    
    
    sys.exit(Budget_app.exec())



#-----------creating user----------------------------------------------------------
def create_user():
    """This function creates a new user"""

    new_user = input('Entert the desired username(13 character max): ')
    do_not_match = False
    while not do_not_match:
        password = input("Please enter desire password(13 character max): ")
        again = input(" Re-enter desire password: ")
        if password == again:
            do_not_match = True
        else:
            print('The entries do not match, try again\n')
    return new_user, password

#-----------coder-Decoder-----------------------------------------------------------
def coder_decoder(character, decoder = False):
    """This function encode and decode a single character using its ancii value"""

    
    # code will be return for encoding before writing in the file
    #decode will be return when reading from file
    if ord(character) < 128:
        code = ord(character) + 128
        decode = ord(character) + 128
    else:
        code = ord(character) - 128
        decode = ord(character) - 128
    
    #selecting return value 
    if decoder:
        return chr(decode)
    return chr(code)





#------------Math functions-----------------------------------------------------------

def dependent(age):
    """This function save a new dependent into a dependent's list"""

    dependet_list.append(age)

    return


def income(hourly_rate, monthly_hours, house_hold = True):
    """This function returns a realistic income after taxes 
    and other obligations not ususally consider are deducted"""

    
    #This variable holds a gross yearlycalculated income
    y_income = hourly_rate * monthly_hours * 12

    # This if-elif-else deducts the faderal taxes Source: Internal Revenue Service
    if (y_income < 15700 and house_hold) or (y_income < 11000 and not house_hold):
        y_income = y_income * 0.9  # 10% withhold
    elif  (y_income < 59850 and house_hold) or (y_income < 44725 and not house_hold): 
        y_income = y_income * 0.88  # 12% withhold
    elif  (y_income < 95350 and house_hold) or (y_income < 95375 and not house_hold): 
        y_income = y_income * 0.78  # 22% withhold
    elif  (y_income < 182100):
        y_income = y_income * 0.76  # 24% withhold
    elif  (y_income < 231250): 
        y_income = y_income * 0.68  # 32% withhold
    elif  (y_income < 578100 and house_hold) or (y_income < 578125 and not house_hold): 
        y_income = y_income * 0.65  # 35% deduction
    else:
        y_income = y_income * 0.63  # 37% deduction

    # discounting annual expenditure on gift for family and friends 
    # source: The National Retail Federation’s annual survey of holiday 
    y_income = y_income - 942

    # discounting average cost per dependent under 17 
    # Note: $12,980 was reported by the USDA for middle income family
    # no data for other income brakets, amount was proportionaly ajusted
    expenditure_per_child = (y_income  / 107400) * 12980

    for child in dependet_list:
        if child <= 17:
            y_income = y_income - expenditure_per_child     

    # after yearly income processed it extimate monthly income
    monthly_income = y_income / 12

    return round(monthly_income, 2)



def mortgage( loan_amount,anual_interest_rate, years,home_value = 0, is_morgatge = False, is_carLoan = False):

    """This function calculates the monthly payment for loan if principal, 
        interest rate and duration are known. Function also have special 
        calculation if is specified as morgage or carloan"""

    
     # this line preprocess the anual interest rate, if id decimal leaved unchanged else turned into decimal
    if anual_interest_rate > 1:
        anual_interest_rate = anual_interest_rate/ 100
        
    # This line creates a variable to hold the calculated duration of loan in months
    months = years * 12
    
    # this line creates a variable to hold the calculated monthly rate
    monthly_rate = anual_interest_rate / 12
    
    # this variable holds the monthly payment and is returned by the function after calculated
    Monthly = loan_amount * (monthly_rate*(1 + monthly_rate)**months ) / ( (1 + monthly_rate)**months - 1) 

    
    if is_morgatge:
        # the real state taxt rate in nevada
        Local_tax = 0.0075
        
        #property insurance extimation
        PI = (home_value * 3.5) / 1000
        
        # assumes PMI only if equaty less than 20%
        if (loan_amount / home_value) > 0.8:   
           
            #the PMI the average of the max and min was selected
            PMI = 0.011
        else:
            PMI = 0
        
        # adding taxes, property insurance and PMI to monthly payment
        Monthly += (home_value * (Local_tax + PMI) + PI) / 12 
        
    if is_carLoan:
        # anual maintenance according to AAA
        Maintenance = 792
        
        #1,682 per year according to carinsurance.com
        Insurance = 1682
        
        # adding maintenance and insurance
        Monthly += (Maintenance + 1682)/12 
    
    # returns the monthly payment
    return round(Monthly,2)

#----------------Testing Functions-------------------------------
AppBox()

# creating a list to store dependents CAUTION !!!! global variable
dependet_list = []

