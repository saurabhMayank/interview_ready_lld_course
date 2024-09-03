from enum import Enum


# Enum to define database types
class DbType(Enum):
    RDS = 1
    DYNAMODB = 2
    ELASTICSEARCH = 3


# Database interface
class IDatabase:
    def save_to_database(self, user):
        raise NotImplementedError("Subclasses should implement this method")


# RDS database implementation
class UserRdsDB(IDatabase):
    def save_to_database(self, user):
        print(f"Saving {user.name} to the RDS database")


# DynamoDB implementation
class UserDynamoDB(IDatabase):
    def save_to_database(self, user):
        print(f"Saving {user.name} to the DynamoDB database")


# User model class with strategy pattern for database persistence
class UserModel:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

    def save_to_database(self, db_type: DbType):
        # Initialize appropriate database strategy based on db_type
        db_strategy = self._get_db_strategy(db_type)
        db_strategy.save_to_database(self)

    def _get_db_strategy(self, db_type: DbType) -> IDatabase:
        """Private method to get the database strategy based on db_type."""
        if db_type == DbType.RDS:
            return UserRdsDB()
        elif db_type == DbType.DYNAMODB:
            return UserDynamoDB()
        else:
            raise ValueError("Unsupported database type")


# Service class that handles user operations and decides which DB to use
class UserService:
    def __init__(self):
        pass

    def create_user(self, name: str, age: int, email: str) -> UserModel:
        """
        Function to create a User and save to the appropriate database
        """
        self.validate_user_input(name, age, email)

        # Determine which database type to use; this could be based on any logic or config
        db_type = self.determine_db_type()

        # Create user model
        user_model = UserModel(name, age, email)

        # Pass the chosen db type to the model to save the user
        user_model.save_to_database(db_type)

        return user_model

    def determine_db_type(self) -> DbType:
        """
        Logic to determine which database type to use; can be based on environment, config, etc.
        """
        # For this example, we'll just return RDS. In a real scenario, this could be more complex.
        return DbType.RDS

    def validate_user_input(self, name: str, age: int, email: str):
        if not isinstance(name, str):
            raise ValueError("User name should be a string")

        if not isinstance(age, int):
            raise ValueError("Age should be a valid integer")

        if not isinstance(email, str):
            raise ValueError("Email should be a string")
        # Additional email format validation can be added here

    def display_user(self, user: UserModel) -> None:
        print(f"Name: {user.name}, Age: {user.age}, Email: {user.email}")


# Service class to handle email operations
class EmailService:
    def send_email(self, user_email: str, message: str) -> None:
        if not isinstance(user_email, str):
            raise ValueError("Email should be a string")

        if not message:
            raise ValueError("Message is empty; pass a valid message")

        print(f"Sending email to {user_email}: {message}")


# Example usage (simulating API handler)
def user_creation_handler(name: str, age: int, email: str):
    user_service = UserService()
    user = user_service.create_user(name, age, email)
    user_service.display_user(user)

    email_service = EmailService()
    email_service.send_email(user.email, "Welcome, Alice!")


# Simulating an API call
user_creation_handler("Alice", 30, "alice@example.com")
