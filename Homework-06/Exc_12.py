"""
Example:

import base64

message = "Hello world!"
message_bytes = message.encode("utf-8")
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode("utf-8")

print(base64_message)

"""

import base64
"""
data=['andry:uyro18890D', 'steve:oppjM13LL9e']
def encode_data_to_base64(data):
    b64_list = []
    for element in data:
        element_b = element.encode('utf-8')
        b64_b = base64.b64encode(element_b)
        b64_el = b64_b.decode('utf-8')
        b64_list.append(b64_el)
    return b64_list
"""
data=['andry:uyro18890D', 'steve:oppjM13LL9e']
b64_list = []
for element in data:
        #print(element)
        element_bytes = element.encode('utf-8')
        base64_bytes = base64.b64encode(element_bytes)
        base64_element = base64_bytes.decode('utf-8')
        #print(base64_element)
        b64_list.append(base64_element)
print(b64_list)