
import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Employee Management Portal",
    page_icon="👨‍💼",
    layout="wide"
)
DB_NAME = "employees.db"

def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            department TEXT NOT NULL,
            designation TEXT NOT NULL,
            salary REAL NOT NULL,
            joining_date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def add_employee(name, email, department,
                 designation, salary, joining_date):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO employees
            (name, email, department, designation,
             salary, joining_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            name, email, department,
            designation, salary, joining_date
        ))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def get_employees():
    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM employees ORDER BY id DESC",
        conn
    )

    conn.close()
    return df


def update_employee(emp_id, name, email, department,
                    designation, salary, joining_date):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE employees
            SET name=?, email=?, department=?,
                designation=?, salary=?, joining_date=?
            WHERE id=?
        """, (
            name, email, department,
            designation, salary, joining_date, emp_id
        ))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def delete_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id=?",
        (emp_id,)
    )

    conn.commit()
    conn.close()

create_table()


st.sidebar.title("👨‍💼 Employee Portal")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Employee",
        "View Employees",
        "Update Employee",
        "Delete Employee"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Employee Management Portal v1.0")


if menu == "Dashboard":

    st.title("📊 Employee Management Dashboard")

    st.write("Welcome to the Employee Management Portal.")

    employees = get_employees()

    total_employees = len(employees)

    total_departments = (
        employees["department"].nunique()
        if not employees.empty else 0
    )

    average_salary = (
        employees["salary"].mean()
        if not employees.empty else 0
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Employees", total_employees)
    col2.metric("Departments", total_departments)
    col3.metric("Average Salary", f"₹{average_salary:,.2f}")

    st.markdown("---")

    st.subheader("Recent Employees")

    if not employees.empty:
        st.dataframe(
            employees.head(5),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No employee records available.")

elif menu == "Add Employee":

    st.title("➕ Add New Employee")

    with st.form("add_employee_form"):

        name = st.text_input("Employee Name")
        email = st.text_input("Email Address")

        department = st.selectbox(
            "Department",
            [
                "IT",
                "HR",
                "Finance",
                "Marketing",
                "Sales",
                "Operations"
            ]
        )

        designation = st.text_input("Designation")

        salary = st.number_input(
            "Salary (₹)",
            min_value=0.0,
            step=1000.0
        )

        joining_date = st.date_input("Joining Date")

        submit = st.form_submit_button("Add Employee")

        if submit:

            if not name.strip() or not email.strip() or not designation.strip():
                st.error("Please fill in all required fields.")

            elif "@" not in email or "." not in email:
                st.error("Please enter a valid email address.")

            elif salary <= 0:
                st.error("Salary must be greater than zero.")

            else:
                result = add_employee(
                    name.strip(),
                    email.strip(),
                    department,
                    designation.strip(),
                    salary,
                    str(joining_date)
                )

                if result:
                    st.success("Employee added successfully!")
                else:
                    st.error("An employee with this email already exists.")


elif menu == "View Employees":

    st.title("👥 Employee Records")

    employees = get_employees()

    if not employees.empty:

        search = st.text_input("Search by name, email or department")

        if search:
            mask = employees.astype(str).apply(
                lambda col: col.str.contains(
                    search, case=False, na=False
                )
            ).any(axis=1)

            employees = employees[mask]

        st.write(f"Total Records: {len(employees)}")

        st.dataframe(
            employees,
            use_container_width=True,
            hide_index=True
        )

        csv = employees.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Employee Records",
            data=csv,
            file_name="employee_records.csv",
            mime="text/csv"
        )

    else:
        st.info("No employee records found.")


elif menu == "Update Employee":

    st.title("✏️ Update Employee Details")

    employees = get_employees()

    if not employees.empty:

        emp_id = st.selectbox(
            "Select Employee ID",
            employees["id"].tolist()
        )

        employee = employees[
            employees["id"] == emp_id
        ].iloc[0]

        with st.form("update_employee_form"):

            name = st.text_input(
                "Employee Name",
                value=employee["name"]
            )

            email = st.text_input(
                "Email Address",
                value=employee["email"]
            )

            departments = [
                "IT", "HR", "Finance",
                "Marketing", "Sales", "Operations"
            ]

            current_department = employee["department"]

            department_options = departments.copy()

            if current_department not in department_options:
                department_options.append(current_department)

            department = st.selectbox(
                "Department",
                department_options,
                index=department_options.index(current_department)
            )

            designation = st.text_input(
                "Designation",
                value=employee["designation"]
            )

            salary = st.number_input(
                "Salary (₹)",
                min_value=0.0,
                value=float(employee["salary"])
            )

            joining_date = st.date_input(
                "Joining Date",
                value=pd.to_datetime(employee["joining_date"]).date()
            )

            submit = st.form_submit_button("Update Employee")

            if submit:

                if not name.strip() or not email.strip() or not designation.strip():
                    st.error("Please fill in all required fields.")

                elif "@" not in email or "." not in email:
                    st.error("Please enter a valid email address.")

                elif salary <= 0:
                    st.error("Salary must be greater than zero.")

                else:
                    result = update_employee(
                        emp_id,
                        name.strip(),
                        email.strip(),
                        department,
                        designation.strip(),
                        salary,
                        str(joining_date)
                    )

                    if result:
                        st.success("Employee details updated successfully!")
                    else:
                        st.error("This email address is already assigned to another employee.")

    else:
        st.info("No employees available to update.")


elif menu == "Delete Employee":

    st.title("🗑️ Delete Employee")

    employees = get_employees()

    if not employees.empty:

        emp_id = st.selectbox(
            "Select Employee ID to Delete",
            employees["id"].tolist()
        )

        employee = employees[
            employees["id"] == emp_id
        ].iloc[0]

        st.warning(
            f"You are about to delete: {employee['name']}"
        )

        if st.button("Delete Employee", type="primary"):

            delete_employee(emp_id)

            st.success("Employee deleted successfully!")

            st.rerun()

    else:
        st.info("No employee records available to delete.")


st.markdown("---")

st.markdown(
    "<center>© 2026 Employee Management Portal | "
    "Developed using Python and Streamlit</center>",
    unsafe_allow_html=True
)
