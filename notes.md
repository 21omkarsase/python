Python Literals
    1. In Python, literals are data values that are directly specified in the code without computation.
    Numeric Literals
        a = 42
        b = 3.14
        c = 2.7e5  # 2.7 x 10^5
    String Literals
        s1 = 'Hello, World!'
        s3 = '''This is a multi-line
        string.'''
        s4 = """He said, "Python is awesome!" """

Operators
    1. Arithmetic
    2. Comparison
    3. Assignment
    4. Logical
    5. Bitwise
    6. Membership
    7. Identity
    
Python Membership Operators
    determine whether an item is present in a given container type object
    e.g in, not in

Python Identity Operator
    The 'is' operator evaluates to True if both the operand objects share the same memory location. 
    e.g is
    
    for mutable objects it compares memory location
    for immutable it compares actual values (similar for int, boolean, none)

Python - Match-Case Statement
    def weekday(n):
        match n:
            case 0: return "Monday"
            case 1: return "Tuesday"
            case 2: return "Wednesday"
            case 3: return "Thursday"
            case 4: return "Friday"
            case 5: return "Saturday"
            case 6: return "Sunday"
            case _: return "Invalid day number"
        print (weekday(3))
        print (weekday(6))
        print (weekday(7))

Positional vs Keyword Argument

Arbitrary Arguments (*args)
    def avg(first, *rest):
        second=max(rest)
        return (first+second)/2
        
    result=avg(40,30,50,25)

Arbitrary Keyword Arguments (**kwargs)
    def percent(math, sci, **optional):
        print ("maths:", math)
        print ("sci:", sci)
        print(optional)

    result=percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)

String Formatting
    from string import Template
    template = Template("Hello, $name. You are $age years old.")
    message = template.substitute(name=name, age=age)
    
    message = "Hello, {}. You are {} years old.".format(name, age)
    
    message = "Hello, %s. You are %d years old." % (name, age)
    
    message = f"Hello, {name}. You are {age} years old."

List
    l = ['abc', 'xyz', 1, 2, 3]
    del[1]
    l = ['abc', 1, 2, 3]

Dict
    my_dict = {'name' : 'omkar', 'age' : 22}
    
    del my_dict['name]
    my_dict.pop('name')
    my_dict.popitem()
    
    
Property Decorators
    In Python, property decorators are a built-in mechanism for creating attributes (properties) within a class that function like regular attributes but can have controlled access.

Abstract Classes
    In Python, abstract classes are used to create blueprints for other classes (subclasses) to inherit from. 
    They define a set of methods that must be implemented by the subclasses, 
    but they themselves cannot be instantiated directly. 

Encapsulation
    Encapsulation in Python refers to the concept of bundling data (attributes) and methods (functions that operate on that data) together within a single unit called a class
    
    It's a fundamental principle of object-oriented programming (OOP) that promotes data hiding and controlled access.
    
    Data Protection:
    Improved Maintainability:
    Modular Design:

Inheritance
    It allows you to create new classes (subclasses) based on existing classes (parent classes). 
    
    Code Reusability:
    Polymorphism: 
    Code Organization: 
    
    MRO
    
    
Abstraction
    Abstraction in Python is a fundamental concept in object-oriented programming (OOP) that focuses on hiding implementation details and exposing essential functionalities to the user. It allows you to create reusable and maintainable code by separating concerns.
    
    Data Abstraction: 
    Improved Code Maintainability:
    Increased Code Reusability: 
    
    
Iterator
    An iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
    
    The Python iterators object is initialized using the iter() method. It uses the next() method for iteration.
    
    __iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object
    __next__(): The next method returns the next value for the iterable. 
    
    When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object, which further uses the next() method to iterate over. This method raises a StopIteration to signal the end of the iteration.
    
    Advantages :
    1. Memory Efficiency: (on the fly)
    2. Lazy Evaluation: (computing only when deeded)
    3. Support for Infinite Sequences:
    4. Encapsulation: (encapsulating logic using custom iterator)
    
    Disadvantages :
    1. Complexity:
    2. Error Handling:
    
    Processing Large Datasets
    Use Case: Analyzing Log Files

Generator
    A Generator in Python is a function that returns an iterator using the Yield keyword. 
    
    A generator function in Python is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
    
    If the body of a def contains yield, the function automatically becomes a Python generator function. 
    
    Advantages : 
    1. Efficient Memory Usage:
    2. Improved Performance:
    3. Simpler Code:
    4. Support for Infinite Sequences:
    
    
    use:
    1. Processing Files Line by Line
    Use Case: Large Log Files
    
    Handling Pagination in APIs
    Use Case: API Pagination



Decorators 
    Decorators in Python are a powerful and versatile feature that allows you to modify the behavior of functions or classes without explicitly changing their code. 
    
    Decorators are widely used for adding functionalities such as logging, caching, authentication.
    
    Advantages : 
    1. Code Reusability and Modularity:
    2. Promotes DRY Principle (Don't Repeat Yourself):
    3. extends fun behaviour
    4. without changing main fun
    
    caching decorators
    logging decorators
    authentication decorators
    
    authenticated_users = ["alice", "bob", "charlie"]

    def authenticate(func):
        def wrapper(username, *args, **kwargs):
            if username in authenticated_users:
                return func(username, *args, **kwargs)
            else:
                raise PermissionError(f"User '{username}' is not authenticated to access '{func.__name__}'.")
        return wrapper
    
    @authenticate
    def view_sensitive_data(username):
        return f"Sensitive data view for user '{username}'."
    
    res = view_sensitive_data('omkar')


Threading
    
    Multithreading in Python refers to the concurrent execution of multiple threads within the same process. A thread is a lightweight sub-process that can be independently scheduled to run tasks. 


Middlewares in django
    
    Middleware is a series of processing layers present between the web server and the view
    
    middleware is a framework that provides a method to process requests and responses globally before they are processed by the view
    
    Middleware components are designed so that they remain between the web server and the view, allowing us to perform various operations on requests and responses as they pass through the Django application and web browser.
    
    
    Request Phase: 
    The request is received by the server and then it passes through each middleware component. If a response is returned from a middleware process_request, further processing is stopped.
    
    View Processing: 
    When a request reaches the view, it processes it and generates a response according to the code written inside the view function.
    
    Response Phase: 
    When Response passes through each middleware component in reverse order. Modified response from each middleware is passed to the next one. A modified response is sent back to the web server and then to the user.
    
    
    # myapp/middleware.py

    import logging

    # Get an instance of a logger
    logger = logging.getLogger(__name__)

    class RequestResponseLoggingMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            # Log when the request is received
            logger.info("req received")

            response = self.get_response(request)

            # Log when the response is sent
            logger.info("res sent")

            return response



Authentication Types

1. Token-Based Authentication    -  Common Implementation: JWT (JSON Web Token)
2. OAuth 2.0                     -  Social logins, API access.
3. Session-Based Authentication  -  Common Frameworks: Django, Flask.
                                    Description: Uses server-side sessions to store user information after login.


Django Request - Response Life Cycle
1. Request initialization (web browser or mobile app)
2. wsgi server passes request to django application
3. request passed through middlewares
4. url routing to view
5. view processing
6. response generated and sent back to the middlewares
7. wsgi server receives the response
8. web server receives the response