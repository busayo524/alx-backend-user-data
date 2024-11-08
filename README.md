# Personal Data Management and Security

## Overview
This project covers fundamental techniques in handling, obfuscating, and securing personal data in a backend environment. It includes concepts such as Personally Identifiable Information (PII), logging and filtering sensitive information, password hashing, and secure database connections.

## Learning Objectives
- Identify PII and understand its importance in data privacy.
- Implement logging filters to obfuscate PII fields in logs.
- Encrypt and validate passwords securely.
- Connect to databases securely using environment variables.

## Requirements
- **Environment**: Ubuntu 18.04 LTS, Python 3.7
- **Style Guide**: pycodestyle (v2.5)
- **Execution**: All scripts should be executable, and Python files should start with `#!/usr/bin/env python3`.

## Project Structure
- `filtered_logger.py`: Handles logging, filtering, and obfuscation of sensitive fields.
- `encrypt_password.py`: Manages password hashing and validation.
- `main.py`: Example script demonstrating the use of functions from `filtered_logger.py` and `encrypt_password.py`.

## Tasks

### Task 0: Regex-ing
Write a `filter_datum` function to obfuscate specified fields in log messages.

### Task 1: Log Formatter
Create a `RedactingFormatter` class to obfuscate specified fields in log messages using the `filter_datum` function.

### Task 2: Create Logger
Implement a `get_logger` function that sets up a logger with `RedactingFormatter` to filter sensitive fields defined in `PII_FIELDS`.

### Task 3: Connect to Secure Database
Develop a `get_db` function to securely connect to a database using credentials from environment variables.

### Task 4: Read and Filter Data
Implement a `main` function to retrieve and display user data with PII fields filtered from log output.

### Task 5: Encrypting Passwords
Write a `hash_password` function to hash user passwords securely with the bcrypt library.

### Task 6: Check Valid Password
Create an `is_valid` function to validate passwords by comparing them against hashed values.

## Usage
Run `main.py` to see examples of each function in action.

## Author
Olowookere Busayomi

