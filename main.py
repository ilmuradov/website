from app import app, db
from app.models import User, Head, Body, Footer

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Head':Head, 'Body':Body, 'Footer':Footer} 
