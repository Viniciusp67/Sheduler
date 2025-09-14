class Process:
    def __init__(self, id, name, priority, necessary_cycles, necessary_resource=None):
        self.id = id
        self.name = name
        self.priority = priority
        self.necessary_cycles = necessary_cycles
        self.necessary_resource = necessary_resource
        self.blocked = False

    def __repr__(self):
        return f"[{self.id}] {self.name} (P{self.priority}) - Cycles: {self.necessary_cycles}"