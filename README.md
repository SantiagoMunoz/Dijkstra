# Dijkstra implementation in Python

This is a sample implementation of the Dijkstra Algorithm, which finds the path
with the lowest cummulative cost between two nodes in a map.

To use it, just need to have a csv specifying the list of connections between nodes
in the following format 'origin, destination, cost'. The actual nodes will be
infered from the list of routes. Example:

```
a,b,10
b,c,5
a,c,20
```

To calculate the shortest patch among any two nodes:

```
$ python3 paths.csv a c
```

Which in the case of the above csv would yield:

```
a -> b
b -> c
Total cost: 15
```
