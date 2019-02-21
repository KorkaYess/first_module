def decorator(func):

    def wrapper():
        print('before call')
        func()
        print('after call')

    return wrapper

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
 
def makeitalic(fn):
    def wrapped():
        return fn.capitalize() + fn() + "</i>"
    return wrapped
 
@makebold
@makeitalic
def hello():
    return "hello habr"
 
print(hello()) ## выведет <b><i>hello habr</i></b>