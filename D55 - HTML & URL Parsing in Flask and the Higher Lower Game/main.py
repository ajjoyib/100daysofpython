class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(func):
    def wrapper_func(*args):
        if args[0].is_logged_in:
            func(args[0])

    return wrapper_func


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("hamidullo")
new_user.is_logged_in = True
create_blog_post(new_user)
