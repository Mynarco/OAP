# Сак-221

import random

random.seed()


class BlackJack:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'] * 4
        self.score = 0
        self.bot_score = 0
        random.shuffle(self.deck)

    def print_card(self, current, score, bot):
        if not bot:
            print(f'Вам попалась карта {current}. У вас {score} очков.')
        else:
            print(f'Крупье попалась карта {current}. У крупье {score} очков')

    def random_card(self, score, bot):
        current = self.deck.pop()
        if type(current) is int:
            score += current
        elif current == 'Ace':
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += 10
        self.print_card(current, score, bot)
        return score

    def choice(self):
        score = self.random_card(self.score, False)
        bot_score = self.random_card(self.bot_score, True)
        while True:
            choice = input('Будете брать карту? y/n\n')
            if choice == 'y':
                score = self.random_card(score, False)
                if bot_score < 19 and score <= 21:
                    bot_score = self.random_card(bot_score, True)
                if score > 21 or bot_score == 21:
                    print('Извините, но вы проиграли')
                    return
                elif score == 21 and bot_score == 21:
                    print('Ничья')
                    return
                elif score == 21 or bot_score > 21:
                    print('Поздравляю, вы победили!')
                    return
            elif choice == 'n':
                if score > bot_score and bot_score < 19:
                    while bot_score < 19:
                        bot_score = self.random_card(bot_score, True)
                if score < bot_score <= 21:
                    print(f'Вы проиграли, у вас {score} очков, у крупье {bot_score} очков')
                else:
                    print(f'Вы победили, у вас {score} очков, у крупье {bot_score} очков')
                return

    def start(self):
        print('Игра в BlackJack началась')
        print('В блэкджеке десятки, валеты, дамы и короли стоят по 10 очков.\nТуз может стоить 1 или 11 очков')
        print('----------------------------------')
        while True:
            self.reset_game()
            self.choice()
            play_again = input('Хотите сыграть ещё раз? y/n\n')
            if play_again.lower() != 'y':
                print('Спасибо за игру! До новых встреч!')
                break


game = BlackJack()
game.start()