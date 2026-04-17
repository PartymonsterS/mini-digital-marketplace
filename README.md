# **Mini Digital Marketplace**

Simple web application built with Django for publishing and browsing digital products.

---

## **Features**

- 🔐 **Authentication**
  - Register, login, logout
- 📦 **Products**
  - Create products with image upload
  - View product detail pages
  - Edit and delete own products
- 📂 **Categories**
  - Group products by category
- 🛒 **Orders**
  - Buy products
  - Prevent duplicate orders per user
- 👤 **User pages**
  - My Products
  - My Orders

---

## **Tech Stack**

- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **Frontend:** Django Templates + Bootstrap

---

## **Project Structure**

```text
mini-digital-marketplace/
│
├── config/
│   ├── settings/
│   └── urls.py
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── products/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── orders/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── templates/
│   ├── base.html
│   ├── accounts/
│   ├── registration/
│   ├── products/
│   └── orders/
│
├── media/
├── static/
│
├── manage.py
└── requirements/
```

## **Setup**

```bash
git clone https://github.com/your-username/mini-digital-marketplace.git
cd mini-digital-marketplace

python -m venv .venv
source .venv/bin/activate

pip install -r requirements/base.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver
```

## **Available URLs**

- `/` — home  
- `/accounts/register/`  
- `/accounts/login/`  
- `/products/create/`  
- `/my-products/`  
- `/orders/my-orders/`  
- `/admin/`  

---

## **Notes**

- Only authenticated users can create, edit, and delete their own products
- Each user can order a product only once
- Draft products are not shown publicly
- Images are stored in the media/ directory