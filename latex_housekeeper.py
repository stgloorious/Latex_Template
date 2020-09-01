# latex_housekeeper.py
# Deletes all unnecessary files latex creates during the build process
#
# Original by Andrej Scheuer (gitlab.com/Hoziax)
# Slightly modified by Stefan Gloor
# September, 2020

import os


class Housekeeper:
    def __init__(self, root_dir=""):
        self.illegal_file_endings = tuple([".aux", ".fdb_latexmk", ".fls", ".log", ".gz", ".auxlock", ".toc", ".out", ".lof", ".lot", ".nav", ".snm"])
        self.num_of_deleted_files = 0
        self.root_dir = root_dir

    @classmethod
    def use_file_dir(cls):
        return cls(os.path.dirname(os.path.realpath(__file__)))

    def cleanup(self):
        for walk_root, walk_dirs, walk_files in os.walk(self.root_dir, topdown=False):
            for file_name in walk_files:
                self.__handle_file(walk_root, file_name)

    def __handle_file(self, walk_root, file_name):
        if file_name.endswith(self.illegal_file_endings):
            os.remove(os.path.join(walk_root, file_name))
            self.num_of_deleted_files += 1

housekeeper = Housekeeper.use_file_dir()

if housekeeper is not None:
    housekeeper.cleanup()
    print("Cleaned up {} files".format(housekeeper.num_of_deleted_files))
