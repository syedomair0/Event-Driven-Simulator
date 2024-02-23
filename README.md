uage:

-events = number of events
-model = either "ba" or "waxman"
-simulations = number of simulations to run
-n = number of nodes
-m = number of connections from each node (only required when -model is "ba")

## for the waxman model

> python3 sim.py -simulations 100 -events 1000 -model waxman -n 200

## for the Barabasi-Albert model

> python3 sim.py -simulations 100 -events 100 -model ba -n 100 -m 5
