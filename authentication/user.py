from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from flask_login import login_user, logout_user


# Register class 


class UserClass:
    
    def register(self, fname, lname, email, password):
        user = User(first_name=fname,last_name=lname,email=email,password=generate_password_hash(password, method='sha256'))
        db.session.add(user)
        db.session.commit()
        return True


    def sing_in(self, email, password):
        try:
            user = User.query.filter_by(email=email).first()
            check_password_hash(user.password ,password)
            login_user(user)
            return user
        except not user and not check_password_hash(user.password, password):
            return None


    def sing_out(self):
        logout_user()
        return True


