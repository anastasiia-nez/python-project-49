from random import randint
import prompt
import brain_games.scripts.brain_games
import brain_games.cli


def generate_rand_num():
    radius_of_random = (1, 30)
    rand_num = randint(radius_of_random[0], radius_of_random[1])
    return rand_num


def main(task_text, game_func):
    brain_games.scripts.brain_games.main()

    print(task_text)
    i = 1
    ROUNDS_AMOUNT = 3

    while i <= ROUNDS_AMOUNT:
        question_text, correct_answer = game_func()
        print(question_text)
        answer = prompt.string('Your answer: ')

        if answer.lower() == correct_answer:
            if i == ROUNDS_AMOUNT:
                print(f'Congratulations, {brain_games.cli.name}!')
            else:
                print('Correct!')
            i += 1
        else:
            i += 3
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {brain_games.cli.name}!")
