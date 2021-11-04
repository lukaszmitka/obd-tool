import obd
# obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.OBD("/dev/ttyUSB0") # create connection with USB 0
cmd = obd.commands.SPEED # select an OBD command (sensor)
response = connection.query(cmd) # send the command, and parse the response
print(response.value) # returns unit-bearing values thanks to Pint
