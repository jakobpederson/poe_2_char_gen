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

FACTIONS = [
    'principi',
    'royal_dreadfire_company',
    'vailian trading company',
    'huana',
]

OPTIONS = {
    'race': RACE,
    'name': NAMES,
    'faction': FACTIONS,
    'background': BACKGROUND,
    'culture': CULTURE,
    'cls_1': CLASS,
    'cls_2': CLASS,
    # 'sub_race': SUBRACE,
}

class Character():

    def __init__(self, **kwargs):
        self.options_1 = {}
        self.options_1.update(kwargs)
        self.get_options(kwargs)

    def get_options(self, kwargs):
        self.options = {}
        self.options.update(kwargs)
        for key, value in OPTIONS.items():
            if isinstance(value, list):
                self.options[key] = self.options[key] if key in self.options.keys() else choice(value)
            else:
                self.options[key] = self.options[key] if key in self.options.keys() else choice(list(value.keys()))
        return self.options

    def print_out(self):
        character = self.sheet['data']['attributes']
        relationships = self.sheet['data']['relationships']
        name = character['name']
        gender = character['gender']
        race = relationships['race']['data']['type']
        culture = relationships['culture']['data']['type']
        background = relationships['culture']['data']['sub_type']
        sub_race = relationships['race']['data']['sub_type']
        faction = character['faction']
        score = character['score'] + relationships['race']['data']['score'] + relationships['culture']['data']['score']
        for val in relationships['classes']['data']:
            score += val['score']
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}|{:<5}|'.format(' NAME', ' ' + name, ' ' + '0'))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}|{:<5}|'.format(' GENDER', ' ' + gender, ' ' + str(GENDER[gender])))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}|{:<5}|'.format(' RACE', ' ' + race, ' ' + str(RACE[race])))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}|{:<5}|'.format(' SUBRACE', ' ' + sub_race, ' ' + str(SUBRACE[race][relationships['race']['data']['sub_type']])))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}|{:<5}|'.format(' FACTION', ' ' + faction, ' 0'))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        for val in relationships['classes']['data']:
            print('|{:<26}|{:<26}|{:<5}|'.format(' CLASS', ' ' + val['type'], ' ' + str(CLASS[val['type']])))
            print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
            print('|{:<26}|{:<26}|{:<5}|'.format(' SUB CLASS', ' ' + val['sub_type'], ' ' + str(SUBCLASS[val['type']][val['sub_type']])))
            print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}|{:<5}|'.format(' CULTURE', ' ' + culture, ' ' + str(CULTURE[culture])))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}|{:<5}|'.format(' BACKGROUND', ' ' + background, ' ' + str(BACKGROUND[background])))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        print('|{:<26}|{:<26}|{:<5}|'.format(' SCORE', ' ' + 'TOTAL', ' ' + str(score)))
        print('+{:<26}+{:<26}+{:<5}+'.format('-' * 26, '-' * 26, '-' * 5))
        return

    @property
    def sheet(self):
        name = self.options['name'] if 'name' in self.options.keys() else choice(NAMES)
        gender = self.options['gender'] if 'gender' in self.options.keys() else choice(list(GENDER.keys()))
        faction = self.options['faction'] if 'faction' in self.options.keys() else choice(FACTIONS)
        race = self.options['race'] if 'race' in self.options.keys() else choice(list(RACE.keys()))
        sub_race = self.options_1['sub_race'] if 'sub_race' in self.options_1 else choice(list(SUBRACE[race].keys()))
        class_1 = self.options['cls_1'] if 'cls_1' in self.options.keys() else choice(list(CLASS.keys()))
        sub_cls_1 = self.options['sub_cls_1'] if 'sub_cls_1' in self.options.keys() else choice(list(SUBCLASS[class_1].keys()))
        if 'cls_2' in self.options.keys():
            cls = self.options['cls_2']
            sub_cls = self.options['sub_cls_2'] if 'sub_cls_2' in self.options.keys() else choice(list(SUBCLASS[cls].keys()))
            class_2 = [{
                'type': cls,
                'sub_type': sub_cls,
                'score': CLASS[cls] + SUBCLASS[cls][sub_cls]
            }] if cls != class_1 else []
            if class_2 in list(COMPATIBLE.keys()) and class_1 in list(COMPATIBLE.keys()):
                sub_cls = choice(COMPATIBLE[cls])
                class_2 = [{
                    'type': cls,
                    'sub_type': sub_cls,
                    'score': CLASS[cls] + SUBCLASS[sub_cls]
                }] if cls == class_1 else []
        else:
            if choice([True, False]):
                cls = self.options['cls_2']
                sub_cls = self.options['sub_cls_2'] if 'sub_cls_2' in self.options.keys() else choice(list(SUBCLASS[cls].keys()))
                class_2 = [{
                    'type': cls,
                    'sub_type': sub_cls,
                    'score': CLASS[cls] + SUBCLASS[cls][sub_cls]
                }]
        culture = self.options['culture'] if 'culture' in self.options.keys() else choice(list(CULTURE.keys()))
        viable_backgrounds = CULTURE_BACKGROUNDS[culture] + CULTURE_BACKGROUNDS['all']
        background = self.options['background'] if 'background' in self.options.keys() else choice(viable_backgrounds)
        return {
            'data': {
                'attributes': {
                    'name': name,
                    'faction': faction,
                    'gender': gender,
                    'score': GENDER[gender]
                },
                'type': 'character',
                'relationships': {
                    'race': {
                        'data': {
                            'type': race,
                            'sub_type': sub_race,
                            'score': RACE[race] + SUBRACE[race][sub_race],
                        }
                    },
                    'classes': {
                        'data': [
                            {
                                'type': class_1,
                                'sub_type': sub_cls_1,
                                'score': CLASS[class_1] + SUBCLASS[class_1][sub_cls_1]
                            }
                        ] + class_2
                    },
                    'culture': {
                        'data': {
                            'type': culture,
                            'sub_type': background,
                            'score': CULTURE[culture] + BACKGROUND[background]
                        }
                    }
                }
            }
        }
