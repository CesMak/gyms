## Installation Linux (Ubuntu)
```
git clone git@github.com:CesMak/gyms.git
sudo apt install python-pip
sudo apt install python3-venv
python3 -m venv gym_env
source gym_env/bin/activate
optional: alias ss_gym='cd ~/witches; source ../gym_env/bin/activate'
```

## Install gym environment
```
cd gym
pip install -e .
```

## Changelog
|Date|Description|commit|
|-|---------|-|
|2020.08.14| |initial_commit  |
|2020.08.22| included witches class that inherits from game class |changed_to_inherit  |

## Further Notes
```
pip freeze > requirements.txt
# to export class model graph:
#sudo apt install pylint
pyreverse -o png gameClasses.py witches.py
```

## Tutorials

### 01_GenerateGymData
```
/01_Tutorials/01_GenerateGymData$ python test_gym.py
```

In case of an incorrect move the output should be:

```
Creating model: Witches_multi-v2
Model state  dimension: 255
Model action dimension: 60
Caution player does not have card: 2 of B_1  choose one of: [3 of B_2, 4 of B_3, 7 of B_6, 10 of B_9, 1 of G_15, 2 of G_16, 6 of G_20, 10 of G_24, °11° of G_25, 15 of G_29, 1 of R_30, 7 of R_36, 10 of R_39, 4 of Y_48, 10 of Y_54]

 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1
 0 0 0 0 1 0 0 0 1 1 0 0 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 0 1 0 0 1 0 0 0 0 1
 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
 0 1 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 1 1 0 0 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 0
 1 0 0 1 0 0 0 0 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0] -100 True {'round_finished': False, 'correct_moves': 0}
```

In case of a correct move the output should change to:

```
Creating model: Witches_multi-v2
Model state  dimension: 255
Model action dimension: 60
[0] 3 Tim	 shifts RL	Card 2 of B_1	Card Index 1	 len 15

 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 1 1 1 0 0 0
 0 1 1 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 1 0 1 0 0 0 0 0
 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
 1 0 0 1 1 1 0 0 0 0 1 1 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0
 0 1 0 1 0 0 0 0 0 0 0 0 1 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0] 0 False {'round_finished': False, 'correct_moves': 1}
```

### 02_GenerateBatches

Generate Data which is used later on to train a policy.

```
Creating model: Witches_multi-v2
Model state  dimension: 255
Model action dimension: 60
Number of steps in one game: 17

Caution player does not have card: 12 of B_11  choose one of: [4 of B_3, 14 of B_13, 15 of B_14, 1 of G_15, 4 of G_18, °11° of G_25, 12 of G_26, 2 of R_31, 12 of R_41, 13 of R_42, 2 of Y_46, 3 of Y_47, 6 of Y_50, 7 of Y_51, 10 of Y_54]
Caution option idx 11 not in (idx) [3, 13, 14, 15, 18, 25, 26, 31, 41, 42, 46, 47, 50, 51, 54]


Actions: [11]
State  : [array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0,
       0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0,
       1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
       1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0,
       0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0])]
Rewards: [-100]
LogProb: [0.2]
Done   : [True]

Benchmark playing 100000 games
Took: 0:00:30.598447 Number of batches:  99586
```

### 03_Parallel_Batch_Generation
uses ray

TODO
fuege schafkopf hinzu bzw ueberlege welche aenderungen noetig waeren...
dass man nur kleine extra klasse schafkopf braucht!

- player has now a type not in the game! TODO implement this !


Todo definiere klasse sauber
fuege room klasse und witches klasse hinzu
nutze auch noch allgemeine game klasse?

room klasse wohl er nicht aber viele methoden von helper klasse in gameClasses mit rein


## Generelles Konzept gameClasses
* alles in einer Datei dass einfacher
* Karten Anzahl und Spieleranzahl sowie unterschiedliche Spiele sollen unterstützt werden
