This repro contains a gym environment for the card game witches by amigo.

In order to test the gym as well as training a Neuronal Network using Proximal Policy Optimization check the **Tutorials**.

You can play and test your trained neuronal network at **https://idgaming.de/**.

## Installation
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

In order to successful run the tutorials make sure to install the requirements.txt file:
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

### 04_Policy_PPO
* include training a neuronal network
* included classes ActorModel, ActorCritic, PPO
```bash
pip install torch
pip install onnx
pip install onnxruntime
```

* As you can see in the output below the batch size is slowly increasing
* The learning rate (lr) remains constant
* The network learns slowly correct actions (playing correct cards)

Output:
```
Creating model: Witches_multi-v2
Model state  dimension: 255
Model action dimension: 60
Parameters for training:
 Latent Layers: 128
 Learing Rate: 0.01  betas  (0.9, 0.999)
 Gamma:  0.99
 Epochs to train:  16
 Epsillon 0.2  decay:  266
 Batch size: 3000 Increase Rate: 10 0


Game ,0030000, mean_rew of 0 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,0.4448, mean_rew ,-1e+02,   0:01:02.479871,playing t=47.7, lr=0.01, batch=29850
Game ,0090300, mean_rew of 0 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,1.331, mean_rew ,-1e+02,   0:02:56.216046,playing t=38.98, lr=0.01, batch=60019
Game ,0151000, mean_rew of 0 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,2.613, mean_rew ,-1e+02,   0:05:04.079445,playing t=48.09, lr=0.01, batch=60444
Game ,0212100, mean_rew of 0 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,3.815, mean_rew ,-1e+02,   0:06:52.493726,playing t=35.36, lr=0.01, batch=60871
Game ,0273600, mean_rew of 0 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,5.399, mean_rew ,-1e+02,   0:08:49.359569,playing t=36.48, lr=0.01, batch=61328
Game ,0335500, mean_rew of 0 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,6.54, mean_rew ,-1e+02,   0:10:52.130442,playing t=35.27, lr=0.01, batch=61698
Game ,0397800, mean_rew of 0 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,7.667, mean_rew ,-1e+02,   0:12:53.752518,playing t=34.44, lr=0.01, batch=62057
Game ,0460500, mean_rew of 8 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,8.468, mean_rew ,-99.8,   0:15:06.189430,playing t=35.24, lr=0.01, batch=62417
Game ,0523600, mean_rew of 50 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,9.415, mean_rew ,-99.0,   0:17:27.621622,playing t=36.44, lr=0.01, batch=62842
Game ,0587100, mean_rew of 172 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,9.969, mean_rew ,-96.6,   0:19:48.402482,playing t=34.53, lr=0.01, batch=63206
Game ,0651000, mean_rew of 458 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,10.82, mean_rew ,-90.8,   0:22:11.855146,playing t=38.55, lr=0.01, batch=63610
Game ,0715300, mean_rew of 491 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,11.12, mean_rew ,-90.2,   0:24:46.470695,playing t=39.03, lr=0.01, batch=63929
Game ,0780000, mean_rew of 807 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,11.75, mean_rew ,-83.9,   0:27:09.343374,playing t=34.38, lr=0.01, batch=64330
Game ,0845100, mean_rew of 1578 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,12.38, mean_rew ,-68.4,   0:29:44.233056,playing t=36.56, lr=0.01, batch=64741
Game ,0910600, mean_rew of 1744 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,12.57, mean_rew ,-65.1,   0:32:42.284432,playing t=41.14, lr=0.01, batch=65096
Game ,0976500, mean_rew of 2124 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,12.79, mean_rew ,-57.5,   0:35:44.918884,playing t=44.99, lr=0.01, batch=65624
Game ,1042800, mean_rew of 2314 finished g. ,0.0, of random ,0.0, corr_moves[max:17] ,13.15, mean_rew ,-53.7,   0:38:32.994020,playing t=40.84, lr=0.01, batch=65888

```

### 05_UsePreTrainedModel

### 08_MCTS_Example
* TODO check my old code for this!



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
|2020.08.22| added test randomplaying case and tut_04 | added_tut_04  |

## TODO
- check that count Result works correctly
- test learning in tutorial_04
- player has now a type not in the game! TODO implement this !
- fuege room klasse methoden noch zu game hinzu
