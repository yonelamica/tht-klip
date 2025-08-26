

A Django-based web application for managing customer accounts, transactions, and financial data.

## Features

- Customer Management: Add, edit, and delete customers with unique account numbers
- Transaction Processing: Record debits and credits with automatic balance calculations
- Customer Enquiries: View transaction histories and generate customer reports
- Data Filtering: Filter transactions by date, type, and customer


## Tech Stack

- Django 4.2
- SQLite3
- HTML/CSS/JavaScript


## Installation

1. Clone the repo:
   
   git clone https://github.com/yonelamica/tht-klip.git
   cd tht-klip
   

2. Set up virtual environment:
   
   python -m venv env
 Activate your veirtual env by running: env\Scripts\activate
   

3. Install dependencies:
   
   pip install -r requirements.txt
   

4. Run migrations:
   
   python manage.py makemigrations
   python manage.py migrate
   

5. Start the server:
   
   python manage.py runserver
   

Open http://127.0.0.1:8000 in your browser.

## Usage

### Managing Customers
Navigate to the Customer Amendments section to add new customers or modify existing ones. Each customer gets a unique account number automatically.

### Recording Transactions
Use the transactions module to record debits and credits. All transactions update customer balances in real-time. You can filter by date range or transaction type.

### Customer Reports
The enquiries section lets you view individual customer transaction histories and sort data by various criteria.


