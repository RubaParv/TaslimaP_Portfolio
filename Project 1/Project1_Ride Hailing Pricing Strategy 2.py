#!/usr/bin/env python
# coding: utf-8

# ## Strategy 2 Simulation: Twelve wages for each of the twelve months
# 
# ## Developed by Taslima Parvin, Toronto, Email: rubaparv@gmail.com

# In[1]:


import numpy as np
import pandas as pd

# importing poisson from scipy
from scipy.stats import poisson

## Assuming three Demand Scenarios



Demand_Scenario=[200, 500, 1000]

# Strategy 2: # Strategy 2: Twelve wages for each of the twelve months



Y2=[0, 0, 0] # Initialize three demand scenario profits as average yearly profit after all simulation runs for each demand
dd=0 ## Initialize iterator to capture final target profit for each demand scenario

# Say, January base rider number as regular monthly demand of 500 passenger traffic from Toledo airport to/from downtown
# Each ride by a an individual rider (no multiple rides by an individual rider assumed at this stage)

# Say, lower rider numbers as demand of January is 200 (Lower Demand Scenario) 
# Say, higher rider numbers as demand of January is 100 (Higher Demand Scenario) 


## Looping three demand scenarios
for d in Demand_Scenario:
    
    ## Number of simulation runs for each demand scenario
    Simu_Run=10
    Simu_Run_list=np.arange(1, Simu_Run+1)

    All_Years_Profit=0  # Stores total profits of each simulation runs/simulation years

    for sr in Simu_Run_list:
        
        Jan_Wage = np.random.randint(5, 31) # Use $5 minimum as booking cost 

        Yearly_Profit=0 # Captures yearly profit as sum of cumulative monthly profit from each simulation run

        ## Crate a blank dataframe of Month 1 (January)
        x = ['RiderID','RiderLambda','RidesReq','RideWageOffered','RideAccepProb','RideAccepted','RideIncome']
        rides_list = np.arange(1, d+1)
        data=[]
        for i in rides_list:
            row=[]
            for j in x:
                row.append(np.int(0)) # Assign zeroes 
            data.append(row)

        df = pd.DataFrame(data, index=rides_list, columns=x)  #df with all zoreos is created
       
        # Assign January vales for all other attributes
        for index, row in df.iterrows():
                df.loc[index, 'RiderID'] = index
                df.loc[index, 'RiderLambda'] = 1  ## January lambda 
                df.loc[index, 'RidesReq'] = poisson.rvs(1, loc=0, size=1, random_state=None)  # Poisson Distribution (January lambda)

#        print(df.head(5))
        ## Remove Riders from the system who did not call a ride
        df = df.drop(df[(df.RidesReq == 0)].index)

        ## Repeat the rides (as append new rows) for customers who called more than 1 ride
        df1=df.apply(np.repeat, repeats=df['RidesReq'])

        ## Assign attributes values as per the business policy, this is still for January calculations
        for index, row in df1.iterrows():

                df1.loc[index, 'RideWageOffered'] = Jan_Wage # Strategy 4 (as equally likely random wage for each ride)
                df1.loc[index, 'RideAccepProb'] = df1.loc[index, 'RideWageOffered']/30 # Probability
                prob=df1.loc[index, 'RideAccepProb']
                if prob.any() >= 0.5:  # Assuming each ride is accepted when probability is more than 0.50 
                    df1.loc[index, 'RideAccepted'] = 1
                    df1.loc[index, 'RideIncome'] = 30 
                elif prob.any() < 0.5:  
                    df1.loc[index, 'RideAccepted'] = 0
                    df1.loc[index, 'RideIncome'] = 0             


        df1['profit']=df1['RideIncome']-df1['RideWageOffered'] # Proft margin from each individual ride by the company
        Yearly_Profit=df1['profit'].sum() # Total monthly profit margin for January now


        ## Prepare data for next months from Februray to December in an iterative fashion

        # Remove rides those were failed in the month of January
        df2 = df1.drop(df1[(df1.RideAccepted == 0)].index)

        # Find total successful/completed rides of each rider for the first month of January, this will be lambda of next month
        df3=df2.groupby(["RiderID"]).size().reset_index(name="RiderLambda")

        # Remaining month iterator list
        Rest_Months=['Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

        ## Looping months from Feb to Dec

        for month in Rest_Months:
            Monthly_Wage = np.random.randint(5, 31) # Use minimum $5            
            df=df3 # Reset df as new base for each month
            for index, row in df.iterrows():
            #    set new rides request by poission distribution when lambda is Rider Lambda of previous month
                    df.loc[index, 'RidesReq'] = poisson.rvs(row.RiderLambda, loc=0, size=1, random_state=None)   

#            print('demand:',d)
#            print('Simu:',sr)
#            print("Month:",month)
#            print(df.head(5))
            
            # Remove the riders who did not request a ride in this month
            df = df.drop(df[(df.RidesReq == 0)].index)

            # Repeat the rides (as append new rows) for customers who called more than 1 ride in this month
            df1=df.apply(np.repeat, repeats=df['RidesReq'])


            # Assign attributes values as per the business rules   
            for index, row in df1.iterrows():
                    df1.loc[index, 'RideWageOffered'] =  Monthly_Wage
                    # Strategy 4 (as equally likely random wage for each ride)
                    df1.loc[index, 'RideAccepProb'] = df1.loc[index, 'RideWageOffered']/30 
                    prob=df1.loc[index, 'RideAccepProb']
                    if prob.any() >= 0.5:
                        df1.loc[index, 'RideAccepted'] = 1
                        df1.loc[index, 'RideIncome'] = 30 
                    elif prob.any() < 0.5:  
                        df1.loc[index, 'RideAccepted'] = 0
                        df1.loc[index, 'RideIncome'] = 0             

            # Profit margin in this month  
            df1['profit']=df1['RideIncome']-df1['RideWageOffered']

            # Accumulative monthly total profit (as cumulative sum of monthly margins)
            Yearly_Profit=Yearly_Profit + df1['profit'].sum()

            # Preparing data for next month by removing not accepted rides
            df2 = df1.drop(df1[(df1.RideAccepted == 0)].index)

            # Preparing for next month's lambda by frequency of accepted rides of each individual rider from this month
            df3=df2.groupby(["RiderID"]).size().reset_index(name="RiderLambda")


         # Cumulative sum of yearly profits after each simulation run/ simulation year   
        All_Years_Profit = All_Years_Profit + Yearly_Profit

         # Average yearly profit margin after each simulation run/ simulation year    
        Average_Yearly_Profit=All_Years_Profit/sr

#        print("Demand:", d, "Simulation Run:",sr,"Yearly_Profit:", Yearly_Profit, 
#              "All_Years_Profit:", All_Years_Profit, 
#              "Average_Yearly_Profit:", Average_Yearly_Profit)

        # Capture the last average yearly profit after end of the all simulations
            
    Y2[dd]= Average_Yearly_Profit  
    
    dd=dd+1    
    
print ("Option 2: Twelve Monthly Wage", Y2)


# In[ ]:





# In[ ]:




