import random


class Cat:
    stats: dict = {
        'name': '',
        'age': 0,
        'happiness': 0,
        'satiety': 0,
        'state': 'play',
        'image': ''
    }

    @classmethod
    def set_start_stats(cls, name: str):
        cls.stats['name'] = name
        cls.stats['age'] = random.randint(1, 20)
        cls.stats['happiness'] = random.randint(1, 60)
        cls.stats['satiety'] = random.randint(1, 60)

    @staticmethod
    def play():
        if Cat.stats.get('state') == 'sleep':
            happy_stat = -5
        else:
            if random.randint(0, 3) > 0:
                happy_stat = 15
            else:
                happy_stat = 0
                Cat.stats['happiness'] = 0
        Cat.change_stats('play', happiness=happy_stat, satiety=-10, image='/happy.jpg')

    @staticmethod
    def feed():
        if Cat.stats.get('state') == 'play':
            Cat.change_stats('feed', satiety=15, happiness=5)
        elif Cat.stats.get('state') == 'feed':
            Cat.change_stats('feed', happiness=-30)

    @staticmethod
    def sleep():
        Cat.change_stats('sleep')

    @staticmethod
    def change_stats(state: str, **kwargs):
        kw_dict = dict(kwargs)
        for k, v in kw_dict.items():
            Cat.stats[k] += v
        Cat.stats['state'] = state

    @classmethod
    def choose_action(cls, action: str):
        match action:
            case 'play':
                Cat.play()
            case 'feed':
                Cat.feed()
            case _:
                Cat.sleep()
