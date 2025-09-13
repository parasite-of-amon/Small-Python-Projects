from Cryptodome.Cipher import AES
KEY = b'12345678901234567\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'


class Encyption:
   def __init__(self):
      pass
   
   def pad(self, entry):
      padded = entry + (16-len(entry)%16) * chr(16 - len(entry)%16)
      return padded
   
   
Encryptor = Encyption()
text = Encryptor.pad("Hello World!")
text = text.encode('utf-8')

Key = "12345678901234567"
key = Encryptor.pad(Key)
key = key.encode('utf-8')

print(key)


