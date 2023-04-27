# Project Title: Budget-Organizer-App

This application is intended to be a tool for managing individual finances. By entering personal but not compromising financial information, this app allows the user to get the monthly financial picture and generate some insights about the impact of likely economic changes.

Motivation: The main idea behind this project was to offer a solution to those who struggle the most with their finances, specifically hourly workers who do not have a fixed income due to the nature of their job and can not rely on a fixed monthly amount and instead are forced to take it week by week. 
Although the financial language used in this app could seem complicated, it is like the one used by banks, lenders, and financial institutions in general to overwhelm their targeted audience, and it was considered that rather than avoid it, it is better to familiarize the user with it.
    The implementation of all the functionalities was to address the learning objectives of the Python Developer Program from NCLab (highly recommended for those looking to learn Python in a fun way)

## Acknowledgements

 - [NCLab support team](https://nclab.com/)
 - [Hudson Rains (coach at NCLab)](https://www.linkedin.com/in/hudson-rains-1ba5791bb/)
 - [Alan D Moore Codes course: Mastering PyQT5](https://www.alandmoore.com)
 - [Readme.so](https://readme.so/editor)


## Authors

- [Ernesto Gonzalez (trainee at NCLab)](https://github.com/Gonzalez-Ernesto/)

## Lessons Learned

This project was meant to be the capstone project of the Python Developer program at NcLab. I could proudly say that the NClab program gave me all the tools to implement the functionality of this app, and avoiding an Object Oriented Design was a priority to prove that although the introductory  Python Developer Course does not dive into OOP and other topics like resources management and data structure, it offers not only the foundation to learn those advance concepts quickly but a set of tools to be successful in the industry starting at entry-level positions.
	Implementing the interface was the most challenging part of this project. Not using the PYQT5 editor was intentional for the same learning purpose described early; however, this approach and avoiding OOP design were costly in several ways. The first and most noticeable consequence was an interface that needs to be updated to make it more friendly and attractive. At the implementation level, the most significant consequence was that the code grew exponentially to the order of thousands of lines, making it extremely hard for only one developer to debug and maintain.
    Lastly, since I did not have previous experience with PYQT5, the initial design had to be modified more than once, reaching improvisation more than once.	

## How to Use It

When running the App, the first widget shows three buttons, as shown in the image below.

-Use button 1: to create a new account (new user)

-Use button 2: if you already have created a profile and want to access your information

-Use button 3 to exit the App.

![create account button](https://user-images.githubusercontent.com/105956722/233906448-122576d4-1755-4c30-aa19-e265fd60fe6d.PNG)


If the Create Account button is clicked on the main widget, the widget shown below will appear. On the field marked as one, the user should introduce the desired username following the instructions shown on the app. To create a password, the user should submit the desired password in fields 2 and 3. Not following the instructions will prevent the user from creating the account successfully.


![create account button](https://user-images.githubusercontent.com/105956722/233907785-10e21c9a-9e24-4877-b7ef-b82792066e57.PNG)


The widget below will appear if the login button clicks on the main widget or an account was created successfully. To access the App's features, the user must introduce the username and the password used when the account was created and click the accept button.


![create account button](https://user-images.githubusercontent.com/105956722/233909067-1d1fa996-c11c-46c6-a348-5696aa45a9b4.PNG)


The widget shown below is where the heavy lifting of the App is done and the hardest to comprehend. The widget is divided into five sections for easy comprehension.

-Section 1 is where the user inputs the financial information

-Section 2 allows the user to visualize the current financial situation

-Section 3 allows the user to assess the impact of upcoming financial events and offers customized feedback according to the specific circumstances considered.

-Section 4 is where the user can find the meaning of complex financial terms used in the App.

-Section 5 is for either login out of the user account or exiting the App.

![create account button](https://user-images.githubusercontent.com/105956722/233910684-858b44f0-90a7-4dc9-ae76-d3de306cf605.PNG)

SECTION 1

This section is where the User can input the financial situation and access this information anytime; This is the first step to organizing one's finances.

Button 1 allows the User to introduce assets. Although this App falls short when considering, possible assets is a good starting point. Once the Assets button is clicked, the widget shown below will appear. Competing for the fields is a simple process that could be completed with the help of the vocabulary from section 4. the User can introduce the information on any field, and as long the accept button is clicked, the information will be saved even though not all fields are completed.

![create account button](https://user-images.githubusercontent.com/105956722/233915391-945cdee1-b8e7-41cf-a89a-3068cae86817.PNG)

![create account button](https://user-images.githubusercontent.com/105956722/233914986-4b091fa9-6a64-46d3-96b9-5e6eae6440d1.PNG)

Button 2 allows the user to introduce information related to transportation. However, currently the app only support information related to owning a car and ignores other features like public transportation or any other kind like Uber or Lyft. These would be good features to add as a contribution.

![create account button](https://user-images.githubusercontent.com/105956722/233916070-0332c41e-0838-4f72-98e6-717aec2e46fe.PNG)

As with the other buttons of section 1 filling up the information should be easy. One important feature addedd to the widged transportation is the marked text which shows the calculated monthly maintenace and gas cost. however these numbers were calculated using national dta which is extremely unaccurate considering the gas price gap among different states.Another drawnback is that this information is not updated in real timeit is necessary to press the accept button.

![create account button](https://user-images.githubusercontent.com/105956722/233916235-fb8b021e-77bd-4685-b766-19868ba0acfe.PNG)

Button 3 allows the user to introduce dependants for financial purpose. This step can be completed by following the instruction from the widget. designing this feature in a more convinient way could be a nice contribution.

![create account button](https://user-images.githubusercontent.com/105956722/233917318-6480afa6-b5ef-44c0-b01a-4cf244f5ace7.PNG)

![create account button](https://user-images.githubusercontent.com/105956722/233918508-58631142-b1f2-4ea0-8491-1ecad2f03406.PNG)

Button 4 allows us to introduce information related to housing. Currently, the app support renters and homeowners. However still lacks other features like considering other housing expenses like alarm systems, pool maintenance, etc. Completing these fields should be possible without complications, and any problematic term should be in the vocabulary.

![create account button](https://user-images.githubusercontent.com/105956722/233918934-6b4d4f64-e9ef-4735-a513-88c440c6cc9c.PNG)

![create account button](https://user-images.githubusercontent.com/105956722/233919741-37bf699a-009e-4192-a88e-44de98617571.PNG)

Button 5 allows the introduction of information related to income. Currently, only hourly income is supported. Expanding the possibilities for the user would be appreciated as a contribution.

![create account button](https://user-images.githubusercontent.com/105956722/233920118-4237c41e-ba6f-48bc-b080-f6acd08ad014.PNG)

![create account button](https://user-images.githubusercontent.com/105956722/233920064-f3897a4a-ef1f-4623-a5bc-71d704bf855e.PNG)

Button 6 allows the introduction of unsecured debts. If the meaning of this is confusing, clarification can be found in the vocabulary. The widget that follows when the button is clicked allows the introduction of information related to credit cards and loans. However, it falls short in allowing the user to name the debt or to introduce more than eight in total. Improving these is a good idea for contribution.

![create account button](https://user-images.githubusercontent.com/105956722/233920880-c47463d4-4df5-4c2c-9184-861202d727d3.PNG)

![create account button](https://user-images.githubusercontent.com/105956722/233920976-4fa0fd8e-cde5-4614-a5be-d022bc04b984.PNG)

SECTION 2
Section 2 only has the "My Financial Picture" button.  

![create account button](https://user-images.githubusercontent.com/105956722/233922163-ca73d6ce-5e02-4371-a9dd-2b5b15cede30.PNG)

When this button is clicked, the widget shown below will appear. 

![create account button](https://user-images.githubusercontent.com/105956722/233922462-af16245b-3f65-4ddd-8af0-d20ab5635886.PNG)

This widget will display all the financial information the user has input. For a better understanding of this widget, it will be divided into three parts. However, it will be explained in one block.

Part 1 summarizes the information the user entered using the six buttons from SECTION 1. These numbers will be confusing at first. To better understand how these numbers are calculated, the button " Explain these Numbers" from Part 3 could be clicked, and a message box will appear about how this is done. It would look like the one shown below.

![create account button](https://user-images.githubusercontent.com/105956722/234183365-3fc4e4dc-c36d-41d2-9961-1eead2b7ffb7.PNG)

If the user wants to see all the information entered at once, this is achieved by clicking the "Detailed Report" button from Part Three, and the following message box will appear.

![create account button](https://user-images.githubusercontent.com/105956722/234183745-0feda7a8-ca65-4733-aab1-be41976b3b4e.PNG)

In order to avoid overloading, the user fields where the input is equal to zero are not displayed on the message.

Part 2 shows a linear graph representing hwhere the user's balance will be in six months if the current situation does not change, this is particulary useful for those living day by day and this insight could be a good suggestion to change the current course if the projected balance is not good.

SECTION 3

Things get more interesting in this section since these functionalities offer a good insight into the financial impact of any of these situations. However, to avoid making this section interminably long, only one functionality will be covered in this tutorial since all of them are similar in the way the input is entered and the output is displayed.

![create account button](https://user-images.githubusercontent.com/105956722/234186129-c069ed47-ba2f-40ce-bd52-0ac0d1e224b0.PNG)

If the marked button is clicked the following widget will appear.

![create account button](https://user-images.githubusercontent.com/105956722/234189113-f636f7d4-e50b-40d0-81df-41807c7462f2.PNG)

	In this particular case, the function called is "Buying a New House"( used as the primary residence.) It is important to remember to whom this app is dedicated. It is not suitable for landlords, investors, or people who, by their own merit, have placed themself outside of low-income hourly workers' reality.
    For this tutorial, the user intends to buy a house worth $350,000, and it will finance $300,000 with an APR of 5% for 30 years. The reason why the value is requested has to do with including Primary Mortgage Insurance in the Monthly Payment.
    
  ![create account button](https://user-images.githubusercontent.com/105956722/234189352-3db7586c-efc7-476b-9156-d9af9326bca2.PNG)
  
  The above widget appears after the Accept button is clicked. It shows in the graph how taking this financial step will compare to the current situation for the next six months. Also, this comparison is explained in detail below the chart. This feedback is unique depending on the actual situation and the planned step.
  
  With slight variations, the rest of the buttons in this section will behave similarly.
  
  Section 4 is just the vocabulary for the App and Section 5 is a to log out or exit the app.
  
  ## How to Contribute
  
  If contributing to this project is something that you would like to do, there are numerous ways to improve this app. Several issues were addressed in the section on How to use it, and this could be a good starting point. As far as I know, I found an issue when entering the dependents that made the app crash; however, I have not been able to reproduce it, and it is still unfixed. I have not found any similar issues related to inputs. If anyone with experience with Pyqt5 would like to contribute to improving the interface and the user experience, that would be great.

The project is 100% in Python. Being familiar with the language is necessary; navigating through the code is highly challenging. If a contributor has Object Oriented Programing Knowledge in Python and wants to implement OOD, go ahead. 
In any case, submit a pull request. 
Here are some helpful links to install the necessary environment locally if it is something that you do not have.
These are just the ones I used; the options are numerous.

For installing Visual Studio
https://visualstudio.microsoft.com/vs/community/

for installing Python for different OS
https://pypi.org/project/PyQt5/

for installing PyQt5 for Pyhton
https://pypi.org/project/PyQt5/

For installing Matplotlib
https://pypi.org/project/pandas/

For installing Pandas
https://pypi.org/project/pandas/

    
    


