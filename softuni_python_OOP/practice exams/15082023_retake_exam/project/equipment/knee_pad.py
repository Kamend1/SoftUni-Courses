from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PERCENTAGE_PRICE_INCREASE = 1.2

    def __init__(self):
        super().__init__(120, 15)

    def increase_price(self):
        self.price *= self.PERCENTAGE_PRICE_INCREASE
