# Ghost Grid - System Definition

## 1. World
The world is a **network of interconnected nodes** organized into layers numbered from **0 to n**, representing different levels of security or distance in the environment.

### 1.1 World Structure
- Each **node** has a list of **connections** to other nodes, with **distance values** between **1 and 10**.
  - **Short distance (1 to 5):** Ghost can see what is in the destination node.
  - **Long distance (6 to 10):** Ghost cannot see what is in the destination node.
- **Connections between nodes are bidirectional**.
- A node belongs to a **specific layer (0 to n)**, and connections can move up to **3 layers**.
- The total loot in the game is **100 units** and can be divided into whole fractions.
- It can't be connections between nodes from the 0 layer to the n layer.

### 1.2 Initial Conditions
- **Ghost:**
  - Spawns in a random node of layer **0**.
  - Starts with **100 total loot**, divided among the Ghosts at the beginning of the game.
  - Has a base energy equivalent to the **average distance of the shortest paths between layer 0 and layer n**.
  - Can **replicate only on the first turn**, dividing the loot among its copies.
- **Sentinel:**
  - Spawns in a random node of layer **n - 1**.
  - Starts with no loot.
  - Their number is always **three times the number of Ghosts**.
  - Has **three times the base energy of Ghost**.
  - Can recharge energy if **another Sentinel is in the same node**, recovering **5% energy per turn**.

---

## 2. Perceptions
Each agent has different perception capabilities about the environment.

### 2.1 General Perceptions (All agents)
- Can see the **connected nodes** from their current position.
- Can see the **layer** of the destination node.
- Can know the **distance** of the path between connected nodes.

### 2.2 Ghost Perceptions
- **Knowledge of Replicas:** Does not know where its replicas are unless they are in the same node.
- **Loot Visibility:**
  - Can see if **there is loot in its current node**.
  - Can see if **there is loot in nodes accessible with a short distance (1-5)**.
  - **Remembers** where it left loot.
  - Can share this information **only when two Ghosts meet in the same node** (strategic meeting).

### 2.3 Sentinel Perceptions
- **Ally Position:** Can see where the other Sentinels are at all times.
- **Loot Detection:** Can detect if there is loot in the node they are in.
- **Structured Patrol:** Can mark nodes as "checked" to optimize their search.
- **Ghost Detection:**
  - If a Sentinel enters a node where there is a Ghost **with loot**, it can capture it immediately.
  - If the Ghost **has no loot**, the Sentinel knows a Ghost is in the node but **cannot apprehend it**.

---

## 3. Functions and Actions
Each agent has a set of available actions.

### 3.1 Ghost Actions
- **Movement:** Can move to a connected node, spending energy **equivalent** to the distance.
- **Deposit Loot:** Can leave a fraction or the total loot in the current node.
- **Take Loot:** Can collect loot from the node it is in.
- **Replicate:** Can create a copy of itself **only on the first turn**, dividing the loot among the Ghosts active at the beginning of the game.

### 3.2 Sentinel Actions
- **Movement:** Can move to a connected node, spending energy **equivalent** to the distance.
- **Recharge Energy:** If **two or more Sentinels are in the same node**, each one recovers **5% energy per turn**.
- **Capture Ghosts:** If it enters a node where there is a Ghost **with loot**, it captures it immediately.
- **Loot Recovery:** Can take loot from a node, but after doing so, **cannot move for the remainder of the pursuit**.
- **Structured Patrol:** Can mark nodes as checked to optimize the search for Ghosts.

---

## 4. Interactions and Reactions

### 4.1 Encounters Between Ghost and Sentinel
- If a Sentinel enters a node where there is a Ghost **with loot**, it captures it immediately.
  - If the captured loot exceeds **50**, the Sentinel turns into a Ghost and those **50 loot are lost**.
- If a Sentinel enters a node where there is a Ghost **without loot**, it cannot capture it.
  - However, **it knows a Ghost is there**.
  - If the Ghost has no energy to move, **it remains trapped in the node**.

### 4.2 Reward Distribution
- **Ghost:** The reward increases the more loot it delivers to layer **n**, but it is divided among the Ghosts **at the start of the game**.
- **Sentinel:** The reward increases with the amount of loot recovered and **multiplies** by the number of Ghosts captured.

---

## 5. Victory and Defeat Conditions
The game ends in the following scenarios:
1. **Time limit reached:** **5n turns** (where **n** is the number of node layers).
2. **Loot fully distributed:** When the **100 loot units are divided** between:
   - Ghosts that managed to bring loot to layer **n**.
   - Sentinels that recovered captured loot.

### 5.1 Victory Criteria
- **Ghost Victory:** If at least **one** manages to bring loot to layer **n**.
- **Sentinel Victory:** If the Sentinels manage to **capture all Ghosts** or recover the **majority of the loot**.
- **Draw:** If the amount of loot recovered by Sentinels and the loot transported by Ghosts is **close to 50%-50%**.

