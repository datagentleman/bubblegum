from starbucks.packet import Message

def test_packet_message_to_bytes():
  bytes = Message("Hello", "World").to_bytes()
  msg = Message.from_bytes(bytes)

  assert(msg.cmd == "Hello")
  assert(msg.args == ("World",))
