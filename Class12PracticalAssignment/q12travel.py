class Travel:
    visits=0
    amount=0
    def __init__(self):
        Travel.visits+=1
    def ticket(self):
        ask=raw_input("Buy tickets?(Y/N)")
        if ask.upper()=='Y':
            amount+=50
    def display(self):
        print 'Visits: %s\nAmount Collected: %s'%(Travel.visits, Travel.amount)
t=Travel()
t.ticket()
t1=Travel()
t1.ticket()
t1.display
