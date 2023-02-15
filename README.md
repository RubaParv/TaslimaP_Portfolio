# TaslimaP_Portfolio
Example Data Science Portfolio

# Project 1: Optimal Pricing Strategy for an Origin Destination (OD) Pair for a Prospective Ride-Hailing Service

Created simulation run scenarios to find out the optimal ride pricing strategy for a specific OD pair
The following four pricing stratgeies were tested:
1.	A single wage across the 12 months.
2.	Twelve wages for each of the twelve months.
3.	A wage for each rider in each of the twelve months.
4.	A wage for each individual ride that the rider requests.

Case Study Problem: You’re launching a ride-hailing service that matches riders with drivers for trips between the Toledo Airport and Downtown Toledo. It’ll be active for only 12 months. You’ve been forced to charge riders $30 for each ride. You can pay drivers any amount between $0 and $30 for each individual ride.

The supply pool (“drivers”) is very deep. When a ride is requested, a very large pool of drivers see a notification informing them of the request. They can choose whether or not to fulfill it. The probability of a ride being accepted once it’s published to the pool of drivers is:

P(accepted | wage) = wage / 30

where wage is what we offer drivers for that ride and may range from $0 to $30.

The demand pool (“riders”) can be acquired at a cost of $30 per rider at any time during the 12 months. “Acquisition” means that the rider has downloaded the app and may request rides. Requested rides may or may not be accepted by the driver pool. In the first month that riders are active, they request rides based on a Poisson distribution where lambda = 1. For each subsequent month, riders request rides based on a Poisson distribution where lambda is the number of rides that they found a match for in the previous month. (As an example, a rider that requests 3 rides in month 1 and finds 2 matches has a lambda of 2 going into month 2.) If a rider finds no matches in a month (which may happen either because they request no rides in the first place based on the Poisson distribution or because they request rides and find no matches), they leave the service and never return.

What level of granularity should the optimal pricing strategy operate at?

[https://github.com/RubaParv/TaslimaP_Portfolio/blob/main/Images/Performances%20of%20Different%20Pricing%20Strategies.png]
