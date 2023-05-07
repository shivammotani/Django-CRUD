# CRUD Operations using Django by both Web-page and REST API

# Intro

This is a Django app which can perform CRUD operations by both, webapp and REST API.

# Requirements
See pipfile and pipfile.lock


### Step 1 : Clone the Repository

`git clone https://github.com/shivammotani/Django-CRUD_USING-WEBAPP_AND_REST_API.git`

### Step 2 : Install Requirements and Dependencies
I'm using pipenv as a virtual environment manager. You can use any other virtual environments as you like.
If you want to use any other virtual environment manager apart from pipenv, here are the steps to generate req.txt from the pipfile:
  * `pip install pipenv`
  * `pipenv requirements > requirements.txt`

Since for this approcah you'll have to install pipenv which obviously you don't want if you're reading this line. Therefore, i'll upload requirements.txt separately for the reference but i'll still suggest you to use
pipenv. It makes managing virtual env and dependencies a lot easier.
For those who want to use pipenv only. Follow these steps:

Goto your directory where you've cloned this repository and open up your terminal and run the below commands:
  * `pipenv shell`
  * `pipenv sync`
 
Voila! Your virtual env is started and ready with all the dependencies required to run this repository.


### Step 3: Configuring Database
For this project I'm using Postgresql instead of default SQLite that comes with Django. Let's configure this:

  * Start by creating a new user/role in the pgadmin interface of postgresql and enable 'can login' option in privileges.
  * Create a new database and assign the newly created user/role as the owner of this database
  * Go to settings.py under employee_project and under DATABASES update the following paramters:
  
    * **'NAME'**: '<your_database_name_that_you_just_created>'
    * **'USER'**: '<name_of_user/role_created>'
    * **'PASSWORD'**: '<password_of_user/role_created>'
  * After this execute the below command:
    * `python manage.py migrate`
    
Voila! You've successfully configure Postgresql in your Django Repository

### Step 4: Running the repository
Now that everything is set up let's run the program and the CRUD operation in real
Start by executing the below code:

  `python manage.py runserver`
  
You should see a url in the termnial. Click on that and you should see a screen with the Employee form as displayed below:

![image](https://user-images.githubusercontent.com/52162019/236696231-ce0e3043-fce6-487e-a906-6baaf1b02eac.png)


Here you can now add employee details and then you can go back to the list using 'Back To List' button
 
![image](https://user-images.githubusercontent.com/52162019/236696319-b3dfe945-e550-4c68-a2db-da69b1df80c1.png)
 
From this screen you can view all the Employee curently present in the database and you can edit and delete them as well.
 
 
## This is how we can inteact with the Webapp to perform CRUD operations. Let's see how we can achieve the same via REST API.
 
### Step 1: Copy the url that was displayed on the termainal and append `/api/` to it. It should look something like this
  * `http://127.0.0.1:8000/api/`

![image](https://user-images.githubusercontent.com/52162019/236696568-5c662734-ee26-49e9-a042-665bac475bb5.png)


### Step 2: You'll now see the API interface of the app which is created uinng DjangoRestFramework library.
Here, you'll be see two url's listed
  * `"http://127.0.0.1:8000/api/employee/"`
  * `"http://127.0.0.1:8000/api/positions/"`
 
 The first url displays all the records that are present in the database in a JSON format. It also gives you an interface to perform POST operations on the app
 
 ![image](https://user-images.githubusercontent.com/52162019/236696726-ab12d68f-a9c0-42fa-b983-b55f6830e49d.png)

### Note: In the position id field we'll have to give the **actual id and not the position name**. This is where the second url comes into picture.
If we visit the second url we can see the id's correspond to all the positions list.

***Do note only GET request is allowed on this URL.***

![image](https://user-images.githubusercontent.com/52162019/236696865-d3f4e6e0-077b-455e-8807-88c5db3ea319.png)

### Step 3: Using postman we can perform GET, POST, PUT(update) and DELETE operations:
## GET REQUEST

  * Get is fairly simple we just need to add the url in the GET input field to see all the records
    * `http://127.0.0.1:8000/api/employee/`
 
![image](https://user-images.githubusercontent.com/52162019/236697071-0cbcc351-3a69-4a0c-8610-d9a9b176d69b.png)

  * To see a specific record just append the ID of that record after that url
    * `http://127.0.0.1:8000/api/employee/<id>`
   
![image](https://user-images.githubusercontent.com/52162019/236697141-fb7b2eff-f643-469e-a608-d18a562ff692.png)

## POST REQUEST
  * Change the type of reuqest to POST
  * Add "Content-Type" in Key and "application/json" in value under Headers Tab in postman
  * Use the below Json format in Body to perform POST operations:
    ``` json 
    {
        "fullname": "<emp_name>",
        "emp_code": "<emp_code>",
        "mobile": "<emp_mobile_no>",
        "position": {
                      "title": "<get_title_id_from_positions_url>"
                    }
      } 
      ```
      
![image](https://user-images.githubusercontent.com/52162019/236697477-569104e2-f2cb-4523-9c69-f92b0072e42e.png)

## PUT REQUEST
  * Change the type of reuqest to PUT
  * Add "Content-Type" in Key and "application/json" in value under Headers Tab in postman
  * Pass the id of the record that you want to update similar to what we did in GET for fetching a specific record
  * Use the below Json format in Body to perform POST operations:

  ``` json 
    {
        "fullname": "<emp_name>",
        "emp_code": "<emp_code>",
        "mobile": "<emp_mobile_no>",
        "position": {
                      "title": "<get_title_id_from_positions_url>"
                    }
      }
   ```
      
![image](https://user-images.githubusercontent.com/52162019/236697631-44f74f62-436d-4a7a-97d0-f5da610eeb1a.png)

## Delete REQUEST
  * Pass the id of the record that you want to delet similar to what we did in GET for fetching a specific record and your record will get deleted

### This is how we can use this repository to perform CRUD using Django via both Webapp and REST API. 

