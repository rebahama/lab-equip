# The lab equipment system project

---

**Project Name:** *Lab Equipment Knowledge Hub (LEKH)*

**Customer Name:** *Zeth Danielsson*

**Student Full Name:** *Rebaz Mohammad Ahmad*

## Table of contents
* [Project description and software requirements](#project-description)

* [Back log](#backlog)

* [Database relations and modeling](#database-relations-and-modeling)

* [Features and functionality](#features-and-functionality)

* [User manual and installing](#user-manual)

* [Test and used technology](#tests)




## Project Description

![Homepage](docs/webpage/homepage.png)

This project is a Django-based web application used for manging labratory equipment. The purpose is to make it easier for students and caretaker to, find and borrow diffrent lab equipments.

Students can create accounts and browse all the lab equipments using search and filter based on serial numbers, available and on loan equipments. Equipment types and categories can also be browsed based on what the students prefers. Students can send a booking request for a specific equipment that is then handled by a caretaker.

Caretakers can manage the labratory equipments by adding and editing the equipments and categories. Caretaker can also review and approve student bookings.

The system includs also user roles that is decided by the admin account, admin can choose diffrent roles for the created accounts. All accounts are created as student account for default and admin decides if an account should change to caretaker.





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
| *Alice* | *Age: 35, background: caretaker, technical skill level 5/10, etc.* | *Needs an overview of borrowed equipment, stocks and overdue items* |*Register equipment,update status, approve or reject borrowed items* |



### Software Requirements

**Functional Requirements**
- *User registration and login, User can register using email, username and password*

- *Diffrent user permissions, The system supports student,admin and caretaker roles*

- *Equipment registration, caretaker registers name, category, description, location and status.*

- *Equipment handling and categories, caretaker will create,read,update and delete the equipments and categories.*

- *Booking equipment, students can book an equipment in a form that will be displayed to caretaker.*

- *Equipment viewing, caretaker and students will be able to view detalied page of each equipment.*

- *Equipment search and filtering, students must be able to search by name and filter by category*

- *Guides and projects searching, students must be able to search by guides and projects.*

- *Equipment fault reporting, students can report faults on diffrent equipment, caretaker will be able to view the reported fault.*

- *Uploading Equipment images, caretakers can upload images.*

- *Guides can be created by caretaker for equipment types, and viewed by students*

- *Students can create projects on equipment-types*

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

## Database relations and modeling

The Database for the application can be viewed from the image below:

![Database diagram](docs/db-diagram.png)

## Features and functionality

### Authentication and user mangement

* Registration - Students can create  account to access the system.
* Login/logout - Users can securely login/logout.
* User roles - Users have diffrent permission based on their role, students, caretaker and admin.
* Role management - Administrators can assign diffrent permission roles to the users.

Create account:
![Create account](docs/webpage/auth-01.png)

Login:

![Login account](docs/webpage/auth-03.png)

Mange roles:

![Mange roles](docs/webpage/auth-02.png)



### Equipment management

* Equipment overview - Users can view all the equipment.

* Equipment Detail - Users can view detalied information in the overview when clicking a link.

* Equipment categories - Equipment are grouped into categories for easiser navigation.

* Equipment status - Equipment can be marked as avalible, on loan, in repair or out of service.

* Equipment management - Caretaker can add, edit and delete equipments.

* Availability - Students can view how many equipments are avalible at the moment and how many are on loan.


View all equipment:
![View all](docs/webpage/equipment-03.png)

View detailed equipment:
![View detail](docs/webpage/equipment-04.png)

View categories
![View categories](docs/webpage/equipment-05.png)

Clicked categories:
![View clicked categories](docs/webpage/equipment-02.png)

View equipment types after categories
![View equiments types](docs/webpage/booking-4.png)

Clicked equipment types
![View equiments types](docs/webpage/booking-2.png)

Equipment status:

![View status](docs/webpage/equipment-07.png)

Equipment create, read, update and delete:

![View crud](docs/webpage/equipment-08.png)

![View edit](docs/webpage/equipment-01.png)

![View delete](docs/webpage/equipment-09.png)

![View crud buttons](docs/webpage/equipment-06.png)


### Booking system

* Booking - Students can request booking equipments.

* Booking approval - Caretaker can approve or reject from students booking.

* My bookings - Students can view their booking when its been approved from caretaker.

* Mange bookings - Caretaker can see all the bookings from students in the caretaker dashboard page.


Students makes a booking: 

![Student booking](docs/webpage/booking-demo-03.png)

![Student booking](docs/webpage/booking-demo-05.png)

If the dates are not correct:

![Student booking](docs/webpage/booking-message.png)

![Student booking](docs/webpage/booking-demo-06.png)

Caretaker recives a booking on caretaker manage booking page:

![Caretaker booking recive](docs/webpage/booking-demo-10.png)

Caretaker approves student booking:


![Caretaker approve](docs/webpage/booking-demo-12.png)


![Caretaker approve](docs/webpage/booking-demo-13.png)

Student recives status updated and can return equipment when caretaker approves:

![Student view booking](docs/webpage/booking-demo-11.png)

Student wants to return equipment:
![Student view booking](docs/webpage/booking-demo-09.png)

![Student view booking](docs/webpage/booking-demo-16.png)

![Caretaker return bookings](docs/webpage/booking-demo-15.png)

Caretaker recives return request on caretaker page and confirms:

![Caretaker return bookings](docs/webpage/booking-demo-14.png)


![Caretaker return message](docs/webpage/booking-demo-02.png)

Student gets updated status badge when caretaker have confirmed returns:

![Caretaker return message](docs/webpage/booking-demo-01.png)


Caretaker can see active, pending and history bookings:

Caretaker edit category page:

![Caretaker active,history bookings](docs/webpage/caretaker-03.png)


Student can see history and active bookings:

![Student current and history](docs/webpage/caretaker-04.png)

### Caretaker dashboard page

* Mange bookings - Only caretaker can see all the bookings from students in the caretaker dashboard page.

* Mange categories - Only caretaker can edit categories.

* Mange equipments - Only caretaker can create/edit/delete equipments from the caretaker page.

Caretaker dashboard page:

![Caretaker page](docs/webpage/booking-demo-07.png)


Caretaker edit category page:

![Caretaker edit category](docs/webpage/caretaker-02.png)


### Search and filter system

* Users can search based on equipment name, serial number, equipment-type and categories.

* Users can filter and render equipment based on categories and status such as: avalible, on loan and repair.

* Users can search guides and projects.


Search on equipment type:

![Search type](docs/webpage/search-01.png)

Search on serial number:

![Search serial](docs/webpage/search-02.png)

Search on guides:

![Search guides](docs/webpage/search-12.png)

![Search guides](docs/webpage/search-10.png)

![Search guides](docs/webpage/search-11.png)


Search on projects:

![Search projects](docs/webpage/search-09.png)

![Search projects](docs/webpage/search-07.png)

![Search projects](docs/webpage/search-08.png)

Filter status that are: "on loan":

![Filter status](docs/webpage/search-03.png)

Filter status that are: "avalible":

![Filter status](docs/webpage/search-04.png)

Filter on categories:

![Filter categories](docs/webpage/search-05.png)


### Report fault system

* Users can report a fault on equipments.

* Caretaker can approve the reported fault and change it to an active repair page.

* Caretaker updates the status to in repair.

* Caretaker can report an equipment type fault and display message on equipment type.

User reports fault:

![Report](docs/webpage/report-02.png)


![Report](docs/webpage/report-01.png)


![Report](docs/webpage/report-05.png)

Caretaker recives the reported fault:

![Report](docs/webpage/report-04.png)

![Report](docs/webpage/report-03.png)


![Report](docs/webpage/report-06.png)

When Caretaker confirms reported fault then status changes to in progress, and its not possible to report the specific equipment anymore untill its been resolved.

Status changes to in progress:

![Report](docs/webpage/report-10.png)

Message on the same equipment.

![Report](docs/webpage/report-13.png)

Status also changes to in repair on the equipment.

![Report](docs/webpage/report-15.png)

When repair is done and caretaker clicks finish resolved equipment can be found on a page only for resolved equipments.

![Report](docs/webpage/report-08.png)


![Report](docs/webpage/report-14.png)

Caretaker reports a equipment type problem:

![Report](docs/webpage/report-22.png)

![Report](docs/webpage/report-18.png)

![Report](docs/webpage/report-17.png)

The reported fault can be displayed on all the equipment types. Notice the diffren serial numbers and that the problem gets displayed on all the types.

![Report](docs/webpage/report-20.png)

![Report](docs/webpage/report-19.png)

### Archived equipments

* When caretaker puts equipment status to: "retired" then equipment is no longer displayed on the view all equipment page.

Message when: out of service or retired is choosen in the edit page for equipments.

![Archived](docs/webpage/archive-04.png)


When clicking the archived equipments
![Archived](docs/webpage/archive-03.png)

When clicking archived page caretaker gets here, this page is only shown for caretaker where all the equipment marked retired is displayed.

![Archived](docs/webpage/archive-02.png)

When searching for the equipment that is retired with the serial number on the view all equipment page that is visable for all users.:

![Archived](docs/webpage/archive-01.png)


### Out of service equipment

When caretaker puts out of service equipment for the status.

![Out service](docs/webpage/out-service-01.png)

Displayed message for that equipment when students view it.

![Out service](docs/webpage/out-service-02.png)

When students clicks the link on the out of service equipment. Link leads the user to available equipmentof the same type.

![Out service](docs/webpage/out-service-03.png)


### Equipment guides

* Caretaker can create guides for equipment type.
* Student can view guides for equipment type.

When caretaker creates guide:

![Guide](docs/webpage/guide-07.png)

![Guide](docs/webpage/guide-08.png)


![Guide](docs/webpage/guide-09.png)

When student views the created guide for Raspberry on the show all guides for equpment type

![Guide](docs/webpage/guide-06.png)


![Guide](docs/webpage/guide-03.png)

When student views detalied guide
![Guide](docs/webpage/guide-05.png)


When student views the created guide for anotgher equipmenttype microcontroller ESP32 on the detailed equipment page:

![Guide](docs/webpage/guide-04.png)


Detalied guide:
![Guide](docs/webpage/guide-05.png)


If there is no guide:
![Guide](docs/webpage/guide-02.png)

### Student projects

* Student can create projects on equipment types.
* Student can view the personal created projects.
* The project is accessed from the indivudual equipments and in student personal page.

When student creates a project:
![Project](docs/webpage/project-06.png)

![Project](docs/webpage/project-01.png)

![Project](docs/webpage/project-02.png)


![Project](docs/webpage/project-08.png)

The detalied projects page:
![Project](docs/webpage/project-07.png)

The created projects depends on the equipment type, so all the equipment type that shows for example Logitech c920. the project will be displayed across all the individual equipment type with that name when clicking view projects.

When viewing from the detalied equipment in this case Logitech c920:

![Project](docs/webpage/project-04.png)


![Project](docs/webpage/project-03.png)

And when viewing another equipment type the project will not be displayed. In this case raspberry pi 4b

![Project](docs/webpage/project-10.png)

The student can also view all the created projects here:

![Project](docs/webpage/project-09.png)

This will display all the created projects for logged in student.

### User interface

* Responsiv - The system is designed to be used also on mobile and tablet screens.

* Success messages - The system displays diffrnet messages when a form is submited.

Mobile screens examples:

![Mobile-01](docs/webpage/mobile-01.png)

![Mobile-02](docs/webpage/mobile-02.png)


## User manual

### Installing
- Python 3.14.2 is used for this project

- Visual studio code was used as code editor

  #### 1. Clone the repository
  * git clone https://github.com/dipt-pa1493-ht26/pa1493-reah23-lekh-zda
  * cd pa1493-reah23-lekh-zda

  #### 2. Create and activate virtual enviorment.
  * run **python -m venv .venv** in the terminal to create virtual enivorment.

  * If using windows run: **.venv\Scripts\activate** to activate the virtual enviorment in the terminal.

  * If using Mac/Linux source: **.venv/bin/activate**

  * If you need to deactivate the virtual enviorment, run **deactivate** in the terminal
 

  #### 3. Install dependencies
  * When virtual enviorment is green and activated run the following in the root project terminal:
   **pip install -r requirements.txt** to install all the dependencies for the project. The dependencies versions can be found in the **requirements.txt** that is located in the root folder of this project.

  
  #### 4 Enviorment variables
  Project requires Django environment variables. CLOUDINARY_URL is not necessary to start project but is required if uploading images when creating equipments or displaying images, more info can be found in: **"5 Static files and uploaded images below"**.
  
  
  Create an env.py file in the same folder as manage.py and add the following:
  
  * SECRET_KEY = your-secret-key

  * CLOUDINARY_URL = your cloudinary API KEY and API SECRET.

  Your SECRET_KEY can be any random combination that you want, your env.py should look like this before starting the application:

  ![Env file](docs/env.png)


  #### 5 Static files and uploaded images
  Project can start without CLOUDINARY_URL but requires CLOUDINARY_URL to upload images to created equipment and display the images correctly. If CLODUINARY_URL is not present then an error will display when trying to upload images or displaying images, the uploaded images will be uploaded to a cloud that is accessed by an image url link, create an account in Cloudinary and copy your secret api key in the CLOUDINARY_URL.
  
  [Click here](https://cloudinary.com/) here to create a free account with Cloudinary.

  * Create a free account.
  * Sign in to your account.
  * Open dashboard.
  * Copy API KEY and API SECRET.
  * Paste the API KEY and API SECRET to the CLOUDINARY_URL env variable.


### Running the application for first time

1. First make sure you have installed the dependencies and created the environment variables by following the [installing instructions](#installing). Make also sure that your virtual enviorment is green and activated before running the **python** commands below. 


2. Apply database migration first by running **python manage.py migrate** in the root folder terminal (same folder as manage.py)" This creates default data in order for the application to run without errors, a test account with caretaker role will also be created when running migrate to add the default data. The login information for the test account can be found below:

    * Username:**testcaretaker**
    * Password:**Testing**


3. If you want to manage user roles you need an admin account, after the database migration run: **python manage.py createsuperuser** in the root folder terminal. A text will appear in terminal, follow the instructions:

    * Username will appear in the terminal, type in your username that you want.

    * Email adress will appear in the terminal, you don´t have to put in email, you can just press enter.

    * Password will appear in terminal, put in a password that you will use, when typing in your password in the terminal it will not show the text that you are typing at the moment. But it will register it, so make sure that you type it in correctly. After you have put in password, press enter.

    * Password (again) will appear in the terminal, put in the same password that you put in earlier to confirm, it will also show up blank here as you are typing the password, but you can be sure that the temrinal is registering it.

    * After you have put in password again a message will appear "Superuser created successfully". You can now use this account to login to the webapplication and manage diffrent user roles, but before you can manage diffrent roles you need to create an account inside the webapplication so that you can choose the created account and give it a student or caretaker role.


4. To start the application run: **python manage.py runserver** in the root folder terminal. You can acess the page by visiting or typing: **http://localhost:8000** in your browser url.

5. When creating an account inside the webapplication page, the default accounts have student permissions, in order to change role to caretaker, login to admin account in webapplication and click "manage accounts" to change the roles and view diffrent functionality for the diffrent account roles. Admin user can not access student and caretaker functions.



## Tests

Tests are divided in the following folders, bookings, equipment, projects and repairs. To run a test for equipment put the following in the terminal:

 * **python manage.py test equipment  --settings=lab_equipment.settings_test**

 This will run the tests for equipment folder, and if you want to run tests for repairs, change the "equipment" to "repairs" in the test command above. A seperate database will be created when running the test and destroyed automatically when test is completed.


### Used Technology

*  Django==6.1.1 - **Webframe used for building the application, models, views url and database functions.**

* django-allauth==65.19.3 - **Used for handling authentication**

* django-cloudinary-storage==0.3.0 - **Used for connection Django files and imagefileds for storing uploaded media files.**

* pillow==12.3.0 - **Used for Python image handling to upload and process.**

* cloudinary==1.46.2 - **Cloudbased media service for storing images.**

* HTML5 - **Used for structuring the application pages.**

* CSS3 - **Used for custom styles for the application.**

* whitenoise==6.12.0 - **Used for serving static files such as, Javascript, CSS and other static files.**

* Bootstrap - **Used for responsiv mobile design and some styling.**