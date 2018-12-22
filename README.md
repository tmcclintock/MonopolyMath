# MonopolyMath

Monopoly is a terrible board game. One realizes this after the age of ten. However, Monopoly is actually a very beautiful game, mathematically speaking. This repository offers some neat tools to simulate the game of Monopoly so that we can look at the mathematical properties of the game. Specifically, you can find here the means to simulate an arbitrary number of rolls in order to numerically calculate the probability of landing on each space. Additionally, you can acquire the "transition matrix" of the game, or the matrix that describes the probability of landing on any other square starting from any particular square. This incorporate such game mechanics as the jail, doubles to escape jail, chance, and community chest cards.

## Installation

To install just do:
```bash
python setup.py install
```
If you are missing any requirements, you can install them with `pip` using
```bash
pip install -r requirements.txt
```
Once the package is installed, run the unit tests with
```bash
pytest
```
If any tests fail, please copy the test output into an issue on GitHub. Thank you!