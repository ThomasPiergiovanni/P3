# Project 3 - Help MacGyver to escape!

## 1. Introduction
This python package is a 2D game named 'Help MacGyver to escape!'. It consist of moving the hero (MacGyver) on a maze and make him escape that place. The hero will be able to leave that place if he reaches the exit. The problem, a guard is protecting the exit and he has no intention to let our hro go out so easily. Therefore, the hero will have to collect all objects dispatch here and there in the maze (a platic tube, a needle and a bottle of ether) in order to, thanks to this inventivity, build a syringe full of ether that will allow him to inject the guard put him to sleep and finally become a free hero again. 

## 2. Prerequisite

* python3
* pygame==1.9.6

## Installation

### 1. Download.
Download this repository on your system, at the location that suit you best.

### 2. Python3 install.
Ensure you have Python 3 installed. If not, you can download it and install it from the [python offical website](https://www.python.org/). You'll find the necessary documentation there.

### 3. Create a vitrtual environment (*optionnal but recommended*).
In order to avoid python version and libraries conflicts:
* Create a virtual environnment using
> venv 
package. Example:
    python -m venv my/game/repository/my_virtual_environnment
* Activate the created virtual envrionnment. Example:
    source my/game/repository/my_virtual_environnment/Scripts/activate
Documentation for this is also available on [python offical website](https://www.python.org/).

### 4. Pygame install.
Ensure you have Python 3 installed. If not, you can download it and install it from the [python offical website](https://www.python.org/). You'll find the necessary documentation there.
Install pygame on you virtual environnement. You can  install it from the [pygame website](https://www.pygame.org/news). You'll find the necessary documentation there to do so.

### 5. Play
The programm is now ready to use. You can lauch xxx.py with your bash:
    python xxx.py

### 6. Leave the virtual environment
Once you're done with playing, you should leave the virtual environnement. Simply type
    deactivate
in your bash.

### 7. Uninstall
If you want to uninstall the game simply delete the complete repository.

## Settings

* No settings required. Files & folders must not be modified.

## User Guide

### Goal:
The goal is to make the hero escape the maze. For that he must:
* collect all objects present on the maze.
* go to the guard, and if all objects have been collected, escape the game usccesfully. If not, then the hero will loose.

### How to:
* Launch the game running the xxx.py file.
* On 'Menu' page, decide to play the game or not (if not is selected, then the programm will end) .
* Use keyboards arrows to move the hero in the maze.
* Objects get collected automatically when hero arrives on their positions.
* Game will end successfuly or not once the hero arrives at the guard position.
* Exit game can be done at any time by clicking on the game window right corner "x" button.