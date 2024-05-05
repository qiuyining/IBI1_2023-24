# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt

vaccination_rates=np.arange(0.1, 1.1, 0.1)
plt.figure(figsize =(6 ,4) , dpi=150)
for rate in vaccination_rates:
    # efine the basic variables 
    N = 10000  # total population
    I = 1      # initial number of infected people
    R = 0      # initial number of recovered people
    V = int(rate * N)
    S = N - I - R -V # initial number of susceptible people

    beta=0.3  # infection  probability 
    gamma=0.05 # recovery pobability 

    susceptible = [S]
    infected = [I]
    recovered = [R]

# loop over 1000 time points
# pick susceptible individuals at random to become infected
# pick infected individuals at random to become recovered
    for i in range(1000):   
        if S > 0:
            infections = np.random.choice(range(2), S, p=[1 - beta * I / N , beta * I / N ])
            new_infections = np.sum(infections)
        else:    
            new_infections = 0

        if I > 0:     
            recoveries = np.random.choice(range(2), I, p=[1-gamma, gamma])
            new_recoveries = np.sum(recoveries) 
        else:
            new_recoveries = 0

    # Update the S, I, R values
        S -= new_infections
        I += new_infections - new_recoveries  
        R += new_recoveries

    # Record the numbers of S, I, R
        susceptible.append(S)
        infected.append(I)
        recovered.append(R)

    plt.plot(infected, label=f'{rate*100:.0f}%') 

plt.title('SIR Model with different vaccination rates')
plt.xlabel('time')
plt.ylabel('number of People')
plt.legend()
plt.savefig("D:/IBI/IBI_git/IBI1_2023-24/Practiacl10/SIR_figure_different_rates.png", format="png")
plt.show()
plt.clf ()
     