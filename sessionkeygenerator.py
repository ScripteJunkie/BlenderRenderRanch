#import base64, M2Crypto
#def generate_session_id(num_bytes = 16):
#    return base64.b64encode(M2Crypto.m2.rand_bytes(num_bytes))

import uuid, os, base64
sname = ""
def generate_session_id():
    #return uuid.uuid1
    return base64.b64encode(os.urandom(16))
alpha = str(generate_session_id())
for character in alpha:
    if character.isalnum():
        sname += character
#print(sname)
#uuid.UUID(bytes = os.urandom.bytes(16))
# UUID('c9bf635f-b0cc-d278-a2c5-01eaae654461')
