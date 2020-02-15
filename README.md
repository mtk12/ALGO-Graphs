# ALGO-Graphs
Implementation and Evaluation of Graph Algorithms 

# Abstract:
In this project we have implemented Prims, Kruskal, Dijkstra, Bellman Ford, and Floyd Warshall,
Clustering Coefficient algorithms on the benchmarks with increasing number of nodes (from 10 to
100). In output, we are displaying the graphical representation of mapping and the final output in
the form of the minimum cost.

# Introduction:
There are many methods for making graph plots. Many languages support the graph
visualization. In this project we have used python. Python’s library Plotly is used for making
interactive graph visualization. So, after user inputs the file we have extracted the relevant
information and made the adjacency matrix. The adjacency is later used for calculating the cost
of the different algorithms.

# Proposed system:
The system is working as follows:
1. The user will enter the benchmark file in the input button.
2. In the backend the file is parsed, and the relevant information is parsed to make the
adjacency matrix.
3. On the basis of the adjacency matrix the graph is plotted, and the algorithms are
applied
4. The plotting is shown on the screen.
<br>The input is transferred from html frontend to python running on backend and the file is
parsed and the values are stored. When user invokes the button of the algorithm the html set
the value to that algorithm and send request to backend (Python). Against the request the
graph is generated, and the cost is displayed on the frontend. Additionally, the path is also
highlighted which is selected for the cost calculation.

# Experimental Setup:
The input of this system is the benchmark file which contain graph information with bandwidth
given as weights. Any other format of graph representation will give an error. The user will
select the input file button and select the benchmark file and the he will be redirected to the
new blank page where different algorithm buttons are shown when specific algorithm button is
clicked the user will be shown the graph plotted against the benchmark file and the cost of the
algorithm.

# Screenshots:
<br>
<img src="https://github.com/mtk12/ALGO-Graphs/blob/master/src/al.JPG"/>
<br>
<br>
<img src="https://github.com/mtk12/ALGO-Graphs/blob/master/src/al2.JPG"/>

# References:
1. Anany V. Levitin. 2006. Introduction to the Design and Analysis of Algorithms
(2nd Edition). Addison-Wesley Longman Publishing Co., Inc., Boston, MA,
USA.<br>2.https://plot.ly/python/(plotly documentation)<br>3.https://networkx.github.io/documentation/stable/(networkx documentation)
