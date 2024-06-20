import os 

cwd = os.getcwd()

os.chdir('O:\My Space') # change dir
# print(os.getcwd())      # curr working dir

# print(os.listdir()) # list of all  listdir(path = optional)


# create directory
# os.makedirs('programming/python/temp_dir/temp/temp')

# deleting directories 
# os.rmdir('programming/python/temp_dir/temp/temp')
# os.removedirs('programming/python/temp_dir')

# import shutil
# shutil.rmtree('programming/python/temp_dir') # delete all nested files and folders

os.chdir('programming/python')

# rename file
# os.rename('python/temp.txt', 'python/temp.py')

# for dirpath, dirnames, filenames in os.walk('programming'):
    # print('dirpath', dirpath)
    # print('dirnames', dirnames)
    # print('filenames', filenames)
    

print(os.environ.get('ALLUSERSPROFILE'))