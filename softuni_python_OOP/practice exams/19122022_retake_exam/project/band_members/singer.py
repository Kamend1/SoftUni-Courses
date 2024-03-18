from typing import List
from project.band_members.musician import Musician


class Singer(Musician):
    AVAILABLE_SKILLS: List[str] = ["sing high pitch notes", "sing low pitch notes"]
    TYPE_ = 'Singer'
