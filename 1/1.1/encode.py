s = "Hi 🙂"
bytes = s.encode('utf-8')
print(bytes)
#What happens?
#The smiley face is encoded into bytes (printed as hex characters) rather than the smiley face


bytes2 = s.encode('utf-16')
print(bytes2)
#How do they differ from the UTF-8 encoding?
#They differ in that the "Hi" substring is also encoded into bytes and printed with hex

#s2 = bytes2.decode('utf-8')
#print(s2)
#What happens?
#The string is encoded in UTF-16, but decoded into UTF-8. The bytes are mismatched, so the terminal returns an error

s2 = bytes2.decode('utf-16')
print(s2)