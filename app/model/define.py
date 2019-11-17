from app.model import db

app_user_user = db.Table(
    'app_user_user',
    db.Column('app_user_id', db.Integer, db.ForeignKey('app_user.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

favorite = db.Table(
    'favorite',
    db.Column('app_user_id', db.Integer, db.ForeignKey('app_user.id')),
    db.Column('recommend_id', db.Integer, db.ForeignKey('recommend.id'))
)

thumb = db.Table(
    'thumb',
    db.Column('app_user_id', db.Integer, db.ForeignKey('app_user.id')),
    db.Column('recommend_id', db.Integer, db.ForeignKey('recommend.id'))
)


class Recommend(db.Model):
    __tablename__ = 'recommend'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.VARCHAR(255))
    create_at = db.Column(db.DATETIME)
    delete_at = db.Column(db.DATETIME)
    user_id = db.Column(db.Integer)


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
    collects = db.relationship('Recommend', secondary=favorite, backref=db.backref('collectors', lazy=True))
    likes = db.relationship('Recommend', secondary=thumb, backref=db.backref('likes', lazy=True))


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(255))
    password = db.Column(db.VARCHAR(255))
    phone = db.Column(db.CHAR(11))
    nickname = db.Column(db.VARCHAR(20), default='nickname')
    sex = db.Column(db.Integer, default='1')
    email = db.Column(db.VARCHAR(255), default='email')
    app_users = db.relationship('AppUser', secondary=app_user_user, backref=db.backref('followers', lazy=True))


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
