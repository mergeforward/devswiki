from store.database import Store

class User(Store):
  pass

class Post(Store):
  pass


user = User('sqlite')
post = User('sqlite')

def add_user(username, password):
    user[username] = password
    return username

def validate(username='anonymous', password='dangerous'):
    print(user[username])
    return user[username] and user[username].value == password


def add_post(title, content, username='anonymous', password='dangerous'):
    valid = validate(username, password)
    if valid:
        return post.add({
            'title': title,
            'content': content,
            'user': username
        })
    else:
        print('invalid')

def query_post_by_user(username):
    return post[f'user={username}']

if __name__ == "__main__":
    add_user('admin', 'admin')
    add_post('这是一篇入门教程', '1. docker 简介\n2. docker 架构\n3. docker 命令基础\n...', 'admin', 'admin')
    posts = query_post_by_user('admin')
    print(posts)





