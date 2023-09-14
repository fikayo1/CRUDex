## API Endpoints

1. **Create a New Person Object (POST)**

   - **Endpoint**: `/api`
   - **Method**: POST
   - **Description**: This endpoint allows you to create a new person object.

   **Request Body**:
   ```json
   {
       "name": "John Doe"
   }
   ```

   **Response (201 Created)**:
   ```json
   {
       "message": "Person created successfully",
       "id": 1,
       "name": "John Doe"
   }
   ```

   **Response (400 Bad Request - Person Already Exists)**:
   ```json
   {
       "error": "person already exists"
   }
   ```

2. **Get Person Object by ID (GET)**

   - **Endpoint**: `/api/<int:user_id>`
   - **Method**: GET
   - **Description**: This endpoint retrieves a person object by its ID.

   **Response (200 OK)**:
   ```json
   {
       "id": 1,
       "name": "John Doe"
   }
   ```

   **Response (404 Not Found - Person Does Not Exist)**:
   ```json
   {
       "error": "person with id {user_id} does not exist"
   }
   ```

3. **Update Person Object by ID (PATCH)**

   - **Endpoint**: `/api/<int:user_id>`
   - **Method**: PATCH
   - **Description**: This endpoint updates a person object's name by its ID.

   **Request Body**:
   ```json
   {
       "name": "Jane Smith"
   }
   ```

   **Response (200 OK)**:
   ```json
   {
       "message": "Person updated successfully",
       "id": 1,
       "name": "Jane Smith"
   }
   ```

   **Response (404 Not Found - Person Does Not Exist)**:
   ```json
   {
       "error": "person with id {user_id} does not exist"
   }
   ```

   **Response (400 Bad Request - Name Already Taken)**:
   ```json
   {
       "error": "name already taken, Pick another name"
   }
   ```

4. **Delete Person Object by ID (DELETE)**

   - **Endpoint**: `/api/<int:user_id>`
   - **Method**: DELETE
   - **Description**: This endpoint deletes a person object by its ID.

   **Response (200 OK)**:
   ```json
   {
       "message": "person object deleted successfully"
   }
   ```

   **Response (404 Not Found - Person Does Not Exist)**:
   ```json
   {
       "error": "person with id {user_id} does not exist"
   }
   ```


- You can test out the api on Postman using this [link](https://documenter.getpostman.com/view/22305104/2s9YC5xruH)