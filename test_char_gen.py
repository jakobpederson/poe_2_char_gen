from unittest import TestCase

from char_gen import Character


class CharGenTests(TestCase):

    def setUp(self):
        data = {
            'name': 'abc',
            'gender': 'male',
            'race' : 'elf',
            'sub_race': 'snow',
            'cls_1': 'fighter',
            'cls_2': 'barbarian',
            'sub_cls_1': 'black_jacket',
            'sub_cls_2': 'berserker',
            'culture':  'ixamitl_plains',
            'background': 'hunter',
            'faction': 'principi'
        }
        self.char = Character(**data)
        data_1 = {
            'name': 'abc',
            'gender': 'male',
            'race' : 'elf',
            'sub_race': 'snow',
            'cls_1': 'priest',
            'cls_2': 'paladin',
            'sub_cls_1': 'eothas',
            'sub_cls_2': 'kind_wayfarers',
            'culture':  'ixamitl_plains',
            'background': 'hunter',
            'faction': 'principi'
        }
        self.char_2 = Character(**data_1)

    def test_x(self):
        result = self.char.sheet
        expected = {
            'data': {
                'relationships': {
                    'culture': {
                        'data': {
                            'attributes': {
                                'type': 'ixamitl_plains',
                                'score': 13,
                                'sub_type': 'hunter'
                            }
                        }
                    },
                    'classes': {
                        'data': [
                            {
                                'attributes': {
                                    'sub_type': 'black_jacket',
                                    'type': 'fighter',
                                    'score': 1
                                }
                            }, {
                                'attributes': {
                                    'sub_type': 'berserker',
                                    'type': 'barbarian',
                                    'score': 3
                                }
                            }
                        ]
                    },
                    'race': {
                        'data': {
                            'attributes': {
                                'sub_type': 'snow',
                                'type': 'elf'
                            }
                        }
                    }
                },
                'type': 'character',
                'attributes': {
                    'faction': 'principi',
                    'name': 'abc'
                }
            }
        }
        self.assertEqual(result, expected)

    def test_y(self):
        result = self.char_2.sheet
        expected = {
            'data': {
                'type': 'character',
                'relationships': {
                    'race': {
                        'data': {
                            'attributes': {
                                'sub_type': 'snow',
                                'score': 1,
                                'type': 'elf'
                            }
                        }
                    },
                    'classes': {
                        'data': [
                            {
                                'attributes': {
                                    'sub_type': 'eothas',
                                    'type': 'priest',
                                    'score': 39
                                }
                            },
                            {
                                'attributes': {
                                    'sub_type': 'kind_wayfarers',
                                    'type': 'paladin',
                                    'score': 10
                                }
                            }
                        ]
                    },
                    'culture': {
                        'data': {
                            'attributes': {
                                'sub_type': 'hunter',
                                'type': 'ixamitl_plains',
                                'score': 13
                            }
                        }
                    }
                },
                'attributes': {
                    'name': 'abc',
                    'faction': 'principi'
                }
            }
        }
        self.assertEqual(result, expected)

    def test_z(self):
        char = Character()
        x = char.print_out()
        self.fail('x')
