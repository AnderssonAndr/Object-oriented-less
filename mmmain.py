class Store:
    def __init__(self, name, address, items:dict):
        self.name = name
        self.address = address
        #self.items = items 
    def add_goods(self):
        self.items.update({str,float})
    def delet_goods(self):
        del self.items[str]
    def goods_price(self, good):
        default = None
        self.good = good
        self.items.get(good[str, default])
        # если товара нет --default


