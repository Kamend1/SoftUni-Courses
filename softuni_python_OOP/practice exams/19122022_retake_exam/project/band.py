from typing import List

from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.band_members.musician import Musician


class Band:
    METAL_NEEDED_SKILLS = {'Singer': ['sing low pitch notes'],
                           'Drummer': ['play the drums with drumsticks'],
                           'Guitarist': ['play metal'],
                           }

    JAZZ_NEEDED_SKILLS = {'Singer': ['sing low pitch notes', 'sing high pitch notes'],
                          'Drummer': ['play the drums with drum brushes'],
                          'Guitarist': ['play jazz'],
                          }

    ROCK_NEEDED_SKILLS = {'Singer': ['sing high pitch notes'],
                          'Drummer': ['play the drums with drumsticks'],
                          'Guitarist': ['play rock'],
                          }

    VALID_GENRES = {"Metal": METAL_NEEDED_SKILLS,
                    "Rock": ROCK_NEEDED_SKILLS,
                    "Jazz": JAZZ_NEEDED_SKILLS,
                    }

    def __init__(self, name: str):
        self.name = name
        self.members: List[Guitarist: Musician, Drummer: Musician, Singer: Musician] = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Band name should contain at least one character!")

        self.__name = value

    # helper function for concert tracker app. Determine if band has needed members
    def can_play(self):
        drummer = any(isinstance(member, Drummer) for member in self.members)
        singer = any(isinstance(member, Singer) for member in self.members)
        guitarist = any(isinstance(member, Guitarist) for member in self.members)
        return drummer and singer and guitarist

    # helper function for concert tracker app. Determine if band members have needed skills
    def members_have_needed_skills(self, concert_genre):
        if concert_genre == 'Rock':
            for band_member in self.members:
                if band_member.__class__.__name__ == 'Drummer' and \
                        "play the drums with drumsticks" not in band_member.skills:
                    return False
                if band_member.__class__.__name__ == 'Singer' and "sing high pitch notes" not in band_member.skills:
                    return False
                if band_member.__class__.__name__ == 'Guitarist' and "play rock" not in band_member.skills:
                    return False

        elif concert_genre == 'Metal':
            for band_member in self.members:
                if band_member.__class__.__name__ == 'Drummer' and "play the drums with drumsticks" not in band_member.skills:
                    return False
                if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
                    return False
                if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
                    return False

        elif concert_genre == 'Jazz':
            for band_member in self.members:
                if band_member.__class__.__name__ == 'Drummer' \
                        and "play the drums with drum brushes" not in band_member.skills:
                    return False
                if band_member.__class__.__name__ == 'Singer' \
                        and ("sing low pitch notes" not in band_member.skills
                             or "sing high pitch notes" not in band_member.skills):
                    return False
                if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
                    return False

        return True

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."
