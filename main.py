import module_strings

def get_number():
    import random
    return random.randint(1, 100)

def get_hello():
    return 'hello'


if __name__ == '__main__':
    print(module_strings.func())

