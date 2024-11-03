class FileInputStream:
    def __init__(self):
        self.file = None  
        self.position = 0
    
    def read(self):
        if self.file.end_of_file() is True:  
            return -1
        else:
            self.position += 1  
            return self.read_number(self.position)
            
    def read_number(self, position):
        # some complicated logic
        pass  # Using pass as placeholder for the implementation

class EndlessFileInputStream(FileInputStream):
    def read(self):
        if self.file.end_of_file() is True:
            self.position = 0
        else:
            self.position += 1
            return self.read_number(self.position)
