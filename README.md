# PA1493 Software Development Project (Distance) HT26

---

## Project Description

**Project Name:** *Lab Equipment Knowledge Hub (LEKH)*

**Customer Name:** *Zeth Danielsson*

**Student Full Name:** *Rebaz Mohammad Ahmad*

### Project Aim and Objectives

* Project is about learning to work in an agile environment
* Plan a software project with the intention of following the
  planned sprints.
* Learn to prioritize software work.
* Learn to fullfill requirements from customer. 

### User Personas

| Name | Characteristics | Needs and Expectations | How will they use the system? |
|---|---|---|---|
| *John Doe* | *Age: 20, background: student, technical skill level 6/10, etc.* | *Need to quickly find avalible equitment for projects without unnecessary paperwork, expects clear instruction about equipment condition* | *Search for equipment,report faults, check availability* |




| Name | Characteristics | Needs and Expectations | How will they use the system? |
|---|---|---|---|
| *Alice* | *Age: 35, background: caretaker, technical skill level 5/10, etc.* | *Needs an overview of borrowed equipment, stocks and overdue items * | *Register equipment,update status, approve or reject borrowed items * |



### Software Requirements

**Functional Requirements**
- *User registration and login, User can register using email, username and password*

- *Diffrent user permissions, The system supports student,admin and caretaker roles*

- *Equipment registration, caretaker registers name, category, description, location and status.*

- *Equipment handling and categories, caretaker will create,read,update and delete the equipments and categories.*

- *Booking equipment, students can book an equipment in a form that will be displayed to caretaker.*

- *Equipment viewing, caretaker and students will be able to view detalied page of each equipment.*

- *Equipment search and filtering, students must be able to search by name and filter by category*

- *Equipment fault reporting, students can report faults on diffrent equipment, caretaker will be able to view the reported fault.*

- *Uploading Equipment images, caretakers can upload images and pdf files.*

**Non-Functional Requirements**
- *Security, system have the right auth permission for the right roles: "students and caretakers".*

- *Data validation, system should validate inputed data when using login, register account and crud operations*

- *Usability, the system should have a consistent interface.*

- *The system should support diffrent formats like tablets and mobile screens.*

- *Images should be optimized for performance and loading times.*


---

## Backlog



### 1. GitHub Issues (the content)

Link to Github issues for this project can be found here:
[Github Issues for this project](https://github.com/dipt-pa1493-ht26/pa1493-reah23-lekh-zda/issues)



Link to the Agile backlog for this project:
[Github Agile board](https://github.com/orgs/dipt-pa1493-ht26/projects/10/views/1)



---


## User manual

### Installing
- Python 3.14.2
- Git
- Visual studio code

  #### 1. Clone the repository
  * git clone https://github.com/dipt-pa1493-ht26/pa1493-reah23-lekh-zda
  * cd repository folder

  #### 2. Create and activate virtual enviorment.
  * python -m venv .venv
  * Run .venv\Scripts\Activate to activate the virtual enviorment.
  * To deactivate, run deactivate to close the terminal for the virtual enviorment
 

  #### 3. Install dependencies
  * pip install -r requirements.txt

  
  #### 4 Enviorment variables
  Project requires Django enviorment variables. Create an env.py file in the same folder as manage.py and add the following:
  
  1. SECRET_KEY = your-secret-key

  2. 


### Running the app

  * Apply database migration first by running "python manage.py migrate in the root folder (same folder as manage.py)"
  * Create admin account by running "python manage.py createsuperuser"
  * To start the application run: "python manage.py runserver" in the root folder


### Used Technology

1. Django==6.1.1 as web framework
2. django-allauth==65.19.3 for auth handling
3. 