#*******************************GRAPHIC USER INTERFACE*******************
import sys , random
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
        self.sign_in.clicked.connect(self.login) 

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

    def login(self):
        self.log = Login_box()
        self.log.show()
        self.close()

        
 #************ADD_USER_WINDOW*********COMPLETED******************       
class User_box(QtWidgets.QWidget):
    """This class creates a new user"""

    def __init__(self, * args, ** kwargs):
        super().__init__(* args, ** kwargs)
        self.setGeometry(300, 300, 400, 280)
        self.setWindowTitle('Create user')

        # user label
        self.user = QtWidgets.QLabel(self)
        self.user.move(40, 50)
        self.user.setText('User name:')
        
        # user label top
        self.user = QtWidgets.QLabel(self)
        self.user.move(135, 20)
        self.user.setText('Enter the desired username(14 character max)')
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
        self.user.setText('Enter the desired password(14 character max)')
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
        self.cancel.clicked.connect(self.mainWin)
        
        # showing the window
        self.show()

    # returns tu main window    
    def mainWin(self):
        self.Main_Window = App_Window()
        self.Main_Window.show()
        self.close()
    
    # redirect to log in window
    def login(self):
        self.log = Login_box()
        self.log.show()
        self.close()
        
    def saving_name(self):
        """This function process all entered information and writes it on a file"""
        
        # these varaiables store the inputs
        userName = self.Username.text()
        password = self.Password.text()
        password2 = self.Re_enterpassword.text() 
        
        taken = False

        with open('Data_base', 'a+') as DB:
            DB.seek(0)
            for line in DB:
                info = line.split()
                if len(info) == 0:
                    continue

                if userName == decode_string(info[0]):
                    taken = True
        
            DB.close()


        # if-elif-else selection to process the input
        if taken:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Username already taken')    
        elif len(userName) > 14:
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
            with open('Data_base', 'a+') as  DB:
                DB.write(decode_string(userName) + ' ')
                DB.write(decode_string(password)+ ' ')
                DB.write(decode_string('0.0 0.0 0.0 0.0 '))
                DB.write(decode_string('none') + '\n')
                DB.close()
            QtWidgets.QMessageBox.information(self, 'Success', 'your information was saved')
            self.close()
            self.login()
           
    
#************LOGIN_WINDOW***************************       
class Login_box(QtWidgets.QWidget):
    """This window allows the usser to log in """

    def __init__(self, * args, ** kwargs):
        super().__init__(* args, ** kwargs)
        self.setGeometry(300,300, 330, 220)
        self.setWindowTitle('Login')
    
        # user label
        self.user = QtWidgets.QLabel(self)
        self.user.move(40, 50)
        self.user.setText('User name:')
        
        # user label top
        self.user = QtWidgets.QLabel(self)
        self.user.move(135, 20)
        self.user.setText('Enter username')
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
        self.user.setText('Enter password')
        self.user.adjustSize()
        
        # password line edit
        self.Password = QtWidgets.QLineEdit(self)
        self.Password.setObjectName('Password')
        self.Password.setEchoMode(2)
        self.Password.move(135, 130)

        # accept button
        self.accept = QtWidgets.QPushButton(self)
        self.accept.setText('Accept')
        self.accept.move(100, 170)
        self.accept.clicked.connect(self.logging)

        # cancel button
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setText('Cancel')
        self.cancel.move(180, 170)
        self.cancel.clicked.connect(self.mainWin)
        
        # showing the window
        self.show()
    
    # returns tu main window    
    def mainWin(self):
        self.Main_Window = App_Window()
        self.Main_Window.show()
        self.close()

    # search for the user
    def logging(self):
        """This function analyses the input from user"""

       
        if  info_Loader(self.Username.text(), self.Password.text()):
                QtWidgets.QMessageBox.information(self, 'Sucess', 'you are logged in')
                self.close()
                self.addFinance()

        else:
                QtWidgets.QMessageBox.critical(self, 'Try Again', 'Wrong User or Passwords ')    
    
    def addFinance(self):
        self.Finances = Financial_box()
        self.Finances.show()

   
        
#************FINANCE_WINDOW***************************       
class Financial_box(QtWidgets.QWidget):
    """This window adds financial information """
    
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300, 600, 600)
        self.setWindowTitle('Add Financial information')  

        info_Loader(Username, Password)

        # income label
        self.income_label = QtWidgets.QLabel(self)
        self.income_label.move(40, 50)
        self.income_label.setText(f'Monthly income: {Monthly_Income} ')

        # asset label 
        self.asset_label = QtWidgets.QLabel(self)
        self.asset_label.move(250, 50)
        self.asset_label.setText(f'Total assets: {Total_assets}')

        # transportation label 
        self.transportation_label = QtWidgets.QLabel(self)
        self.transportation_label.move(40, 80)
        self.transportation_label.setText(f'Monthly transportation expenses: {Monthly_transportation_expenses}')

        # housing label 
        self.housing_label = QtWidgets.QLabel(self)
        self.housing_label.move(250, 80)
        self.housing_label.setText(f'Monthly housing expenses: {Monthly_housing_expenses}')

        # dependent label
        self.dependent_label = QtWidgets.QLabel(self)
        self.dependent_label.move(40, 120)
        self.dependent_label.setText(f'Dependents: {dependent_list}')
         
        # add assets button
        self.assets_button = QtWidgets.QPushButton(self)
        self.assets_button.setText('Assets')
        self.assets_button.move(50, 300)
        self.assets_button.clicked.connect(self.close)

        # add dependents button
        self.dependents_button = QtWidgets.QPushButton(self)
        self.dependents_button.setText('Dependants')
        self.dependents_button.move(50, 400)
        self.dependents_button.clicked.connect(self.add_dependents)
        
        # add income button
        self.income_button = QtWidgets.QPushButton(self)
        self.income_button.setText('Income')
        self.income_button.move(250, 300)
        self.income_button.clicked.connect(self.add_income_window)

        # add transportation expenses button
        self.transportation_button = QtWidgets.QPushButton(self)
        self.transportation_button.setText('Transportation')
        self.transportation_button.move(250, 400)
        self.transportation_button.clicked.connect(self.add_transportation)
        
        # add housing expenses button
        self.housing_button = QtWidgets.QPushButton(self)
        self.housing_button.setText('Housing')
        self.housing_button.move(450, 400)
        self.housing_button.clicked.connect(self.add_housing)

        # Logout button
        self.accept = QtWidgets.QPushButton(self)
        self.accept.setText('Log out')
        self.accept.move(100, 550)
        self.accept.clicked.connect(self.mainWin)


        # cancel button
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setText('Exit')
        self.cancel.move(500, 550)
        self.cancel.clicked.connect(self.close)
        self.show()
    
    # returns tu main window    
    def mainWin(self):
        self.Main_Window = App_Window()
        self.Main_Window.show()
        self.close()

    # calling add income window    
    def add_income_window(self):
        """creates an object type add_income"""
        self.close()
        self.income_window = add_income()
        self.income_window.show()

    # calling add housing window    
    def add_housing(self):
        """creates an object type add_housing"""
        self.close()
        self.housing_window = add_housing()
        self.housing_window.show()

    # calling add transportation window    
    def add_transportation(self):
        """creates an object type add_housing"""
        self.close()
        self.transportation_window = add_transportation()
        self.transportation_window.show()

    # calling add dependents window    
    def add_dependents(self):
        """creates an object type add_housing"""
        self.close()
        self.dependents_window = add_dependents()
        self.dependents_window.show()  
    
#//////////////////SUBWINDOWs OF ADD FINANCE//////////////////////
#-------------------------Income window--------------------------
class add_income(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 600, 400, 200)
        self.setWindowTitle('Add Financial information')
        
        # income label 
        self.hours_label = QtWidgets.QLabel(self)
        self.hours_label.move(40, 50)
        self.hours_label.setText('Enter your hourly rate and number of hours per week:')

        # rate label
        self.rate_label = QtWidgets.QLabel(self)
        self.rate_label.move(40, 80)
        self.rate_label.setText('Hourly rate:')
        
        # rate line edit
        self.rate_line = QtWidgets.QLineEdit(self)
        self.rate_line.setText('0.0')
        self.rate_line.setObjectName('rate')
        self.rate_line.move(135, 80)

        # hours label
        self.hours_label = QtWidgets.QLabel(self)
        self.hours_label.move(40, 120)
        self.hours_label.setText('Hours per week:')
        
        # hours line edit
        self.hours_line = QtWidgets.QLineEdit(self)
        self.hours_line.setText('0.0')
        self.hours_line.setObjectName('rate')
        self.hours_line.move(135, 120)

         # accept button
        self.accept = QtWidgets.QPushButton(self)
        self.accept.setText('accept')
        self.accept.move(40, 160)
        self.accept.clicked.connect(self.updatingIncome)


        # cancel button
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setText('Exit')
        self.cancel.move(135, 160)
        self.cancel.clicked.connect(self.addFinance)
        
        self.show()
        
    # this function saves the information and return to the dashboard
    def updatingIncome(self):
        """This function updates the total income passing the entered information to teh function income"""
        
        global Monthly_Income
        try:
            total = income(float(self.rate_line.text()), float(self.hours_line.text()))
        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Enter numbers only ')
            return
        
        if Monthly_Income != total:
            Monthly_Income = total
           
        self.close()
        info_Saver(Username, Password)
        self.return_window = Financial_box()
        self.return_window.show()

    # creates an object type addFinances
    def addFinance(self):
        self.close()
        self.Finances = Financial_box()
        self.Finances.show()

#-------------------------housing window--------------------------
class add_housing(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 600, 350, 350)
        self.setWindowTitle('Add Housing expenses')
        
        # top label 
        self.hours_label = QtWidgets.QLabel(self)
        self.hours_label.move(40, 20)
        self.hours_label.setText('Please fill all the information related to housing expenses')

        # gross payment label
        self.payment_label = QtWidgets.QLabel(self)
        self.payment_label.move(20, 50)
        self.payment_label.setText('Monthly rent or mortgage payment:')
        
        # gross payment line edit
        self.payment_line = QtWidgets.QLineEdit(self)
        self.payment_line.setText('0.0')
        self.payment_line.setObjectName('payment')
        self.payment_line.move(200, 50)

        # property insurance label
        self.insurance_label = QtWidgets.QLabel(self)
        self.insurance_label.move(20, 80)
        self.insurance_label.setText('Property Insurance:')
        
        # property insurance line edit
        self.insurance_line = QtWidgets.QLineEdit(self)
        self.insurance_line.setObjectName('insurance')
        self.insurance_line.setText('0.0')
        self.insurance_line.move(200, 80)

        # electric bill label
        self.electric_label = QtWidgets.QLabel(self)
        self.electric_label.move(20, 110)
        self.electric_label.setText('Electric Bill:')
        
        # electric bill line edit
        self.electric_line = QtWidgets.QLineEdit(self)
        self.electric_line.setObjectName('electric')
        self.electric_line.setText('0.0')
        self.electric_line.move(200, 110)

         # Internet bill label
        self.Internet_label = QtWidgets.QLabel(self)
        self.Internet_label.move(20, 140)
        self.Internet_label.setText('Internet Bill:')
        
        # Internet bill line edit
        self.Internet_line = QtWidgets.QLineEdit(self)
        self.Internet_line.setObjectName('Internet')
        self.Internet_line.setText('0.0')
        self.Internet_line.move(200, 140)     

        # homeowners label
        self.homeowners_label = QtWidgets.QLabel(self)
        self.homeowners_label.move(90, 170)
        self.homeowners_label.setText('Homeownership Only')

        # property taxes label
        self.taxes_label = QtWidgets.QLabel(self)
        self.taxes_label.move(20, 200)
        self.taxes_label.setText('Property Taxes:')
        
        # property taxes line edit
        self.taxes_line = QtWidgets.QLineEdit(self)
        self.taxes_line.setObjectName('taxes')
        self.taxes_line.setText('0.0')
        self.taxes_line.move(200, 200)

        # HOA label
        self.HOA_label = QtWidgets.QLabel(self)
        self.HOA_label.move(20, 230)
        self.HOA_label.setText('HOA dues:')
        
        # HOA line edit
        self.HOA_line = QtWidgets.QLineEdit(self)
        self.HOA_line.setObjectName('HOA')
        self.HOA_line.setText('0.0')
        self.HOA_line.move(200, 230)

        # gas bill label
        self.gas_label = QtWidgets.QLabel(self)
        self.gas_label.move(20, 260)
        self.gas_label.setText('Gas bill:')
        
        # gas bill line edit
        self.gas_line = QtWidgets.QLineEdit(self)
        self.gas_line.setObjectName('Gas')
        self.gas_line.setText('0.0')
        self.gas_line.move(200, 260)

         # accept button
        self.accept = QtWidgets.QPushButton(self)
        self.accept.setText('accept')
        self.accept.move(40, 290)
        self.accept.clicked.connect(self.updatingHousing)

        # cancel button
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setText('Exit')
        self.cancel.move(135, 290)
        self.cancel.clicked.connect(self.addFinance)
        
        self.show()

    # this function saves the information and return to the dashboard    
    def updatingHousing(self):
        """This function calculates updates the total housing expenses"""
        
        global Monthly_housing_expenses
        try:
            total = float(self.payment_line.text()) + float(self.insurance_line.text())
            total += float(self.electric_line.text()) + float(self.Internet_line.text())
            total += float(self.taxes_line.text()) + float(self.HOA_line.text())
            total += float(self.gas_line.text())
        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Enter numbers only ')
            return
        
        if Monthly_housing_expenses != total:
            Monthly_housing_expenses = total

        self.close()
        info_Saver(Username, Password)
        self.return_window = Financial_box()
        self.return_window.show()

     # creates an object type addFinances to closes current window without changes
    def addFinance(self):
        self.close()
        self.Finances = Financial_box()
        self.Finances.show()

#-------------------------transportation window--------------------------
class add_transportation(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 600, 450, 250)
        self.setWindowTitle('Add Housing expenses')
        
        # top label 
        self.hours_label = QtWidgets.QLabel(self)
        self.hours_label.move(40, 20)
        self.hours_label.setText('Please fill all the information related to transportation expenses')

        # car payment label
        self.payment_label = QtWidgets.QLabel(self)
        self.payment_label.move(20, 50)
        self.payment_label.setText('Monthly Car Payment(if any):')
        
        # gross payment line edit
        self.payment_line = QtWidgets.QLineEdit(self)
        self.payment_line.setText('0.0')
        self.payment_line.setObjectName('payment')
        self.payment_line.move(200, 50)

        # car insurance label
        self.insurance_label = QtWidgets.QLabel(self)
        self.insurance_label.move(20, 80)
        self.insurance_label.setText('Monthly Car Insurance:')
        
        # car insurance line edit
        self.insurance_line = QtWidgets.QLineEdit(self)
        self.insurance_line.setObjectName('insurance')
        self.insurance_line.setText('0.0')
        self.insurance_line.move(200, 80)   

        # mileage label
        self.mileage_label = QtWidgets.QLabel(self)
        self.mileage_label.move(20, 110)
        self.mileage_label.setText('Average Mileage per Month:')
        
        # mileage line edit
        self.mileage_line = QtWidgets.QLineEdit(self)
        self.mileage_line.setObjectName('mileage')
        self.mileage_line.setText('0.0')
        self.mileage_line.move(200, 110)

        # text was too long
        text = 'The total monthly cost includes gas and maintenace cost base on national average'
        text2 = 'Accurate numbers depend of several factors like year model and type of engine ect.'

        # accept button
        self.accept = QtWidgets.QPushButton(self)
        self.accept.setText('accept')
        self.accept.move(40, 200)
        self.accept.clicked.connect(self.updatingTransportation)

        # cancel button
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setText('Exit')
        self.cancel.move(135, 200)
        self.cancel.clicked.connect(self.addFinance)
        
        self.show()

    # this function saves the information and return to the dashboard    
    def updatingTransportation(self):
        """This function calculates updates the total transportation expenses"""
        
        global Monthly_transportation_expenses
        
        try:
            total = float(self.payment_line.text()) + float(self.insurance_line.text())
            total += float(self.mileage_line.text()) * 0.0955 + int(self.mileage_line.text()) * 0.09 
            
        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Enter numbers only ')
            return
        
        if total != Monthly_transportation_expenses:
            Monthly_transportation_expenses = total

        self.close()
        info_Saver(Username, Password)
        self.return_window = Financial_box()
        self.return_window.show()

     # creates an object type addFinances to closes current window without changes
    def addFinance(self):
        self.close()
        self.Finances = Financial_box()
        self.Finances.show()

#-------------------------dependents window--------------------------
class add_dependents(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 600, 460, 140)
        self.setWindowTitle('Add Housing expenses')
        
        # top label 1
        self.top_label = QtWidgets.QLabel(self)
        self.top_label.move(20, 20)
        self.top_label.setText('Please add each dependant age seperated by a comma e.g.: 1, 34 , 53, ...')

        # top label 2
        self.top_label = QtWidgets.QLabel(self)
        self.top_label.move(20, 50)
        self.top_label.setText('Use only whole numbers for the age for instance is dependent is 9 moths old input zero')

        # dependents lable label
        self.dependents_label = QtWidgets.QLabel(self)
        self.dependents_label.move(120, 80)
        self.dependents_label.setText('Dependents:')
        
        # dependent line edit
        self.dependents_line = QtWidgets.QLineEdit(self)
        self.dependents_line.setText('')
        self.dependents_line.setObjectName('dependents')
        self.dependents_line.move(200, 80)

        # accept button
        self.accept = QtWidgets.QPushButton(self)
        self.accept.setText('accept')
        self.accept.move(90, 110)
        self.accept.clicked.connect(self.updatingDependents)

        # cancel button
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setText('Exit')
        self.cancel.move(300, 110)
        self.cancel.clicked.connect(self.addFinance)
        
        self.show()

    # this function saves the information and return to the dashboard    
    def updatingDependents(self):
        """This function updates the number of dependents"""
        
        global dependent_list
        
        try:
            text = self.dependents_line.text().replace(',', ' ')
            total = list(text.split())
    
        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Please follow the instructions')
            return
        
        if total != dependent_list:
            dependent_list = total

        self.close()
        info_Saver(Username, Password)
        self.return_window = Financial_box()
        self.return_window.show()

     # creates an object type addFinances to closes current window without changes
    def addFinance(self):
        self.close()
        self.Finances = Financial_box()
        self.Finances.show()  
#********************CREATING THE APP*********************************           
def AppBox():
    # creating main window
    Budget_app =  QApplication(sys.argv)
    Main_Window = App_Window()
    
    
    
    
    sys.exit(Budget_app.exec())


#-----------coder-Decoder-----------------------------------------------------------
def coder_decoder(character):
    """This function encode and decode a single character using its ancii value"""

    
    # code will be return for encoding before writing in the file
    if ord(character) < 128:
        code = ord(character) + 128

    else:
        code = ord(character) - 128
    
    # return value
    return chr(code)

# -----------------------decoding string---------------------------------------------
def decode_string(string):
    """This function decodes a string using coder_decoder function"""
    decoded = ''
    for char in string:
        decoded += coder_decoder(char)

    return decoded
#------------Math functions-----------------------------------------------------------
def dependent(age):
    """This function save a new dependent into a dependent's list"""

    dependent_list.append(age)

    return

def income(hourly_rate, weekly_hours, house_hold = True):
    """This function returns a realistic income after taxes 
    and other obligations not ususally consider are deducted"""

    
    #This variable holds a gross yearlycalculated income
    y_income = hourly_rate * weekly_hours * 52

    if y_income == 0:
        return 0

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

    if dependent_list[0] != "none":
        for child in dependent_list:
            if int(child) <= 17:
                
                y_income = y_income - expenditure_per_child     

    # after yearly income processed it extimates monthly income
    monthly_income = y_income / 12

    return round(monthly_income, 2)



def mortgage( loan_amount, anual_interest_rate, years,home_value = 0, is_morgatge = False, is_carLoan = False):

    """This function calculates the monthly payment for loan if principal, 
        interest rate and duration are known. Function also have special 
        calculation if is specified as mortgage or carloan"""

    
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


# this blok loads the financial variables for the user
def info_Loader(userName, password, logged = False):
    "This function loads the information for a user"

    Logged = False

    global line_position

    info = []

    with open('Data_base', 'a+') as DB:
        DB.seek(0)

        first_line = DB.readline().split()
        if len(first_line) == 0:
            return False

        DB.seek(0)       
        for line in DB:
            line_position += 1
            info = line.split()
            if len(info) == 0:
                continue

            if (userName == decode_string(info[0]) and  password == decode_string(info[1])):
                Logged = True
                break

    global Username
    Username = decode_string(info[0])

    global Password
    Password = decode_string(info[1])

    global Monthly_Income
    Monthly_Income = float(decode_string(info[2]))

    global Total_assets
    Total_assets = float(decode_string(info[3]))

    global Monthly_housing_expenses
    Monthly_housing_expenses = float(decode_string(info[5]))

    global Monthly_transportation_expenses 
    Monthly_transportation_expenses = float(decode_string(info[4]))

    global dependent_list
    dependent_list = []
    for child in range(6, len(info)):
        dependent_list.append(decode_string(info[child]))

    return Logged

# this block saves the financial variables for the user
def info_Saver(username, password):
    "This function saves the information for a user"
    
    global line_position

    with open('Data_base', 'a+') as DB:
        DB.seek(0)
        whole_text = DB.readlines()
        DB.close()
    with open('Data_base', 'w') as DB:
        for line in whole_text:
            if Username == decode_string(line.split()[0]) and  Password == decode_string(line.split()[1]):
                DB.write(f"{decode_string(Username)} {decode_string(Password)} ") 
                DB.write(f"{decode_string(str(Monthly_Income))} {decode_string(str(Total_assets))} ")
                DB.write(f"{decode_string(str(Monthly_transportation_expenses))} {decode_string(str(Monthly_housing_expenses))} ") 
                if dependent_list[0] != 'none':
                    for child in dependent_list:
                        DB.write(f"{decode_string(child)} ")
                    DB.write(f"\n")
                else:
                    DB.write(f"{decode_string('none')} \n")     
    
                continue
            DB.write(line)
            
#---------------Global Variables-------------------------------
#This string var stores the  username 
Username = ''

#This string var stores the password
Password = ''

#this float var stores the monthly income
Monthly_Income = ''

# this float var stores the total assets
Total_assets = 0.0

#this float var stores the monthly housing expenses
Monthly_housing_expenses = 0.0

#this float var stores the monthly transportation
Monthly_transportation_expenses = 0.0

# this list stores the age of dependents
dependent_list = []

#This var stores the position of teh user line in file
line_position = 0

#----------------APPLICATION-------------------------------
AppBox()
