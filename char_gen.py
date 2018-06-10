from random import choice

from char_data import GENDER, CLASS, RACE, SUBCLASS, CULTURE, BACKGROUND, CULTURE_BACKGROUNDS, SUBRACE, NAMES

CHECK = {
    'sub_class': SUBCLASS,
    'culture': CULTURE,
    'background': BACKGROUND,
    'sub_race': SUBRACE,
}

ALWAYS_SUBCLASS = [
    'priest',
    'paladin'
]

COMPATIBLE = {
    'bleak_walkers': ['magran', 'wael'],
    'darcozzi': ['wael', 'eothas'],
    'goldpact_knights': ['skaen', 'eothas', 'berath'],
    'kind_wayfarers': ['eothas'],
    'shieldbearers_of_st_elga': ['eothas', 'berath'],
}

FACTION = [
    'principi',
    'royal_dreadfire_company',
    'vailian trading company',
    'huana',
]

OPTIONS = {
    'race': RACE,
    'sub_race': SUBRACE,
    'name': NAMES,
    'cls_1': CLASS,
    'prestige_1': SUBCLASS,
    'cls_2': CLASS,
    'prestige_2': SUBCLASS,
    'faction': FACTION,
    'background': BACKGROUND,
    'culture': CULTURE,
}


class Character():

    def __init__(self, **kwargs):
        self.options = {}
        self.options.update(kwargs)

        # self.gender = gender if not random else choice(list(GENDER.keys()))
        # self.race = race if not random else choice(list(RACE.keys()))
        # if random:
        #     self.sub_race = choice(list(SUBRACE[self.race].keys()))
        #     self.char_class_1 = choice(list(CLASS.keys()))
        #     if sub or self.char_class_1 in ALWAYS_SUBCLASS:
        #         self.sub_class_1 = choice(list(SUBCLASS[self.char_class_1]))
        #     else:
        #         self.sub_class_1 = None
        #     if multi:
        #         self.char_class_2 = choice([x for x in CLASS.keys() if x != self.char_class_1])
        #         sub = choice([True, False])
        #         if sub or self.char_class_2 in ALWAYS_SUBCLASS:
        #             if self.char_class_1 in COMPATIBLE.keys():
        #                 self.sub_class_2 = choice([x for x in SUBCLASS[self.char_class_2] if x in COMPATIBLE[self.sub_class_2]])
        #             else:
        #                 self.sub_class_2 = choice(list(SUBCLASS[self.char_class_2]))
        #         else:
        #             self.sub_class_2 = None
        #     else:
        #         self.char_class_2 = None
        #         self.sub_class_2 = None
        # self.culture = culture if not random else choice(list(CULTURE.keys()))
        # self.background = self.get_background(background) if not random else choice(CULTURE_BACKGROUNDS[self.culture])
        # self.faction = choice(FACTION)
        # self.score = self.get_score()

    def get_char(self):
        for key, item in OPTIONS.items():
            self.options[key] = self.options[key] if key in self.options.keys() else choice(list(item.keys()))
        print(self.options)
        return self.options

    def get_name(self):
        return self.options['name'] if 'name' in self.options.keys() else choice(NAMES)

    # def get_background(self, background):
    #     return background if background and background in CULTURE_BACKGROUNDS[self.culture] or background in CULTURE_BACKGROUNDS['all'] else None

    # def get_score(self):
    #     score = GENDER[self.gender] + CLASS[self.char_class_1] + RACE[self.race]
    #     x = 'Score = {} ({}) + {} ({}) + {} ({})'.format(GENDER[self.gender], self.gender,  CLASS[self.char_class_1], self.char_class_1, RACE[self.race], self.race)
    #     for key, item in self.__dict__.items():
    #         if key in CHECK.keys():
    #             if item in CHECK[key].keys():
    #                 score += CHECK[key][item]
    #                 x += ' + {} ({})'.format(CHECK[key][item], item)
    #     return score

    def get_sheet(self):
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}+{:<5}|'.format(' Name', ' ' + self.name, ' ' + '0'))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}+{:<5}|'.format(' Gender', ' ' + self.gender, ' ' + str(GENDER[self.gender])))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}+{:<5}|'.format(' Race', ' ' + self.race, ' ' + str(RACE[self.race])))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}+{:<5}|'.format(' SubRace', ' ' + self.sub_race, ' ' + str(SUBRACE[self.race][self.sub_race])))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}+{:<5}|'.format(' Class 1', ' ' + self.char_class_1, ' ' + str(CLASS[self.char_class_1])))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        sub_class_val = SUBCLASS[self.char_class_1][self.sub_class_1] if self.sub_class_1 else '0'
        print('|{:<26}|{:<26}+{:<5}|'.format(' SubClass', ' ' + self.sub_class_1 if self.sub_class_1 else ' None', ' ' + str(sub_class_val)))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}+{:<5}|'.format(' Class 2', ' ' + self.char_class_2 if self.char_class_2 else ' None', ' ' + str(sub_class_val)))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        sub_class_val = SUBCLASS[self.char_class_2][self.sub_class_2] if self.sub_class_2 else '0'
        print('|{:<26}|{:<26}+{:<5}|'.format(' SubClass 2', ' ' + self.sub_class_2 if self.sub_class_2 else ' None', ' ' + str(sub_class_val)))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}+{:<5}|'.format(' Faction', ' ' + self.faction, ' 0'))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}+{:<5}|'.format(' Culture', ' ' + self.culture, ' ' + str(CULTURE[self.culture])))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}+{:<5}|'.format(' Background', ' ' + self.background, ' ' + str(BACKGROUND[self.background])))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}+{:<5}|'.format(' Score', ' total', ' ' + str(self.get_score())))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        return ''


def generate_character(
        name=None,
        gender='male',
        char_class_1='cipher',
        race='human',
        sub_class_1=None,
        culture=None,
        background=None,
        random=False
    ):
    return Character(
        name=name,
        gender=gender,
        char_class_1=char_class_1,
        race=race,
        sub_class_1=sub_class_1,
        culture=culture,
        background=background,
        random=random
    )

