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

tag_recommemd = db.Table(
    'tag_recommend',
    db.Column('tag_id', db.Integer, db.ForeignKey('second_tag.id')),
    db.Column('recommend_id', db.Integer, db.ForeignKey('recommend.id'))
)


class Recommend(db.Model):
    __tablename__ = 'recommend'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.VARCHAR(255))
    create_at = db.Column(db.DATETIME)
    delete_at = db.Column(db.DATETIME)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    imgs = db.relationship('Img', backref=db.backref('recommend'))


class AppUser(db.Model):
    __tablename__ = 'app_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(20))
    password = db.Column(db.VARCHAR(255))
    phone = db.Column(db.CHAR(11))
    nickname = db.Column(db.VARCHAR(20), default='nickname')
    sex = db.Column(db.Integer, default='1')
    email = db.Column(db.VARCHAR(255), default='email')
    avatar = db.relationship('AppAvatar', backref=db.backref('avatars'), lazy=True)
    collects = db.relationship('Recommend', secondary=favorite, backref=db.backref('collectors', lazy=True))
    likes = db.relationship('Recommend', secondary=thumb, backref=db.backref('likers', lazy=True))


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
    recommends = db.relationship('Recommend', backref=db.backref('who', lazy=True))
    avatar = db.relationship('Avatar', backref=db.backref('belong', lazy=True))



class AppUserColor(db.Model):
    __tablebame__ = 'app_user_color'
    app_user_id = db.Column(db.Integer, primary_key=True)
    color_id = db.Column(db.Integer)


class Img(db.Model):
    __tablename__ = 'img'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255))
    type = db.Column(db.CHAR)
    create_at = db.Column(db.DATETIME)
    delete_at = db.Column(db.DATETIME)
    recommend_id = db.Column(db.Integer, db.ForeignKey('recommend.id'))


color_tag = db.Table(
    'color_tag',
    db.Column('color_id', db.Integer, db.ForeignKey('color.id')),
    db.Column('second_id', db.Integer, db.ForeignKey('second_tag.id'))
)


class Color(db.Model):
    __tablename__ = 'color'
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.VARCHAR(255))
    second_tag = db.relationship('SecondTag', secondary=color_tag, backref=db.backref('colors', lazy=True))


class SecondTag(db.Model):
    __tablename__ = 'second_tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255))
    recommends = db.relationship('Recommend', secondary=tag_recommemd, backref=db.backref('tags', lazy=True))


class Notice(db.Model):
    __tablename__ = 'notice'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.VARCHAR(255))
    type = db.Column(db.Integer)
    create_at = db.Column(db.DATETIME)


class AppAvatar(db.Model):
    __tablename__ = 'app_avatar'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255))
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('app_user.id'), nullable=False)


class Avatar(db.Model):
    __tablename__ = 'avatar'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255))
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
