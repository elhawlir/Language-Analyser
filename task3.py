# Task 3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import task2

# Visualisation of gathered statistics

class Visualisation:
    
    def __init__(self, data):
        self.data = data # indices 0 to 5 of this dataset belong to sli and indices 6 to 11 is for td
        self.mean = [] # relating to the 

    def compute_averages(self):
        for average in self.data:
            self.mean.append(np.mean(average))
            
        df = pd.DataFrame(self.mean[0:6])
        df.columns = ['SLI Means']
        df.index = ["L_o_T", "U_W", "Rep_W", "Ret_W", "Gra_Err", "N_o_P"]
        print(df)
        
        df1 = pd.DataFrame(self.mean[6:12])
        df1.index = ["L_o_T", "U_W", "Rep_W", "Ret_W", "Gra_Err", "N_o_P"]
        df1.columns = ['TD Means']
        print(df1)

    def visualise_statistics(self):
        
        for average in self.data:
            self.mean.append(np.mean(average))
            
        df = pd.DataFrame(self.mean[0:6])
        df.index = ["L_o_T", "U_W", "Rep_W", "Ret_W", "Gra_Err", "N_o_P"]
        df.columns = ['SLI Means']
        ax = df.plot(kind="bar", title="Statistics for SLI Groups", color="r")
        ax.set_xlabel('Statistics')
        ax.set_ylabel('Mean values of Statistics')
        
        
        df1 = pd.DataFrame(self.mean[6:12])
        df1.index = ["L_o_T", "U_W", "Rep_W", "Ret_W", "Gra_Err", "N_o_P"]
        df1.columns = ['TD Means']        
        ax1 = df1.plot(kind="bar", title="Statistics for TD Groups", color='g')
        ax1.set_xlabel('Statistics')
        ax1.set_ylabel('Mean values of Statistics')        
        

data = sli_stats + td_stats
v1 = Visualisation(data)
# print(v1.compute_averages())
print(v1.visualise_statistics())
        


