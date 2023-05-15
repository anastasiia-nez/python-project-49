### Hexlet tests and linter status:
[![Actions Status](https://github.com/anastasiia-nez/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/anastasiia-nez/python-project-49/actions)

### Maintainability:
[![Maintainability](https://api.codeclimate.com/v1/badges/d8cb7553b2ceef7c8dd2/maintainability)](https://codeclimate.com/github/anastasiia-nez/python-project-49/maintainability)

### Description
 "Brain Games" is a set of five console games based on popular mobile brain training apps.
Each game asks questions that need to be answered correctly.
After three correct answers, the game is considered to be completed.
Wrong answers end the game and offer to play it again.

The project consists of the main folder "brain_games" and auxiliary files.
"brain_games" itself includes "game_engine.py",which is the engine of all games,
"games" subsection with the logic of each game, and "scripts" subsection with scripts that launch games.

To add a new game to the project, you need to create a file with its logic in the "games" folder and a file in the "scripts" folder that launches the game.
Also in the pyproject.toml in the "tool.poetry.scripts" section, you need to make an appropriate entry about the new game.

To install games, you need to clone the project on your device.
Next, you need to sequentially enter the make-commands "install",
"build", "publish", "package-install" while in the cloned repository.

#### Games:

      - brain-calc         -Calculator. Arithmetic expressions to be evaluated
      - brain-progression  -Finding missing numbers in a sequence of numbers
      - beain-even         -Definition of an even number
      - brain-gcd          -Definition of the Greatest Common Divisor
      - brain-prime        -Definition of prime number

### Examples:
[![asciicast](https://asciinema.org/a/5jG4VIkF3tcjBRfiBycFJZKgC.svg)](https://asciinema.org/a/5jG4VIkF3tcjBRfiBycFJZKgC)

[![asciicast](https://asciinema.org/a/573440.svg)](https://asciinema.org/a/573440)

[![asciicast](https://asciinema.org/a/573624.svg)](https://asciinema.org/a/573624)

[![asciicast](https://asciinema.org/a/574996.svg)](https://asciinema.org/a/574996)

[![asciicast](https://asciinema.org/a/575054.svg)](https://asciinema.org/a/575054)

