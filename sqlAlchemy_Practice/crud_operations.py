from database import session
from models import User, Post
 
#Create a new user
new_user = User(name='John Doe', email='john@example.com')
session.add(new_user)
session.commit()
 
#create users number 2
new_user_2 = User(name='Jacob Gimachombe', email='jacob@example.com')
session.add(new_user_2)
session.commit()

# Create a new post
new_post = Post(title='First Post', content='This is my first post.', author=new_user_2)
session.add(new_post)
session.commit() # commit method saves the changes to the database

#create a second post
new_post = Post(title='Second Post', content='This is my second post.', author=new_user_2)
session.add(new_post)
session.commit()


# Read users and their posts
# query method is used to retrieve data from the database.
users = session.query(User).all() 
for user in users:
    print(user)
    for post in user.posts:
        print(post)
 
# Update a user
user_to_update = session.query(User).filter_by(name='John Doe').first()
user_to_update.email = 'john.doe@example.com'
session.commit()
 
# Delete a post
post_to_delete = session.query(Post).filter_by(title='First Post').first()
session.delete(post_to_delete)
session.commit()

