# Math 407 Final Project
- Name: Richard Jiang
- Email: hjiang86@usc.edu
- Section: 39625

## Setup Steps
- This project requires python3, matplotlib, and numpy installed

### step 1: install python with packages: matplotlib, numpy
- https://www.python.org/downloads/
- https://matplotlib.org/stable/users/installing/index.html
- https://numpy.org/install/

### step 2: copy this program to your folder
- open one newly created empty folder in terminal and type 
```
git clone git@github.com:Msornerrrr/math407-project.git
```

### step 3: open the folder in terminal
- you'll get a folder with name math407-project
- open it and you'll see p1.py & p2.py
- you could then run the program with terminal

## Problem 1
```
python3 p1.py
```
### a) Plot points on sphere 
- run the program with the command above in terminal
- you will get a 3d graph of 1000 plotted points

### b) Estimate area of continents
- you will also get estimated area of Antarctica & Africa printed in the terminal

#### few comments
- the relative errors of two estimation are quite similar
- as we increase the points, the accuracy also increase, on average, we get closer to the actual value
- all of these make sense, since all points are uniformly distributed over the surface of the sphere


## Problem 2
```
python3 p2.py
```
- wait for a minute, you'll get a graph, blue -> Champernowne, green -> Copeland-Erdos
- the x-axis represents number of number concatenated
- the y-axis represents the ratio of number of 1 over number of 0
### Champernowne
- for the blue line, as the number concatenated increase, the ratio goes closer to 1
- so Champernowne number is quite random since number of 0 and 1 are close and become closer

### Copeland-Erdos
- for the green line, as the number concatenated increase, the ratio also goes closer to 1
- so Copeland-Erdos number is also random

#### compare those two number
- I notice that the line is closer to 1 for Champernowne number, which indicates that Champernowne number are more random
- However, the number of 1 is always slightly more than 0, so both number may actually not that random
- Randomness, in this case, is defined by the ratio of number of 1 and 0, since if trully random, the ratio should close to 1
