from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()
DEFAULT_IMAGE_URL = 'https://tse2.mm.bing.net/th?id=OIP.pwTChrJBhUgphNJ8DlLg3QHaH7&pid=Api&P=0&h=180'




class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    post = db.relationship('Post')

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"



class Post(db.Model):
    """Post model class"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User')

    post_tags = db.relationship('PostTag', backref='post')
    tags = db.relationship('Tag', secondary='post_tags', backref='posts')




class Tag(db.Model):
    """Tag model class"""

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    post_tags = db.relationship('PostTag', backref='tag')
    posts = db.relationship('Post', secondary='post_tags', backref='tags')


class PostTag(db.Model):
    """PostTag model class"""

    __tablename__ = "post_tags"

    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), primary_key=True)




def connect_db(app):
    db.app = app
    db.init_app(app)