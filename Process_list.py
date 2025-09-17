class No:
    def __init__(self, process):
        self.process = process
        self.current = None

class ProcessList:
    def __init__(self):
        self.start = None
        self.end = None

    def insert_end(self, process):
        new = No(process)
        if not self.start:
            self.start = self.end = new
        else:
            self.end.current = new
            self.end = new

    def remove_start(self):
        if not self.start:
            return None
        process = self.start.process
        self.start = self.start.current
        if not self.start:
            self.end = None
        return process

    def empty(self):
        return self.start is None

    def display_names(self):
        names = []
        current = self.start
        while current:
            names.append(str(current.process))
            current = current.current
        return " -> ".join(names) if names else "empty"