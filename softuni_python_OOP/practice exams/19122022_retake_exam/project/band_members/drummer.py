from typing import List
from project.band_members.musician import Musician


class Drummer(Musician):
    AVAILABLE_SKILLS: List[str] = ["play the drums with drumsticks",
                                   "play the drums with drum brushes",
                                   "read sheet music"
                                   ]
    TYPE_ = 'Drummer'
