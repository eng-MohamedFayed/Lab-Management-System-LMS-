# Lab Management System (LMS)

Welcome to the Lab Management System (LMS) project. This system is designed to manage lab resources, student reports, maintenance requests, and user management.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
- Python 3.x
- Oracle Database
- cx_Oracle module

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Lab-Management-System.git
   cd Lab-Management-System
   ```
    Install the required Python packages:

   ```bash

    pip install -r requirements.txt
   ```
    Set up the Oracle database:
        Install Oracle Database.
        Create a user LMS with password 123.
        Run the provided SQL script in the sql/ directory to set up the database schema and populate initial data.

    Update the database connection settings in the config/config.py file if needed.

### Usage

    Run the CLI script to interact with the LMS:

    bash

    python cli/CLI.py

    Follow the prompts in the CLI to login and navigate through the menu options.

### project-structure
```graphql
Lab-Management-System/
├── cli/
│   ├── CLI.py                # Command-line interface script
│   └── __init__.py           # Init file for the cli package
├── config/
│   ├── config.py             # Configuration file for database settings
│   └── __init__.py           # Init file for the config package
├── database/
│   ├── connection.py         # Database connection handling
│   └── __init__.py           # Init file for the database package
├── sql/
│   ├── create_tables.sql     # SQL script to create tables and insert data
│   └── README.md             # Description of SQL scripts
├── docs/
│   ├── Important Diagrams/
│   │   ├── ERD/
│   │   ├── DFD/
│   │   ├── SCHEMA/
└── requirements.txt          # Python dependencies
```

Features

    User Authentication: Secure login for different user types (admin, student, etc.).
    Lab Reports: Generate and view lab reports.
    Student Reports: Manage and view student reports.
    Maintenance Requests: Create and manage maintenance requests.
    User Management: Add and remove users from the system.

Contributing

Contributions are welcome! Please follow these steps:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes.
    Commit your changes (git commit -m 'Add some feature').
    Push to the branch (git push origin feature-branch).
    Open a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.
