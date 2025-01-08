# Invogen

Invogen is a Django-based web application that simplifies the process of generating professional invoices in PDF format. With preformatted invoice templates, inventory management features, and product selection tools, Invogen streamlines billing and invoicing for businesses of all sizes.

---

## Features

- **PDF Invoice Generation**: Create and download invoices in a professional PDF format using preformatted templates.
- **Inventory Management**: Store and manage products, including their details (name, price, description, etc.).
- **Product Selection**: Easily add products from the inventory to the invoice.
- **Client Management**: Store client details for quick invoice generation.
- **User Authentication**: Secure access for users to manage their invoices and inventory.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gajeet11000/Invogen.git
   cd Invogen
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open the app in your browser:
   ```
   http://127.0.0.1:8000/
   ```

---
