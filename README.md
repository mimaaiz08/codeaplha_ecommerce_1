# 🛍️ Django E-Commerce Website

A simple and responsive **E-Commerce web application** built using **Django**, **HTML**, **CSS**, and **JavaScript**, allowing users to register, log in, browse products, add items to the cart, and place orders.

---

## 🚀 Features

### 🧑‍💻 User Authentication
- Register, Login, and Logout system using Django’s built-in authentication.  
- Session-based authentication with personalized greetings.  
- User-specific shopping cart.  

### 🛒 Shopping Cart
- Add, remove, and update item quantities (+ / - buttons).  
- Real-time cart updates and total calculation.  
- Persistent cart for logged-in users.  

### 💻 Products
- View product listings with images, descriptions, and prices.  
- Simple and responsive grid layout for all screen sizes.  
- Supports product images like **laptops** and **headphones**.  

### 💳 Checkout System
- Checkout page for order details and confirmation.  
- Simple order placement simulation.  
- Clears cart automatically after order completion.  

### 🎨 Frontend
- Built completely with **HTML5**, **CSS3**, and **Vanilla JavaScript** — no Bootstrap or Tailwind.  
- Clean and minimal UI with responsive layout.  
- Separate pages for Login, Register, Cart, Checkout, and Home.  

---

## 🛠️ Technology Stack

| Component | Technology |
|------------|-------------|
| Backend | Django 5.2.7 |
| Frontend | HTML5, CSS3, JavaScript (ES6) |
| Database | SQLite |
| Authentication | Django Built-in Auth |
| Media Handling | Django Static & Media Management |

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd codeaplha_ecommerce
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Website: http://127.0.0.1:8000/

📂 Project Structure

ecommerce/
├── customer_users/         # User authentication and home page
├── shop_products/          # Product models and logic
├── shop_cart/              # Cart and checkout functionality
├── static/                 # Static assets (CSS, JS, images)
├── templates/              # HTML templates
├── db.sqlite3              # Database file
├── manage.py
└── requirements.txt

🧠 How It Works

1.User registers/logs in to access the platform.

2.Products are displayed on the homepage from the database.

3.Users can add items to their cart, adjust quantities, or remove them.

4.The cart total updates dynamically.

5.On checkout, users fill in details and confirm the order.

6.The thank-you page confirms successful order placement.

🧰 Admin Panel

The Django Admin Dashboard provides powerful management tools:

Add and manage Products

Manage Users and Orders

Edit Product details and Prices

Access via:
👉 http://127.0.0.1:8000/admin/

👨‍💻 Author

Muhammed Ismail Maaiz
Built using Django, HTML, CSS, and JavaScript.
