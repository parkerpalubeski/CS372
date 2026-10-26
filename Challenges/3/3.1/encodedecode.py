def encode_data(message: str, value: int) -> bytes:
    msg_bytes = message.encode('utf-8')
    msg_length = len(msg_bytes)

    #'big' for big-endian
    val_bytes = value.to_bytes(4, byteorder='big', signed=True)
    
    full_length = 2 + msg_length + 4
    
    len_bytes = full_length.to_bytes(2, byteorder='big', signed=False)
    
    return len_bytes + msg_bytes + val_bytes

def decode_data(encoded_bytes: bytes):
    value = int.from_bytes(encoded_bytes[-4:], byteorder='big', signed=True)
    msg_bytes = encoded_bytes[2:-4]
    message = msg_bytes.decode('utf-8')
    return message, value

# Encode
original_message = "Hello, world!"
original_value = -12345

encoded = encode_data(original_message, original_value)
print("Encoded:", encoded)

# Decode
decoded_message, decoded_value = decode_data(encoded)
print("Decoded Message:", decoded_message)
print("Decoded Value:", decoded_value)