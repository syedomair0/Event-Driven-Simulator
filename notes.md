code for event driven simulator for CSCI 4930 taken @ SLU
barbasi algorithm

preferential attachment (related to barbasi algorithm)
- degree of nodes

- waxmem. ?
    - random (n(odes), p(robability of connection))

adjacency matrix

_....
._...
.._..
..._.
...._

SIP models? for public health (extra)

existing simulators

- BRITE
- GT top...?

topology gets flatter...

System Features

- network topology configuration
- traffic modeling
- packet routing and forwarding
- congestion control and management

interface design

- simulation control interface
- reporting and analysis tools


- simulator
- emulator
- prototype

configuration.ini

Event Driven Simulator

node
+-> 


traffic manager

network consists of nodes

nodes have a connection list

a connection consists of [id, capacity]



engine

"general purpose simulator"


ECE flag

- used to detect congestion
- when a router's queue reaches a capacity, it starts 
  flagging packets by turning the ECE flag to 1

RED

Designing a general purpose event driven network simulator

## architecture

simulation engine
network model

## features

traffic modeling
network topology config
packet routing and forwarding
congestion control and management

> config.ini to specify simulation parameters

## plugins

- none for now but add for new features

## interface design

- simulation control interface
- reporting and analysis tool (quick prototyping)

## performance considerations

- scalability
- accuracy

