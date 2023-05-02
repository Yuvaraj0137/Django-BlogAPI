# Django BlogAPI
This is a Django-based web application that allows users to register and log in, and create and view blog posts through API endpoints.

## Features
* User registration and login
* Ability to create, update, view and delete blog posts
* Search functionality to search for blog posts by title or text
* Pagination of blog posts
* Authentication using JWT tokens

## Technologies
This project was built using the following technologies:

* Django
* Django REST framework
* Django REST framework Simple JWT
* Sqlite3

## Installation
1.Clone the repository
```bash
git clone <repository_url>
```
2.Create a virtual environment and activate it
```bash
virtualenv venv
source venv/bin/activate
```
3.Install dependencies
```bash
pip install -r requirements.txt
```

4.Create the database
```bash
python manage.py migrate
```

5.Run the server
```bash
python manage.py runserver
```
6.Access the application in your browser at http://localhost:8000/ or You can use API development and  testing tools such as **Postman**,  **Insomnia**,    **swagger**, etc...

## Usage
### 1.User registration
To register, send a POST request to http://localhost:8000/api/blog_account/register/ 
```json
{ 
    "first_name": "your_first_name", 
    "last_name": "your_last_name", 
    "username":"your_username", 
    "password": "your_password" 
}
```
### 2.User login
To log in, send a POST request to http://localhost:8000/api/blog_account/login/ with the following data:
```json
{ 
    "username": "your_username", 
    "password": "your_password" 
}

This will return a JWT token that you can use to authenticate subsequent requests.

### 3.Create a blog post
To create a blog post, send a POST request to http://localhost:8000/api/home/my_blogs/ with the following data:
```json
{ 
    "title": "your_post_title", 
    "blog_text": "your_post_text" 
}
```
Make sure to include the JWT token in the Authorization header of the request, like this:
```makefile
Authorization: Bearer <your_token_here>
```
### 4.Update a blog post
To update a blog post, send a PATCH request to http://localhost:8000/api/home/my_blogs/ with the which data do you want to update, but the **uid** field is necessasary to update like this:
```json
{ 
    "uid": "8e6ea874-4c1f-4005-a0b7-7eea8d5f1f67",
    "title": "updated_post_title", 
    "blog_text": "updated_post_text" 
}
```
Make sure to include the JWT token in the Authorization header of the request, like this:
```makefile
Authorization: Bearer <your_token_here>
```
### 5.Delete a blog post
To delete a blog post, send a DELETE request to http://localhost:8000/api/home/my_blogs/ with the **uid** like this:
```json
{
    "uid": "8e6ea874-4c1f-4005-a0b7-7eea8d5f1f67"
  
}
```

Make sure to include the JWT token in the Authorization header of the request, like this:
```makefile
Authorization: Bearer <your_token_here>
```
### 6.View all blog posts
To view all blog posts, send a GET request to http://localhost:8000/api/home/blogs/. You can also add a search parameter to search for blog posts by **title** or **text** or **date** like this:

```ruby
http://localhost:8000/api/blogs/?search=< title or text or date >
```
### 7.View your blog posts
To view your blog posts, send a GET request to http://localhost:8000/api/my_blogs/. You can also add a search parameter to search for your blog posts by title or text, like this:

```ruby
http://localhost:8000/api/my_blogs/?search=query_here
```

Make sure to include the JWT token in the Authorization header of the request, like this:
```makefile
Authorization: Bearer <your_token_here>
```

# Credits
This project was built by Yuvaraj-Ponnusamy.
