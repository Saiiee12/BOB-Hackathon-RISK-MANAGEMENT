import numpy as np
import matplotlib.pyplot as plt

# Define the utility function
def utility(x, gamma):
    return np.exp(gamma * x)

# Define the supply and demand functions
def supply(Q, c):
    return np.mean(pi[-Q:]) * c

def demand(D, y, c, gamma):
    return np.sum(utility(y - D, gamma) > pi * utility(y - c, gamma) + (1 - pi) * utility(y, gamma))

# Generate random probability of loss data
pi = np.random.uniform(0, 1, 20)
pi = np.sort(pi)

# Define the parameters
y = 2
c = 1.5
Q = 5
D = 0.01
gamma = 0.4

# Calculate the supply and demand
supply_val = supply(Q, c)
demand_val = demand(D, y, c, gamma)

# Print results
print("Supply:", supply_val)
print("Demand:", demand_val)

# Visualize the supply and demand curves
plt.figure()
plt.plot(pi, [supply(Q, c) for _ in range(len(pi))], label='Supply')
plt.plot(pi, [demand(D, y, c, gamma) for _ in range(len(pi))], label='Demand')
plt.xlabel('Probability of Loss')
plt.ylabel('Quantity')
plt.title('Supply and Demand Curves')
plt.legend()
plt.show()
