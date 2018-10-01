class FileReader(object):
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            self.file = open(self.path, 'r')
            return self.file.read()
        except IOError:
            return ""


reader = FileReader("/home/clara/dump/detect/lfw_result_20180926-072604.txt")
print(reader.read())
