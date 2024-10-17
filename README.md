# Ovaloop-Python-Assessment

## Inventory & Sales Management API

This project implements an Inventory and Sales Management API, designed to allow users to create products, manage stock, track cost and selling prices, and record sales. It features functionality to handle multiple unit measurements for products, manage quantities using the FIFO (First In, First Out) method, and calculate profits for sales transactions.

## Features

1. **Product Creation**: Allows users to create new products with various attributes, including multiple unit measurements.
2. **Retrieve Product Information**: Fetches detailed information about a specific product.
3. **Add Quantity to Products**: Enables users to add stock to existing products while tracking cost prices for each batch.
4. **Sell Products**: Supports selling multiple products in various units and calculates profit based on the FIFO methodology.
5. **Sales History**: Provides users with a history of all sales transactions.

- Create and manage products with detailed attributes.
- Track inventory levels and quantities.
- Manage multiple unit measurements for each product.
- Handle sales transactions and calculate profits.
- Retrieve sales history for analysis.

## Tech Stack

- **Backend Framework**: Django, Django REST Framework
- **Database**: PostgreSQL (or any Django-compatible database)
- **Deployment**: You can use Heroku, Railway, Render, etc.

## API Endpoints

### 1. Create Product

**Endpoint:** `POST /api/products/add_product/`

**Request Body:**

```json
{
  "product_name": "Noodles",
  "quantity": 100,
  "selling_price": "250.00",
  "cost_price": "200.00",
  "category": "Food",
  "unit_measurements": [
    {
      "unit_type": "Pack",
      "quantity": 20,
      "price_per_unit": "200.00"
    },
    {
      "unit_type": "Carton",
      "quantity": 5,
      "price_per_unit": "2400.00"
    }
  ]
}
```

**Response:**

- `201 Created` - When the product is successfully created.
- `400 Bad Request` - If there are validation errors.

### 2. Retrieve Product Information

**Endpoint:** `GET /api/products/`

**Response:**

- Returns a list of products with their details.

### 3. Add Quantity to Products

**Endpoint:** `POST /api/products/add_quantity/`

**Request Body:**

```json
{
  "product_id": 1,
  "quantity": 10,
  "cost_price": "220.00"
}
```

**Response:**

- `200 OK` - When the quantity is successfully added.
- `404 Not Found` - If the product does not exist.

### 4. Sell Products

**Endpoint:** `POST /api/sales/sell_product/`

**Request Body:**

```json
{
  "sales": [
    {
      "product_id": 1,
      "quantity": 2,
      "unit_type": "Pack"
    },
    {
      "product_id": 1,
      "quantity": 1,
      "unit_type": "Carton"
    }
  ]
}
```

**Response:**

- `200 OK` - When the sale is successfully processed.
- `400 Bad Request` - If there are validation errors.

### 5. Retrieve Sales History

**Endpoint:** `GET /api/sales/history/`

**Response:**

- Returns a list of sales transactions with their details.

## Usage

You can test the API endpoints using tools like Postman or cURL. Make sure to include the appropriate headers and request body as specified in the API endpoints section.

## Documentation

The API documentation is generated using Swagger UI and can be accessed by visiting:

`http://<your-server-url>/`

`http://<your-server-url>/redoc/`


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
