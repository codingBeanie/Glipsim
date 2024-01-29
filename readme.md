![Glipsim](https://raw.githubusercontent.com/codingBeanie/Glipsim/main/doc/glipsim_banner.webp)

This is a *Django* server which runs a virtual life simulation of a fictional fantasy population of Glips. The website for exploring the simulation will be available here: [INSERT URL] (not yet deployed).

In brief, a summary of the basic mechanics is following in this document. For a more extensive documentation check this: [INSERT URL] (not yet implemented).

For the current road map and planned features check this: [road map](https://github.com/codingBeanie/Glipsim/blob/main/todo.md)


## Glips
A Glip is a pretty simple genderless creature with a individual dna. The dna sequence consists of different genes that determine special preferences, appearence and other behavioural attributes.

## The Simulation
The simulation operates as a turn-based system. A turn represents one time-unit (e.g. a year). On each turn a number of phases is called sequentially. Each phase triggers specific functions and calculations. After the last phase is completed, the next turn is started.

### Phase 1: Evaluation
In the first phase each Glip decides what action to take. Each Glip can only take one action per turn. The decision process considers the current resources and status of a Glip as well as a individual preference based on its genes. Each Glips decides for a strategy, which further results in specific decision tree, ultimately ending in a event. 
![Evaluation Phase](https://raw.githubusercontent.com/codingBeanie/Glipsim/main/doc/Glipsim_Evaluation.webp)

### Phase 2: Events
Each action of a Glip results in an event. The events are handled sequential.

### Phase 3: Aging
Every Glip is getting one year older. A probability for dying is checked (depended on age and health). 

### Phase 4: Statistics
This is a special phase for background data collection. Here nothing happens in the simulation, just data is gathered and stored, so that i can display nice graphs and analyze the status of the simulation.

### Phase 5: Uptick
The next round (year) of the simulation is starting.

