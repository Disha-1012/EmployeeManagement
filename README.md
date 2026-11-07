# 👨‍💼 Employee Management Portal

### A Python-Based Employee Management System

## 📌 About the Project

Employee Management Portal is a web-based application developed using Python and Streamlit.

It provides a simple and user-friendly interface for managing employee information, maintaining employee records, and performing essential employee management operations.

The application uses SQLite as its database to store employee information. GraphQL is specified as the API layer for structured and flexible employee data operations.

## ✨ Features

- 📊 Dashboard with employee statistics.
- ➕ Add new employee records.
- 👥 View all employee details.
- 🔍 Search employees by name, email, or department.
- ✏️ Update existing employee information.
- 🗑️ Delete employee records.
- 📥 Export employee records as CSV.
- 💾 SQLite database integration.
- 🔗 GraphQL API specification for employee data management.
- 📡 Structured data retrieval through GraphQL queries and mutations.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | Web application interface |
| SQLite | Database management |
| Pandas | Data handling and processing |
| GraphQL | API specification and data querying |
| GraphQL SDL | Defining employee types, queries, and mutations |

## 📂 Project Structure

```text
EmployeeManagement/
│
├── app.py
├── README.md
├── requirements.txt
└── index.html
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Disha-1012/EmployeeManagement.git
```

### 2. Navigate to the Project Directory

```bash
cd EmployeeManagement
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

## 🔗 GraphQL API Specification

GraphQL is a query language for APIs that allows clients to request specific data and perform operations through a structured schema.

The Employee Management Portal defines the following GraphQL API specification for employee management.

### 1. Employee Type

The Employee type represents the structure of employee information.

```graphql
type Employee {
    id: ID!
    name: String!
    email: String!
    department: String!
    designation: String!
    salary: Float!
    joining_date: String!
}
```

### 2. Queries

Queries are used to retrieve employee information.

```graphql
type Query {
    employees: [Employee!]!
    employee(id: ID!): Employee
    searchEmployees(search: String!): [Employee!]!
}
```

**Available Operations:**

- `employees`: Retrieves all employee records.
- `employee`: Retrieves a specific employee using their ID.
- `searchEmployees`: Searches employees based on relevant information.

### 3. Mutations

Mutations are used to create, update, and delete employee records.

```graphql
type Mutation {
    addEmployee(
        name: String!
        email: String!
        department: String!
        designation: String!
        salary: Float!
        joining_date: String!
    ): Employee

    updateEmployee(
        id: ID!
        name: String!
        email: String!
        department: String!
        designation: String!
        salary: Float!
        joining_date: String!
    ): Employee

    deleteEmployee(id: ID!): Boolean!
}
```

**Available Operations:**

- `addEmployee`: Creates a new employee record.
- `updateEmployee`: Updates existing employee information.
- `deleteEmployee`: Deletes an employee using their ID.

### 4. Example GraphQL Queries

**Retrieve All Employees**

```graphql
query {
    employees {
        id
        name
        email
        department
        designation
    }
}
```

**Retrieve a Specific Employee**

```graphql
query {
    employee(id: "1") {
        name
        email
        salary
    }
}
```

**Add a New Employee**

```graphql
mutation {
    addEmployee(
        name: "Rahul Das"
        email: "rahul@example.com"
        department: "IT"
        designation: "Software Developer"
        salary: 45000.0
        joining_date: "2026-11-07"
    ) {
        id
        name
        email
    }
}
```

**Delete an Employee**

```graphql
mutation {
    deleteEmployee(id: "1")
}
```

*Note: The GraphQL schema and operations above represent the proposed API specification. A GraphQL server, resolvers, and database integration must be implemented separately before these operations become executable. The current Streamlit application uses SQLite directly.*

## 🔄 Application Modules

1. Dashboard – Displays employee statistics.
2. Add Employee – Registers new employees.
3. View Employees – Displays and searches employee records.
4. Update Employee – Modifies existing employee information.
5. Delete Employee – Removes employee records.
6. GraphQL API Specification – Defines structured queries and mutations for employee data operations.

## 🚀 Future Enhancements

- GraphQL server implementation with Python.
- GraphQL resolvers and SQLite database integration.
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

**Disha Dutta**

GitHub: https://github.com/Disha-1012

## 📄 License

This project is available for educational and learning purposes.
