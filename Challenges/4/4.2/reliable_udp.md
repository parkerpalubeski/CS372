# Packet Numbering
Because UDP can arrive out of order or be lost entirely, the application would include a number for the packet in the metadata indicated which place the packet is supposed to be received in, sequentially. That way, if packet 56 arrives before packet 55, the receiver will know packet 55 is either still out there or was lost, and it can continue to listen and request it again after a timeout.
# ACKs
The receiver confirms to the sender that it recceived the packet.
# File Flagging
Each packet is flagged to the file which they belong, so they can be reassembled correctly and multiple files can be sent concurrently.