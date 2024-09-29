![image](https://github.com/user-attachments/assets/c041ce59-9c47-4554-a0c3-a046a5042ee8)# Inventory Management API

This is an inventory management system built using Django Rest Framework (DRF) with PostgreSQL as the database and JWT authentication for security.

## Features
- JWT Authentication for securing API endpoints.
- CRUD operations for managing inventory items.
- Logging for API monitoring and debugging.
- Unit tests for verifying API functionality.

## Prerequisites
- Python 3.x
- PostgreSQL
- Django and Django Rest Framework
- JWT Authentication packages

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rani-Rajan/inventory-management.git
   cd inventory-management

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   
4. Set up the PostgreSQL database:
   - Create a new database and user.
   - Update the database settings in settings.py.
   
5. Run migrations:
   ```bash
   python manage.py migrate

6. Start the development server:
   ```bash
   python manage.py runserver

## API Documentation

1. Authentication:
   Login:
   Endpoint: /api/auth/login/
   Method: POST
   Request Body:
   json
   {
  	"username": "your_username",
  	"password": "your_password"
   }
   Response: Returns a JWT token for authentication.

2. Inventory Item Operations
      1. Create Item
	 Endpoint: /api/items/
	 Method: POST
	 Request Body:
	 json
	 {
  		"name": "Item Name",
  		"quantity": 10,
  		"price": 25.99
	 }
         Response: Returns the created item details.
      2. Retrieve Items
	 Endpoint: /api/items/
	 Method: GET
	 Response: Returns a list of all inventory items.
      3. Update Item
	 Endpoint: /api/items/<int:item_id>/
	 Method: PUT
	 Request Body:
	 json
	 {
  		"name": "Updated Item Name",
  		"quantity": 20,
  		"price": 30.99
	 }
	 Response: Returns the updated item details.
      4. Delete Item
	 Endpoint: /api/items/<int:item_id>/
	 Method: DELETE
	 Response: Returns a confirmation message.


3. Usage Examples
  1.  Example: Creating an Item
      ```bash
      curl -X POST http://localhost:8000/api/items/ \
      -H "Authorization: Bearer YOUR_JWT_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{"name": "New Item", "quantity": 5, "price": 10.00}'
 2.  Example: Retrieving Items
     ```bash
     curl -X GET http://localhost:8000/api/items/ \
     -H "Authorization: Bearer YOUR_JWT_TOKEN"

### Additional Notes
- email address -> raniranjitham97@gmail.com
- You can also include a section for acknowledgments if you’ve used any libraries or resources that you want to credit.


