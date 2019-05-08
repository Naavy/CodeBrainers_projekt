from . import app, db_wrapper
from .models import User, Role, UserRoles


@app.cli.command()
def create_db():
    """Create a database."""
    print("Tworzenie bazy danych...")
    db_wrapper.database.create_tables([User, Role, UserRoles])

    print("Dodawanie użytkowników...")
    users = (
        ('test@test.com', 'haslo'),
        ('admin@example.org', 'admin'),
    )
    for email, password in users:
        User(email=email, password=password).save()
