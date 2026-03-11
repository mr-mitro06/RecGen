import traceback
from app import create_app, db

try:
    print("Creating app...")
    app = create_app()
    with app.app_context():
        print("Creating all tables...")
        db.create_all()
        print("Success!")
except Exception as e:
    print("Error occurred:")
    traceback.print_exc()
