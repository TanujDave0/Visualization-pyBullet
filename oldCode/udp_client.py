from udp import udp


test = udp()
msg = test.listen()
print(msg)
test.close()