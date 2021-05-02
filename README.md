# Voice-Based-Train-Enquiry-System
Voice Based Enquiry System is the enquiry system which operates based on the voice input given by the user. There is no communication which is understood more appropriately than voice. This system too uses the voice commands and gives the required information in the form of voice. This project is developed using Python Programming language. This uses SQL Lite server for storing the information to be provided to the user. This uses mic to detect the voice from the user and uses the speech control to deliver the output in the form of text. Google speech to text converter would help convert the speech into text. 


Building a voice based train enquiry system using Google speech recognition, mysqlite, python tkinter utility.

Overview

    Import Key python packages 
    Prepare a database of railway data(sample train.db provided)
    Executing first time would need to create a user profile for database administration(not required if using train.db)
    

Prerequisites

    Basic programming experience in python
    Basic understanding of Database CRUD properties 
    Basic working understanding of tkinter UI functions


Execution Steps

    Getting this project running in dev environment is pretty simple.
    
    1.Execute the FRONT.py module via any IDE
    2.Administration tab provided would lead to database monitoring window wherein user can modify record entries.
    3."Give command in Speech" tab would activate speech recognition module wherein you can mention your enquiry regarding any train present in the database.
    4.The speech should include keywords like "from", "to", <source_name> or/and <destination_name",<date>

