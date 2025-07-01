
from iphone_factory import Iphone_Factory

factory = Iphone_Factory()
phone = factory.create_phone()
phone_charger = factory.create_charger()

print(phone.get_type())
print(phone_charger.get_type())
