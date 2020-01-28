# Dijkstra implementation in Python

This is a sample implementation of the Dijkstra Algorithm, which finds the path
with the lowest cummulative cost between two nodes in a map.

To use it, just make a csv specifying the list of connections between nodes
in the following format 'origin, destination, cost'. Example:

```
a,b,10
b,c,5
a,c,20
```

Routes can be unidirectional, or have different prices on each way.

To calculate the shortest patch among any two nodes:

$ python3 dijkstra.py paths.csv a c
```
$ python3 paths.csv a c
```

Which in the case of the above csv would yield:

```
a -> b
b -> c
Total cost: 15
```
