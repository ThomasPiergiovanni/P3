# Project 3 - Help MacGyver to escape!

## 1. Introduction.
This python package is a 2D game named **'Help MacGyver to escape!'**. It consist of **moving the hero** (MacGyver) **on a maze** and **make him escape that place**. The hero will be able to leave that place if he **reaches the exit**. The problem, **a guard** is protecting the exit and he **has no intention to let our hero go out** so easily. Therefore, the hero will have to **collect all objects** dispatch here and there in the maze (a platic tube, a needle and a bottle of ether). This in order to build a syringe full of ether that will allow him to inject the guard and put him to sleep. **This is how, our hero can become a free again**. 

## 2. Prerequisite.
This programm requires the following components:
* **python 3**
* **pygame==1.9.6***

## 3. Installation.
### 3.1. Download.
Download/Clone this repository on your system, at the location that suits you best.

### 3.2. Python 3 install.
Make sure you have **Python 3** installed. If not, you can download it and install it from the [python offical website](https://www.python.org/). You'll find the necessary documentation there.

### 3.3. Create a virtual environment (*optionnal but recommended*).
In order to avoid system conflicts:
* Create a virtual environment using **venv** package.
> python3 -m venv myenv

* Activate the virtual envrionment.
> source myenv/Scripts/activate

Documentation is also available on [python offical website](https://www.python.org/).

### 3.4. Pygame install.
Install **pygame** on you virtual environement using the requirements.txt file.   
> pip install -r requirements.txt

If necessary documentation for pygame can be found on the [pygame website](https://www.pygame.org/news).

### 3.5. Play.
The programm is now ready to use. You can launch **launch.py** with your bash.  
> python3 launch.py  

### 3.6. Leave the virtual environment.
Once you're done with playing, you should leave the virtual environement. Simply type the following in your bash.
> deactivate  

### 3.7. Uninstall.
If you want to uninstall the game simply delete the complete repository.

## 4. Settings.
Changing settings can only be done to constants in the **constants.py** file.

#### 4.1. DATA_FILE
**Description** : Source data, the labyrinthe.  
**Mandatory** : Yes.  
**Settings** : "data/labyrinthe.txt" (default).  
**Comments** : File can contain only values "0" i.e. wall, "1" i.e. path,"2" i.e.  start and "3"  i.e. end. Raws and columns number can be changed but parity 'columns 'vs' raws' must be kept. If changed, make sure to set the constant NUMBER_OF_CELLS_PER_SIDE accordingly. 

#### 4.2. NUMBER_OF_CELL_PER_SIDE
**Description** : Number of cells (i.e. where player can potentially move) per labyrinthe side.     
**Mandatory** : Yes.   
**Settings** : 15 (default).  
**Comments** : Can be changed according to DATA_FILE file changes. See DATA_FILE commments. 

#### 4.3. CELL_SIZE
**Description** : Heights and width of a cell (in pixels).   
**Mandatory** : Yes.  
**Settings** : 32 (default).   
**Comments** :  Size is set accoring to the game images size (in pixel). Cannot be changed unless all games images, except IMAGE_GAMECOVER, are changed accordingly.

#### 4.4. OBJECTS
**Description** : Objects list.  
**Mandatory** : Yes.  
**Settings** : "Needle", "Plastic tube", "Ether"(default).  
**Comments** : Can be more numerous but only having the same name.  

#### 4.5. IMAGE_GAMECOVER
**Description** : Game cover image.  
**Mandatory** : Yes.    
**Settings** : 'data/gamecover480.png' (default).   
**Comments** : Can be changed but accordingly to the grid size dimensions (i.e. NUMBER_OF_CELL_PER_SIDE * CELL_SIZE ).

#### 4.6. IMAGE_\*
**Description** : Various cell images.   
**Mandatory** : Yes.    
**Settings** : 'data/\*32.png'.   
**Comments** : Can be changed but accordingly to the CELL_SIZE dimensions.

#### 4.7. COLOR_\*
**Description** : Various RGB colors for game messages.   
**Mandatory** : Yes.  
**Settings** : (R, G, B).  
**Comments** : Can be changed.

## 5. User's Guide.

### 5.1 Goal:
The goal is to make the hero escape the maze. For that he must:
* collect all objects present on the maze.
* go to the guard, and if all objects have been collected, escape the game usccesfully. If not, then the hero will loose.

### 5.2. How to:
* Launch the game running  **launch.py** file.
* On 'Menu' page, decide to play the game or not (if not is selected, then the programm will end) .
* Use **keyboards arrows** to move the hero in the maze.
* **Objects get collected automatically** when the hero arrives on their positions.
* **Game will end** successfuly or not **once the hero arrives at the guard position**.
* **Exit game** can be done at any time by clicking on the game **window right corner "x" button**.