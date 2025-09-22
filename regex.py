import re

class DataValidator:
    """
    A data validator using regular expressions
    """
    
    def __init__(self):
        # Regular expression patterns for validation
        self.validation_patterns = {
            'email': re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),
            'url': re.compile(r'^(https?://)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(/[^\s]*)?$'),
            'phone': re.compile(r'^(\()?\d{3}(\))?[-.\s]?\d{3}[-.\s]?\d{4}$'),
            'credit_card': re.compile(r'^\d{4}[-.\s]?\d{4}[-.\s]?\d{4}[-.\s]?\d{4}$')
        }

    def validate(self, data_type: str, value: str) -> bool:
        """
        Validate a single value against a specific data type pattern
        """
        if data_type not in self.validation_patterns:
            raise ValueError(f"Unknown data type: {data_type}")
        
        pattern = self.validation_patterns[data_type]
        return bool(pattern.match(value.strip()))

def main():
    # Initialize the validator
    validator = DataValidator()
    
    print("=== DATA VALIDATION EXAMPLES ===")
    
    # Test validation - exactly matching your desired output
    test_cases = [
        ('email', 'user@example.com'),
        ('email', 'hirwamaxiime99@gmail.com'),
        ('email', 'invalid-email'),
        ('url', 'https://www.example.com'),
        ('url', 'invalid-url'),
        ('phone', '(123) 456-7890'),
        ('phone', '123-456-7890'),
        ('credit_card', '1234-5678-9012-3456'),
        ('credit_card', '1234 5678 9012'),
    ]
    
    for data_type, value in test_cases:
        is_valid = validator.validate(data_type, value)
        print(f"{data_type:15} {value:25} -> {'VALID' if is_valid else 'INVALID'}")

if __name__ == "__main__":
    main()
    