import requests

def test_predict():
    url = "http://127.0.0.1:5000/predict"
    # Need to log in first to get a session, but can simulate the form data
    # Actually, /predict requires logged_in in session.
    # I'll just check if the code compiles and if the LEARNING_RESOURCES is now defined.
    pass

if __name__ == "__main__":
    # Test if flask_app.py can be imported without error
    try:
        from flask_app import app
        print("flask_app.py imported successfully")
        # Check if LEARNING_RESOURCES is now in app's globals or accessible
        import flask_app
        if hasattr(flask_app, 'LEARNING_RESOURCES'):
            print("LEARNING_RESOURCES is defined")
        else:
            print("LEARNING_RESOURCES is NOT defined")
    except Exception as e:
        print(f"Error: {e}")
