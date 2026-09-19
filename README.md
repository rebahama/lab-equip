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


- *Equipment registration, caretaker must be able to register new equipment.*


- *Equipment search and filtering, students must be able to search by name and filter by category*

**Non-Functional Requirements**
- *Security, system have the right auth permission for the right role*
- *Data validation, system should validate inputed data.*

---

## Your Backlog

Your backlog lives in two places, working together:

### 1. GitHub Issues (the content)

Link to Github issues for this project can be found here:
[Github Issues for this project](https://github.com/dipt-pa1493-ht26/pa1493-reah23-lekh-zda/issues)



Link to the Agile backlog for this project:
[Github Agile board](https://github.com/orgs/dipt-pa1493-ht26/projects/10/views/1)


For every user story, feature, and task, create a GitHub Issue with a clear title and description. Use the issue template provided in this repository (see `.github/ISSUE_TEMPLATE/`).

Write them in this order:
1. All **user stories** first (format: *"As [a user], I want [action] so that [goal]"*)
2. Then all **features**
3. Then all **tasks**

### 2. Project Board (the backlog itself)

Add every Issue to a Project board. The board is your backlog, not the issue text.

Your repository does not come with a board already set up — see **[PROJECT_BOARD.md](PROJECT_BOARD.md)** for step-by-step instructions on creating your board and setting up the required fields (Priority, Estimated Effort, Sprint). 

You'll need a working board by the end of Sprint 1, as Status Report 3 requires it.


---

## Development

From Week 38 onward:
- Set up your development environment and start development.
- You're free to organise your code however works best for you — for example, using `src/` and `docs/` folders, or any other structure. There's no required folder layout; 
- At the end of each sprint, your work will be demonstrated to the customer at that sprint's Demo
- Keep this README as the one place that always explains how to install and run your project.


Your repository must remain **Private** for the entire course. This protects your customer's requirements and your own work.

---

## User manual

### Installing
- Python 3.14.2
- Git
- Visual studio code

  #### 1. Clone the repository
  * git clone https://github.com/dipt-pa1493-ht26/* pa1493-reah23-lekh-zda
  * cd repository folder

  #### 2. Create and activate virtual enviorment.
  * python -m venv .venv
  * Run .venv\Scripts\Activate to activate the virtual enviorment.
  * Run deactivate to close the terminal for the virtual enviorment.
 

  #### 3. Install dependencies
  * pip install -r requirements.txt

  
  #### 4 Enviorment variables
  Project requires Django enviorment variables. Create an env.py file in the same folder as manage.py and add the following:
  
  SECRET_KEY = your-secret-key


### Running the app

  * Apply database migration first by running "python manage.py migrate in the root folder (same folder as manage.py)"
  * Create admin account by running "python manage.py createsuperuser"
  * To start the application run: "python manage.py runserver" in the root folder


### Used Technology

1. Django==6.1.1 as web framework
2. django-allauth==65.19.3 for auth handling
3. 