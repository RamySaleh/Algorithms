from Helpers import profiler as prof
from General.Stack import stack
import os

class Solution:

    def __init__(self):
        self.stack_folders = stack()

    def search(self, folder):
        files = os.listdir(folder)
        for file_name in files:
            full_path = os.path.join(folder, file_name)
            if os.path.isfile(full_path):
                print(full_path)
            else:
                self.search(full_path)

    # get each folder and its files
    def search2(self, folder):
        files = os.listdir(folder)
        files_list = []

        for file_name in files:
            full_path = os.path.join(folder, file_name)
            if os.path.isfile(full_path):
                files_list.append(full_path)
            else:
                self.search2(full_path)

        self.stack_folders.push((folder , files_list))

        return self.stack_folders

    # each folder then its content
    def search3(self, folder):
        files = os.listdir(folder)
        folders = []
        print()
        print(folder)
        for file_name in files:
            full_path = os.path.join(folder, file_name)
            print(full_path)
            if os.path.isdir(full_path):
                folders.append(full_path)

        for folder in folders:
            self.search3(folder)


def run1(parms):
    res = Solution().search(parms[0])

def run2(parms):
    res = Solution().search2(parms[0])
    while not res.is_empty():
        folder_node = res.pop().value
        folder = folder_node[0]
        print()
        print(folder)
        for file in folder_node[1]:
            print(file)

def run3(parms):
    res = Solution().search3(parms[0])

input = "/Users/ramy.saleh/Downloads/test"

prof.profile(run3, input)