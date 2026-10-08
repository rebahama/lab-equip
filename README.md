# PA1493 Software Development Project (Distance) HT26

---

**Project Name:** *Lab Equipment Knowledge Hub (LEKH)*

**Customer Name:** *Zeth Danielsson*

**Student Full Name:** *Rebaz Mohammad Ahmad*



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

- *Equipment fault reporting, students can report faults on diffrent equipment, caretaker will be able to view the reported fault.*

- *Uploading Equipment images, caretakers can upload images and pdf files.*

- *Guides can be created by caretaker for equipment types, and viewed by students*

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


Search on equipment type:

![Search type](docs/webpage/search-01.png)

Search on serial number:

![Search serial](docs/webpage/search-02.png)

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

### User interface

* Responsiv - The system is designed to be used also on mobile and tablet screens.

* Success messages - The system displays diffrnet messages when a form is submited.

Mobile screens examples:

![Mobile-01](docs/webpage/mobile-01.png)

![Mobile-02](docs/webpage/mobile-02.png)


## User manual

### Installing
- Python 3.14.2
- Git
- Visual studio code

  #### 1. Clone the repository
  * git clone https://github.com/dipt-pa1493-ht26/pa1493-reah23-lekh-zda
  * cd project name

  #### 2. Create and activate virtual enviorment.
  * python -m venv .venv
  * Run .venv\Scripts\Activate to activate the virtual enviorment.
  * To deactivate, run deactivate to close the terminal for the virtual enviorment
  * Windows: .venv\Scripts\activate
  * Mac/Linux source: .venv/bin/activate
 

  #### 3. Install dependencies
  * When virtual enviorment is green and activated run the following: pip install -r requirements.txt to install all the dependencies.

  
  #### 4 Enviorment variables
  Project requires Django enviorment variables. Create an env.py file in the same folder as manage.py and add the following:
  
  * SECRET_KEY = your-secret-key

  * CLOUDINARY_URL = your cloudinary secret api key 


### Running the app first time

  * Apply database migration first by running "python manage.py migrate in the root folder (same folder as manage.py)"

  * Create admin account by running "python manage.py createsuperuser"

  * To start the application run: "python manage.py runserver" in the root folder.

  * When migrations are completed only "python manage.py runserver" is needed to run the application in the root folder.


### Used Technology

1. Django==6.1.1

* Webframe used for building the application, models, views url and database functions.

2. django-allauth==65.19.3

* Used for handling authentication

3. django-cloudinary-storage==0.3.0
* Used for connection Django files and imagefileds for storing uploaded media files.
4. pillow==12.3.0

* Used for Python image handling to upload and process.

5. cloudinary==1.46.2

* Cloudbased media service for storing images.

6. HTML5

* Used for structuring the application pages.

7. CSS3

* Used for custom styles for the application.

8. whitenoise==6.12.0 

* Used for serving static files such as, Javascript, CSS and other static files.

9. Bootstrap

* Used for responsiv mobile design and some styling.