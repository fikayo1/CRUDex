## CRUDex

An API that performs simple CRUD function .

### Prerequisites

- Python 3.7+
- Django 
- Database (e.g., PostgreSQL, SQLite)
- Other in requirement.txt

### Installation

1. **Clone the Repository:**
   ```
   git clone https://github.com/fikayo1/CRUDex.git
   ```

2. **Create a Virtual Environment (Optional but recommended):**
   ```
   python -m venv myenv
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source myenv/bin/activate
     ```

4. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Database Setup:**
   - Create database tables:
     ```
     python manage.py migrate
     ```

6. **Run the Development Server:**
   ```
   python manage.py runserver
   ```

7. **Access the API:**
   - Open a web browser and go to `http://crudex.pythonanywhere.com/api` to access the API.

Certainly! Below, I'll explain the API endpoints and provide usage examples for your Django project.


### Usage Examples

#### Creating a New Person

To create a new person, send a POST request to the `/api` endpoint with a JSON request body containing the person's name:

```shell
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://crudex.pythonanywhere.com/api
```

#### Retrieving a Person

To retrieve a person by ID, send a GET request to `/<user_id>`:

```shell
curl http://crudex.pythonanywhere.com/api/1
```

#### Updating a Person

To update a person's name by ID, send a PATCH request to `/<user_id>` with a JSON request body containing the new name:

```shell
curl -X PATCH -H "Content-Type: application/json" -d '{"name": "Jane Smith"}' http://crudex.pythonanywhere.com/api/1
```

#### Deleting a Person

To delete a person by ID, send a DELETE request to `/<user_id>`:

```shell
curl -X DELETE http://crudex.pythonanywhere.com/api/1
```


### Contact Information

[email:soetandan@gmail.com](soetandan@gmail.com) 