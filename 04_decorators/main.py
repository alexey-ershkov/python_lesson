def decorator(function):
    def wrapper(*args, **kwargs):
        print('Before call')
        function(*args, **kwargs)
        print('After call')

    return wrapper


@decorator
def say_hi(name: str):
    print('Hi ' + name)


if __name__ == '__main__':
    say_hi('Alex')
