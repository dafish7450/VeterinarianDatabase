# 🌟 Highlights

- Easily Add/Update Pets
- Easily View Receipts
- Easily View All Past Transactions, by Pet And Clinic
- Easily Track Billing by Pet Owner
- Track Visits Per Veterinarian


# ℹ️ Overview

This website is a faux internal web server for a Veterinarian Service, which tracks and updates several different database tables/relations, including Veterinarians employed, Pets, Pet Owners, Visits, Billing, and even parent companies (those that employ veterinarians). My name is Reece Fish, I am a senior at the University of St. Thomas, and I made this project in my Database Design I (CISC 480) class as the final project of the class. The purpose of this project was not only to showcase everything we had learned to that point, but apply it in a way that would reflect what work would be done in the Data Analytics field. I specifically played a major role in the schema design of the database, as well as bug-fixing the python script that allows the site to function. This website is very simplistic in its design, with buttons that allow you to view and modify each table of the database. This website utilizes flask and sqlalchemy to mesh python and MySQL together to achieve a fully functioning website.


### ✍️ Authors

- Georgia Crane -- Primary Python Coder ([Georgia's Senior Portfolio](https://github.com/cran5518/portfolio))
- Alejandro -- Project Manager, Primary Bug Fixer, Documenter
- Reece Fish -- Primary Schema Designer


## 🚀 Usage

This website allows you to access each of the tables of the database, as well as modify them! Here's some examples of what that would look like:

Here's the Main Website Page: 
![Main Vet Page](https://github.com/dafish7450/SignatureWorkImages/blob/main/Screenshot%202025-12-06%20133244.png "Main Vet Page")


Here's what the Pet page looks like: 
![Pet Table Page](https://github.com/dafish7450/SignatureWorkImages/blob/main/Screenshot%202025-12-06%20133251.png "Pet Table Page")


Here's what the Pet Owner Page before editing looks like: 
![Pet Owner Table Page](https://github.com/dafish7450/SignatureWorkImages/blob/main/Screenshot%202025-12-06%20133410.png "Pet Owner Table Before Page")


Here's what adding a Pet Owner look like: 
![Added Pet Owner](https://github.com/dafish7450/SignatureWorkImages/blob/main/Screenshot%202025-12-06%20133945.png "Pet Owner Add Page")


Here's what the Pet Owner Page looks like, after adding a new Pet Owner: 
![Pet Table Page](https://github.com/dafish7450/SignatureWorkImages/blob/main/Screenshot%202025-12-06%20133954.png "Pet Owner Table After Page")


## ⬇️ Installation

You wil first need to have:
- Access to a Web Browser
- Access to Visual Studio

Then, you will need to copy the contents of this repo to a folder in VS, and in the terminal, run the following:

```bash
pip3 install flask
pip3 install sqlalchemy
python app.py
```
Once this is done, you can access the website on local host at port 5000, or http://127.0.0.1:5000
