import os, shutil, sys

#DOESNT WORK YET

if 'clean' in sys.argv:
    shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'build'))
    shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dist'))
    shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'main.spec'))

else:
    os.system('pyinstaller -F src/main.py')
