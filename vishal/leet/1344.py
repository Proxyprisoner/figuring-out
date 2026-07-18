#run in terminal: python "vishal/leet/1344.py"
def angleClock(hour, minutes):
        ma=minutes*6
        ha=(hour%12)*30+minutes*(0.5)
        ang=abs(ha-ma)
        return min(ang,360-ang)
hour=int(input("Enter hour: "))
minutes=int(input("Enter minutes: "))
print(angleClock(hour,minutes))