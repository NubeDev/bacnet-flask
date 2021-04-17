import time

from bacpypes.basetypes import ServicesSupported

import BAC0

from src.bacnet_master.interfaces.device_supported_services import SupportedServices

bacnet = BAC0.lite()

# Write null @ 16
address = '192.168.15.196'
object_type = 'device'
object_instance = "1234"

read_vals = f'{address} {object_type} {object_instance} 97'

aaa = SupportedServices.get(address, object_type, object_instance)
print(aaa)
#
ss = bacnet.read(read_vals)
print(ss)
print(SupportedServices.check(ss))
# print(aaaa)

# for x in range(len(ss)):
#     print(22222)
#     print(x)
# # def get_key(val):
#     for key, value in types.items():
#         if val == value:
#             return key
#
#     return "key doesn't exist"
#
#
# readProperty = get_key(14)
# print(aa)