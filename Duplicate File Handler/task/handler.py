import os
import sys


class FileHandler:
    def __init__(self):
        self.files_path = []
        self.files_size = {}
        self.dpl_size = []

    def get_files_path(self):
        try:
            root_dir = sys.argv[1]
        except IndexError:
            print("Directory is not specified")
        else:
            for root, dirs, files in os.walk(root_dir, topdown=False):
                for name in files:
                    self.files_path.append(os.path.join(root, name))

    def get_file_size(self):
        print("Enter file format:")
        file_type = input()

        for file_path in self.files_path:
            if not file_type or os.path.splitext(file_path)[1] == file_type:
                size = os.path.getsize(file_path)
                self.files_size.setdefault(size, []).append(file_path)

        for size in self.files_size:
            if len(self.files_size[size]) > 1:
                self.dpl_size.append(size)

    def compare_file_size(self):
        print('''Size sorting options:
1. Descending
2. Ascending''')
        while True:
            print('''
Enter a sorting option:''')
            sort_option = input()
            if sort_option not in ["1", "2"]:
                print("Wrong option")
                continue
            else:
                descending = sort_option == "1"
                for size in sorted(self.dpl_size, reverse=descending):
                    print(f"{size} bytes")
                    print(*self.files_size[size], sep="\n")
                    print()
                    break


handler = FileHandler()
handler.get_files_path()
handler.get_file_size()
handler.compare_file_size()
