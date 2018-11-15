def do_stuff_with(data):
    print data


class CallbackA(object):
    def transmit(self,data):
        do_stuff_with(data)

class CallbackB(object):
    def doRead(self,data): # this is called by Twisted
        self.point_to_A.transmit(data)

class bigClass(object):
    def __init__(self):
        self.A = CallbackA()
        self.B = CallbackB()
        self.B.point_to_A = self.A

test = bigClass()
test.B.doRead('derp')
