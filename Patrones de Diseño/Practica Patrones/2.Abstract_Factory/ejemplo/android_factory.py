from factory import Factory
from Android import Android
from android_charger import Android_Charger


class Android_Factory(Factory):
    def create_phone(self):
        return Android()
    
    def create_charger(self):
        return Android_Charger()