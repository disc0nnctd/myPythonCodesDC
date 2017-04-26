"""
Reads a Time class object storing hours and minutes and
raises a user defined error if values other than 0-24 entered for hours
or values other than 0-59 is entered for minutes.
"""


class Time:
    def __init__(self, hours, minutes, errmsg):
        self.errmsg = errmsg
        self.hrs = hours
        self.mins = minutes

    def errchk(self):
        a = self.hrs in range(0, 25)
        b = self.mins in range(0, 60)
        if not a or not b:
            raise Exception(self.errmsg)


hours = int(input("hours"))
minutes = int(input("minutes"))
errmsg = raw_input("error message")
time = Time(hours, minutes, errmsg)
time.errchk()
