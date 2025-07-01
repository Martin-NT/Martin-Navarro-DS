class AutoDirector:
    def __init__(self):
        self.auto_builder = None

    def set_auto_builder(self, auto_builder):
        self.auto_builder = auto_builder

    def build(self):
        self.auto_builder.buid_marca()
        self.auto_builder.buid_modelo()
        self.auto_builder.buid_motor()
        self.auto_builder.build_puertas()
    
    def get_auto(self):
        return self.auto_builder.get_auto()