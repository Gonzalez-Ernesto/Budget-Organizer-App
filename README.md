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

This project was meant to be the capstone project of the Python Developer program at NcLab. I could proudly say that the NClab program gave me all the tools to implement the functionality of this app, and avoiding an Object Oriented Design was a priority to prove that although the introductory  Python Developer Course does not dive into OOP and other topics like resources and data structure, still offer not only the foundation to learn those advance concepts quickly but a set of tools to be successful in the industry starting at entry-level positions.
	Implementing the interface was the most challenging part of this project. Not using the PYQT5 editor was intentional for the same learning purpose described early; however, this approach and avoiding OOP design were costly in several ways. The first and most noticeable consequence was an interface that needed to be updated and attractive. At the implementation level, the most significant consequence was that the code grew exponentially to the order of thousands of lines, making it extremely hard for only one developer to debug and maintain the code.
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

![create account button](https://user-images.githubusercontent.com/105956722/233922163-ca73d6ce-5e02-4371-a9dd-2b5b15cede30.PNG)

![create account button](https://user-images.githubusercontent.com/105956722/233922462-af16245b-3f65-4ddd-8af0-d20ab5635886.PNG)
