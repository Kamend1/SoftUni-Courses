from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PERCENTAGE_PRICE_INCREASE = 1.1

    def __init__(self):
        super().__init__(90, 25)

    def increase_price(self):
        self.price *= self.PERCENTAGE_PRICE_INCREASE
