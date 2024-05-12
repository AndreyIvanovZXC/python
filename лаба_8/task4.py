import random

def generate_doors(num_doors, num_prizes):
    doors = ["пусто"] * num_doors
    prize_indices = random.sample(range(num_doors), num_prizes)
    for idx in prize_indices:
        doors[idx] = "приз"
    return doors

def simulate_game(num_doors, num_prizes):
    doors = generate_doors(num_doors, num_prizes)
    player_choice = random.randint(0, num_doors - 1)  # Игрок выбирает дверь
    revealed_door = random.choice([idx for idx, content in enumerate(doors) if content == "пусто" and idx != player_choice])
    # Ведущий открывает одну из пустых дверей
    remaining_doors = [idx for idx in range(num_doors) if idx != revealed_door and idx != player_choice]
    # Игрок выбирает, остаться при своем выборе или изменить
    player_stays = random.choice([True, False])
    if player_stays:
        return doors[player_choice] == "приз"
    else:
        return doors[remaining_doors[0]] == "приз"

def calculate_win_probabilities(num_doors, num_prizes, num_simulations):
    switch_wins = 0
    stay_wins = 0
    for _ in range(num_simulations):
        if simulate_game(num_doors, num_prizes):
            switch_wins += 1
        else:
            stay_wins += 1
    switch_win_prob = switch_wins / num_simulations
    stay_win_prob = stay_wins / num_simulations
    return switch_win_prob, stay_win_prob

num_doors = 3
num_prizes = 1
num_simulations = 10000

switch_win_prob, stay_win_prob = calculate_win_probabilities(num_doors, num_prizes, num_simulations)

print("Вероятность выигрыша для игрока, меняющего свой выбор:", switch_win_prob)
print("Вероятность выигрыша для игрока, оставшегося при своем первоначальном выборе:", stay_win_prob)