Relative imports are used within packages to refer to modules relative to the location of the current module. They use a dot notation to specify the current and parent directories.
Syntax:

    Single dot (.): Refers to the current package level.
    Double dot (..): Refers to one level up in the package hierarchy.
    Triple dot (...): Refers to two levels up, and so on.
    
    # module_b.py

    # Importing module_a from the parent package
    from .. import module_a

    # Importing a specific function from module_a
    from ..module_a import some_function
    

Parent imports refers to the practice of importing modules from a parent package or higher-level module without using relative imports. 

    # module_b.py

    # Importing module_a using an absolute import
    import package.module_a

    # Importing a specific function from module_a
    from package.module_a import some_function