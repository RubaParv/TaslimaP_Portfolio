# TaslimaP_Portfolio
Example Data Science Portfolio
[Fore more coding details of each project, please visit: https://github.com/RubaParv/TaslimaP_Portfolio]
[Please note that I am still working on uploading all data science and machine learning projects one by one]

# Project 1: Optimal Pricing Strategy for an Origin Destination (OD) Pair for a Prospective Ride-Hailing Service

Created simulation run scenarios to find out the optimal ride pricing strategy for a specific OD pair
The following four pricing stratgeies were tested:
1.	A single wage across the 12 months.
2.	Twelve wages for each of the twelve months.
3.	A wage for each rider in each of the twelve months.
4.	A wage for each individual ride that the rider requests.

Case Study Problem: 
Launching a ride-hailing service that matches riders with drivers for trips between the Toledo Airport and Downtown Toledo. It’ll be active for only 12 months. You’ve been forced to charge riders $30 for each ride. You can pay drivers any amount between $0 and $30 for each individual ride.

The supply pool (“drivers”) is very deep. When a ride is requested, a very large pool of drivers see a notification informing them of the request. They can choose whether or not to fulfill it. The probability of a ride being accepted once it’s published to the pool of drivers is:

P(accepted | wage) = wage / 30

where wage is what we offer drivers for that ride and may range from $0 to $30.

The demand pool (“riders”) can be acquired at a cost of $30 per rider at any time during the 12 months. “Acquisition” means that the rider has downloaded the app and may request rides. Requested rides may or may not be accepted by the driver pool. In the first month that riders are active, they request rides based on a Poisson distribution where lambda = 1. For each subsequent month, riders request rides based on a Poisson distribution where lambda is the number of rides that they found a match for in the previous month. (As an example, a rider that requests 3 rides in month 1 and finds 2 matches has a lambda of 2 going into month 2.) If a rider finds no matches in a month (which may happen either because they request no rides in the first place based on the Poisson distribution or because they request rides and find no matches), they leave the service and never return.

What level of granularity should the optimal pricing strategy operate at?

Answer:
https://github.com/RubaParv/TaslimaP_Portfolio/blob/main/Images/Performances%20of%20Different%20Pricing%20Strategies.png



# Project 2: Covid-19 Impact of Visits to Businesses, Offices and Other Places of  Toronto in 2020

The Community Mobility Reports by Google show movement trends by region, across different categories of places.
The objective was to see the Covid impact on different sectorwise businesses and places, 
so that top management may have some insights to decide operating budget in this Covid induced conditions.

Baseline: The data shows how visitors to (or time spent in) categorized places change compared to our baseline days. 
A baseline day represents a normal value for that day of the week. 
The baseline day is the median value from the 5 week period Jan 3 – Feb 6, 2020.
The mobility reports show relative changes, and not absolute visitors or duration.
This study covers Toronto Area visits only.


The raw excel or csv file data compares mobility for the report date to the baseline day. 
It was calculated for the report date (unless there are gaps) and reported as a positive or negative percentage.

Some Key Takeways:
Visits or travel to all places including transit stations, workplaces, retails and recreation dropped significantly during the pandemic
Park visits increased as other recreational facilities were closed
People tend to spend more time at home 
Travel to groceries stays about the same to pre-covid level except during short period of time after stay-at-home orders 
Both travel to transit stations and workplaces dropped significantly and these are slow to rebound 

Example Time Series Trends:

https://github.com/RubaParv/TaslimaP_Portfolio/blob/main/Images/newplot%20(24).png

https://github.com/RubaParv/TaslimaP_Portfolio/blob/main/Images/newplot%20(25).png

https://github.com/RubaParv/TaslimaP_Portfolio/blob/main/Images/newplot%20(26).png

https://github.com/RubaParv/TaslimaP_Portfolio/blob/main/Images/newplot%20(27).png

https://github.com/RubaParv/TaslimaP_Portfolio/blob/main/Images/newplot%20(28).png

https://github.com/RubaParv/TaslimaP_Portfolio/blob/main/Images/newplot%20(29).png

