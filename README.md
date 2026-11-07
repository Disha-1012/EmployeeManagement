
# 👨‍💼 Employee Management Portal

### A Python-Based Employee Management System

## 📌 About the Project

Employee Management Portal is a web-based application developed using Python and Streamlit.

It provides a simple and user-friendly interface for managing employee information, maintaining employee records, and performing essential employee management operations.

The application uses SQLite as its database to store employee information.

## ✨ Features

- 📊 Dashboard with employee statistics.
- ➕ Add new employee records.
- 👥 View all employee details.
- 🔍 Search employees by name, email, or department.
- ✏️ Update existing employee information.
- 🗑️ Delete employee records.
- 📥 Export employee records as CSV.
- 💾 SQLite database integration.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | Web application interface |
| SQLite | Database management |
| Pandas | Data handling and processing |

## 📂 Project Structure

```text
Employee-Management-Portal/
│
├── app.py
├── README.md
├── requirements.txt
└── employees.db
```

Note: `employees.db` is automatically created when the application runs.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Employee-Management-Portal.git
```

### 2. Navigate to the Project Directory

```bash
cd Employee-Management-Portal
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

Default local URL:

```text
http://localhost:8501
```

## 🗄️ Database Structure

The application uses an SQLite database named `employees.db`.

The employees table contains the following fields:

| Field | Description |
|---|---|
| id | Unique employee ID |
| name | Employee name |
| email | Employee email address |
| department | Employee department |
| designation | Employee job designation |
| salary | Employee salary |
| joining_date | Employee joining date |

## 🔄 Application Modules

1. Dashboard – Displays employee statistics.
2. Add Employee – Registers new employees.
3. View Employees – Displays and searches employee records.
4. Update Employee – Modifies existing employee information.
5. Delete Employee – Removes employee records.

## 🚀 Future Enhancements

- Admin login and authentication.
- Employee profile management.
- Role-based access control.
- Attendance management.
- Leave management.
- Salary and payroll management.
- Employee performance tracking.
- Database integration with MySQL or MongoDB.
- Deployment on Streamlit Community Cloud.

## 👩‍💻 Author

**Your Name**

GitHub: https://github.com/Disha-1012

## 📄 License

This project is available for educational and learning purposes.
