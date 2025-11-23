import json
import os

DB_FILE = "employees.json"

# --------------------------
# Utility Functions
# --------------------------

def load_db():
    """Load the employee JSON database. Create a new one if missing."""
    pass

def save_db(data):
    """Save the full employee database."""
    pass


# --------------------------
# Employee CRUD Operations
# --------------------------

def add_employee(employee_obj):
    """Add a new employee. Expects a dict."""
    pass

def get_employee(emp_id):
    """Return employee record by ID."""
    pass

def update_employee(emp_id, updates):
    """Update fields on an employee record."""
    pass

def delete_employee(emp_id):
    """Delete an employee by ID."""
    pass

def list_employees():
    """Return all employee records."""
    pass
