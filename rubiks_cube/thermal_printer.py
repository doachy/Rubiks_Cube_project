from escpos.printer import Serial

""" 9600 Baud, 8N1, Flow Control Enabled """
p = Serial(devfile='/dev/ttyS0',
           baudrate=19200,
           bytesize=8,
           parity='N',
           stopbits=1,
           timeout=1.00,
           dsrdtr=True)

p.text("Hello World\n")
p.text("Hello World\n")
p.text("Hello World\n")
p.qr("You can readme from your smartphone")
p.text("Hello World\n")
p.text("Hello World\n")
p.text("Hello World\n")
p.text("Hello World\n")
p.qr("You can readme from your smartphone")
p.text("Hello World\n")
p.text("Hello World\n")
p.text("Hello World\n")
p.text("Hello World\n")
p.text("Hello World\n")
p.text("Hello World\n")
p.text("Hello World\n")
p.text("Hello World\n")
p.text("Hello World\n")
p.text("Hello World\n")
p.text("Hello World\n")
p.qr("You can readme from your smartphone")
'''p.cut()'''