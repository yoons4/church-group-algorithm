### Instructions on how to run program
1. Install networkx python library if it's not installed on your machine.
```
pip install networkx 
```
2. Run main.py
```
python findChurchGroup.py
```
3. Main method will ask you to type in: filename and group size

4. For the group1.txt, try group size of 4. For the group2.txt, try group size of 8. For the group3.txt, try group size of 6.


### 500 words discussion:
To find the set of sets of groups in the minimum amount of iterations, I used a greedy algorithm. Here, I see the problem as a graph problem. The program initializes the graph by making each node as a member of the church. Then, it connects each node with every other nodes in the graph. Each edge represents that the start node has not visited the end node. The goal is to remove all the edges from the graph. 

The program picks one of nodes when the node has the maximum indegree. Indegree of a node is the number of incoming edges. The reason why I pick the maximium indegree is because I want to make a person/couple with most unvisited people as the next host. After I pick the host, I include as many people as possible to create a new group. These visitors will never be assigned to another host. It means that the directed edges from the invited people to the host are removed. Then, the program repeats this loop for a new small group until we have enough small groups for this iteration.

The time complexity is O(n^6). The largest runtime occurs at the function names as find_solution from the main function. The function's outer loop is while loop, which figures out if edges from the graph are gone. This loop takes about O(e) because in order to escape this loop, number of edges (e) from this graph must be disappear. If each loop removes one edge in the worst case, it will take about O(e). Inside of this outer loop, the inner loop that compares the numbers from "groups" and "num_groups" is depending on the number of all nodes from the graph. So, it is O(n). Inside of the first inner loop, the loop that takes O(E*n) takes the longest runtime. Then, total runtime is O(n^2 * E^2). However, the number of edges is equal to (n * (n-1)). Then, E will be about n^2. As a result, O(E) is equal to O(n^2). The total runtime is evaluated as O(n^6).

I had couple of difficulties. First, I am not experienced in python coding. For example, I did not know how to indent correctly in order to make the loops working properly. Moreover, I did not know Python, so I had to learn Python. Fortunately, I found a website called Codecademy. I took lessons how to code in Python. Second, my algorithm solving is hard. My initial algorithm gave a wrong output and was not efficient. My idea is trying to make the source code that uses nested loops mainly to make a set of small groups. However, it takes a long time and efforts to complete it. Even after I finished coding, there were still errors. Then, I had to debug for many hours. I had to collaborate with other people by talking to them and getting new ideas, so I managed to producde an algorithm that works. I was able to finish the project.

### Screenshots of my program running
I uploaded SANGHA_YOON_SCREENSHOT1 and SANGHA_YOON_SCREENSHOT2.

### Set of sets for each file

For group1.txt with group size 4
```
Type file name: group1.txt
Type number of people per group: 4
Total 16
Names:  {0: 'A,B', 1: 'C,D', 2: 'E,F', 3: 'G,H', 4: 'I,J', 5: 'K,L', 6: 'M,N', 7: 'O,P'}
Iteration  0 : {'A,B': ['C,D'], 'E,F': ['G,H'], 'I,J': ['K,L'], 'M,N': ['O,P']}
Iteration  1 : {'C,D': ['A,B'], 'G,H': ['E,F'], 'K,L': ['I,J'], 'O,P': ['M,N']}
Iteration  2 : {'A,B': ['E,F'], 'C,D': ['G,H'], 'I,J': ['M,N'], 'K,L': ['O,P']}
Iteration  3 : {'E,F': ['A,B'], 'G,H': ['C,D'], 'M,N': ['I,J'], 'O,P': ['K,L']}
Iteration  4 : {'A,B': ['G,H'], 'C,D': ['E,F'], 'I,J': ['O,P'], 'K,L': ['M,N']}
Iteration  5 : {'E,F': ['C,D'], 'G,H': ['A,B'], 'M,N': ['K,L'], 'O,P': ['I,J']}
Iteration  6 : {'A,B': ['I,J'], 'C,D': ['K,L'], 'E,F': ['M,N'], 'G,H': ['O,P']}
Iteration  7 : {'I,J': ['A,B'], 'K,L': ['C,D'], 'M,N': ['E,F'], 'O,P': ['G,H']}
Iteration  8 : {'A,B': ['K,L'], 'C,D': ['I,J'], 'E,F': ['O,P'], 'G,H': ['M,N']}
Iteration  9 : {'I,J': ['C,D'], 'K,L': ['A,B'], 'M,N': ['G,H'], 'O,P': ['E,F']}
Iteration  10 : {'A,B': ['M,N'], 'C,D': ['O,P'], 'E,F': ['I,J'], 'G,H': ['K,L']}
Iteration  11 : {'I,J': ['E,F'], 'K,L': ['G,H'], 'M,N': ['A,B'], 'O,P': ['C,D']}
Iteration  12 : {'A,B': ['O,P'], 'C,D': ['M,N'], 'E,F': ['K,L'], 'G,H': ['I,J']}
Iteration  13 : {'I,J': ['G,H'], 'K,L': ['E,F'], 'M,N': ['C,D'], 'O,P': ['A,B']}
```
```
Type file name: group2.txt
Type number of people per group: 8
Total 29
Names:  {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'Sangha', 27: 'SPU', 28: 'Gremlin'}
Iteration  0 : {'A': ['B', 'C', 'D', 'E', 'F', 'G', 'H'], 'I': ['J', 'K', 'L', 'M', 'N', 'O', 'P'], 'Q': ['R', 'S', 'T', 'U', 'V', 'W', 'X'], 'Y': ['Z', 'Sangha', 'SPU', 'Gremlin']}
Iteration  1 : {'B': ['A', 'C', 'D', 'E', 'F', 'G', 'H'], 'J': ['I', 'K', 'L', 'M', 'N', 'O', 'P'], 'R': ['Q', 'S', 'T', 'U', 'V', 'W', 'X'], 'Z': ['Y', 'Sangha', 'SPU', 'Gremlin']}
Iteration  2 : {'C': ['A', 'B', 'D', 'E', 'F', 'G', 'H'], 'K': ['I', 'J', 'L', 'M', 'N', 'O', 'P'], 'S': ['Q', 'R', 'T', 'U', 'V', 'W', 'X'], 'Sangha': ['Y', 'Z', 'SPU', 'Gremlin']}
Iteration  3 : {'D': ['A', 'B', 'C', 'E', 'F', 'G', 'H'], 'L': ['I', 'J', 'K', 'M', 'N', 'O', 'P'], 'T': ['Q', 'R', 'S', 'U', 'V', 'W', 'X'], 'SPU': ['Y', 'Z', 'Sangha', 'Gremlin']}
Iteration  4 : {'E': ['A', 'B', 'C', 'D', 'F', 'G', 'H'], 'M': ['I', 'J', 'K', 'L', 'N', 'O', 'P'], 'U': ['Q', 'R', 'S', 'T', 'V', 'W', 'X'], 'Gremlin': ['Y', 'Z', 'Sangha', 'SPU']}
Iteration  5 : {'F': ['A', 'B', 'C', 'D', 'E', 'G', 'H'], 'N': ['I', 'J', 'K', 'L', 'M', 'O', 'P'], 'V': ['Q', 'R', 'S', 'T', 'U', 'W', 'X'], 'Y': ['Z', 'Sangha', 'SPU', 'Gremlin']}
Iteration  6 : {'G': ['A', 'B', 'C', 'D', 'E', 'F', 'H'], 'O': ['I', 'J', 'K', 'L', 'M', 'N', 'P'], 'W': ['Q', 'R', 'S', 'T', 'U', 'V', 'X'], 'Y': ['Z', 'Sangha', 'SPU', 'Gremlin']}
Iteration  7 : {'H': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'P': ['I', 'J', 'K', 'L', 'M', 'N', 'O'], 'X': ['Q', 'R', 'S', 'T', 'U', 'V', 'W'], 'Y': ['Z', 'Sangha', 'SPU', 'Gremlin']}
Iteration  8 : {'Y': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'Z': ['H', 'I', 'J', 'K', 'L', 'M', 'N'], 'Sangha': ['O', 'P', 'Q', 'R', 'S', 'T', 'U'], 'SPU': ['V', 'W', 'X', 'Gremlin']}
Iteration  9 : {'Gremlin': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'H': ['I', 'J', 'K', 'L', 'M', 'N', 'O'], 'P': ['Q', 'R', 'S', 'T', 'U', 'V', 'W'], 'X': ['Y', 'Z', 'Sangha', 'SPU']}
Iteration  10 : {'A': ['I', 'J', 'K', 'L', 'M', 'N', 'O'], 'B': ['P', 'Q', 'R', 'S', 'T', 'U', 'V'], 'C': ['W', 'X', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin'], 'D': ['E', 'F', 'G', 'H']}
Iteration  11 : {'D': ['I', 'J', 'K', 'L', 'M', 'N', 'O'], 'E': ['P', 'Q', 'R', 'S', 'T', 'U', 'V'], 'F': ['W', 'X', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin'], 'A': ['B', 'C', 'G', 'H']}
Iteration  12 : {'G': ['I', 'J', 'K', 'L', 'M', 'N', 'O'], 'Q': ['A', 'B', 'C', 'D', 'E', 'F', 'H'], 'R': ['P', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin', 'S'], 'T': ['U', 'V', 'W', 'X']}
Iteration  13 : {'I': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'J': ['H', 'Q', 'R', 'S', 'T', 'U', 'V'], 'K': ['W', 'X', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin'], 'L': ['M', 'N', 'O', 'P']}
Iteration  14 : {'L': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'M': ['H', 'Q', 'R', 'S', 'T', 'U', 'V'], 'N': ['W', 'X', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin'], 'I': ['J', 'K', 'O', 'P']}
Iteration  15 : {'O': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'S': ['H', 'I', 'J', 'K', 'L', 'M', 'N'], 'T': ['P', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin', 'Q'], 'R': ['U', 'V', 'W', 'X']}
Iteration  16 : {'U': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'V': ['H', 'I', 'J', 'K', 'L', 'M', 'N'], 'W': ['O', 'P', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin'], 'Q': ['R', 'S', 'T', 'X']}
Iteration  17 : {'SPU': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'X': ['H', 'I', 'J', 'K', 'L', 'M', 'N'], 'Y': ['O', 'P', 'Q', 'R', 'S', 'T', 'U'], 'Z': ['V', 'W', 'Sangha', 'Gremlin']}
Iteration  18 : {'Sangha': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'Gremlin': ['H', 'I', 'J', 'K', 'L', 'M', 'N'], 'R': ['O', 'V', 'W', 'Y', 'SPU'], 'Z': ['P', 'Q', 'S', 'T', 'U', 'X']}
Iteration  19 : {'T': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'H': ['P', 'Q', 'R', 'S', 'U', 'V', 'W'], 'I': ['X', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin', 'J'], 'K': ['L', 'M', 'N', 'O']}
Iteration  20 : {'A': ['P', 'Q', 'R', 'S', 'T', 'U', 'V'], 'B': ['I', 'J', 'K', 'L', 'M', 'N', 'O'], 'D': ['W', 'X', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin'], 'C': ['E', 'F', 'G', 'H']}
Iteration  21 : {'C': ['I', 'J', 'K', 'L', 'M', 'N', 'O'], 'E': ['W', 'X', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin'], 'F': ['P', 'Q', 'R', 'S', 'T', 'U', 'V'], 'A': ['B', 'D', 'G', 'H']}
Iteration  22 : {'G': ['P', 'Q', 'R', 'S', 'T', 'U', 'V'], 'J': ['A', 'B', 'C', 'D', 'E', 'F', 'W'], 'K': ['H', 'I', 'M', 'N', 'O'], 'L': ['X', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin']}
Iteration  23 : {'M': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'N': ['H', 'Q', 'R', 'S', 'T', 'U', 'V'], 'O': ['W', 'X', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin'], 'I': ['J', 'K', 'L', 'P']}
Iteration  24 : {'P': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'Q': ['I', 'J', 'K', 'L', 'M', 'N', 'O'], 'R': ['H', 'T', 'U', 'V', 'W', 'X'], 'S': ['Y', 'Z', 'Sangha', 'SPU', 'Gremlin']}
Iteration  25 : {'U': ['H', 'I', 'J', 'K', 'L', 'M', 'N'], 'V': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'SPU': ['O', 'P', 'Q', 'R', 'S', 'T', 'W'], 'X': ['Gremlin', 'Y', 'Z', 'Sangha']}
Iteration  26 : {'W': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'K': ['Q', 'R', 'S', 'T', 'U', 'V', 'Z'], 'Y': ['H', 'I', 'J', 'L', 'M', 'N', 'X'], 'Gremlin': ['O', 'P', 'Sangha', 'SPU']}
Iteration  27 : {'R': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'Sangha': ['H', 'I', 'J', 'K', 'L', 'M', 'N'], 'S': ['O', 'P', 'Q', 'T', 'V', 'W', 'X'], 'SPU': ['U', 'Y', 'Z', 'Gremlin']}
Iteration  28 : {'X': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'Z': ['O', 'R', 'K', 'L', 'M', 'N', 'P'], 'I': ['H', 'Q', 'S', 'T', 'U', 'V', 'W'], 'J': ['Y', 'Sangha', 'SPU', 'Gremlin']}
Iteration  29 : {'L': ['H', 'Q', 'R', 'S', 'T', 'U', 'V'], 'Gremlin': ['W', 'X', 'B', 'D', 'E', 'F', 'G'], 'A': ['Y', 'Z', 'Sangha', 'SPU', 'I', 'J', 'K'], 'C': ['P', 'M', 'N', 'O']}
Iteration  30 : {'T': ['H', 'I', 'J', 'K', 'L', 'M', 'N'], 'B': ['W', 'X', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin'], 'D': ['P', 'Q', 'R', 'S', 'U', 'V', 'A'], 'E': ['O', 'C', 'F', 'G']}
Iteration  31 : {'F': ['I', 'J', 'K', 'L', 'M', 'N', 'O'], 'G': ['W', 'X', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin'], 'H': ['T', 'A', 'B', 'C', 'D', 'E', 'R'], 'Q': ['P', 'S', 'U', 'V']}
Iteration  32 : {'K': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'M': ['W', 'X', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin'], 'O': ['H', 'Q', 'R', 'S', 'T', 'U', 'V'], 'I': ['J', 'L', 'N', 'P']}
Iteration  33 : {'N': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'P': ['H', 'X', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin'], 'U': ['O', 'Q', 'R', 'S', 'T', 'V'], 'W': ['I', 'J', 'K', 'L', 'M']}
Iteration  34 : {'S': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'V': ['O', 'P', 'Y', 'Z', 'Sangha', 'SPU', 'Gremlin'], 'H': ['X', 'Q', 'T', 'U', 'W'], 'R': ['I', 'J', 'K', 'L', 'M', 'N']}
Iteration  35 : {'Z': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'SPU': ['H', 'I', 'J', 'K', 'L', 'M', 'N'], 'Q': ['Y', 'Sangha', 'Gremlin', 'O', 'R', 'S', 'T'], 'U': ['P', 'V', 'W', 'X']}
Iteration  36 : {'C': ['Q', 'R', 'S', 'T', 'U', 'V', 'B'], 'E': ['I', 'J', 'K', 'L', 'M', 'N', 'D'], 'H': ['Y', 'Z', 'Sangha', 'SPU', 'Gremlin', 'F', 'G'], 'A': ['W', 'X', 'O', 'P']}
Iteration  37 : {'Gremlin': ['Q', 'R', 'S', 'T', 'U', 'V', 'A'], 'J': ['G', 'X', 'Z', 'B', 'C', 'D', 'E'], 'Y': ['K', 'W', 'F', 'H', 'I', 'L', 'M'], 'N': ['O', 'P', 'Sangha', 'SPU']}
Iteration  38 : {'U': ['Y', 'Z', 'Sangha', 'SPU', 'Gremlin', 'A', 'B'], 'Q': ['G', 'C', 'D', 'E', 'F', 'I', 'J'], 'W': ['H', 'N', 'K', 'L', 'M', 'R', 'S'], 'X': ['O', 'P', 'T', 'V']}
Iteration  39 : {'Sangha': ['V', 'W', 'X', 'B', 'C', 'E', 'F'], 'Q': ['Z', 'SPU', 'G', 'H', 'I', 'J', 'K'], 'A': ['Gremlin', 'L', 'M', 'N', 'O', 'P', 'R'], 'D': ['T', 'S', 'U', 'Y']}
Iteration  40 : {'I': ['R', 'A', 'B', 'C', 'D', 'E', 'F'], 'L': ['W', 'G', 'H', 'J', 'K', 'M', 'N'], 'T': ['O', 'P', 'Q', 'S', 'U', 'X', 'Z'], 'Y': ['V', 'Sangha', 'SPU', 'Gremlin']}
```

```
Type file name: group3.txt
Type number of people per group: 6
Total 34
Names:  {0: 'Sangha,A', 1: 'Ultra,B', 2: 'RAbbit,C', 3: 'Peter,D', 4: 'Time,E', 5: 'Theo,E', 6: 'Ghot,G', 7: 'Time,T', 8: 'Right,R', 9: 'Eater,Q', 10: 'Haunted,H', 11: 'Bee,F', 12: 'Space,S', 13: 'Yay,Y', 14: 'Leo,L', 15: 'Queen,Q', 16: 'House,H'}
Iteration  0 : {'Sangha,A': ['Ultra,B', 'RAbbit,C'], 'Peter,D': ['Time,E', 'Theo,E'], 'Ghot,G': ['Time,T', 'Right,R'], 'Eater,Q': ['Haunted,H', 'Bee,F'], 'Space,S': ['Yay,Y', 'Leo,L'], 'Queen,Q': ['House,H']}
Iteration  1 : {'Ultra,B': ['Sangha,A', 'RAbbit,C'], 'Time,E': ['Peter,D', 'Theo,E'], 'Time,T': ['Ghot,G', 'Right,R'], 'Haunted,H': ['Eater,Q', 'Bee,F'], 'Yay,Y': ['Space,S', 'Leo,L'], 'House,H': ['Queen,Q']}
Iteration  2 : {'RAbbit,C': ['Sangha,A', 'Ultra,B'], 'Theo,E': ['Peter,D', 'Time,E'], 'Right,R': ['Ghot,G', 'Time,T'], 'Bee,F': ['Eater,Q', 'Haunted,H'], 'Leo,L': ['Space,S', 'Yay,Y'], 'Queen,Q': ['House,H']}
Iteration  3 : {'Queen,Q': ['Sangha,A', 'Ultra,B'], 'House,H': ['RAbbit,C', 'Peter,D'], 'Time,E': ['Ghot,G', 'Time,T'], 'Theo,E': ['Right,R', 'Eater,Q'], 'Haunted,H': ['Space,S', 'Yay,Y'], 'Bee,F': ['Leo,L']}
Iteration  4 : {'Sangha,A': ['Peter,D', 'Time,E'], 'Ultra,B': ['Theo,E', 'Ghot,G'], 'RAbbit,C': ['Time,T', 'Right,R'], 'Eater,Q': ['Space,S', 'Yay,Y'], 'Leo,L': ['Haunted,H', 'Bee,F'], 'Queen,Q': ['House,H']}
Iteration  5 : {'Peter,D': ['Sangha,A', 'Ultra,B'], 'Ghot,G': ['RAbbit,C', 'Time,E'], 'Time,T': ['Theo,E', 'Eater,Q'], 'Right,R': ['Haunted,H', 'Bee,F'], 'Space,S': ['Queen,Q', 'House,H'], 'Yay,Y': ['Leo,L']}
Iteration  6 : {'Yay,Y': ['Sangha,A', 'Ultra,B'], 'Bee,F': ['RAbbit,C', 'Peter,D'], 'Queen,Q': ['Time,E', 'Theo,E'], 'House,H': ['Ghot,G', 'Time,T'], 'Right,R': ['Eater,Q', 'Space,S'], 'Haunted,H': ['Leo,L']}
Iteration  7 : {'Sangha,A': ['Theo,E', 'Ghot,G'], 'Ultra,B': ['Peter,D', 'Time,E'], 'RAbbit,C': ['Eater,Q', 'Haunted,H'], 'Time,T': ['Bee,F', 'Space,S'], 'Yay,Y': ['Right,R', 'Queen,Q'], 'Leo,L': ['House,H']}
Iteration  8 : {'Peter,D': ['RAbbit,C', 'Ghot,G'], 'Time,E': ['Sangha,A', 'Ultra,B'], 'Theo,E': ['Time,T', 'Haunted,H'], 'Eater,Q': ['Right,R', 'Leo,L'], 'Space,S': ['Bee,F', 'House,H'], 'Queen,Q': ['Yay,Y']}
Iteration  9 : {'Ghot,G': ['Sangha,A', 'Ultra,B'], 'Haunted,H': ['RAbbit,C', 'Peter,D'], 'Bee,F': ['Time,E', 'Theo,E'], 'Space,S': ['Time,T', 'Right,R'], 'Leo,L': ['Eater,Q', 'Queen,Q'], 'House,H': ['Yay,Y']}
Iteration  10 : {'Sangha,A': ['Time,T', 'Right,R'], 'Ultra,B': ['Eater,Q', 'Haunted,H'], 'RAbbit,C': ['Peter,D', 'Time,E'], 'Theo,E': ['Ghot,G', 'Bee,F'], 'Yay,Y': ['House,H'], 'Queen,Q': ['Space,S', 'Leo,L']}
Iteration  11 : {'Peter,D': ['Time,T', 'Right,R'], 'Time,E': ['RAbbit,C', 'Eater,Q'], 'Ghot,G': ['Theo,E', 'Haunted,H'], 'House,H': ['Sangha,A', 'Ultra,B'], 'Bee,F': ['Space,S', 'Yay,Y'], 'Leo,L': ['Queen,Q']}
Iteration  12 : {'Time,T': ['Sangha,A', 'Ultra,B'], 'Right,R': ['RAbbit,C', 'Peter,D'], 'Eater,Q': ['Time,E', 'Theo,E'], 'Haunted,H': ['Ghot,G', 'Queen,Q'], 'Yay,Y': ['Bee,F'], 'House,H': ['Space,S', 'Leo,L']}
Iteration  13 : {'Space,S': ['Sangha,A', 'Ultra,B'], 'Leo,L': ['RAbbit,C', 'Peter,D'], 'Time,E': ['Right,R', 'Haunted,H'], 'Theo,E': ['Yay,Y', 'Queen,Q'], 'Ghot,G': ['Eater,Q', 'Bee,F'], 'Time,T': ['House,H']}
Iteration  14 : {'Sangha,A': ['Eater,Q', 'Haunted,H'], 'Ultra,B': ['Time,T', 'Right,R'], 'RAbbit,C': ['Theo,E', 'Ghot,G'], 'Peter,D': ['Bee,F', 'Space,S'], 'Yay,Y': ['Time,E', 'Leo,L'], 'Queen,Q': ['House,H']}
Iteration  15 : {'Right,R': ['Sangha,A', 'Ultra,B'], 'Eater,Q': ['RAbbit,C', 'Peter,D'], 'Queen,Q': ['Ghot,G', 'Time,T'], 'Haunted,H': ['Time,E', 'Theo,E'], 'Bee,F': ['House,H', 'Space,S'], 'Yay,Y': ['Leo,L']}
Iteration  16 : {'Time,T': ['RAbbit,C', 'Peter,D'], 'Space,S': ['Time,E', 'Theo,E'], 'Yay,Y': ['Ghot,G', 'Eater,Q'], 'Leo,L': ['Sangha,A', 'Ultra,B'], 'Right,R': ['Queen,Q', 'House,H'], 'Haunted,H': ['Bee,F']}
Iteration  17 : {'Sangha,A': ['Bee,F', 'Space,S'], 'Ultra,B': ['Yay,Y', 'Leo,L'], 'RAbbit,C': ['Queen,Q', 'House,H'], 'Peter,D': ['Eater,Q', 'Haunted,H'], 'Time,T': ['Time,E', 'Theo,E'], 'Ghot,G': ['Right,R']}
Iteration  18 : {'Time,E': ['Bee,F', 'Space,S'], 'Theo,E': ['Sangha,A', 'Ultra,B'], 'Ghot,G': ['Peter,D', 'Yay,Y'], 'Eater,Q': ['Time,T', 'Queen,Q'], 'House,H': ['Right,R', 'Haunted,H'], 'RAbbit,C': ['Leo,L']}
Iteration  19 : {'Bee,F': ['Sangha,A', 'Ultra,B'], 'Queen,Q': ['RAbbit,C', 'Peter,D'], 'Haunted,H': ['Time,T', 'Right,R'], 'Space,S': ['Ghot,G', 'Eater,Q'], 'Yay,Y': ['Theo,E', 'House,H'], 'Leo,L': ['Time,E']}
Iteration  20 : {'Sangha,A': ['Yay,Y', 'Leo,L'], 'Ultra,B': ['Bee,F', 'Space,S'], 'Peter,D': ['Queen,Q', 'House,H'], 'Theo,E': ['RAbbit,C', 'Ghot,G'], 'Time,T': ['Haunted,H', 'Eater,Q'], 'Right,R': ['Time,E']}
Iteration  21 : {'Time,E': ['Yay,Y', 'Leo,L'], 'Ghot,G': ['Space,S', 'Queen,Q'], 'Eater,Q': ['Sangha,A', 'Ultra,B'], 'Bee,F': ['Time,T', 'Right,R'], 'House,H': ['Theo,E', 'RAbbit,C'], 'Peter,D': ['Haunted,H']}
Iteration  22 : {'Yay,Y': ['RAbbit,C', 'Peter,D'], 'Leo,L': ['Theo,E', 'Ghot,G'], 'Queen,Q': ['Right,R', 'Eater,Q'], 'Haunted,H': ['Sangha,A', 'Ultra,B'], 'House,H': ['Time,E', 'Bee,F'], 'Time,T': ['Space,S']}
Iteration  23 : {'RAbbit,C': ['Bee,F', 'Space,S'], 'Theo,E': ['Leo,L', 'House,H'], 'Time,T': ['Yay,Y', 'Queen,Q'], 'Eater,Q': ['Ghot,G', 'Sangha,A'], 'Ultra,B': ['Peter,D', 'Time,E'], 'Right,R': ['Haunted,H']}
Iteration  24 : {'Right,R': ['Theo,E', 'Yay,Y'], 'Space,S': ['RAbbit,C', 'Peter,D'], 'Sangha,A': ['Queen,Q', 'House,H'], 'Ghot,G': ['Leo,L', 'Ultra,B'], 'Time,E': ['Time,T', 'Eater,Q'], 'Haunted,H': ['Bee,F']}
Iteration  25 : {'Ultra,B': ['Queen,Q', 'House,H'], 'Peter,D': ['Yay,Y', 'Leo,L'], 'Bee,F': ['Ghot,G', 'Sangha,A'], 'Theo,E': ['Space,S', 'RAbbit,C'], 'Time,E': ['Time,T', 'Right,R'], 'Eater,Q': ['Haunted,H']}
Iteration  26 : {'Time,E': ['Queen,Q', 'House,H'], 'Yay,Y': ['Time,T', 'Haunted,H'], 'Leo,L': ['Right,R', 'Sangha,A'], 'Ultra,B': ['RAbbit,C', 'Peter,D'], 'Theo,E': ['Ghot,G', 'Eater,Q'], 'Bee,F': ['Space,S']}
Iteration  27 : {'Queen,Q': ['Haunted,H', 'Bee,F'], 'RAbbit,C': ['Yay,Y', 'Sangha,A'], 'Ghot,G': ['House,H', 'Ultra,B'], 'Time,T': ['Leo,L', 'Peter,D'], 'Time,E': ['Theo,E', 'Right,R'], 'Eater,Q': ['Space,S']}
Iteration  28 : {'Right,R': ['Leo,L', 'Sangha,A'], 'Eater,Q': ['House,H', 'Ultra,B'], 'Bee,F': ['Queen,Q', 'RAbbit,C'], 'Space,S': ['Haunted,H', 'Peter,D'], 'Time,E': ['Theo,E', 'Ghot,G'], 'Time,T': ['Yay,Y']}
Iteration  29 : {'Haunted,H': ['House,H', 'Sangha,A'], 'Leo,L': ['Time,T', 'Ultra,B'], 'RAbbit,C': ['Peter,D', 'Time,E'], 'Theo,E': ['Ghot,G', 'Right,R'], 'Eater,Q': ['Bee,F', 'Space,S'], 'Yay,Y': ['Queen,Q']}
Iteration  30 : {'House,H': ['Eater,Q', 'Sangha,A'], 'Ultra,B': ['RAbbit,C', 'Peter,D'], 'Time,E': ['Theo,E', 'Ghot,G'], 'Time,T': ['Right,R', 'Haunted,H'], 'Bee,F': ['Space,S', 'Yay,Y'], 'Leo,L': ['Queen,Q']}
```

### YouTube Video

https://youtu.be/3z-wB6Y7YGY