# AI Pacman Search

This project contains implementations of search algorithms for the Pacman AI framework.  
It is part of a lab/assignment on search strategies and demonstrates how algorithms work in a grid-based environment.

---

## 📂 Project Overview
The goal of this project is to explore classic search algorithms by applying them to Pacman mazes.  
Algorithms implemented include:
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search with heuristics

---

## ⚙️ Requirements
- Python 3.x  
- Git  
- (Optional) VS Code for editing  

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/jacksonharmon2/AI-pacman-search.git
   cd AI-pacman-search
python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
