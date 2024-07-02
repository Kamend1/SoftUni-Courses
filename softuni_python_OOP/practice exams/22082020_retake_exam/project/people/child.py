class Child:

    def __init__(self, food_cost: int, *toys_cost):
        cost = food_cost + sum(toy_cost for toy_cost in toys_cost)
        self.cost = cost
