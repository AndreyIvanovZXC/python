import random
def computer_question():
    question = [
        "как тебя зовут?",
        "где ты живешь?",
        "где ты учишься?",
        "какой твой любимый цвет",
        "на чем ты програмируешь",
        "где ты учишься?",
        "кем хочешь работать?",
        "какие фильмы смотришь?",
        "в какую страну хочешь поехать",
        "какую машину ты себе хочешь?"
    ]
    return random.choice(question)
def computer_otvet():
    otvet = [
        "да",
        "абсолютно",
        "нет",
        "возможно",
        "сомнительно но ОКЭ",
        "мало вероятно",
        "Майбах",
        "швеция",
        "пайтон",
        "МГУ!"
    ]
    return random.choice(otvet)
def play_game():
    computer_hot = random.random < 0.7
    if computer_hot:
        print("Компьютер бросает мяч")
        print("Вы поймали мяч")
        question = ("Вопрос:")






















play_game()
