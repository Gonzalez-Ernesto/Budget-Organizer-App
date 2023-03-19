#*******************************GRAPHIC USER INTERFACE*******************
import sys , random, matplotlib.pyplot as ptl , numpy as np, pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QPushButton, QStackedLayout, QLabel, QGridLayout
from PyQt5.QtCore import  QRect, QPropertyAnimation, QSize


#----------------Main Window---------------------------------
class App_Window(QtWidgets.QWidget):
    def __init__(self, * args, ** kwargs):
        super().__init__(* args, ** kwargs)
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Budget Organizer')
        
        global Interactive_layout
        Interactive_layout = QVBoxLayout()
        Interactive_layout.addWidget(Menu_Window())
        self.setLayout(Interactive_layout)
    
        self.show()

#---------------Menu Window------------------------------------------------
class Menu_Window(QtWidgets.QWidget):
    def __init__(self, * args, ** kwargs):
        super().__init__(* args, ** kwargs)
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Menu')

        button_layout = QHBoxLayout()
        button_layout.addWidget(QPushButton('Create Account', clicked = self.signup))
        button_layout.addWidget(QPushButton('Login', clicked = self.login))
        button_layout.addWidget(QPushButton('Exit', clicked = closing))

        #Creating the layout manager
        layout_manager = QHBoxLayout()
        layout_manager.addLayout(button_layout)
        self.setLayout(layout_manager)
    
        self.show()
    
    def signup(self):
        self.close()
        global Interactive_layout
        Interactive_layout.addWidget(User_box())

    def login(self):
        self.close()
        global Interactive_layout
        Interactive_layout.addWidget(Login_box())

def closing():
    sys.exit()

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
        self.cancel.clicked.connect(self.closing)
        
        # showing the window
        self.show()

    def closing(self):
        self.close()
        global Interactive_layout
        Interactive_layout.addWidget(Menu_Window())

    def saving_name(self):
        """This function process all entered information and writes it on a file"""
        
        # these varaiables store the inputs
        userName = self.Username.text().strip()
        password = self.Password.text().strip()
        password2 = self.Re_enterpassword.text().strip() 
        
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
            global Interactive_layout 
            Interactive_layout.addWidget(Login_box())   
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
        cancel = QtWidgets.QPushButton(self)
        cancel.setText('Cancel')
        cancel.move(180, 170)
        cancel.clicked.connect(self.closing)
        
        # showing the window
        self.show()
    

    def closing(self):
        self.close()
        global Interactive_layout
        Interactive_layout.addWidget(Menu_Window())

    # search for the user
    def logging(self):
        """This function analyses the input from user"""

        if  info_Loader(self.Username.text().strip(), self.Password.text().strip()):
                QtWidgets.QMessageBox.information(self, 'Sucess', 'you are logged in')
                self.close()
                global Interactive_layout 
                Interactive_layout.addWidget(Financial_box())

        else:
                QtWidgets.QMessageBox.critical(self, 'Try Again', 'Wrong User or Passwords ')    

#************FINANCE_WINDOW***************************       
class Financial_box(QtWidgets.QWidget):
    """This window adds financial information """
    
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300, 600, 650)
        self.setWindowTitle('Add Financial information')  

        info_Loader(Username, Password)

        #variables for Graphs communication
        global amount
        amount  = Monthly_Income

        global Func_Type
        Func_Type = 'Default'

        self.Pressed = False

        # add assets button
        assets_button = QtWidgets.QPushButton(self)
        assets_button.setText('Assets')
        assets_button.clicked.connect(self.add_Assets)

        # add dependents button
        dependents_button = QtWidgets.QPushButton(self)
        dependents_button.setText('Dependants')
        dependents_button.clicked.connect(self.add_dependents)
        
        # add income button
        income_button = QtWidgets.QPushButton(self)
        income_button.setText('Income')
        income_button.clicked.connect(self.add_income_window)

        # add transportation expenses button
        transportation_button = QtWidgets.QPushButton(self)
        transportation_button.setText('Transportation')
        transportation_button.clicked.connect(self.add_transportation)
        
        # add housing expenses button
        housing_button = QtWidgets.QPushButton(self)
        housing_button.setText('Housing')
        housing_button.clicked.connect(self.add_housing)

        # add unsecured debt button
        debt_button = QtWidgets.QPushButton(self)
        debt_button.setText('Unsecured debt')
        debt_button.clicked.connect(self.add_Unsecured_Debts)

        # income label
        income_label = QtWidgets.QLabel(self)
        income_label.setFixedSize(QSize(280, 50))
        income_label.setFont(QtGui.QFont('Arial', 12))
        income_label.setText(f'Monthly income: {Monthly_Income} ')

        # asset label 
        asset_label = QtWidgets.QLabel(self)
        asset_label.setFixedSize(QSize(280, 50))
        asset_label.setFont(QtGui.QFont('Arial', 12))
        asset_label.setText(f'Total assets: {Total_assets}')

        # transportation label 
        transportation_label = QtWidgets.QLabel(self)
        transportation_label.setFixedSize(QSize(280, 50))
        transportation_label.setFont(QtGui.QFont('Arial', 12))
        transportation_label.setText(f'Monthly transportation expenses: {Monthly_transportation_expenses}')

        # housing label 
        housing_label = QtWidgets.QLabel(self)
        housing_label.setFixedSize(QSize(280, 50))
        housing_label.setFont(QtGui.QFont('Arial', 12))
        housing_label.setText(f'Monthly housing expenses: {Monthly_housing_expenses}')

        # debts label 
        debts_label = QtWidgets.QLabel(self)
        debts_label.setFixedSize(QSize(280, 50))
        debts_label.setFont(QtGui.QFont('Arial', 12))
        debts_label.setText(f'Total monthly debt obligations: {Monthly_Debt_expenses}')

        # dependent label
        dependent_label = QtWidgets.QLabel(self)
        dependent_label.setFixedSize(QSize(280, 50))
        dependent_label.setFont(QtGui.QFont('Arial', 12))
        dependent_label.setText(f'Dependents: {dependent_list}')
        
        Label_layout = QGridLayout()
        Label_layout.addWidget(income_label, 0, 0)
        Label_layout.addWidget(asset_label, 0, 1)
        Label_layout.addWidget(transportation_label, 1, 0)
        Label_layout.addWidget(housing_label, 1, 1)
        Label_layout.addWidget(debts_label, 2, 0)
        Label_layout.addWidget(dependent_label, 2, 1)
        Label_layout.addWidget(QPushButton('Explain These numbers to me' , clicked = self.Explanation))
        Label_layout.addWidget(QPushButton('Detailed Report' , clicked = self.detailed_info))

        button_layout = QHBoxLayout()
        button_layout.addWidget(assets_button)
        button_layout.addWidget(dependents_button)
        button_layout.addWidget(income_button)
        button_layout.addWidget(transportation_button)
        button_layout.addWidget(housing_button)
        button_layout.addWidget(debt_button)

        button_layout2 = QHBoxLayout()
        button_layout2.addWidget(QPushButton('Nothing Changes' , clicked = self.Nothing_changes))
        button_layout2.addWidget(QPushButton('Buying House', clicked = self.Buying_House))
        button_layout2.addWidget(QPushButton('Receive More Assets', clicked = self.MoreAssets_Event))
        button_layout2.addWidget(QPushButton('Payoff Debts', clicked = self.PayingOff_Debts))

        button_layout3 = QHBoxLayout()
        button_layout3.addWidget(QPushButton('Switch Jobs' , clicked = self.New_Income))
        button_layout3.addWidget(QPushButton('Lose Job', clicked = self.Losing_Job))
        button_layout3.addWidget(QPushButton('Buying Car', clicked = self.Buying_Car))
        button_layout3.addWidget(QPushButton('Get More Debts', clicked = self.Getting_Debts))
        button_layout3.addWidget(QPushButton('Unexpected Negative Balance', clicked = self.Unexpected_Event))
        
        # Hypotetical label
        Hypotetical = QLabel(self)
        Hypotetical.setFont(QtGui.QFont('Arial', 14))
        Hypotetical.setText('Where I would be in six months if I...')

        button_layout4 = QHBoxLayout()
        button_layout4.addWidget(QPushButton('Log out', clicked = self.closing))
        button_layout4.addWidget(QPushButton('Exit', clicked = closing))
        
        # layout with with buttons and lables
        LabelBUtton_layout = QVBoxLayout()
        LabelBUtton_layout.addLayout(Label_layout)
        LabelBUtton_layout.addLayout(button_layout)
        LabelBUtton_layout.addWidget(Hypotetical)
        LabelBUtton_layout.addLayout(button_layout2)
        LabelBUtton_layout.addLayout(button_layout3)
        LabelBUtton_layout.addLayout(button_layout4)
        
        #Creating the layout manager
        self.layout_manager = QVBoxLayout()
        self.layout_manager.addLayout(LabelBUtton_layout, 50)
        self.layout_manager.addWidget(add_Graph())
        self.setLayout(self.layout_manager)
        
        self.show()

    
    
    #defining buying car
    def Buying_Car(self):
        """Creates a dialog window for buying car"""

        global Interactive_layout
        global Func_Type
        
        #setting Func_Type to order desired graph from add_graph window
        Func_Type = 'Buying Car'

        self.Balance = QtWidgets.QLineEdit(self)
        self.Balance.setText('0.0')
        self.APR = QtWidgets.QLineEdit(self)
        self.APR.setText('0.0')
        self.LoanTerm = QtWidgets.QLineEdit(self)
        self.LoanTerm.setText('0.0')
        
        global Layout
        Layout = QGridLayout()
        Layout.addWidget(QLabel('Enter The portion of the car loan that you are financing, the APR and loan term'), 0, 0)
        Layout.addWidget(QLabel('Balance'), 1, 0)
        Layout.addWidget(self.Balance, 1, 1)
        Layout.addWidget(QLabel('Rate'), 2, 0)
        Layout.addWidget(self.APR, 2, 1)
        Layout.addWidget(QLabel('Car Loan Term'), 3, 0)
        Layout.addWidget(self.LoanTerm,3 ,1)
        Layout.addWidget(QPushButton('Accept', clicked = self.Call_MoreDebtGraph))
        Layout.addWidget(QPushButton('Back', clicked = self.Back))
        
        self.close()
        global Window
        Window = QtWidgets.QWidget()
        Window.setLayout(Layout)

        Interactive_layout.addWidget(Window)
    
    #defining paying off debts
    def PayingOff_Debts(self):
        """Creates a dialog window for paying off debts"""

        global Interactive_layout
        global Func_Type
        
        #setting Func_Type to order desired graph from add_graph window
        Func_Type = 'Pay off Debt'

        self.Balance = QtWidgets.QLineEdit(self)
        self.Balance.setText('0.0')
        self.APR = QtWidgets.QLineEdit(self)
        self.APR.setText('0.0')
        self.LoanTerm = QtWidgets.QLineEdit(self)
        self.LoanTerm.setText('0.0')
        
        global Layout
        Layout = QGridLayout()
        Layout.addWidget(QLabel('Enter The Amount that you are planing to pay off, the APR and loan term'), 0, 0)
        Layout.addWidget(QLabel('Balance'), 1, 0)
        Layout.addWidget(self.Balance, 1, 1)
        Layout.addWidget(QLabel('Rate'), 2, 0)
        Layout.addWidget(self.APR, 2, 1)
        Layout.addWidget(QLabel('Loan Term'), 3, 0)
        Layout.addWidget(self.LoanTerm,3 ,1)
        Layout.addWidget(QPushButton('Accept', clicked = self.Call_MoreDebtGraph))
        Layout.addWidget(QPushButton('Back', clicked = self.Back))
        
        self.close()
        global Window
        Window = QtWidgets.QWidget()
        Window.setLayout(Layout)

        Interactive_layout.addWidget(Window)  

    def Unexpected_Event(self):
        """Creates a dialog window for Unexpected event"""

        global Interactive_layout
        global Func_Type
        
        #setting Func_Type to order desired graph from add_graph window
        Func_Type = 'Unexpected'

        self.rate = QtWidgets.QLineEdit(self)
        self.rate.setText('0.0')
        
        global Layout
        Layout = QVBoxLayout()
        Layout.addWidget(QLabel('Enter the cost of the financial unexpected event'))
        Layout.addWidget(self.rate)
        Layout.addWidget(QPushButton('Accept', clicked = self.Call_UnexpectedEventGraph))
        Layout.addWidget(QPushButton('Back', clicked = self.Back))
        
        self.close()
        global Window
        Window = QtWidgets.QWidget()
        Window.setLayout(Layout)

        Interactive_layout.addWidget(Window) 

    #defining buying house
    def Buying_House(self):
        """Creates a dialog window for buying house"""

        global Interactive_layout
        global Func_Type
        
        #setting Func_Type to order desired graph from add_graph window
        Func_Type = 'Buying House'

        self.Balance = QtWidgets.QLineEdit(self)
        self.Balance.setText('0.0')
        self.HouseValue = QtWidgets.QLineEdit(self)
        self.HouseValue.setText('0.0')
        self.APR = QtWidgets.QLineEdit(self)
        self.APR.setText('0.0')
        self.LoanTerm = QtWidgets.QLineEdit(self)
        self.LoanTerm.setText('0.0')

        global Layout
        Layout = QGridLayout()
        Layout.addWidget(QLabel('Enter the portion of the cost that you are planing to finance,\n the value of the house, the APR and mortgage term'), 0, 0)
        Layout.addWidget(QLabel('Balance'), 1, 0)
        Layout.addWidget(self.Balance, 1, 1)
        Layout.addWidget(QLabel('Home Value'), 2, 0)
        Layout.addWidget(self.HouseValue, 2, 1)
        Layout.addWidget(QLabel('APR'), 3, 0)
        Layout.addWidget(self.APR, 3, 1)
        Layout.addWidget(QLabel('Mortgage Term'), 4, 0)
        Layout.addWidget(self.LoanTerm,4 ,1)
        Layout.addWidget(QPushButton('Accept', clicked = self.Call_MoreDebtGraph))
        Layout.addWidget(QPushButton('Back', clicked = self.Back))
        
        self.close()
        global Window
        Window = QtWidgets.QWidget()
        Window.setLayout(Layout)

        Interactive_layout.addWidget(Window) 

    #defining unexpected event
    def Unexpected_Event(self):
        """Creates a dialog window for Unexpected event"""

        global Interactive_layout
        global Func_Type
        
        #setting Func_Type to order desired graph from add_graph window
        Func_Type = 'Unexpected'

        self.rate = QtWidgets.QLineEdit(self)
        self.rate.setText('0.0')
        
        global Layout
        Layout = QVBoxLayout()
        Layout.addWidget(QLabel('Enter the cost of the financial unexpected event'))
        Layout.addWidget(self.rate)
        Layout.addWidget(QPushButton('Accept', clicked = self.Call_UnexpectedEventGraph))
        Layout.addWidget(QPushButton('Back', clicked = self.Back))
        
        self.close()
        global Window
        Window = QtWidgets.QWidget()
        Window.setLayout(Layout)

        Interactive_layout.addWidget(Window)    
    #defining more debts
    def Getting_Debts(self):
        """Creates a dialog window for more debts"""

        global Interactive_layout
        global Func_Type
        
        #setting Func_Type to order desired graph from add_graph window
        Func_Type = 'More Debt'

        self.Balance = QtWidgets.QLineEdit(self)
        self.Balance.setText('0.0')
        self.APR = QtWidgets.QLineEdit(self)
        self.APR.setText('0.0')
        self.LoanTerm = QtWidgets.QLineEdit(self)
        self.LoanTerm.setText('0.0')

        global Layout
        Layout = QGridLayout()
        Layout.addWidget(QLabel('Enter The Amount that you are planing to borrow, the APR and the loan term'), 0, 0)
        Layout.addWidget(QLabel('Balance'), 1, 0)
        Layout.addWidget(self.Balance, 1, 1)
        Layout.addWidget(QLabel('Rate'), 2, 0)
        Layout.addWidget(self.APR, 2, 1)
        Layout.addWidget(QLabel('Loan Term'), 3, 0)
        Layout.addWidget(self.LoanTerm,3 ,1)
        Layout.addWidget(QPushButton('Accept', clicked = self.Call_MoreDebtGraph))
        Layout.addWidget(QPushButton('Back', clicked = self.Back))
        
        self.close()
        global Window
        Window = QtWidgets.QWidget()
        Window.setLayout(Layout)

        Interactive_layout.addWidget(Window)    
    #defining unexpected event
    def Unexpected_Event(self):
        """Creates a dialog window for Unexpected event"""

        global Interactive_layout
        global Func_Type
        
        #setting Func_Type to order desired graph from add_graph window
        Func_Type = 'Unexpected'

        self.rate = QtWidgets.QLineEdit(self)
        self.rate.setText('0.0')
        
        global Layout
        Layout = QVBoxLayout()
        Layout.addWidget(QLabel('Enter the cost of the financial unexpected event'))
        Layout.addWidget(self.rate)
        Layout.addWidget(QPushButton('Accept', clicked = self.Call_UnexpectedEventGraph))
        Layout.addWidget(QPushButton('Back', clicked = self.Back))
        
        self.close()
        global Window
        Window = QtWidgets.QWidget()
        Window.setLayout(Layout)

        Interactive_layout.addWidget(Window)

    #defining unexpected event
    def MoreAssets_Event(self):
        """Creates a dialog window for More Assets"""

        global Interactive_layout
        global Func_Type
        
        #setting Func_Type to order desired graph from add_graph window
        Func_Type = 'MoreAssets'

        self.rate = QtWidgets.QLineEdit(self)
        self.rate.setText('0.0')
        
        global Layout
        Layout = QVBoxLayout()
        Layout.addWidget(QLabel('Enter the capital that you are receiving'))
        Layout.addWidget(self.rate)
        Layout.addWidget(QPushButton('Accept', clicked = self.Call_UnexpectedEventGraph))
        Layout.addWidget(QPushButton('Back', clicked = self.Back))
        
        self.close()
        global Window
        Window = QtWidgets.QWidget()
        Window.setLayout(Layout)

        Interactive_layout.addWidget(Window)

    # defining Nothing changes
    def Nothing_changes(self):
        """Orders a graph with the current situation only"""

        global Interactive_layout
        global Func_Type
       
        Func_Type = 'Nothing Changes'
        self.close()

        #Brings the graph to the front
        Interactive_layout.addWidget(add_Graph())
    
    # defining New Income
    def  New_Income(self):
        """Orders a graph comparing current and expected income"""
        global Interactive_layout
        global Func_Type
       
        #setting Func_Type to order desired graph from add_graph window
        Func_Type = 'Different Income'
        
        actual_info = self.input_loader('Income_DBase')
        #editline to get the rate
        self.rate = QtWidgets.QLineEdit(self)
        self.hours = QtWidgets.QLineEdit(self)
        if len(actual_info) != None:
            self.hours.setText(f'{actual_info[2]}')
            self.rate.setText(f'{actual_info[1]}')
        else:
            self.hours.setText(f'0.0')
            self.rate.setText(f'0.0')
            
        self.close()

        global Layout
        Layout = QGridLayout()
        Layout.addWidget(QLabel('Enter the new income information'), 0, 0)
        Layout.addWidget(QLabel('Enter the new rate'), 1, 0 )
        Layout.addWidget(self.rate, 1, 1)
        Layout.addWidget(QLabel('Enter the expected hours per week'), 2, 0)
        Layout.addWidget(self.hours, 2, 1)
        Layout.addWidget(QPushButton('Accept', clicked = self.Call_NewIncomeGraph), 3, 0)
        Layout.addWidget(QPushButton('Back', clicked = self.Back), 3, 1)

        global Window
        Window = QtWidgets.QWidget()
        Window.setLayout(Layout)

        Interactive_layout.addWidget(Window)

    def Losing_Job(self):
        """Orders a graph setting income to zero"""

        global Interactive_layout
        global Func_Type

        global amount
        amount = 0
       
        Func_Type = 'Lose Job'
        self.close()

        #Brings the graph to the front
        Interactive_layout.addWidget(add_Graph())

    def Call_MoreDebtGraph(self):
        """Orders a graph comparing current income vs more debt"""
        
        house = False

        car = False

        homeValue = 0

        global amount
        if float(self.Balance.text().strip()) <= 0:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'If your balance is zero then press the BACK button')    
            return
        
        if Func_Type == 'Buying House':
            house = True
            homeValue = float(self.HouseValue.text().strip())

        elif Func_Type == 'Buying Car':
            car = True
            
                
        if float(self.Balance.text().strip()) > 0 and float(self.LoanTerm.text().strip()) == 0:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'If Balance is different from zero term cannot be zero')
            return    
        
        try:
            amount = mortgage(float(self.Balance.text().strip()), float(self.APR.text().strip()),
                               float(self.LoanTerm.text().strip())/12,home_value= homeValue
                                 ,is_morgatge=house, is_carLoan=car)
        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Enter numbers only ')
            return
        self.close()
        global Window
        Interactive_layout.removeWidget(Window)
        del Window
        Interactive_layout.addWidget(add_Graph())

    def Call_UnexpectedEventGraph(self):
        """Orders a graph comparing current income vs expected income"""
        
        if float(self.rate.text().strip()) <= 0:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'If your balance is zero then press the BACK button')    
            return
        
        try:
            global amount
            amount = float(self.rate.text().strip())

             #setting Func_Type to order desired graph from add_graph window
        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Enter numbers only ')
            return
        self.close()
        global Window
        Interactive_layout.removeWidget(Window)
        del Window
        Interactive_layout.addWidget(add_Graph())

    def Call_NewIncomeGraph(self):
        """Orders a graph comparing current income vs expected income"""
        
        
        
        try:
            global amount
            amount = income(float(self.rate.text().strip()), float(self.hours.text().strip()))
        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Enter numbers only ')
            return
        if amount == 0:
            QtWidgets.QMessageBox.critical(self, 'Try Again','If your projected income is zero, then you are\n' 
                                           'actually losing your job.\n Press BACK if that is the case ')
            return
        
        self.close()
        global Window
        Interactive_layout.removeWidget(Window)
        del Window
        Interactive_layout.addWidget(add_Graph())

    def Continue(self):
        self.Pressed = True
        return self.Pressed

    def Back(self):
        self.close()
        global Window
        Interactive_layout.removeWidget(Window)
        del Window
        Interactive_layout.addWidget(Financial_box())

    # returns tu main window    
    def closing(self):
        self.close()
        global Interactive_layout
        Interactive_layout.addWidget(Menu_Window())

    # calling add income window    
    def add_income_window(self):
        """creates an object type add_income"""
        self.close()
        global Interactive_layout 
        Interactive_layout.addWidget(add_income())

    # calling add housing window    
    def add_housing(self):
        """creates an object type add_housing"""
        self.close()
        global Interactive_layout 
        Interactive_layout.addWidget(add_housing())

    # calling add transportation window    
    def add_transportation(self):
        """creates an object type add_transportation"""
        self.close()
        global Interactive_layout 
        Interactive_layout.addWidget(add_transportation())

    # calling add dependents window    
    def add_dependents(self):
        """creates an object type add_dependents"""
        self.close()
        global Interactive_layout 
        Interactive_layout.addWidget(add_dependents())

    # calling add assets window    
    def add_Assets(self):
        """creates an object type add_Assets"""
        self.close()
        global Interactive_layout 
        Interactive_layout.addWidget(add_Assets())

    # calling add Unsecured debt window    
    def add_Unsecured_Debts(self):
        """creates an object type add_Unsecured_Debts"""
        self.close()
        global Interactive_layout 
        Interactive_layout.addWidget(add_Unsecured_Debts())

    def Explanation(self):
        """shows explanation"""
        
        text = "Income: Your hourly rate and hours per week are used to estimate your yearly income.\n"
        text += "using the IRS guidelines, the expected federal taxes are also subtracted.\n"
        text += "For each dependent under the age of 18, a fixed amount is calculated based on the national average,\n"
        text += "and your gross income is also deducted from your estimated after-tax income, the rest is divided into 12 months.\n\n"
        text += "Transportation: The estimated annual maintenance and fuel cost is divided into 12 months\n\n"
        text += "Unsecured Debts: Interest is also included in the monthly payment, and for credit cards,\n" 
        text += "the monthly payment is estimated aiming to pay off the balance in three years\n"

        QtWidgets.QMessageBox.information(self, 'Explanation', text)

    def detailed_info(self):
        """Shows detailed info"""

        income_array = self.input_loader('Income_DBase')
        housing_array = self.input_loader('Housing_DBase')
        assets_array = self.input_loader('Assets_DBase')
        transportation_array = self.input_loader('Transportation_DBase')
        debts_array = self.input_loader('Debts_DBase')

        #number of childs
        children = 0
        children_total = 0
        if dependent_list[0] != 'none':
            for child in dependent_list:
                if int(child) < 18:
                    children  += 1

            #calculating monthly child expenses
            children_total = children * round(((income_array[1] * income_array[2] * 52)/ 107400) * 12980 / 12, 2)    
        
        #Adding only relevant information  (variable or result != 0)
        text = "Income:\n"
        if income_array != None:
            if income_array[1] != 0 and income_array[2] != 0:
                text += " Monthly Gross Income: " + str(round((income_array[1] * income_array[2] * 52)/12, 2)) + '\n'
        if children_total != 0:
            text += " Extimated Cost of Rising Your Children per Month: " + str(children_total) + '\n'
        text += '\n'

        text += "Assets Expenses:\n"
        if assets_array != None:
            if assets_array[1] != 0:
                text += "  Money on Checking Accounts: " + str(assets_array[1]) + '\n'
            if assets_array[2] != 0:
                text += "  Money on Saving Accounts: " + str(assets_array[2]) + '\n'
            if assets_array[3] != 0:
                text += "  Money Invested in Bonds: "  +  str(assets_array[3]) + '\n'      
            if assets_array[4] != 0:
                text += "  Money Invested in Stocks: "  +  str(assets_array[4]) + '\n'
            if assets_array[1] != 0:
                text += "  Cash: "  +  str(assets_array[5]) + '\n'
            text += '\n'

        text += "Housing Expenses:\n"
        if housing_array != None:
            if housing_array[1] != 0:
                text += "  Monthly House Payment: " + str(housing_array[1]) + '\n'
            if housing_array[2] != 0:
                text += "  Monthly Extimated Property insurance: " + str(housing_array[2]) + '\n'
            if housing_array[3] != 0:
                text += "  Monthly Electric Bill: " + str(housing_array[3]) + '\n'
            if housing_array[4] != 0:    
                text += "  Monthly Internet Bill: " + str(housing_array[4]) + '\n'
            if housing_array[5] != 0:
                text += "  Monthly Extimated Property Taxes: " + str(housing_array[5]) + '\n'
            if housing_array[6] != 0:
                text += "  Monthly HOA Dues: " + str(housing_array[6]) + '\n'
            if housing_array[7] != 0:
                text += "  Monthly Extimated Gas Bill: " + str(housing_array[7]) + '\n'
            text += '\n'

        
        text += "Transpotation Expenses:\n" 
        if transportation_array != None:
            if transportation_array[1] != 0:
                text += "  Monthly Car Payment: " + str(transportation_array[1]) + '\n'
            if transportation_array[2] != 0:
                text += "  Monthly car Insurance Payment: " + str(transportation_array[2]) + '\n'
            if transportation_array[3] != 0:
                text += "  Monthly Car Extimated Maintenance: " + str(round(transportation_array[3]* 0.09, 2)) + '\n'
                text += "  Monthly Fuel Cost : " + str(round(transportation_array[3] * 0.0955, 2)) + '\n' 
            text += '\n'   
        
        text += "Monthly Unsecured Debt Obligations:\n"
        if debts_array != None:
            if debts_array[21] != 0:
                text += "  Credit Card1 Monthly Payment: " + str(debts_array[21]) + '\n'
            if debts_array[22] != 0:
                text += "  Credit Card2 Monthly Payment: " + str(debts_array[22]) + '\n'
            if debts_array[23] != 0:
                text += "  Credit Card3 Monthly Payment: " + str(debts_array[23]) + '\n'
            if debts_array[24] != 0:
                text += "  Credit Card4 Monthly Payment: " + str(debts_array[24]) + '\n'
            if debts_array[25] != 0:
                text += "  Loan1 Monthly Payment: " + str(debts_array[25]) + '\n'
            if debts_array[26] != 0:
                text += "  Loan2 Card1 Monthly Payment: " + str(debts_array[26]) + '\n'
            if debts_array[27] != 0:
                text += "  Loan3 Card1 Monthly Payment: " + str(debts_array[27]) + '\n'
            if debts_array[28] != 0:
                text += "  Loan4 Card1 Monthly Payment: " + str(debts_array[28]) + '\n'
    
        QtWidgets.QMessageBox.information(self, 'Detailed Information', text)
    
    def input_loader(self, file):
        """This function loads current input"""     
        
        info1 = []
        with open(file, 'a+') as DB:
            DB.seek(0)
            for line in DB:
                info = line.split()
                if len(info) == 0:
                    continue
                if str(User_Id) == decode_string(info[0]):
                    for i in info:
                        info1.append(float(decode_string(i)))
                    return info1
        
#//////////////////Sub Window Graph //////////////////////////////
class add_Graph(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 600, 400, 200)
        self.setWindowTitle('Add Financial information')

        #creating graphs
        
        # variables
        global amount
        
        Liabilities = Monthly_Debt_expenses  + Monthly_housing_expenses
        Liabilities += Monthly_transportation_expenses 

        Residual_income = Monthly_Income - Liabilities

        months = []
        for month in range(7):
            months.append(Residual_income*month)

        default_graph = MplCanvas(self, width=5, height=4, dpi=100)
    
        #default dictionary
        d = {
               'Current situation' : months
            }
        
        if Func_Type == 'Different Income':

            Residual_income += amount - Monthly_Income
            months1 = []
            for i in range(7):
                months1.append(Residual_income*i)

            d['If you switch jobs'] = months1

        elif Func_Type == 'Lose Job':
        
            months1 = []
            for i in range(7):
                months1.append(Liabilities*i*(-1))
  
            d['Lose jobs'] = months1

        elif Func_Type == 'More Debt':
            Liabilities += amount
            Residual_income = Monthly_Income - Liabilities

            months1 = []
            for i in range(7):
                months1.append(Residual_income*i)
  
            d['More Debt'] = months1
        
        elif Func_Type == 'Pay off Debt':
            Liabilities -= amount

            Residual_income = Monthly_Income - Liabilities

            months1 = []
            for i in range(7):
                months1.append(Residual_income*i)
  
            d['Paying off Debt'] = months1

        elif Func_Type == 'Buying House':
            Liabilities += amount - Monthly_housing_expenses

            Residual_income = Monthly_Income - Liabilities

            months1 = []
            for i in range(7):
                months1.append(Residual_income*i)
  
            d['New house as your primary residence'] = months1

        elif Func_Type == 'Buying Car':
            Liabilities += amount - Monthly_transportation_expenses

            Residual_income = Monthly_Income - Liabilities

            months1 = []
            for i in range(7):
                months1.append(Residual_income*i)
  
            d['Remplacing Your Car'] = months1


        # creating the informational layout
        layout_info = QVBoxLayout()

        #if-elif-else text generator
        text = f'Your projected accumulated capital if your situation does not change  is {round(months[6], 2)}.\n'
        if Func_Type == 'Different Income':
            text += f'If you switch jobs your projected accumulated capital for the six months is {round(months1[6], 2)}.\n'
            if months[6] < months1[6]:
                text += f'This is better than your current situation.\n'
                if months1[6] > 0 and  Monthly_Debt_expenses > 0:
                    text += "You should pay some debts as soon you start receiving the new income.\n"
                elif months1[6] > 0:
                    text += "Although you would have extra money do not forget to save some.\n"
                else:
                    text += "Although your situation would look better it would not be enough to afford your current live style.\n"
            elif months1[6] - months[6] < 50:
                text += "Your financial situation would be about the same if you switch jobs.\n"
                text += "However money should not be the main or only reason for your decision.\n"
            else:
                text += "Your financial situation would be worse if you switch jobs.\n"
                text += "However money should not be the main or only reason for your decision.\n"
        elif Func_Type == 'Lose Job':
            text += f'If you lose your job your projected accumulated capital for the six months is {round(months1[6], 2)}.\n'
            text += f"Your total assets is {Total_assets}.\n"
            how_long = 0
            if Liabilities > 0:
                int(Total_assets/Liabilities)
            if Total_assets - months1[6] != 0:
                text += "You have enough assets to afford this period. You can take a break if you want to.\n"
            
            elif how_long > 0:
                if how_long != 0:   
                    text += f"You have enough assets to afford {how_long}. Think about your situaation carefuly.\n"
            else:
                text += "You do not have enough assets to afford a month. " 
                text += "You should start looking for another job asap.\n"
        elif Func_Type == 'Unexpected':
            text += f"Your total assets is {Total_assets} and you need {amount}.\n"
            if Total_assets >= amount:
                text += f"You can cover this amount with your assets "
                if Total_assets - amount > 500:
                    text += f"and you still will have {Total_assets - amount}.\n" 
                elif Total_assets - amount < 500 and Total_assets - amount > 0: 
                    text += f"but this will almost wipe out your assets entirelly.\n"
                else: 
                    text += "but this is it.\n "
            if amount > Total_assets:
                text += f"You do not have enough liquidity to cover this amount entiraly.\n"
                text += f"You still need {amount - Total_assets}.\n If this is not an "
                text += f" emergency you may want to avoid this event.\n"
                text += f"otherwise you need to borrow the difference\n" 
        elif Func_Type == 'MoreAssets':
            text += f"You are receiving {amount}. This are great News!!!"
            if months[6] < 0:
                text += f"However do not forget that your proyected accumulated capital \n"
                text += f"for the next six months is negative."
                if amount > abs(months[6]) :
                    text += f"You can cover this deficit with this amount without changing \n "
                    text += f"The current state of your assets and debts.\n"
                    if  amount - abs(months[6]) > 50:
                        text += f" and you still would have {round(amount - abs(months[6]), 2)}.\n"
                    else:
                        text += "and you get to keep the change.\n "
                else:
                    text += f"You can cover {int(amount/Liabilities)} months.\n"
            elif months[6] >= 0 and Monthly_Debt_expenses > 0:
                text += "You should use this amount to pay some debts.\n"
            elif months[6] >= 0 and Total_assets < 500:
                text += "Since your current assets are low you should save this amount.\n"
            else:
                text += "Your financial situation is in a good shape just do not forget to save some.\n"
        elif Func_Type == 'More Debt':
            text += f'Your projected accumulated capital if you get this loan is {round(months1[6], 2)}.\n'
            if Total_assets > 0:
                f"You should consider using your assets if you can before getting this loan.\n"
            if months[6]  < 0:
                text +=  "Getting this loan would make worse your already bad financial situation. "
                if Monthly_Debt_expenses > 0:
                    text += "You should pay other debts if possible.\n"
                else:
                    "\n"
                text += "Using the money to cover your monthly deficit is the best idea.\n"
            elif months[6] > 0 and months1[6] < 0:
                text += "This loan will nearly or actually create a monthly deficit that you wiould not have otherwise.\n"
        elif Func_Type == 'Pay off Debt':
            text += f'Your projected accumulated capital if you paritally or totally pay off your debts is {round(months1[6], 2)}.\n'
            if amount > Monthly_Debt_expenses:
                text += "Remember that you cannot pay more than what you owe so the rest goes towar your assets.\n"
            text += f'Paying of your debts is good for your financial health.\n'
            if int(Monthly_Debt_expenses) >= int(amount):
                text += f'In this case you would be debt free.\n'
            else:
                text += f"Although you still have to pay {round(Monthly_Debt_expenses - amount, 2)} every month \n"
                text += "your financial situation would improve.\n"
            if Total_assets < 300:
                text += f"One last consideration is that your assets are low, you may want to put some money toward your assets \n "    
                text += "in case you need it in the future even though this means paying less debts.\n"
        elif Func_Type == 'Buying House':
            text += f'If you buy a new house your projected accumulated capital for the six months is {round(months1[6], 2)}.\n'
            text += f"Your new monthly housing expenses would be {round(amount, 2)}.\n"
            if  amount - Monthly_housing_expenses  > 50:
                text += "This is more than your current monthly housing expenses.\n"
                if months[6] < 0:
                    text += "This will make worse your already bad financial situation.\n"
                elif months[6] > 0 and  months1[6] < 0:
                    text += "This will create a negative projected balance\n"
                else:
                    text += "You still can afford this change.\n"                             
            elif amount - Monthly_housing_expenses  < 50 or amount - Monthly_housing_expenses  > -50:
                 text += "This is about your current monthly housing expenses.\n"
            else:  
                text += "This is less than your current monthly housing expenses and\n"
                text += "definitively a great decision. However money should not be the only factor to consider.\n"
            
        elif Func_Type == 'Buying Car':
            text += f'If you change your car your projected accumulated capital for the six months is {round(months1[6], 2)}.\n'
            text += f"Your new monthly transportation expenses would be {round(amount, 2)}.\n"
            if  amount - Monthly_transportation_expenses  > 50:
                text += "This is more than your current monthly transportation expenses.\n"
                if months[6] < 0:
                    text += "This will make worse your already bad financial situation.\n"
                elif months[6] > 0 and  months1[6] < 0:
                    text += "This will create a negative projected balance\n"
                else:
                    text += "You still can afford this change.\n"                             
            elif amount - Monthly_transportation_expenses  < 50 or amount - Monthly_transportation_expenses  > -50:
                 text += "This is about your current monthly transportation expenses.\n"
            else:  
                text += "This is less than your current monthly transportation expenses and\n"
                text += "definitively a great decision. However money should not be the only factor to consider.\n"
        
        if Func_Type != 'Default':
            layout_info.addWidget(QLabel(text))
        layout_info.addWidget(QPushButton("Back", clicked = self.Closing))
        
        #defining the data frame
        df = pd.DataFrame(d)
        df.plot(ax=default_graph.axes)
        
        #Creating the layout manager
        layout_manager = QVBoxLayout()
        layout_manager.addWidget(default_graph)
        layout_manager.addLayout(layout_info)
        self.setLayout(layout_manager)     
            
        self.show()   
    
    def Closing(self):
        global Func_Type
        Func_Type = 'Default' 

        global amount
        amount = Monthly_Income  
        self.close()

        global Interactive_layout
        Interactive_layout.addWidget(Financial_box())

#//////////////////SUBWINDOWs OF ADD FINANCE//////////////////////
#-------------------------Income window--------------------------
class add_income(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 600, 400, 200)
        self.setWindowTitle('Add Financial information')

        # Creating the file
        self.input_loader()

        #loading saved info
        Income_info = self.input_loader()
        
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
        self.rate_line.setText(decode_string(Income_info[1]))
        self.rate_line.setObjectName('rate')
        self.rate_line.move(135, 80)

        # hours label
        self.hours_label = QtWidgets.QLabel(self)
        self.hours_label.move(40, 120)
        self.hours_label.setText('Hours per week:')
        
        # hours line edit
        self.hours_line = QtWidgets.QLineEdit(self)
        self.hours_line.setText(decode_string(Income_info[2]))
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
        
        #self.show()
        
    # this function saves the information and return to the dashboard
    def updatingIncome(self):
        """This function updates the total income passing the entered information to teh function income"""
        
        global Monthly_Income
        try:
            total = income(float(self.rate_line.text().strip()), float(self.hours_line.text().strip()))
        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Enter numbers only ')
            return
        
        if Monthly_Income != total:
            Monthly_Income = total

        with open('Income_Dbase', 'a+') as DB:
            DB.seek(0)
            whole_text = DB.readlines()
            DB.close()
        with open('Income_Dbase', 'w') as DB:    
            for line in whole_text:
                if str(User_Id) == decode_string(line.split()[0]):
                    DB.write(f"{decode_string(str(User_Id))} {decode_string(self.rate_line.text().strip())} ") 
                    DB.write(f"{decode_string(self.hours_line.text().strip())} \n")   
                    continue
                DB.write(line)
            DB.close()    
        self.close()

        #Updating global variables and returning to addFinances
        info_Saver(Username, Password)
        self.close()
        global Interactive_layout 
        Interactive_layout.addWidget(Financial_box())

    # This function load/creates income info 
    def input_loader(self):
        """This function loads current input"""     

        with open('Income_Dbase', 'a+') as DB:
            DB.seek(0)
            for line in DB:
                info = line.split()
                if len(info) == 0:
                    continue

                if str(User_Id) == decode_string(info[0]):
                    return info    
                   
            DB.write(f"{decode_string(str(User_Id))} ")
            DB.write(decode_string('0.0 ') * 2)
            DB.write('\n')
            DB.close()
            self.input_loader()

    # creates an object type addFinances
    def addFinance(self):
        self.close()
        global Interactive_layout 
        Interactive_layout.addWidget(Financial_box())

#-------------------------housing window--------------------------
class add_housing(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 600, 350, 350)
        self.setWindowTitle('Add Housing expenses')
        
        # Creating the file
        self.input_loader()

        #loading saved info
        Housing_info = self.input_loader()
        
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
        self.payment_line.setText(decode_string(Housing_info[1]))
        self.payment_line.setObjectName('payment')
        self.payment_line.move(200, 50)

        # property insurance label
        self.insurance_label = QtWidgets.QLabel(self)
        self.insurance_label.move(20, 80)
        self.insurance_label.setText('Property Insurance:')
        
        # property insurance line edit
        self.insurance_line = QtWidgets.QLineEdit(self)
        self.insurance_line.setObjectName('insurance')
        self.insurance_line.setText(decode_string(Housing_info[2]))
        self.insurance_line.move(200, 80)

        # electric bill label
        self.electric_label = QtWidgets.QLabel(self)
        self.electric_label.move(20, 110)
        self.electric_label.setText('Electric Bill:')
        
        # electric bill line edit
        self.electric_line = QtWidgets.QLineEdit(self)
        self.electric_line.setObjectName('electric')
        self.electric_line.setText(decode_string(Housing_info[3]))
        self.electric_line.move(200, 110)

         # Internet bill label
        self.Internet_label = QtWidgets.QLabel(self)
        self.Internet_label.move(20, 140)
        self.Internet_label.setText('Internet Bill:')
        
        # Internet bill line edit
        self.Internet_line = QtWidgets.QLineEdit(self)
        self.Internet_line.setObjectName('Internet')
        self.Internet_line.setText(decode_string(Housing_info[4]))
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
        self.taxes_line.setText(decode_string(Housing_info[5]))
        self.taxes_line.move(200, 200)

        # HOA label
        self.HOA_label = QtWidgets.QLabel(self)
        self.HOA_label.move(20, 230)
        self.HOA_label.setText('HOA dues:')
        
        # HOA line edit
        self.HOA_line = QtWidgets.QLineEdit(self)
        self.HOA_line.setObjectName('HOA')
        self.HOA_line.setText(decode_string(Housing_info[6]))
        self.HOA_line.move(200, 230)

        # gas bill label
        self.gas_label = QtWidgets.QLabel(self)
        self.gas_label.move(20, 260)
        self.gas_label.setText('Gas bill:')
        
        # gas bill line edit
        self.gas_line = QtWidgets.QLineEdit(self)
        self.gas_line.setObjectName('Gas')
        self.gas_line.setText(decode_string(Housing_info[7]))
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
            total = float(self.payment_line.text().strip()) + float(self.insurance_line.text().strip())
            total += float(self.electric_line.text().strip()) + float(self.Internet_line.text().strip())
            total += float(self.taxes_line.text().strip()) + float(self.HOA_line.text().strip())
            total += float(self.gas_line.text().strip())
        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Enter numbers only ')
            return
        
        if Monthly_housing_expenses != total:
            Monthly_housing_expenses = total

        #saving the information
        with open('Housing_Dbase', 'a+') as DB:
            DB.seek(0)
            whole_text = DB.readlines()
            DB.close()
        with open('Housing_Dbase', 'w') as DB:    
            for line in whole_text:
                if str(User_Id) == decode_string(line.split()[0]):
                    DB.write(f"{decode_string(str(User_Id))} {decode_string(self.payment_line.text().strip())} ") 
                    DB.write(f"{decode_string(self.insurance_line.text().strip())} {decode_string(self.electric_line.text().strip())} ") 
                    DB.write(f"{decode_string(self.Internet_line.text().strip())} {decode_string(self.taxes_line.text().strip())} ") 
                    DB.write(f"{decode_string(self.HOA_line.text().strip())} {decode_string(self.gas_line.text().strip())} \n")   
                    continue
                DB.write(line)
            DB.close() 

        #closing the window   
        self.close()
        info_Saver(Username, Password)
        global Interactive_layout 
        Interactive_layout.addWidget(Financial_box())

    # This function load/creates housing info 
    def input_loader(self):
        """This function loads current input"""     

        with open('Housing_Dbase', 'a+') as DB:
            DB.seek(0)
            for line in DB:
                info = line.split()
                if len(info) == 0:
                    continue

                if str(User_Id) == decode_string(info[0]):
                    return info    
                   
            DB.write(f"{decode_string(str(User_Id))} ")
            DB.write(decode_string('0.0 ') * 7)
            DB.write('\n')
            DB.close()
            self.input_loader()

     # creates an object type addFinances to closes current window without changes
    def addFinance(self):
        self.close()
        global Interactive_layout 
        Interactive_layout.addWidget(Financial_box())

#-------------------------transportation window--------------------------
class add_transportation(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 600, 450, 290)
        self.setWindowTitle('Add Transportation expenses')
        
        # Creating the file
        self.input_loader()

        #loading saved info
        Transportation_info = self.input_loader()
        
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
        self.payment_line.setText(decode_string(Transportation_info[1]))
        self.payment_line.setObjectName('payment')
        self.payment_line.move(200, 50)

        # car insurance label
        self.insurance_label = QtWidgets.QLabel(self)
        self.insurance_label.move(20, 80)
        self.insurance_label.setText('Monthly Car Insurance:')
        
        # car insurance line edit
        self.insurance_line = QtWidgets.QLineEdit(self)
        self.insurance_line.setObjectName('insurance')
        self.insurance_line.setText(decode_string(Transportation_info[2]))
        self.insurance_line.move(200, 80)   

        # mileage label
        self.mileage_label = QtWidgets.QLabel(self)
        self.mileage_label.move(20, 110)
        self.mileage_label.setText('Average Mileage per Month:')
        
        # mileage line edit
        self.mileage_line = QtWidgets.QLineEdit(self)
        self.mileage_line.setObjectName('mileage')
        self.mileage_line.setText(decode_string(Transportation_info[3]))
        self.mileage_line.move(200, 110)

        # text was too long
        text = 'The total monthly cost includes gas and maintenace cost base on national average'
        text2 = 'Accurate numbers depend of several factors like year model and type of engine ect.'

        fuel_cost = str(round(float(decode_string(Transportation_info[3])) * 0.0955, 2))
        maintenance_cost = str(round(float(decode_string(Transportation_info[3])) * 0.09, 2))

        # description 1 label 
        self.hours_label = QtWidgets.QLabel(self)
        self.hours_label.move(40, 140)
        self.hours_label.setText(text)

        # description 2 label 
        self.hours_label = QtWidgets.QLabel(self)
        self.hours_label.move(40, 160)
        self.hours_label.setText(text2)

        # car payment label
        self.payment_label = QtWidgets.QLabel(self)
        self.payment_label.move(20, 190)
        self.payment_label.setText(f'Extimated Monthly Fuel Cost: {fuel_cost}')

        # car payment label
        self.payment_label = QtWidgets.QLabel(self)
        self.payment_label.move(20, 220)
        self.payment_label.setText(f'Extimated Monthly Maintenance cost: {maintenance_cost}')

        # accept button
        self.accept = QtWidgets.QPushButton(self)
        self.accept.setText('accept')
        self.accept.move(40, 250)
        self.accept.clicked.connect(self.updatingTransportation)

        # cancel button
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setText('Exit')
        self.cancel.move(135, 250)
        self.cancel.clicked.connect(self.addFinance)
        
        self.show()

    # this function saves the information and return to the dashboard    
    def updatingTransportation(self):
        """This function calculates updates the total transportation expenses"""
        
        global Monthly_transportation_expenses
        
        try:
            total = float(self.payment_line.text().strip()) + float(self.insurance_line.text().strip())
            total += float(self.mileage_line.text().strip()) * 0.0955 + float(self.mileage_line.text().strip()) * 0.09 
            
        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Enter numbers only ')
            return
        
        if total != Monthly_transportation_expenses:
            Monthly_transportation_expenses = total

        with open('Transportation_Dbase', 'a+') as DB:
            DB.seek(0)
            whole_text = DB.readlines()
            DB.close()
        with open('Transportation_Dbase', 'w') as DB:    
            for line in whole_text:
                if str(User_Id) == decode_string(line.split()[0]):
                    DB.write(f"{decode_string(str(User_Id))} {decode_string(self.payment_line.text().strip())} ") 
                    DB.write(f"{decode_string(self.insurance_line.text().strip())} {decode_string(self.mileage_line.text().strip())} \n")   
                    continue
                DB.write(line)
            DB.close()    
        
        self.close()
        info_Saver(Username, Password)
        global Interactive_layout 
        Interactive_layout.addWidget(Financial_box())
    
    # This function load/creates transportation info 
    def input_loader(self):
        """This function loads current input"""     

        with open('Transportation_Dbase', 'a+') as DB:
            DB.seek(0)
            for line in DB:
                info = line.split()
                if len(info) == 0:
                    continue

                if str(User_Id) == decode_string(info[0]):
                    return info    
                   
            DB.write(f"{decode_string(str(User_Id))} ")
            DB.write(decode_string('0.0 ') * 3)
            DB.write('\n')
            DB.close()
            self.input_loader()

     # creates an object type addFinances to closes current window without changes
    def addFinance(self):
        self.close()
        global Interactive_layout 
        Interactive_layout.addWidget(Financial_box())

#-------------------------dependents window--------------------------
class add_dependents(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 600, 460, 140)
        self.setWindowTitle('Add dependents')
        
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
        
        if self.dependents_line.text() == '' and dependent_list[0] == 'none':
            dependent_list = ['none']
        elif self.dependents_line.text() == '':
            self.close()
            global Interactive_layout
            Interactive_layout.addWidget(Financial_box())
            return
        else:        
            try:
                text = self.dependents_line.text().strip().replace(',', ' ')
                total = list(text.split())
    
            except:
                QtWidgets.QMessageBox.critical(self, 'Try Again', 'Please follow the instructions')
                return
        
            if total != dependent_list:
                dependent_list = total
        
        #updating the income with the new dependents list
        global Monthly_Income 
        Monthly_Income = 0
        if self.income_loader != None:
            Monthly_Income = income(float(decode_string(self.income_loader()[1])), float(decode_string(self.income_loader()[2])))

        # Returning to addFinances and updating global variables
        self.income_loader()
        self.close()
        info_Saver(Username, Password)
        
        Interactive_layout.addWidget(Financial_box())

     # Return addFinances to closes current window without changes
    def addFinance(self):
        self.close()
        global Interactive_layout
        Interactive_layout.addWidget(Financial_box())

    # This function load/creates income info. CATION!!! manipulation of Income_Dbase
    def income_loader(self):
        """This function loads current input"""     

        with open('Income_Dbase', 'a+') as DB:
            DB.seek(0)
            for line in DB:
                info = line.split()
                if len(info) == 0:
                    continue

                if str(User_Id) == decode_string(info[0]):
                    return info    
                   
            DB.write(f"{decode_string(str(User_Id))} ")
            DB.write(decode_string('0.0 ') * 2)
            DB.write('\n')
            DB.close()
            self.income_loader()

#-------------------------Assets window--------------------------
class add_Assets(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 600, 500, 230)
        self.setWindowTitle('Add Assets')
        
        # Creating the file
        self.input_loader()

        #loading saved info
        Assets_info = self.input_loader()

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
        self.checking_line.setText(decode_string(Assets_info[1]))
        self.checking_line.setObjectName('checking')
        self.checking_line.move(350, 50)

        # saving accounts balance label
        self.saving_label = QtWidgets.QLabel(self)
        self.saving_label.move(20, 80)
        self.saving_label.setText('Total balance on saving accounts:')
        
        # saving accounts balance line edit
        self.saving_line = QtWidgets.QLineEdit(self)
        self.saving_line.setObjectName('savings')
        self.saving_line.setText(decode_string(Assets_info[2]))
        self.saving_line.move(350, 80)

        # saving bonds label
        self.bonds_label = QtWidgets.QLabel(self)
        self.bonds_label.move(20, 110)
        self.bonds_label.setText('Total face value of serie I, serie EE treasure notes or other bonds:')
        
        # saving bonds line edit
        self.bonds_line = QtWidgets.QLineEdit(self)
        self.bonds_line.setObjectName('bonds')
        self.bonds_line.setText(decode_string(Assets_info[3]))
        self.bonds_line.move(350, 110)

         # stocks label
        self.stocks_label = QtWidgets.QLabel(self)
        self.stocks_label.move(20, 140)
        self.stocks_label.setText('Non retirement stocks:')
        
        # stocks line edit
        self.stocks_line = QtWidgets.QLineEdit(self)
        self.stocks_line.setObjectName('stocks')
        self.stocks_line.setText(decode_string(Assets_info[4]))
        self.stocks_line.move(350, 140)

        # cash balance label
        self.cash_label = QtWidgets.QLabel(self)
        self.cash_label.move(20, 170)
        self.cash_label.setText('Total cash:')
        
        # cash line edit
        self.cash_line = QtWidgets.QLineEdit(self)
        self.cash_line.setText(decode_string(Assets_info[5]))
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
            total = float(self.checking_line.text().strip()) + float(self.saving_line.text().strip())
            total += float(self.bonds_line.text().strip()) + float(self.stocks_line.text().strip())
            total += float(self.cash_line.text().strip())
        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Enter numbers only ')
            return
        
        if  Total_assets != total:
            Total_assets = total
        
        #saving the inputs
        with open('Assets_Dbase', 'a+') as DB:
            DB.seek(0)
            whole_text = DB.readlines()
            DB.close()
        with open('Assets_Dbase', 'w') as DB:    
            for line in whole_text:
                if str(User_Id) == decode_string(line.split()[0]):
                    DB.write(f"{decode_string(str(User_Id))} {decode_string(self.checking_line.text().strip())} ") 
                    DB.write(f"{decode_string(self.saving_line.text().strip())} {decode_string(self.bonds_line.text().strip())} ")
                    DB.write(f"{decode_string(self.stocks_line.text().strip())} {decode_string(self.cash_line.text().strip())} \n")   
                    continue
                DB.write(line)
            DB.close()    
        
        # closing window and returning, updating global variables to add Finances
        self.close()
        info_Saver(Username, Password)
        global Interactive_layout
        Interactive_layout.addWidget(Financial_box())
    
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
            DB.write(decode_string('0.0 ') * 5)
            DB.write('\n')
            DB.close()
            self.input_loader()

     # Open addFinances and closes current window without changes
    def addFinance(self):
        self.close()
        global Interactive_layout
        Interactive_layout.addWidget(Financial_box())
    
    #-------------------------Debt window--------------------------
class add_Unsecured_Debts(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 600, 530, 350)
        self.setWindowTitle('Adding Unsecured Debts')
        
        # Creating the file
        self.input_loader()
       
        #loading saved info
        Debts_info = self.input_loader()
        
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

        # Monthly Payment  label 
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(420, 50)
        self.Term_label.setText('Monthly Payment')

        # Credit card1 label
        self.card1_label = QtWidgets.QLabel(self)
        self.card1_label.move(20, 80)
        self.card1_label.setText('Credit Card balance 1:')
        
        # Credit card11 line edit
        self.card11_line = QtWidgets.QLineEdit(self)
        self.card11_line.setText(decode_string(Debts_info[1]))
        self.card11_line.setFixedWidth(75)
        self.card11_line.setObjectName('Balance')
        self.card11_line.move(150, 80)

        # Credit card12 line edit
        self.card12_line = QtWidgets.QLineEdit(self)
        self.card12_line.setText(decode_string(Debts_info[2]))
        self.card12_line.setFixedWidth(50)
        self.card12_line.setObjectName('APR')
        self.card12_line.move(250, 80)

        # Loan Term 1 label 
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(330, 80)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText('N/A')

        # Monthly Payment label 1
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(450, 80)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText(f'{decode_string(Debts_info[21])}')

        # Credit card2 label
        self.card2_label = QtWidgets.QLabel(self)
        self.card2_label.move(20, 110)
        self.card2_label.setText('Credit Card balance 2:')
        
        # Credit card21 line edit
        self.card21_line = QtWidgets.QLineEdit(self)
        self.card21_line.setText(decode_string(Debts_info[3]))
        self.card21_line.setFixedWidth(75)
        self.card21_line.setObjectName('Balance')
        self.card21_line.move(150, 110)

        # Credit card22 line edit
        self.card22_line = QtWidgets.QLineEdit(self)
        self.card22_line.setText(decode_string(Debts_info[4]))
        self.card22_line.setFixedWidth(50)
        self.card22_line.setObjectName('APR')
        self.card22_line.move(250, 110)

        # Loan Term 2 label 
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(330, 110)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText('N/A')

        # Monthly Payment label 2
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(450, 110)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText(f'{decode_string(Debts_info[22])}')

        # Credit card3 label
        self.card3_label = QtWidgets.QLabel(self)
        self.card3_label.move(20, 140)
        self.card3_label.setText('Credit Card balance 3:')
        
        # Credit card31 line edit
        self.card31_line = QtWidgets.QLineEdit(self)
        self.card31_line.setText(decode_string(Debts_info[5]))
        self.card31_line.setFixedWidth(75)
        self.card31_line.setObjectName('Balance')
        self.card31_line.move(150, 140)

        # Credit card32 line edit
        self.card32_line = QtWidgets.QLineEdit(self)
        self.card32_line.setText(decode_string(Debts_info[6]))
        self.card32_line.setFixedWidth(50)
        self.card32_line.setObjectName('APR')
        self.card32_line.move(250, 140)

        # Loan Term 3 label 
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(330, 140)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText('N/A')

        # Monthly Payment label 3
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(450, 140)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText(f'{decode_string(Debts_info[23])}')

        # Credit card4 label
        self.card4_label = QtWidgets.QLabel(self)
        self.card4_label.move(20, 170)
        self.card4_label.setText('Credit Card balance 4:')
        
        # Credit card41 line edit
        self.card41_line = QtWidgets.QLineEdit(self)
        self.card41_line.setText(decode_string(Debts_info[7]))
        self.card41_line.setFixedWidth(75)
        self.card41_line.setObjectName('Balance')
        self.card41_line.move(150, 170)

        # Credit card42 line edit
        self.card42_line = QtWidgets.QLineEdit(self)
        self.card42_line.setText(decode_string(Debts_info[8]))
        self.card42_line.setFixedWidth(50)
        self.card42_line.setObjectName('APR')
        self.card42_line.move(250, 170)

        # Loan Term 4 label 
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(330, 170)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText('N/A')

        # Monthly Payment label 4
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(450, 170)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText(f'{decode_string(Debts_info[24])}')

        # Personal loan1 label
        self.loan1_label = QtWidgets.QLabel(self)
        self.loan1_label.move(20, 200)
        self.loan1_label.setText('Personal Loan 1:')
        
        # Personal loan11 line edit
        self.loan11_line = QtWidgets.QLineEdit(self)
        self.loan11_line.setText(decode_string(Debts_info[9]))
        self.loan11_line.setFixedWidth(75)
        self.loan11_line.setObjectName('Balance')
        self.loan11_line.move(150, 200)

        # Personal loan12 line edit
        self.loan12_line = QtWidgets.QLineEdit(self)
        self.loan12_line.setText(decode_string(Debts_info[10]))
        self.loan12_line.setFixedWidth(50)
        self.loan12_line.setObjectName('APR')
        self.loan12_line.move(250, 200)

        # Personal loan13 line edit
        self.loan13_line = QtWidgets.QLineEdit(self)
        self.loan13_line.setText(decode_string(Debts_info[11]))
        self.loan13_line.setFixedWidth(50)
        self.loan13_line.setObjectName('loan term')
        self.loan13_line.move(330, 200)

        # Monthly Payment label 5
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(450, 200)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText(f'{decode_string(Debts_info[25])}')

        # Personal loan2 label
        self.loan1_label = QtWidgets.QLabel(self)
        self.loan1_label.move(20, 230)
        self.loan1_label.setText('Personal Loan 2:')
        
        # Personal loan21 line edit
        self.loan21_line = QtWidgets.QLineEdit(self)
        self.loan21_line.setText(decode_string(Debts_info[12]))
        self.loan21_line.setFixedWidth(75)
        self.loan21_line.setObjectName('Balance')
        self.loan21_line.move(150, 230)

        # Personal loan22 line edit
        self.loan22_line = QtWidgets.QLineEdit(self)
        self.loan22_line.setText(decode_string(Debts_info[13]))
        self.loan22_line.setFixedWidth(50)
        self.loan22_line.setObjectName('APR')
        self.loan22_line.move(250, 230)

        # Personal loan23 line edit
        self.loan23_line = QtWidgets.QLineEdit(self)
        self.loan23_line.setText(decode_string(Debts_info[14]))
        self.loan23_line.setFixedWidth(50)
        self.loan23_line.setObjectName('loan term')
        self.loan23_line.move(330, 230)

        # Monthly Payment label 6
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(450, 230)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText(f'{decode_string(Debts_info[26])}')

         # Personal loan3 label
        self.loan1_label = QtWidgets.QLabel(self)
        self.loan1_label.move(20, 260)
        self.loan1_label.setText('Personal Loan 3:')
        
        # Personal loan31 line edit
        self.loan31_line = QtWidgets.QLineEdit(self)
        self.loan31_line.setText(decode_string(Debts_info[15]))
        self.loan31_line.setFixedWidth(75)
        self.loan31_line.setObjectName('Balance')
        self.loan31_line.move(150, 260)

        # Personal loan32 line edit
        self.loan32_line = QtWidgets.QLineEdit(self)
        self.loan32_line.setText(decode_string(Debts_info[16]))
        self.loan32_line.setFixedWidth(50)
        self.loan32_line.setObjectName('APR')
        self.loan32_line.move(250, 260)

        # Personal loan33 line edit
        self.loan33_line = QtWidgets.QLineEdit(self)
        self.loan33_line.setText(decode_string(Debts_info[17]))
        self.loan33_line.setFixedWidth(50)
        self.loan33_line.setObjectName('loan term')
        self.loan33_line.move(330, 260)

        # Monthly Payment label 7
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(450, 260)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText(f'{decode_string(Debts_info[27])}')

        # Personal loan4 label
        self.loan4_label = QtWidgets.QLabel(self)
        self.loan4_label.move(20, 290)
        self.loan4_label.setText('Personal Loan 4:')
        
        # Personal loan41 line edit
        self.loan41_line = QtWidgets.QLineEdit(self)
        self.loan41_line.setText(decode_string(Debts_info[18]))
        self.loan41_line.setFixedWidth(75)
        self.loan41_line.setObjectName('Balance')
        self.loan41_line.move(150, 290)

        # Personal loan42 line edit
        self.loan42_line = QtWidgets.QLineEdit(self)
        self.loan42_line.setText(decode_string(Debts_info[19]))
        self.loan42_line.setFixedWidth(50)
        self.loan42_line.setObjectName('APR')
        self.loan42_line.move(250, 290)

        # Personal loan43 line edit
        self.loan43_line = QtWidgets.QLineEdit(self)
        self.loan43_line.setText(decode_string(Debts_info[20]))
        self.loan43_line.setFixedWidth(50)
        self.loan43_line.setObjectName('loan term')
        self.loan43_line.move(330, 290)

        # Monthly Payment label 8
        self.Term_label = QtWidgets.QLabel(self)
        self.Term_label.move(450, 290)
        self.Term_label.setFixedWidth(50)
        self.Term_label.setText(f'{decode_string(Debts_info[28])}')

         # accept button
        self.accept = QtWidgets.QPushButton(self)
        self.accept.setText('accept')
        self.accept.move(165, 320)
        self.accept.clicked.connect(self.updatingDebt)

        # cancel button
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setText('Exit')
        self.cancel.move(330, 320)
        self.cancel.clicked.connect(self.addFinance)
        
        self.show()

    # this function saves the information and return to the dashboard    
    def updatingDebt(self):
        """This function calculates and updates the total debts"""

        if float(self.loan11_line.text().strip()) != 0 and float(self.loan13_line.text().strip()) == 0:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'If a loan have a balance cannot have 0 as loan term ')
            return
        if float(self.loan21_line.text().strip()) != 0 and float(self.loan23_line.text().strip()) == 0:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'If a loan have a balance cannot have 0 as loan term ')
            return
        if float(self.loan31_line.text().strip()) != 0 and float(self.loan33_line.text().strip()) == 0:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'If a loan have a balance cannot have 0 as loan term ')
            return
        if float(self.loan41_line.text().strip()) != 0 and float(self.loan43_line.text().strip()) == 0:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'If a loan have a balance cannot have 0 as loan term ')
            return    
        
        global Monthly_Debt_expenses
        try:          
            balance1 = mortgage(float(self.card11_line.text().strip()), float(self.card12_line.text().strip()), 3)
            balance2 = mortgage(float(self.card21_line.text().strip()), float(self.card22_line.text().strip()), 3)
            balance3 = mortgage(float(self.card31_line.text().strip()), float(self.card32_line.text().strip()), 3)
            balance4 = mortgage(float(self.card41_line.text().strip()), float(self.card42_line.text().strip()), 3)
            balance5 = mortgage(float(self.loan11_line.text().strip()), float(self.loan12_line.text().strip()), round(float(self.loan13_line.text().strip())/12), 2)
            balance6 = mortgage(float(self.loan21_line.text().strip()), float(self.loan22_line.text().strip()), round(float(self.loan23_line.text().strip())/12), 2)
            balance7 = mortgage(float(self.loan31_line.text().strip()), float(self.loan32_line.text().strip()), round(float(self.loan33_line.text().strip())/12), 2)
            balance8 = mortgage(float(self.loan41_line.text().strip()), float(self.loan42_line.text().strip()), round(float(self.loan43_line.text().strip())/12), 2)
            
            total = balance1 + balance2 + balance3 + balance4 + balance5 + balance5 + balance6 + balance7 + balance8
        except:
            QtWidgets.QMessageBox.critical(self, 'Try Again', 'Enter numbers only ')
            return
        
        if Monthly_Debt_expenses != total:
            Monthly_Debt_expenses = total
        
        # Saving the inputs
        with open('Debts_Dbase', 'a+') as DB:
            DB.seek(0)
            whole_text = DB.readlines()
            DB.close()
        with open('Debts_Dbase', 'w') as DB:    
            for line in whole_text:
                if str(User_Id) == decode_string(line.split()[0]):
                    DB.write(f"{decode_string(str(User_Id))} {decode_string(self.card11_line.text())} ") 
                    DB.write(f"{decode_string(self.card12_line.text().strip())} {decode_string(self.card21_line.text().strip())} ")
                    DB.write(f"{decode_string(self.card22_line.text().strip())} {decode_string(self.card31_line.text().strip())} ")
                    DB.write(f"{decode_string(self.card32_line.text().strip())} {decode_string(self.card41_line.text().strip())} ")
                    DB.write(f"{decode_string(self.card42_line.text().strip())} {decode_string(self.loan11_line.text().strip())} ")
                    DB.write(f"{decode_string(self.loan12_line.text().strip())} {decode_string(self.loan13_line.text().strip())} ")
                    DB.write(f"{decode_string(self.loan21_line.text().strip())} {decode_string(self.loan22_line.text().strip())} ")
                    DB.write(f"{decode_string(self.loan23_line.text().strip())} {decode_string(self.loan31_line.text().strip())} ")
                    DB.write(f"{decode_string(self.loan32_line.text().strip())} {decode_string(self.loan33_line.text().strip())} ")
                    DB.write(f"{decode_string(self.loan41_line.text().strip())} {decode_string(self.loan42_line.text().strip())} ")
                    DB.write(f"{decode_string(self.loan43_line.text().strip())} {decode_string(str(balance1))} ") 
                    DB.write(f"{decode_string(str(balance2))} {decode_string(str(balance3))} {decode_string(str(balance4))} ") 
                    DB.write(f"{decode_string(str(balance5))} {decode_string(str(balance6))} {decode_string(str(balance7))} ")  
                    DB.write(f"{decode_string(str(balance8))}\n")    
                    continue
                DB.write(line)
            DB.close()    
        self.close()
        
        #closing the window and updating global variables
        self.close()
        info_Saver(Username, Password)
        global Interactive_layout 
        Interactive_layout.addWidget(Financial_box())
    
    # This function load/creates debts info 
    def input_loader(self):
        """This function loads current input"""     

        with open('Debts_Dbase', 'a+') as DB:
            DB.seek(0)
            for line in DB:
                info = line.split()
                if len(info) == 0:
                    continue

                if str(User_Id) == decode_string(info[0]):
                    return info    
                   
            DB.write(f"{decode_string(str(User_Id))} ")
            DB.write(decode_string('0.0 ') * 28)
            DB.write('\n')
            DB.close()
            self.input_loader()

     # Open addFinances to closes current window without changes
    def addFinance(self):
        self.close()
        global Interactive_layout 
        Interactive_layout.addWidget(Financial_box())

#--------graph window---------------------------------------
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

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
        y_income = y_income * 0.65  # 35% withhold
    else:
        y_income = y_income * 0.63  # 37% withhold

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

# this function returns the monthly payment of a loan if interest rate, balance and loan term are known
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
        Monthly += (Maintenance + Insurance)/12 
    
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
    Monthly_Income = round(float(decode_string(info[2])), 2)

    global Total_assets
    Total_assets = round(float(decode_string(info[3])), 2)

    global Monthly_housing_expenses
    Monthly_housing_expenses = round(float(decode_string(info[5])), 2)

    global Monthly_transportation_expenses 
    Monthly_transportation_expenses = round(float(decode_string(info[4])), 2)

    global Monthly_Debt_expenses
    Monthly_Debt_expenses = round(float(decode_string(info[6])), 2)

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
