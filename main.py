
class Animal():
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice

    def make_voice(self):
        print("Тварина каже", self.voice)


class Cat(Animal):
    def __init__(self, name, voice, hp=9):
        super().__init__(name, voice)
        self.hp = hp

    def sleep_all_day(self):
        print('Кіт спить весь день')


tom = Cat('Tom', 'мяу')
tom.make_voice()
tom.name = "Jerry"
tom.sleep_all_day()
print(tom.hp, 'життів')

