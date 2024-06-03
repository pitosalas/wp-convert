---
title: "Daily ChatGPT: Solve a simple network traversal"
author: Pito Salas
date: 2023-05-19
---

Tell me how this is simple word completion. Can this be broadened to a more
complicated network. Could it be used for some kind of semi-intelligent
navigation?

## Prompt:

Assume a map that is described in sentences, with node names and costs to go
between nodes. Here is map1:

Node A costs 5 to got to Node C and 10 to go to Node D  
Node C costs 100 to go to node E and 50 to go to node F  
Node D costs 10 to go to node E and 100 to go to node F

What is the best route to go from Node A to node E? And what is the best route
to go from Node A to node F?

## Response:

To find the best route from Node A to Node E, we need to calculate the total
cost for each possible path.

Path 1: Node A -> Node C -> Node E  
Cost: 5 (A to C) + 100 (C to E) = 105

Path 2: Node A -> Node D -> Node E  
Cost: 10 (A to D) + 10 (D to E) = 20

The best route from Node A to Node E is Path 2 (A -> D -> E) with a total cost
of 20.

To find the best route from Node A to Node F, we need to calculate the total
cost for each possible path.

Path 1: Node A -> Node C -> Node F  
Cost: 5 (A to C) + 50 (C to F) = 55

Path 2: Node A -> Node D -> Node F  
Cost: 10 (A to D) + 100 (D to F) = 110

The best route from Node A to Node F is Path 1 (A -> C -> F) with a total cost
of 55.


* **Link to site:** **[Daily ChatGPT: Solve a simple network traversal](None)**
