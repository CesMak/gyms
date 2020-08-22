## Changelog
|Date|Description|commit|
|-|---------|-|
|2020.08.14| sudo apt install pylint to export nice graphs using 'pyreverse -o png gameClasses.py witches.py'  |  |

## Installation Linux (Ubuntu)
```
clone repro

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

pip freeze > requirements.txt

use pip freeze for requirements

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
