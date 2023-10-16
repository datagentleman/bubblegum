from starbucks.packet import Message

def test_packet_message_to_bytes():
  msg = Message("Hello", "World")
  print(msg.to_bytes())