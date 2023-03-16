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
            #This block generates the unique Id number
            
            Id_available = False
            
            Id = 0
            
            while not Id_available:
                Id = random.randint (100000, 999999)
                
                Id_available = True
                
                with open('Data_base', 'a+') as DB:
                    DB.seek(0)
                    for line in DB:
                        info = line.split()
                        
                        if len(info) == 0:
                            continue

                        if Id == decode_string(info[7]):
                            Id_available = False

                    DB.close()
            
            
            
            
            # writing user information
            with open('Data_base', 'a+') as  DB:
                DB.write(decode_string(userName) + ' ')
                DB.write(decode_string(password)+ ' ')
                DB.write(decode_string('0.0 0.0 0.0 0.0 0.0 '))
                DB.write(f"{decode_string(str(Id))} ")
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
        self.setGeometry(300,300, 600, 650)
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

        # housing label 
        self.housing_label = QtWidgets.QLabel(self)
        self.housing_label.move(40, 120)
        self.housing_label.setText(f'Total monthly debt obligations: {Monthly_Debt_expenses}')

        # dependent label
        self.dependent_label = QtWidgets.QLabel(self)
        self.dependent_label.move(250, 120)
        self.dependent_label.setText(f'Dependents: {dependent_list}')
         
        # add assets button
        self.assets_button = QtWidgets.QPushButton(self)
        self.assets_button.setText('Assets')
        self.assets_button.move(20, 300)
        self.assets_button.clicked.connect(self.add_Assets)

        # add dependents button
        self.dependents_button = QtWidgets.QPushButton(self)
        self.dependents_button.setText('Dependants')
        self.dependents_button.move(115, 300)
        self.dependents_button.clicked.connect(self.add_dependents)
        
        # add income button
        self.income_button = QtWidgets.QPushButton(self)
        self.income_button.setText('Income')
        self.income_button.move(210, 300)
        self.income_button.clicked.connect(self.add_income_window)

        # add transportation expenses button
        self.transportation_button = QtWidgets.QPushButton(self)
        self.transportation_button.setText('Transportation')
        self.transportation_button.move(305, 300)
        self.transportation_button.clicked.connect(self.add_transportation)
        
        # add housing expenses button
        self.housing_button = QtWidgets.QPushButton(self)
        self.housing_button.setText('Housing')
        self.housing_button.move(400, 300)
        self.housing_button.clicked.connect(self.add_housing)

        # add unsecured debt button
        self.debt_button = QtWidgets.QPushButton(self)
        self.debt_button.setText('Unsecured debt')
        self.debt_button.move(495, 300)
        self.debt_button.clicked.connect(self.add_Unsecured_Debts)

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
        """creates an object type add_transportation"""
        self.close()
        self.transportation_window = add_transportation()
        self.transportation_window.show()

    # calling add dependents window    
    def add_dependents(self):
        """creates an object type add_dependents"""
        self.close()
        self.dependents_window = add_dependents()
        self.dependents_window.show()

    # calling add assets window    
    def add_Assets(self):
        """creates an object type add_Assets"""
        self.close()
        self.Assets_window = add_Assets()
        self.Assets_window.show()

    # calling add Unsecured debt window    
    def add_Unsecured_Debts(self):
        """creates an object type add_Unsecured_Debts"""
        self.close()
        self.Unsecured_Debts_window = add_Unsecured_Debts()
        self.Unsecured_Debts_window.show()  
    
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

#-------------------------Assets window--------------------------
class add_Assets(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 600, 500, 230)
        self.setWindowTitle('Add Assets')
        
        # top label 
        self.hours_label = QtWidgets.QLabel(self)
        self.hours_label.move(40, 20)
        self.hours_label.setText('Add your assets, do not include retirement accounts')

        # checking accounts balance label
        self.checking_label = QtWidgets.QLabel(self)
        self.checking_label.move(20, 50)
        self.checking_label.setText('Total balance on checking accounts:')
        
        # checking accounts balance line edit
        self.checking_line = QtWidgets.QLineEdit(self)
        self.checking_line.setText('0.0')
        self.checking_line.setObjectName('checking')
        self.checking_line.move(350, 50)

        # saving accounts balance label
        self.saving_label = QtWidgets.QLabel(self)
        self.saving_label.move(20, 80)
        self.saving_label.setText('Total balance on saving accounts:')
        
        # saving accounts balance line edit
        self.saving_line = QtWidgets.QLineEdit(self)
        self.saving_line.setObjectName('savings')
        self.saving_line.setText('0.0')
        self.saving_line.move(350, 80)

        # saving bonds label
        self.bonds_label = QtWidgets.QLabel(self)
        self.bonds_label.move(20, 110)
        self.bonds_label.setText('Total face value of serie I, serie EE treasure notes or other bonds:')
        
        # saving bonds line edit
        self.bonds_line = QtWidgets.QLineEdit(self)
        self.bonds_line.setObjectName('bonds')
        self.bonds_line.setText('0.0')
        self.bonds_line.move(350, 110)

         # stocks label
        self.stocks_label = QtWidgets.QLabel(self)
        self.stocks_label.move(20, 140)
        self.stocks_label.setText('Non retirement stocks:')
        
        # stocks line edit
        self.stocks_line = QtWidgets.QLineEdit(self)
        self.stocks_line.setObjectName('stocks')
        self.stocks_line.setText('0.0')
        self.stocks_line.move(350, 140)

        # cash balance label
        self.cash_label = QtWidgets.QLabel(self)
        self.cash_label.move(20, 170)
        self.cash_label.setText('Total cash:')
        
        # cash line edit
        self.cash_line = QtWidgets.QLineEdit(self)
        self.cash_line.setText('0.0')
        self.cash_line.setObjectName('checking')
        self.cash_line.move(350, 170)

         # accept button
        self.accept = QtWidgets.QPushButton(self)
        self.accept.setText('accept')
        self.accept.move(40, 200)
        self.accept.clicked.connect(self.updatingHousing)

        # cancel button
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setText('Exit')
        self.cancel.move(135, 200)
        self.cancel.clicked.connect(self.addFinance)
        
        self.show()

    # this function saves the information and return to the dashboard    
    def updatingHousing(self):
        """This function calculates updates the total housing expenses"""
        
        global Total_assets
        try:
            total = float(self.checking_line.text()) + float(self.saving_line.text())
            total += float(self.bonds_line.text()) + float(self.stocks_line.text())
            total += float(self.cash_line.text())
        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Enter numbers only ')
            return
        
        if  Total_assets != total:
            Total_assets = total

        self.close()
        info_Saver(Username, Password)
        self.return_window = Financial_box()
        self.return_window.show()

     # creates an object type addFinances to closes current window without changes
    def addFinance(self):
        self.close()
        self.Finances = Financial_box()
        self.Finances.show()
    
    #-------------------------housing window--------------------------
class add_Unsecured_Debts(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 600, 400, 360)
        self.setWindowTitle('Adding Unsecured Debts')
        
        
        Assets_info = self.input_loader()
        
        # Window's variables
        self.card1Line1 = Assets_info[1]; self.card1Line2 = Assets_info[2]
        self.card2Line1 = Assets_info[3]; self.card2Line2 = Assets_info[4]
        self.card3Line1 = Assets_info[5]; self.card3Line2 = Assets_info[6]
        self.card4Line1 = Assets_info[7]; self.card4Line2 = Assets_info[8]

        decode_string(Assets_info[1])
        
        # top label 
        self.hours_label = QtWidgets.QLabel(self)
        self.hours_label.move(40, 20)
        self.hours_label.setText('Fill your credit card balances and personal loans (up to 4 each)')

        # Balance label 
        self.Balance_label = QtWidgets.QLabel(self)
        self.Balance_label.move(160, 50)
        self.Balance_label.setText('Balance')

        # APR label 
        self.hours_label = QtWidgets.QLabel(self)
        self.hours_label.move(265, 50)
        self.hours_label.setText('APR')

        # Loan Term  label 
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(320, 50)
        self.Term_label.setText('Loan Term')

        # Credit card1 label
        self.card1_label = QtWidgets.QLabel(self)
        self.card1_label.move(20, 80)
        self.card1_label.setText('Credit Card balance 1:')
        
        # Credit card11 line edit
        self.card11_line = QtWidgets.QLineEdit(self)
        self.card11_line.setText(decode_string(Assets_info[1]))
        self.card11_line.setFixedWidth(75)
        self.card11_line.setObjectName('Balance')
        self.card11_line.move(150, 80)

        # Credit card12 line edit
        self.card12_line = QtWidgets.QLineEdit(self)
        self.card12_line.setText(decode_string(Assets_info[2]))
        self.card12_line.setFixedWidth(50)
        self.card12_line.setObjectName('APR')
        self.card12_line.move(250, 80)

        # Loan Term 1 label 
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(330, 80)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText('N/A')

        # Credit card2 label
        self.card2_label = QtWidgets.QLabel(self)
        self.card2_label.move(20, 110)
        self.card2_label.setText('Credit Card balance 2:')
        
        # Credit card21 line edit
        self.card21_line = QtWidgets.QLineEdit(self)
        self.card21_line.setText(decode_string(Assets_info[3]))
        self.card21_line.setFixedWidth(75)
        self.card21_line.setObjectName('Balance')
        self.card21_line.move(150, 110)

        # Credit card22 line edit
        self.card22_line = QtWidgets.QLineEdit(self)
        self.card22_line.setText(decode_string(Assets_info[4]))
        self.card22_line.setFixedWidth(50)
        self.card22_line.setObjectName('APR')
        self.card22_line.move(250, 110)

        # Loan Term 2 label 
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(330, 110)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText('N/A')

        # Credit card3 label
        self.card3_label = QtWidgets.QLabel(self)
        self.card3_label.move(20, 140)
        self.card3_label.setText('Credit Card balance 3:')
        
        # Credit card31 line edit
        self.card31_line = QtWidgets.QLineEdit(self)
        self.card31_line.setText(decode_string(Assets_info[5]))
        self.card31_line.setFixedWidth(75)
        self.card31_line.setObjectName('Balance')
        self.card31_line.move(150, 140)

        # Credit card32 line edit
        self.card32_line = QtWidgets.QLineEdit(self)
        self.card32_line.setText(decode_string(Assets_info[6]))
        self.card32_line.setFixedWidth(50)
        self.card32_line.setObjectName('APR')
        self.card32_line.move(250, 140)

        # Loan Term 1 label 
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(330, 140)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText('N/A')

        # Credit card4 label
        self.card4_label = QtWidgets.QLabel(self)
        self.card4_label.move(20, 170)
        self.card4_label.setText('Credit Card balance 4:')
        
        # Credit card41 line edit
        self.card41_line = QtWidgets.QLineEdit(self)
        self.card41_line.setText(decode_string(Assets_info[7]))
        self.card41_line.setFixedWidth(75)
        self.card41_line.setObjectName('Balance')
        self.card41_line.move(150, 170)

        # Credit card42 line edit
        self.card42_line = QtWidgets.QLineEdit(self)
        self.card42_line.setText(decode_string(Assets_info[8]))
        self.card42_line.setFixedWidth(50)
        self.card42_line.setObjectName('APR')
        self.card42_line.move(250, 170)

        # Loan Term 4 label 
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(330, 170)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText('N/A')

        # Personal loan1 label
        self.loan1_label = QtWidgets.QLabel(self)
        self.loan1_label.move(20, 200)
        self.loan1_label.setText('Personal Loan 1:')
        
        # Personal loan11 line edit
        self.loan11_line = QtWidgets.QLineEdit(self)
        self.loan11_line.setText(decode_string(Assets_info[9]))
        self.loan11_line.setFixedWidth(75)
        self.loan11_line.setObjectName('Balance')
        self.loan11_line.move(150, 200)

        # Personal loan12 line edit
        self.loan12_line = QtWidgets.QLineEdit(self)
        self.loan12_line.setText(decode_string(Assets_info[10]))
        self.loan12_line.setFixedWidth(50)
        self.loan12_line.setObjectName('APR')
        self.loan12_line.move(250, 200)

        # Personal loan13 line edit
        self.loan13_line = QtWidgets.QLineEdit(self)
        self.loan13_line.setText(decode_string(Assets_info[11]))
        self.loan13_line.setFixedWidth(50)
        self.loan13_line.setObjectName('loan term')
        self.loan13_line.move(330, 200)

        # Personal loan2 label
        self.loan1_label = QtWidgets.QLabel(self)
        self.loan1_label.move(20, 230)
        self.loan1_label.setText('Personal Loan 2:')
        
        # Personal loan21 line edit
        self.loan21_line = QtWidgets.QLineEdit(self)
        self.loan21_line.setText(decode_string(Assets_info[12]))
        self.loan21_line.setFixedWidth(75)
        self.loan21_line.setObjectName('Balance')
        self.loan21_line.move(150, 230)

        # Personal loan12 line edit
        self.loan22_line = QtWidgets.QLineEdit(self)
        self.loan22_line.setText(decode_string(Assets_info[13]))
        self.loan22_line.setFixedWidth(50)
        self.loan22_line.setObjectName('APR')
        self.loan22_line.move(250, 230)

        # Personal loan13 line edit
        self.loan23_line = QtWidgets.QLineEdit(self)
        self.loan23_line.setText(decode_string(Assets_info[14]))
        self.loan23_line.setFixedWidth(50)
        self.loan23_line.setObjectName('loan term')
        self.loan23_line.move(330, 230)

         # Personal loan3 label
        self.loan1_label = QtWidgets.QLabel(self)
        self.loan1_label.move(20, 260)
        self.loan1_label.setText('Personal Loan 3:')
        
        # Personal loan31 line edit
        self.loan31_line = QtWidgets.QLineEdit(self)
        self.loan31_line.setText(decode_string(Assets_info[15]))
        self.loan31_line.setFixedWidth(75)
        self.loan31_line.setObjectName('Balance')
        self.loan31_line.move(150, 260)

        # Personal loan32 line edit
        self.loan32_line = QtWidgets.QLineEdit(self)
        self.loan32_line.setText(decode_string(Assets_info[16]))
        self.loan32_line.setFixedWidth(50)
        self.loan32_line.setObjectName('APR')
        self.loan32_line.move(250, 260)

        # Personal loan33 line edit
        self.loan33_line = QtWidgets.QLineEdit(self)
        self.loan33_line.setText(decode_string(Assets_info[17]))
        self.loan33_line.setFixedWidth(50)
        self.loan33_line.setObjectName('loan term')
        self.loan33_line.move(330, 260)

        # Personal loan4 label
        self.loan4_label = QtWidgets.QLabel(self)
        self.loan4_label.move(20, 290)
        self.loan4_label.setText('Personal Loan 4:')
        
        # Personal loan41 line edit
        self.loan41_line = QtWidgets.QLineEdit(self)
        self.loan41_line.setText(decode_string(Assets_info[18]))
        self.loan41_line.setFixedWidth(75)
        self.loan41_line.setObjectName('Balance')
        self.loan41_line.move(150, 290)

        # Personal loan42 line edit
        self.loan42_line = QtWidgets.QLineEdit(self)
        self.loan42_line.setText(decode_string(Assets_info[19]))
        self.loan42_line.setFixedWidth(50)
        self.loan42_line.setObjectName('APR')
        self.loan42_line.move(250, 290)

        # Personal loan43 line edit
        self.loan43_line = QtWidgets.QLineEdit(self)
        self.loan43_line.setText(decode_string(Assets_info[20]))
        self.loan43_line.setFixedWidth(50)
        self.loan43_line.setObjectName('loan term')
        self.loan43_line.move(330, 290)

         # accept button
        self.accept = QtWidgets.QPushButton(self)
        self.accept.setText('accept')
        self.accept.move(110, 320)
        self.accept.clicked.connect(self.updatingDebt)

        # cancel button
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setText('Exit')
        self.cancel.move(205, 320)
        self.cancel.clicked.connect(self.addFinance)
        
        self.show()

    # this function saves the information and return to the dashboard    
    def updatingDebt(self):
        """This function calculates updates the total housing expenses"""

        global Monthly_Debt_expenses
        try:          
            total = mortgage(float(self.card11_line.text()), float(self.card12_line.text()), 3)
            total += mortgage(float(self.card21_line.text()), float(self.card22_line.text()), 3)
            total += mortgage(float(self.card31_line.text()), float(self.card32_line.text()), 3)
            total += mortgage(float(self.card41_line.text()), float(self.card42_line.text()), 3)
            total += mortgage(float(self.loan11_line.text()), float(self.loan12_line.text()), float(self.loan13_line.text())/12)
            total += mortgage(float(self.loan21_line.text()), float(self.loan22_line.text()), float(self.loan23_line.text())/12)
            total += mortgage(float(self.loan31_line.text()), float(self.loan32_line.text()), float(self.loan33_line.text())/12)
            total += mortgage(float(self.loan41_line.text()), float(self.loan42_line.text()), float(self.loan43_line.text())/12)

        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Enter numbers only ')
            return
        
        if Monthly_Debt_expenses != total:
            Monthly_Debt_expenses = total
        
        with open('Assets_Dbase', 'a+') as DB:
            DB.seek(0)
            whole_text = DB.readlines()
            DB.close()
        with open('Assets_Dbase', 'w') as DB:    
            for line in whole_text:
                if str(User_Id) == decode_string(line.split()[0]):
                    DB.write(f"{decode_string(str(User_Id))} {decode_string(self.card11_line.text())} ") 
                    DB.write(f"{decode_string(str(self.card12_line.text()))} {decode_string(str(self.card21_line.text()))} ")
                    DB.write(f"{decode_string(str(self.card22_line.text()))} {decode_string(str(self.card31_line.text()))} ")
                    DB.write(f"{decode_string(str(self.card32_line.text()))} {decode_string(str(self.card41_line.text()))} ")
                    DB.write(f"{decode_string(str(self.card42_line.text()))} {decode_string(str(self.loan11_line.text()))} ")
                    DB.write(f"{decode_string(str(self.loan12_line.text()))} {decode_string(str(self.loan13_line.text()))} ")
                    DB.write(f"{decode_string(str(self.loan21_line.text()))} {decode_string(str(self.loan22_line.text()))} ")
                    DB.write(f"{decode_string(str(self.loan23_line.text()))} {decode_string(str(self.loan31_line.text()))} ")
                    DB.write(f"{decode_string(str(self.loan32_line.text()))} {decode_string(str(self.loan33_line.text()))} ")
                    DB.write(f"{decode_string(str(self.loan41_line.text()))} {decode_string(str(self.loan42_line.text()))} ")
                    DB.write(f"{decode_string(str(self.loan43_line.text()))}  \n")   
                    continue
                DB.write(line)
            DB.close()    
        self.close()
        info_Saver(Username, Password)
        self.return_window = Financial_box()
        self.return_window.show()
    
    # This function load/creates assets info 
    def input_loader(self):
        """This function loads current input"""     

        with open('Assets_Dbase', 'a+') as DB:
            DB.seek(0)
            for line in DB:
                info = line.split()
                if len(info) == 0:
                    continue

                if str(User_Id) == decode_string(info[0]):
                    return info    
                   
            DB.write(f"{decode_string(str(User_Id))} ")
            DB.write(decode_string('0.0 ') * 20)
            DB.write('\n')
            DB.close()
            self.input_loader()

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
        
    # preventing division by zero
    if years == 0:
        months = 1
    
    else:
        # This line creates a variable to hold the calculated duration of loan in months
        months = years * 12
    
    # this line creates a variable to hold the calculated monthly rate
    monthly_rate = anual_interest_rate / 12
    
    # this variable holds the monthly payment and is returned by the function after calculated
    if monthly_rate == 0:
        Monthly = loan_amount/ months

    else:
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

    global Monthly_Debt_expenses
    Monthly_Debt_expenses = float(decode_string(info[6]))

    global User_Id
    User_Id =  int(decode_string(info[7]))

    global dependent_list
    dependent_list = []
    for child in range(8, len(info)):
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
                DB.write(f"{decode_string(str(Monthly_Debt_expenses))} {decode_string(str(User_Id))} ") 
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

#this float var stores the monthly total debt obligations
Monthly_Debt_expenses = 0.0

#This int var stores the user ID number to communicate with otehr files
User_Id = 0      

# this list stores the age of dependents
dependent_list = []

#This var stores the position of the user line in file
line_position = 0



#----------------APPLICATION-------------------------------
AppBox()
