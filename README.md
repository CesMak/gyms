This repro contains a gym environment for the card game witches by amigo.

In order to test the gym as well as training a Neuronal Network using Proximal Policy Optimization check the **Tutorials**.

You can play and test your trained bot (ai) at **https://idgaming.de/**.

## Installation Linux (Ubuntu)
```bash
git clone git@github.com:CesMak/gyms.git
sudo apt install python-pip
sudo apt install python3-venv
python3 -m venv gym_env
source gym_env/bin/activate
#optional: alias ss_gym='cd ~/witches; source ../gym_env/bin/activate'
pip3 install -r requirements.txt # the requirements.txt file is in the Tutorials folder
```

## Install gym environment
```bash
cd gym
pip install -e .
```

## Tutorials

In order to sucessfully run the tutorials make sure to install the requirements.txt file:
```bash
pip3 install -r requirements.txt # the requirements.txt file is in the Tutorials folder
```

### 01_GenerateGymData
```bash
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
* uses ray for parallel batch generation
* pip install ray==0.8.1
* python3 gen_batches_parallel.py
* is 33% faster

```
2020-08-22 19:10:56,149	WARNING worker.py:682 -- WARNING: Not updating worker name since `setproctitle` is not installed. Install this with `pip install setproctitle` (or ray[debug]) to enable monitoring of worker processes.
2020-08-22 19:10:56,156	INFO resource_spec.py:212 -- Starting Ray with 7.08 GiB memory available for workers and up to 3.54 GiB for objects. You can adjust these settings with ray.init(memory=<bytes>, object_store_memory=<bytes>).
2020-08-22 19:10:56,397	WARNING services.py:1080 -- Failed to start the dashboard. The dashboard requires Python 3 as well as 'pip install aiohttp psutil setproctitle grpcio'.
Creating model: Witches_multi-v2
Model state  dimension: 255
Model action dimension: 60

Benchmark playing 10000 games
Took: 0:00:19.996094 Number of batches:  99420
```

### 04_Include_Policy_PPO
* include classes Actor Critic PPO


### 05_Include Monte Carlo Tree search random sampling




## Further Notes
```bash
pip freeze > requirements.txt
# to export class model graph:
#sudo apt install pylint
pyreverse -o png gameClasses.py witches.py
```

## General gym design
* alles in einer Datei dass einfacher
* Karten Anzahl und Spieleranzahl sowie unterschiedliche Spiele sollen unterstützt werden


## Changelog
|Date|Description|commit|
|-|---------|-|
|2020.08.14| |initial_commit  |
|2020.08.22| included witches class that inherits from game class |changed_to_inherit  |
|2020.08.22| added color free tests | added_color_free_test  |
|2020.08.22| added ray batch generation | added_tut_03  |

## TODO
- check that count Result works correctly
- test learning in tutorial_04
- player has now a type not in the game! TODO implement this !
- fuege room klasse methoden noch zu game hinzu
