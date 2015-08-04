a_var = 'global value'
 
def a_func():
    a_var = 'local value'
    print(a_var, '[ a_var inside a_func() ]')
 
a_func()
print(a_var, '[ a_var outside a_func() ]')

 
def a_func1():
    global a_var
    a_var = 'local value'
    print(a_var, '[ a_var inside a_func1() ]')
 
print(a_var, '[ a_var outside a_func1() ]')
a_func1()
print(a_var, '[ a_var outside a_func1() ]')


a_var = 'global value'
 
def outer():
    a_var = 'enclosed value'
 
    def inner():
        a_var = 'local value'
        print(a_var)
 
    inner()
 
outer()