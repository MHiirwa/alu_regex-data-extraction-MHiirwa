Regex Data Validator
A Python tool for validating common data patterns using regular expressions.

Quick Start
Installation
bash
# Clone the repository
git clone https://github.com/yourusername/regex-validator.git
cd regex-validator
Usage
bash
# Run the validator
python regex_validator.py
Output
text
=== DATA VALIDATION EXAMPLES ===
email           user@example.com          -> VALID
email           hirwamaxiime99@gmail.com  -> VALID
email           invalid-email             -> INVALID
url             https://www.example.com   -> VALID
url             invalid-url               -> INVALID
phone           (123) 456-7890            -> VALID
phone           123-456-7890              -> VALID
credit_card     1234-5678-9012-3456       -> VALID
credit_card     1234 5678 9012            -> INVALID
How It Operates
The tool validates four types of data patterns:

Supported Data Types
Emails: user@domain.com, name@company.co.uk

URLs: https://domain.com, http://sub.domain/path

Phone Numbers: (123) 456-7890, 123-456-7890, 123.456.7890

Credit Cards: 1234-5678-9012-3456, 1234 5678 9012 3456

As a Module
python
from regex_validator import DataValidator

validator = DataValidator()
is_valid = validator.validate('email', 'test@example.com')