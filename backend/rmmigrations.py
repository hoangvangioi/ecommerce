import os

directories = ['book', 'category', 'clothes', 'common', 'mobile', 'payment', 'search']


for directory in directories:
    migrations_dir = os.path.join(directory, 'migrations')

    if os.path.exists(migrations_dir) and os.path.isdir(migrations_dir):
        for filename in os.listdir(migrations_dir):
            file_path = os.path.join(migrations_dir, filename)
    
            if os.path.isfile(file_path) and filename != '__init__.py':
                os.remove(file_path)
            elif os.path.isdir(file_path):
                for subfile in os.listdir(file_path):
                    subfile_path = os.path.join(file_path, subfile)
                    os.remove(subfile_path)
                os.rmdir(file_path)
