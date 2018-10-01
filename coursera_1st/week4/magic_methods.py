import os
import uuid
import tempfile

class File:
    def __init__(self, filename):
        self.path = filename
        self.pos = 0

    def read(self):
        with open(self.path, "r") as f:
            return f.read()

    def write(self, text):
        with open(self.path, "w") as f:
            return f.write(text)

    def __add__(self, other):
        new_path = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
        new_file = type(self)(new_path)
        new_file.write(self.read() + other.read())
        return new_file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.pos)
            row = f.readline()
            if not row:
                self.pos = 0
                raise StopIteration('EOF')

            self.pos = f.tell()
        return row

    def __str__(self):
        return self.path


first = File('/home/clara/jupyter/python_course/coursera_1st/1.txt')
second = File('/home/clara/jupyter/python_course/coursera_1st/2.txt')
new_obj = first + second

for i in first:
    print(i)

print(first)
