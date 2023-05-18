prise_diod = 150  # стоимость диодной лампы
prise_en = 90   # стоимость энергосберегающей лампы
prise_svet = 2.32   # стоимость 1 КВт энергии
life_diod = 50000   # срок службы диодной лампы в часах
life_en = 10000   # срок службы энергосберегающей лампы
consumption_diod = 0.035   # потребление диодной лампы КВт в час
consumption_en = 0.075   # Потребление енергосберегающей лампы КВт в час
print('Здраствуйте, это приложени которое вам поможет увидеть сколько вы сэкономите денег за энергию поменяв свои електросберегающие ламы на диодные для этого введите количество ваших электросберегающих ламп')
class House():
    """Класс для хранения информации о количестве ламп в доме"""
    def __init__(self, lamp_en):
        self.lamp_en = lamp_en
        self.lamp_diod = self.calc_need()

    def calc_need(self):
        return self.lamp_en

    def calc_price(self):
        return self.lamp_diod * prise_diod

    def calc_income(self):
        prise_consumption_diod = ((consumption_diod * life_en) * prise_svet) * self.lamp_diod
        prise_consumption_en = ((consumption_en * life_en) * prise_svet) * self.lamp_en
        return prise_consumption_en - prise_consumption_diod

    def calculate(self):
        print("Необходимо", self.lamp_diod, "новых диодных ламп")
        print('Стоимость модернизации:', self.calc_price())
        print('Через 10000 часов лампы окупятся на', self.calc_income())

def choose_house():
    while True:
        res = int(input('Введите количество энергосберегающих ламп у вас дома: '))
        if res >= 1:
            return House(res)
        else:
            print('Введено неверное число')

while True:
    repeat = input("Продолжить? (да/нет): ")
    if repeat.lower() == 'нет':
        break
    else:
        house = choose_house()
        house.calculate()
