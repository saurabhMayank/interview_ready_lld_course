
from enum import Enum


class Temp:
    def __init__(self, item_dict):
        self.total_price = self.total_price_calc()
        self.temp_status = TempStatus

    def total_price_calc(self):
        price = 0
        for item,item_price in item_dict.items():
            price = price + item_price
        return price

class TempStatus(Enum):
    UNSHIPPED, PENDING, SHIPPED, COMPLETED, CANCELED, REFUND_APPLIED = 1, 2, 3, 4, 5, 6

if __name__ == "__main__":
    item_dict = {"surf": 10, "soap": 20, "shampoo": 30}
    temp_obj = Temp(item_dict)
    print(temp_obj.total_price)
    print(temp_obj.temp_status.SHIPPED)
    print(list(TempStatus))
    print(type(temp_obj.temp_status.SHIPPED.name))
    if "SHIPPED" == temp_obj.temp_status.SHIPPED.name:
        print("inside the if case")

