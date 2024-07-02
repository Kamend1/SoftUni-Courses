from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationRepository:

    def __init__(self):
        self.decorations: List[Ornament: BaseDecoration, Plant: BaseDecoration] = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True

        return False

    def find_by_type(self, decoration_type: str):
        return next(filter(lambda d: d.type == decoration_type, self.decorations), "None")
