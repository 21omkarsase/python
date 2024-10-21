class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.var = 'var1'
    
    
   
singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton.var)
print(new_singleton.var)

singleton.var = 'var 22222'
 
print(singleton is new_singleton)
 

print(singleton.var)
print(new_singleton.var)
 
 
singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)
