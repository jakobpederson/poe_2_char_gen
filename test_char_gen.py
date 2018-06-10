from unittest import TestCase

from char_gen import generate_character, Character


class CharGenTests(TestCase):

    def test_x(self):
        char = generate_character(name='Test 1', gender='male', char_class='cipher', race='human')
        self.assertEqual(char.gender, 'male')
        self.assertEqual(char.char_class, 'cipher')
        self.assertEqual(char.score, 31)
        char = generate_character(name='Test 2', gender='female', char_class='cipher', race='human')
        self.assertEqual(char.gender, 'female')
        self.assertEqual(char.char_class, 'cipher')
        self.assertEqual(char.score, 35)
        char = generate_character(name='Test 3', gender='female', char_class='cipher', sub_class='ascendant', race='human')
        self.assertEqual(char.sub_class, 'ascendant')
        self.assertEqual(char.score, 35)
        char = generate_character(name='Test 4', gender='female', char_class='druid', sub_class='fury', race='human')
        self.assertEqual(char.sub_class, 'fury')
        self.assertEqual(char.score, 34)
        char = generate_character(
            name='Test 5',
            gender='female',
            char_class='druid',
            sub_class='fury',
            race='human',
            culture='old_vailia'
        )
        self.assertEqual(char.score, 48)
        char = generate_character(
            name='Test 6',
            gender='female',
            char_class='druid',
            sub_class='fury',
            race='human',
            culture='old_vailia',
            background='merchant'
        )
        self.assertEqual(char.score, 60)
        self.fail('x')

    def test_y(self):
        char = generate_character(
            name='Test 7',
            gender='female',
            char_class='fighter',
            sub_class='fury',
            race='human',
            culture='the_living_lands',
            background='aristocrat'
        )
        self.assertEqual(char.score, 21)

    def test_a(self):
        char = generate_character(
            name='Test 7',
            gender='female',
            char_class_1='paladin',
            sub_class_1='ascendant',
            race='human',
            culture='the_living_lands',
            background='aristocrat'
        )
        print(char.get_sheet())
        self.fail('x')

    def test_z(self):
        char = generate_character(random=True)
        print(char.get_sheet())
        self.fail('x')

    def test_123(self):
        char = Character(name='abc')
        self.assertEqual(char.get_char(), 'abc')
