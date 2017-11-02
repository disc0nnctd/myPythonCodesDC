class ITEMINFO():
    def __init__(self):
        self.icode=0
        self.item=""
        self.price=0
        self.qty=0
        self.discount=0
        self.netprice=0
    def FindDisc(self):
        q=self.qty
        if q<10:
            d=0
        if q in range(11,21):
            d=15
        if q>=20:
            d=20
        self.discount=self.price*(d/100.0)
        self.netprice=(self.price*self.qty - self.discount)
    def Buy(self):
        self.icode=input("Icode: ")
        self.item=raw_input("Item: ")
        self.price=input("Price: ")
        self.qty=input("Qty: ")
        FindDisc()
    def ShowAll(self):
        print "Icode: ", self.icode
        print "Item: ", self.item
        print "Price: ", self.price
        print "Qty: ", self.qty
        print "Discount: ", self.discount
        print "Net Price: ", self.netprice
a=ITEMINFO()
a.Buy()
a.ShowAll()
