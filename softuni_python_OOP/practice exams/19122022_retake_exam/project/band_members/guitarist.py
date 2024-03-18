from typing import List
from project.band_members.musician import Musician


class Guitarist(Musician):
    AVAILABLE_SKILLS: List[str] = ["play metal", "play rock", "play jazz"]
    TYPE_ = 'Guitarist'
