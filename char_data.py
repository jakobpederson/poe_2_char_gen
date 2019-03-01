RACE = {
    'godlike': 44,
    'orlan': 30,
    'dwarf': 17,
    'aumaua': 10,
    'elf': 3,
    'human': 2,
}


GENDER = {
    'female': 8,
    'male': 4,
}

SUBRACE = {
    'aumaua': {
        'island': 102,
        'coastal': 25,
    },
    'godlike': {
        'fire': 31,
        'death': 25,
        'moon': 11,
        'nature': 10,
    },
    'dwarf': {
        'boreal': 9,
        'mountain': 5,
    },
    'human': {
        'ocean': 7,
        'meadow folk': 2,
    },
    'elf': {
        'snow': 5,
        'wood': 1,
    },
    'orlan': {
        'wild': 0,
        'hearth': 0,
    },
}

CLASS = {
    'cipher': 25,
    'priest': 25,
    'druid': 24,
    'ranger': 21,
    'wizard': 13,
    'chanter': 10,
    'monk': 9,
    'paladin': 7,
    'rogue': 5,
    'barbarian': 3,
    'fighter': 0,
}

SUBCLASS = {
    'cipher': {
        'ascendant': 0,
        'beguiler': 0,
        'soul_blade': 0,
        'none': 0,
    },
    'priest': {
        'magran': 25,
        'eothas': 14,
        'berath': 12,
        'wael': 7,
        'skaen': 6,
    },
    'druid': {
        'fury': 1,
        'shifter': 0,
        'life_giver': 0,
        'animist': 0,
    },
    'ranger': {
        'ghost_heart': 13,
        'stalker': 1,
        'sharpshooter': 0,
        'none': 0,
    },
    'wizard': {
        'conjurer': 0,
        'illusionist': 0,
        'enchanter': 1,
        'evoker': 0,
        'transmuter': 0,
        'none': 0,
    },
    'chanter': {
        'skald': 1,
        'troubadour': 0,
        'beckoner': 0,
        'none': 0,
    },
    'monk': {
        'nalpazca': 1,
        'shattered_pillar': 0,
        'helwalker': 0,
        'none': 0,
    },
    'paladin': {
        'goldpact_knights': 16,
        'bleak_walkers': 7,
        'kind_wayfarers': 3,
        'darcozzi': 1,
        'shieldbearers_of_st_elga': 0,
    },
    'rogue': {
        'assassin': 4,
        'trickster': 3,
        'streetfighter': 1,
        'none': 0,
    },
    'barbarian': {
        'corpse eater': 2,
        'berserker': 0,
        'mage_killer': 0,
        'none': 0,
    },
    'fighter': {
        'black_jacket': 1,
        'unbroken': 0,
        'devoted': 0,
        'none': 0,
    }
}

CULTURE = {
    'deadfire_archipelago': 157,
    'rauatai': 62,
    'old_vailia': 14,
    'aedyr': 13,
    'the_living_lands': 11,
    'the_white_that_wends': 7,
    'ixamitl_plains': 6,
}


BACKGROUND = {
    'aristocrat': 21,
    'scientist': 20,
    'mystic': 19,
    'scholar': 18,
    'mercenary': 17,
    'philosopher': 14,
    'merchant': 12,
    'raider': 12,
    'clergy': 11,
    'explorer': 10,
    'drifter': 9,
    'slave': 9,
    'dissident': 8,
    'laborer': 8,
    'hunter': 7,
    'artist': 5,
    'colonist': 3,
    'soldier': 2,
}

CULTURE_BACKGROUNDS = {
    'all': ['hunter', 'laborer', 'merchant', 'drifter'],
    'deadfire_archipelago': ['aristocrat', 'mercenary', 'explorer', 'raider', 'slave'],
    'rauatai': ['aristocrat', 'dissident', 'mercenary', 'scholar', 'slave'],
    'old_vailia': ['aristocrat', 'artist', 'colonist', 'dissident', 'mercenary', 'slave'],
    'aedyr': ['aristocrat', 'clergy', 'colonist', 'dissident', 'mercenary', 'slave'],
    'the_living_lands': ['colonist', 'mercenary', 'explorer', 'scientist'],
    'the_white_that_wends': ['aristocrat', 'explorer', 'mystic'],
    'ixamitl_plains': ['aristocrat', 'dissident', 'mercenary', 'philosopher', 'scholar'],
}

NAMES = [
    'Iscon',
    'Corien Sumatris',
    'Armaros',
    'Gessart',
    'Marcus Heilbron',
    'Reinhart',
    'Brant',
    'Folkert',
    'Draco',
    'Marius Reinhart',
    'Karlaen',
    'Donatos Aphael',
    'Machiavi',
    'Erasmus Tycho',
    'Castigon',
    'Sendini',
    'Raxiatel',
    'Phaeton',
    'Zedrenael',
    'Sendroth',
    'Borgio',
    'Alenso',
    'Leonatos',
    'Morleo Moriar',
    'Abel Zorael',
    'Davian Thule',
    'Indrick Boreale',
    'Apollo Diomedes',
    'Daed',
    'Obiareus',
    'Alessio Cortez',
    'Crixus',
    'Telamon',
    'Belial',
    'Sammael',
    'Nadael',
    'Aderson',
    'Alajos',
    'Astoric',
    'Darius',
    'Galedan',
    'Melian',
    'Tragan',
    'Kerith Roac',
    'Calas Typhon',
    'Ignatius Grulgor',
    'Nathaniel Garro',
    'Kolak',
    'Elias',
    'Balthus',
    'Consultus',
    'Grimmer Slayne',
    'Julius Kaesoron',
    'Solomon Demeter',
    'Marius Vairosean',
    'Saul Tarvitz',
    'Lucius',
    'Odovocar',
    'Vilius',
    'Belloch',
    'Leitz',
    'Silas Alberec',
    'Ignatius Sable',
    'Tarnus Vale',
    'Elam Courbray',
    'Narth Orlandra',
    'Portan',
    'Taremar Aurellian',
    'Arvann Stern',
    'Anval Thawn',
    'Fidelis',
    'Valafar',
    'Orlando Furioso',
    'Darnath Lysander',
    'Kleitus',
    'Sigismund',
    'Taelos',
    'Quirion Octavius',
    'Lexandro D\'Arquebus',
    'Alexis Polux',
    'Amandus Tyr',
    'Oriax Dantalion',
    'Fafnir Rann',
    'Sien',
    'Cadulon',
    'Phobor',
    'Cules',
    'Pheus',
    'Quentus Carmagon',
    'Ezekyle Abaddon',
    'Tarik Torgaddon',
    'Iacton Qruze',
    'Horus Aximand',
    'Garviel Loken',
    'Luc Sedirae',
    'Vaas',
    'Anton Narvaez',
    'Magnar Tytus',
    'Vinyar',
    'Vorr',
    'Theus Solocii',
    'Ithillion',
    'Jexad',
    'Shoma',
    'Mordaci Blaylock',
    'Darius Troy',
    'Herulian',
    'Lyonus',
    'Numine',
    'Kaedes',
    'Maodes Karib',
    'Mito',
    'Orelius',
    'Oradias',
    'Aajz Solari',
    'Kayvaan Shrike',
    'Alerin',
    'Aethon Shaan',
    'Koryn',
    'Corvane Valar',
    'Korvydae',
    'Aremis Koryn',
    'Rykas',
    'Stenn',
    'Denon',
    'Pellas Mir\'san',
    'Adrax Agatone',
    'N\'keln',
    'Dac\'tyr',
    'Theodosios',
    'Eddan Bourne',
    'Andreas Kulle',
    'Vaylund Cal',
    'Ragnar Blackmane',
    'Zhrukal Androcles',
    'Kortar',
    'Abroghan Callister',
    'Adrasta',
    'Severus Agemman',
    'Saul Invictus',
    'Agies',
    'Cato Sicarius',
    'Keorn Asata',
    'Severus',
    'Mikael Fabian',
    'Jehnnus Ardias',
    'Idaeus',
    'Tiy Newman',
    'Uriel Ventris',
    'Caito Galenus',
    'Epathus',
    'Ixion',
    'Numitor',
    'Sinon',
    'Antilochus',
    'Adallus',
    'Aloysius',
    'Calistes',
    'Garus',
    'Kruger',
    'Kor\'sarro Khan',
    'Angnar',
    'Jurga Khan',
    'Mad Chainsaw Johnson',
    'Subodai',
    'Suboden Khan',
    'Balthus',
    'Varren',
    'Ehrlen',
    'Khârn',
    'Aenarion',
    'Alarielle',
    'Alith Anar'
    'Eltharion'
    'Asarnil'
    'Finubar',
    'Imrik',
    'Teclis',
    'Tyrion',
    'Caradryan',
    'Korhil',
    'Selafyn of the Annulii',
    'Malekith',
    'Malus Darkblade',
    'Morathi',
    'Shadowblade',
    'Hellebron',
    'Lokhir Fellheart',
    'Kouran',
    'Tullaris',
    'Hubris Rakarth',
    'Alarie the Mad',
    'Alrik Ranulfsson',
    'Garagrim Ironfist',
    'Gotrek Gurnisson',
    'Grimnir',
    'Grombrindal the White Dwarf',
    'Josef Bugman',
    'King Kazador',
    'Malakai Makaisson',
    'Snorri Nosebiter',
    'Thorek Ironbow',
    'Thorgrim Grudgebearer',
    'Ungrim Ironfist',
]
