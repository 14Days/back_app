from app.model import db


class AppUser(db.Model):
    __tablename__ = 'app_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(20))
    password = db.Column(db.VARCHAR(255))
    phone = db.Column(db.CHAR(11))
    nickname = db.Column(db.VARCHAR(20), default='nickname')
    sex = db.Column(db.Integer, default='1')
    email = db.Column(db.VARCHAR(255), default='email')
    avatar = db.Column(db.VARCHAR(255), default='avatar')


class AppUserColor(db.Model):
    __tablebame__ = 'app_user_color'
    app_user_id = db.Column(db.Integer, primary_key=True)
    color_id = db.Column(db.Integer)


class Color(db.Model):
    __tablename__ = 'color'
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.VARCHAR(255))


class Notice(db.Model):
    __tablename__ = 'notice'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.VARCHAR(255))
    type = db.Column(db.Integer)
    create_at = db.Column(db.DATETIME)


