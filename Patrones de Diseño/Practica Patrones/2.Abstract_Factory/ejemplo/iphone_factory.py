from factory import Factory
from iphone import Iphone
from iphone_charger import Iphone_Charger

class Iphone_Factory(Factory):
    def create_phone(self):
        return Iphone()
    
    def create_charger(self):
        return Iphone_Charger()