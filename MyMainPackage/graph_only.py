#!/usr/bin/env python
# coding: utf-8

# In[25]:


#get_ipython().system('pip install ffmpeg')


# In[26]:


import numpy as np
import matplotlib.pyplot as plt 
#import ffmpeg
from IPython.display import HTML
import matplotlib.animation as ani
import random as rand
import matplotlib


# In[27]:


def tick(matrix, tmatrix):
    new_state = np.copy(matrix)
    new_time  = np.copy(tmatrix)
    #assigning neighbours
    # (-1) means we are on the edge of the matrix we cannot look further for neighbours
    for i in range(np.size(matrix,0)):
        for j in range(np.size(matrix,1)):
            #north neighbour:
            if i > 0:
                north = matrix[i-1][j]
            else:
                north = -1
            #south neighbour:
            if i != (np.size(matrix,0)-1):
                south = matrix[i+1][j]
            else: 
                south = -1
            #west neighbour:
            if j > 0:
                west = matrix[i][j-1]
            else:
                west = -1
            #east neighbour:
            if j != (np.size(matrix,1)-1):
                east = matrix[i][j+1]
            else:
                east = -1
            #ne:
            if i > 0 and j != (np.size(matrix,1)-1):
                ne = matrix[i-1][j+1]
            else:
                ne = -1
            #nw:
            if i > 0 and j > 0:
                nw = matrix[i-1][j-1]
            else:
                nw = -1
            #se:
            if i != (np.size(matrix,0)-1) and j != (np.size(matrix,1)-1):
                se = matrix[i+1][j+1]
            else:
                se = -1
            #sw
            if i != (np.size(matrix,0)-1) and j > 0:
                sw = matrix[i+1][j-1]
            else:
                sw = -1

            #neighbours = [north, south, west, east, ne, nw, se, sw]

            #rules:

            #for empty cells:
            if matrix[i][j] == 0:
                new_state[i][j] = 0

            #for susceptibles:
            elif matrix[i][j] == 1:
                if north == 2:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif south == 2:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif west == 2:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif east == 2:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif ne == 2:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif nw == 2:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif se == 2:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif sw == 2:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif north == 3:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif south == 3:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif west == 3:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif east == 3:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif ne == 3:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif nw == 3:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif se == 3:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                elif sw == 3:
                    if np.random.randint(1,101) > 50:
                        new_state[i][j] = 2
                else:
                    new_state[i][j] = 1

            #for exposed:
            elif matrix[i][j] == 2:
                if tmatrix[i][j] < 7: #seven day incubation period
                    new_state[i][j] = 2
                    new_time[i][j] = tmatrix[i][j] + 1
                else:
                    if np.random.randint(1,101) < 70:
                        new_state[i][j] = 3
                        new_time[i][j] = 0
                    else:
                        new_state[i][j] = 1
                        new_time[i][j] = 0

            #for infected:
            elif matrix[i][j] == 3:
                if tmatrix[i][j] < 3: #2 days until testing
                    new_state[i][j] = 3
                    new_time[i][j] = tmatrix[i][j] + 1
                else:
                    if np.random.randint(1,101) < 60: #chance of being tested
                        new_state[i][j] = 4
                        new_time[i][j] = 0
                    else:
                        if tmatrix[i][j] < 14: #the virus lasts for 14 days
                            new_time[i][j] = tmatrix[i][j] + 1
                        else:
                            new_state[i][j] = 5
                            new_time[i][j] = 0

            #for quarantine:
            elif matrix[i][j] == 4:
                if tmatrix[i][j] < 10:
                    new_state[i][j] = 4
                    new_time[i][j] = tmatrix[i][j] + 1
                else:
                    new_state[i][j] = 5
                    new_time[i][j] = 0

            #for recovered:
            elif matrix[i][j] == 5:
                new_state[i][j] = 5

    return new_state, new_time


# In[28]:


def plot_func(matrix):
    # 0 - dead cell
    # 1 - susceptible
    # 2 - exposed
    # 3 - infected
    # 4 - quarantined
    # 5 - recovered 
    sus = 0
    exp = 0
    inf = 0
    quar = 0
    rec = 0
    for i in range(np.size(matrix,0)):
        for j in range(np.size(matrix,1)):
            if matrix[i][j] == 1:
                sus += 1
            elif matrix[i][j] == 2:
                exp += 1
            elif matrix[i][j] == 3:
                inf += 1
            elif matrix[i][j] == 4:
                quar += 1 
            elif matrix[i][j] == 5:
                rec += 1
    return sus, exp, inf, quar, rec


# In[29]:


def initial_state(type_inf, pop):
    # grid size and proportion of the pop that can be affected
    grid_size = int(pop**0.5)
    affected = int(pop * 0.7)

    # time matrix
    tmatrix = np.zeros((grid_size, grid_size))

    # randomly created matrix
    arr = np.zeros((grid_size, grid_size))
    index_1 = np.random.choice(arr.size, affected, replace=False)
    arr.ravel()[index_1] = 1

    if type_inf == "single":
        x = rand.randint(0, grid_size-1)
        y = rand.randint(0, grid_size-1)
        arr[x][y] = 3
    elif type_inf == "random":
        n = rand.randint(0, pop//2) # how many infected people are present
        for i in range(n):
            x = rand.randint(0, grid_size-1)
            y = rand.randint(0, grid_size-1)
        arr[x][y] = 3
    elif type_inf == "cluster":
        n = rand.randint(0, grid_size) # number of clusters
        for i in range(n):
            x = rand.randint(0, grid_size-2)
            y = rand.randint(0, grid_size-2)
            arr[x][y] = 3
            arr[x][y-1] = 3 if y-1>0 else arr[x][y-1]
            arr[x][y+1] = 3 if y+1<grid_size else arr[x][y+1]
            arr[x-1][y] = 3 if x-1>0 else arr[x-1][y]
            arr[x+1][y] = 3 if x+1<grid_size else arr[x+1][y]

            arr[x+1][y+1] = 3 if x+1<grid_size and y+1<grid_size else arr[x+1][y+1]
            arr[x-1][y+1] = 3 if x-1>0 and y+1<grid_size else arr[x-1][y+1]
            arr[x-1][y-1] = 3 if x-1>0 and y-1>0 else arr[x-1][y-1]
            arr[x+1][y-1] = 3 if x+1<grid_size and y-1>0 else arr[x+1][y-1]
    else:
        return "The input is invalid. Please try again!"
    return arr, tmatrix

# In[31]:


def animator_graph(frames, ininterval, matrix, tmatrix):

    susceptible = []
    exposed = []
    infected = []
    quarantined = []
    recovered = []

    for i in range(frames):
        matrix, tmatrix = tick(matrix, tmatrix)

        sus, exp, inf, quar, rec = plot_func(matrix)

        susceptible.append(sus)
        exposed.append(exp)
        infected.append(inf)
        quarantined.append(quar)
        recovered.append(rec)


    # plots 
    susceptible = np.asarray(susceptible)
    exposed = np.asarray(exposed)
    infected = np.asarray(infected)
    quarantined = np.asarray(quarantined)
    recovered = np.asarray(recovered)

    plt.figure(figsize=(6,5))

    plt.title('Disease progression')
    plt.xlabel('Time')
    plt.ylabel('Number of people')

    plt.plot(np.arange(susceptible.shape[0]), susceptible, color='blue')
    plt.plot(np.arange(exposed.shape[0]), exposed, color='yellow')
    plt.plot(np.arange(infected.shape[0]), infected, color='red')
    plt.plot(np.arange(quarantined.shape[0]), quarantined, color='cyan')
    plt.plot(np.arange(recovered.shape[0]), recovered, color='green')
    plt.legend(labels=['Susceptible', 'Exposed','Infected', 'Quarantined','Recovered'], loc='upper right')
    plt.show()

#matrix, tmatrix = initial_state('cluster', 2500)
#animator(100, 100, matrix, tmatrix) 


# In[ ]:





# In[ ]:





# In[ ]:




