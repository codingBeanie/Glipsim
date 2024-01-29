![Glipsim](https://raw.githubusercontent.com/codingBeanie/Glipsim/main/doc/glipsim_banner.webp)

This is a *Django* server which runs a virtual life simulation of a fictional fantasy population of Glips. This whole project is a fun project. Nevertheless, i try to learn many things about backend-developement, simulations, APIs and webpages.

## Glips
A Glip is a pretty simple non-binary creature with a individual dna. The dna sequence consists of different genes that determine special preferences, appearence and other behavioural attributes.

## The Simulation
The simulation operates as a turn-based system. A turn represents one time-unit (e.g. a year). On each turn a number of phases is called sequentially. Each phase triggers specific functions and calculations. After the last phase is completed, the next turn is started.

### Phase 1: Evaluation
In the first phase each Glip decides what action to take. Each Glip can only take one action per turn. The decision process considers the current resources and status of a Glip as well as a individual preference based on its genes. Each Glips decides for a strategy, which further results in specific events. 

#### Strategy: Reproduction
If a glip decides to reproduce, it is checked whether the glip is partnered or not. If it has a partner, it will want to mate (Event Mating), if not it will want to date other Glips (Event Dating).


### Phase 2: Events
Each action of a Glip results in an event. The events are handled sequential.

#### Event: Dating
Every Glip that wants to date is collected and assigned to a random other Glip that also wants to date. Each Glip has a appearance that is mainly represented by its color, defined by its genes. Also each Glip has a preferred color and age for its mating partner, which can be different from its own appearance and age. 
Moreover, each Glip has a tolerance for differences in preferred color and age, also defined by its genes. If the random allocated partner matches the preferred appearance to a certain threshold, the Glip will want to be coupled. If both Glips of the dating pairs want to be coupled, they get partnered. Otherwise they will not have found a partner and stay single.
Note: Siblings do not want to be partners, but can still be meeting in the dating event. Then they will just enjoy their company.

#### Event: Mating
It is checked if both partnered Glips want to mate. If both are willing, the probability for sucess is calculated (dependend on age and health). If successful a new Glip is born and assigned to the household of the parents.

### Phase 3: Aging
Every Glip is getting one year older. A probability for dying is checked (depended on age and health). 

### Phase 4: Statistics
This is a special phase for background data collection. Here nothing happens in the simulation, just data is gathered and stored, so that i can display nice graphs and analyze the status of the simulation.

### Phase 5: Uptick
The next round (year) of the simulation is starting.

