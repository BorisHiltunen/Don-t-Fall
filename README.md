# Don't Fall

## Description
Don't Fall is a Python game project that uses Pygame library. In the game your objective is to cross a bridge and not fall. The player has to find out the correct path by counting the calculation given by the game's calculation board. The Don-t-Fall app also contains music and sounds. The game can be used for learning or just be played for fun. It can also be customized with different pictures, words, sounds or music.

## Authors
Boris Hiltunen ([BorisHiltunen](https://github.com/BorisHiltunen))

## Tools and Libraries
- [Pygame](https://www.pygame.org/docs/)
- You can find required packets from requirements.txt

## Setup
- Clone or fork the repository.

- Install virtualenv if not already
-> (pip install virtualenv)

- Make an Virtual Environment
-> (virtualenv env)

- Access it
-> (Windows -> .\env\Scripts\activate -> Mac source env/bin/activate)

- Install requirements.txt
-> (pip install -r requirements.txt)

- Run
-> (Go inside refactored folder and write python runner.py)

## Game's structure
```GAP
- ├── env
- ├── game
- |   ├── refactored
- |   |   ├── app
- |   |   |   ├── __init__.py
- |   |   |   ├── cube_management.py
- |   |   |   ├── event_analyser.py
- |   |   |   ├── file_management.py
- |   |   |   ├── game_data.py
- |   |   |   ├── game_visualizer.py
- |   |   |   ├── path_management.py
- |   |   |   ├── roller.py
- |   |   ├── images
- |   |   ├── music
- |   |   ├── sounds
- |   |   ├── __init__.py
- |   |   ├── runner.py
- |   ├── unrefactored
- ├── progress
- ├── testing
- ├── .qitignore
- ├── picture_of_the_game.jpg
- ├── picture_of_the_game.png
- ├── README.md
- ├── requirements
```

## Demonstration

<p align="center">
  <img src="https://github.com/BorisHiltunen/Don-t-Fall/raw/main/picture_of_the_game.png"/>
</p>
