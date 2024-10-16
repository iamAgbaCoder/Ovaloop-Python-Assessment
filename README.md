# Ovaloop-Python-Assessment

## Inventory & Sales Management API

This project implements an Inventory and Sales Management API, designed to allow users to create products, manage stock, track cost and selling prices, and record sales. It features functionality to handle multiple unit measurements for products, manage quantities using the FIFO (First In, First Out) method, and calculate profits for sales transactions.

## Features

1. **Product Creation**: Allows users to create new products with various attributes, including multiple unit measurements.
2. **Retrieve Product Information**: Fetches detailed information about a specific product.
3. **Add Quantity to Products**: Enables users to add stock to existing products while tracking cost prices for each batch.
4. **Sell Products**: Supports selling multiple products in various units and calculates profit based on the FIFO methodology.
5. **Sales History**: Provides users with a history of all sales transactions.

## Tech Stack

- **Backend Framework**: Django, Django REST Framework
- **Database**: PostgreSQL (or any Django-compatible database)
- **Deployment**: You can use Heroku, Railway, Render, etc.

---

## API Endpoints

### 1. Product Creation

**URL**: `/api/products/`  
**Method**: `POST`

This endpoint allows users to create a new product.

#### Request Body

```json
{
  "product_name": "Noodles",
  "quantity": 10,
  "cost_price": 150,
  "selling_price": 200,
  "category": 1,
  "unit_measurements": {
    "Pack": 200,
    "Carton": 2400
  }
}
```

| Field             | Type     | Description                                    |
|-------------------|----------|------------------------------------------------|
| product_name       | string   | Name of the product                            |
| quantity           | integer  | Initial quantity available                     |
| cost_price         | decimal  | Cost price of the product                      |
| selling_price      | decimal  | Selling price of the product                   |
| category           | integer  | Foreign key to the product category            |
| unit_measurements  | JSON     | Dictionary mapping units to their selling price|

#### Response Example

```json
{
  "id": 1,
  "product_name": "Noodles",
  "quantity": 10,
  "cost_price": 150,
  "selling_price": 200,
  "category": 1,
  "unit_measurements": {
    "Pack": 200,
    "Carton": 2400
  }
}
```

---

### 2. Retrieve Product Information

**URL**: `/api/products/<product_id>/`  
**Method**: `GET`

This endpoint retrieves detailed information about a specific product by its ID.

#### Response Example

```json
{
  "id": 1,
  "product_name": "Noodles",
  "quantity": 10,
  "cost_price": 150,
  "selling_price": 200,
  "category": 1,
  "unit_measurements": {
    "Pack": 200,
    "Carton": 2400
  }
}
```

---

### 3. Add Quantity to Products

**URL**: `/api/products/<product_id>/add_quantity/`  
**Method**: `PATCH`

This endpoint allows users to add stock to an existing product while keeping track of different cost prices for each batch.

#### Request Body

```json
{
  "quantity": 10,
  "cost_price": 180
}
```

| Field       | Type    | Description                         |
|-------------|---------|-------------------------------------|
| quantity    | integer | Number of units being added         |
| cost_price  | decimal | Cost price for the new batch        |

#### Response Example

```json
{
  "message": "Quantity added successfully"
}
```

---

### 4. Sell Products

**URL**: `/api/sales/`  
**Method**: `POST`

This endpoint processes sales transactions for multiple products and calculates profits based on the FIFO method.

#### Request Body

```json
{
  "sales": [
    {
      "product_id": 1,
      "quantity": 2,
      "unit": "Pack"
    },
    {
      "product_id": 2,
      "quantity": 1,
      "unit": "Carton"
    }
  ]
}
```

| Field        | Type     | Description                                       |
|--------------|----------|---------------------------------------------------|
| product_id   | integer  | ID of the product being sold                      |
| quantity     | integer  | Quantity of units being sold                      |
| unit         | string   | Unit of measurement (e.g., "Pack", "Carton")      |

#### Response Example

```json
{
  "total_profit": 300
}
```

---

### 5. Retrieve Sales History

**URL**: `/api/sales/`  
**Method**: `GET`

This endpoint retrieves the sales history of the user, including product details, quantity sold, unit, and profit.

#### Response Example

```json
[
  {
    "product": "Noodles",
    "quantity_sold": 2,
    "unit": "Pack",
    "profit": 100,
    "created_at": "2024-10-15T08:00:00Z"
  },
  {
    "product": "Rice",
    "quantity_sold": 1,
    "unit": "Carton",
    "profit": 200,
    "created_at": "2024-10-15T08:10:00Z"
  }
]
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/iamAgbaCoder/inventory-sales-api.git
cd inventory-sales-api
```

### 2. Set Up Virtual Environment

```bash
python -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

In the `settings.py` file, update your database configuration. For PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

---

## Testing

You can test the API using tools like **Postman** or **curl** by hitting the endpoints described above.

Example using `curl` to create a product:

```bash
curl -X POST http://localhost:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{"product_name": "Rice", "quantity": 10, "cost_price": 1200, "selling_price": 1500, "category": 1, "unit_measurements": {"Bag": 1500, "Carton": 18000}}'
```

---

## Deployment

To deploy the API on a free hosting service such as Heroku, Render, or Railway, follow these steps:

### 1. Prepare for Deployment

Ensure the following:
- You have a `Procfile` if deploying to Heroku.
- Update the `ALLOWED_HOSTS` and `DATABASES` in `settings.py` to match your hosting service.
  
Example for Heroku:
```python
ALLOWED_HOSTS = ['your-app.herokuapp.com']
```

### 2. Push to GitHub

Ensure your code is pushed to a GitHub repository.

### 3. Deploy to the Hosting Service

Follow the instructions for your hosting platform (e.g., for Heroku: `heroku create`, `git push heroku master`, etc.).

---

## Future Improvements

1. Add authentication for managing access to the API.
2. Implement pagination for sales history.
3. Add more robust error handling and validation for inputs.
4. Allow searching and filtering on sales history.
5. Add automated testing using `pytest` or `unittest`.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact

For any questions, reach out to [demiladebamgboye@gmail.com](mailto:demiladebamgboye@gmail.com).
