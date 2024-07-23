# 3azmy  
Sales and Store Management System based on pyonedark by wonderson

## Overview
This project is a comprehensive system designed to manage sales and store operations efficiently. It includes features for inventory management, sales tracking, customer management, and reporting, all built using PyQt for the GUI and Python for the backend, with MySQL as the database.
![alt text](https://github.com/medhatjachour/3azmy/blob/main/sample/6.png?raw=true)

## Features
- **Inventory Management**: Track stock levels, manage product details, and handle restocking.
- **Sales Tracking**: Record sales transactions, generate invoices, and monitor sales performance.
- **Customer Management**: Maintain customer records, track purchase history, and manage customer interactions.
- **Reporting**: Generate detailed reports on sales, inventory, and customer data.
- **Data Backup**: Backup data to google drive .

## Installation
To get started with the project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/medhatjachour/3azmy.git
    cd 3azmy
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    - Ensure you have a running instance of MySQL.
    - Create a `.env` file in the root directory and add your MySQL connection details:
      ```env
      DATABASE_URL=mysql+pymysql://username:password@localhost/sales_store
      ```

5. **Run the application**:
    ```bash
    python main.py
    ```

## Usage
- **Inventory Management**: Use the Inventory section to add, update, or delete products.
- **Sales Tracking**: Use the Sales section to record new sales and view past transactions.
- **Customer Management**: Manage customer information in the Customers section.
- **Reporting**: Generate and view reports in the Reports section.

## Contributing
We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or suggestions, please contact us at medhatjachour@gmail.com.

---

Feel free to customize this README to better fit your project's specifics. Let me know if you need any more details or assistance! 😊
