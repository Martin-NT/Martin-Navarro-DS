class Lado:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def __repr__(self):
        return f"Lado({self.punto1}, {self.punto2})"
