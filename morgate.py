#*******************************GRAPHIC USER INTERFACE*******************
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

class App_Window(QtWidgets.QWidget):
    def __init__(self, * args, ** kwargs):
        super().__init__(* args, ** kwargs)
        self.setGeometry(300,300, 600, 600)
        self.setWindowTitle('Budget Organizer')
        
        self.sign_up = QtWidgets.QPushButton(self)
        self.sign_up.setText('Create Account')
        self.sign_up.adjustSize()
        self.sign_up.move(100, 170)
        self.sign_up.clicked.connect(self.signup)

        self.sign_in = QtWidgets.QPushButton(self)
        self.sign_in.setText('Login')
        self.sign_in.adjustSize()
        self.sign_in.move(200, 170)
        self.sign_in.clicked.connect(self.close) 

        self.Exit = QtWidgets.QPushButton(self)
        self.Exit.setText('Exit')
        self.Exit.adjustSize()
        self.Exit.move(300, 170)
        self.Exit.clicked.connect(self.close)  
        
        self.show()

    def signup(self):
        self.CreateUser = User_box()
        self.CreateUser.show()
        self.close()

        
 #************ADD_USER_WINDOW*********COMPLETED******************       
class User_box(QtWidgets.QWidget):
    """This class creates a new user"""

    def __init__(self, * args, ** kwargs):
        super().__init__(* args, ** kwargs)
        self.setGeometry(300,300, 600, 600)
        self.setWindowTitle('Create user')

        # user label
        self.user = QtWidgets.QLabel(self)
        self.user.move(40, 50)
        self.user.setText('User name:')
        
        # user label top
        self.user = QtWidgets.QLabel(self)
        self.user.move(135, 20)
        self.user.setText('Entert the desired username(14 character max)')
        self.user.adjustSize()

        # user lineedit
        self.Username = QtWidgets.QLineEdit(self)
        self.Username.setObjectName('User Name')
        self.Username.move(135, 50)

        # password label
        self.psswd = QtWidgets.QLabel(self)
        self.psswd.move(40, 130)
        self.psswd.setText('Password:')

        # password label top
        self.user = QtWidgets.QLabel(self)
        self.user.move(135, 90)
        self.user.setText('Entert the desired password(14 character max)')
        self.user.adjustSize()
        
        # password line edit
        self.Password = QtWidgets.QLineEdit(self)
        self.Password.setObjectName('Password')
        self.Password.setEchoMode(2)
        self.Password.move(135, 130)

        # 2nd password label
        self.psswd2 = QtWidgets.QLabel(self)
        self.psswd2.move(40, 210)
        self.psswd2.setText('Re-enter Password:')

        # password label top
        self.user = QtWidgets.QLabel(self)
        self.user.move(135, 170)
        self.user.setText('Re-enter desired password')
        self.user.adjustSize()

        # 2nd password line edit
        self.Re_enterpassword = QtWidgets.QLineEdit(self)
        self.Re_enterpassword.setObjectName('Re_Enter')
        self.Re_enterpassword.setEchoMode(2)
        self.Re_enterpassword.move(135, 210)
        

        
        # accept button
        self.accept = QtWidgets.QPushButton(self)
        self.accept.setText('Accept')
        self.accept.move(100, 250)
        self.accept.clicked.connect(self.saving_name)

        # cancel button
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setText('Cancel')
        self.cancel.move(180, 250)
        self.cancel.clicked.connect(self.close)
        

        
        # showing the window
        self.show()
         
        
    def saving_name(self):
        """This function process all entered information and writes it on a file"""
        
        # these varaiables store teh inputs
        userName = self.Username.text()
        password = self.Password.text()
        password2 = self.Re_enterpassword.text() 

        # if-elif-else selection to process the input
        if len(userName) > 14:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Username is too long')

        elif len(userName) < 5:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'You need a Username of at least 5 characters')

        elif password == '' or len(password) < 5:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'You need a Password of at least 5 characters')

        elif len(password) > 14:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Password is too long')

        elif  password != password2:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Passwords do ot match')

        else:
            encodedUser = ''
            encodedPassword = ''
            for character in userName:
                encodedUser += coder_decoder(character)    
            for character in password:
                encodedPassword += coder_decoder(character)    
            
            encodedUser += (15 - len(encodedUser)) * ' '
            encodedPassword += (15 - len(encodedPassword)) * ' '

            with open('Data_base', 'a+') as  DB:
                DB.write(encodedUser)
                DB.seek(15)
                DB.write(encodedPassword)

            QtWidgets.QMessageBox.information(self, 'Sucess', 'your information was saved')
            self.close()
            self.addFinance()

    def addFinance(self):
        self.Finances = Financial_box()
        self.Finances.show()


        
 #************ADD_FINANCE_WINDOW***************************       
class Financial_box(QtWidgets.QWidget):
    """This class adds financial information """

    def __init__(self, * args, ** kwargs):
        super().__init__(* args, ** kwargs)
        self.setGeometry(300,300, 600, 600)
        self.setWindowTitle('Add Financial information')  

        # user label
        self.user = QtWidgets.QLabel(self)
        self.user.move(40, 50)
        self.user.setText('User name:')
        
        # user label top
        self.user = QtWidgets.QLabel(self)
        self.user.move(135, 20)
        self.user.setText('Entert the desired username(14 character max)')
        self.user.adjustSize()

        # user lineedit
        self.Username = QtWidgets.QLineEdit(self)
        self.Username.setObjectName('User Name')
        self.Username.move(135, 50)
        
        
        
        
        
        
        # accept button
        self.accept = QtWidgets.QPushButton(self)
        self.accept.setText('Accept')
        self.accept.move(100, 550)
        self.accept.clicked.connect(self.close)

        # cancel button
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setText('Cancel')
        self.cancel.move(500, 550)
        self.cancel.clicked.connect(self.close)
        self.show()

        
#********************CREATING THE APP*********************************
            
def AppBox():
    # creating main window
    Budget_app =  QApplication(sys.argv)
    Main_Window = App_Window()
    
    
    
    
    sys.exit(Budget_app.exec())


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

 #adding two dependents to test functions
dependent(4)
dependent(5)

# trying morgtgage function in morgatge mode
payment = mortgage(140000, 4.87, 30, 140000, True )
print(payment)

# Trying morgatge function in carloan mode
payment = mortgage(14000, 4.87, 5, is_morgatge = False, is_carLoan = True )
print(payment)


# Testing income function
real_income = income(28, 160)
print(real_income)


#testing coder_decoder
string = "Ernesto Gonzalez"
coded =''
decoded = ''

for character in string:
    coded += coder_decoder(character)

#output encoded str
print(coded)

for character in coded:
    decoded += coder_decoder(character, True)

# output decoded str
print(decoded)


#creating user name
name, passw = create_user()

print(name)
print(passw)