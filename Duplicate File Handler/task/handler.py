import os
import sys


try:
    root_dir = sys.argv[1]
except IndexError:
    print("Directory is not specified")
else:
    for root, dirs, files in os.walk(root_dir, topdown=True):
        for name in files:
            print(os.path.join(root, name))
