from __future__ import annotations
import re
from typing import List, Optional, Union


class Dir:
    def __init__(self, name: str, parent: Optional[Dir] = None):
        self.name = name
        self.files = []
        self.parent = parent

    def __repr__(self):
        return f"Dir {self.name} ({self.get_size()})"

    def add_file(self, file: Union[File, Dir]):
        self.files.append(file)

    def get_size(self):
        return sum([x.get_size() for x in self.files])

    def get_subdirs(self):
        subdirs = []
        for x in self.files:
            if isinstance(x, Dir):
                subdirs += [x] + x.get_subdirs()
        return subdirs

    def get_parent(self):
        return self.parent

    def get_dir_by_name(self, name: str):
        return next(x for x in self.files if isinstance(x, Dir) and x.name == name)


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"File {self.name} ({self.get_size()})"

    def get_size(self):
        return self.size


def build_graph(lines: List[str]):
    root = Dir(name="/")
    wd = root
    for line in lines:
        # Change dir
        if line.startswith("$ cd"):
            [_, _, name] = line.split(" ")
            if name == "..":
                wd = wd.get_parent()
            elif name == "/":
                wd = root
            else:
                wd = wd.get_dir_by_name(name)
        # Discover a dir
        if line.startswith("dir"):
            [_, name] = line.split(" ")
            wd.add_file(Dir(name, wd))
        if re.match(r"^\d", line):
            [size, name] = line.split(" ")
            wd.add_file(File(name, int(size)))
    return root


def lvl1(dirs: List[Union[Dir, File]]):
    return sum(x.get_size() for x in dirs if x.get_size() < 100000)


def lvl2(dirs: List[Union[Dir, File]], needed_space: int):
    for dir in dirs:
        if dir.get_size() > needed_space:
            return dir.get_size()


def solve(lines):
    root = build_graph(lines)
    TOTAL_SPACE = 70000000
    MIN_SPACE = 30000000
    needed_space = MIN_SPACE - (TOTAL_SPACE - root.get_size())
    all_dirs = [root] + root.get_subdirs()
    all_dirs.sort(key=lambda x: x.get_size())
    return lvl1(all_dirs), lvl2(all_dirs, needed_space)
