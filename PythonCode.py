# Project Risk quantification in R. A repository for simulating and analyzing risk scenarios in Python.

# Status This project is actively being developed and is in the production  stage.

# Tags/Topics - Risk management - Data Analysis - Python

# License This project is open source, originally provided by Prof. Hernan Huwyler, MBA CPA.


import numpy as np
import matplotlib.pyplot as plt

# Data input
Simulations = 10000  # Number of scenarios to simulate
Events = 4           # Number of expected annual events to materialize (Poisson distribution)
Loss = 20000         # Expected average financial loss per event (Lognormal distribution)
Mean = 0.2           # Standard deviation of the losses in R
Reserve = 0.8        # This percentile is a measure of the risk exposure, indicating the level of loss that would be lower in a specific proportion of the simulated scenarios

# Simulate Poisson-distributed random variables (number of events)
Prob = np.random.poisson(Events, Simulations)

# Simulate Lognormal-distributed random variables (financial loss per event)
Impact = np.random.lognormal(mean=np.log(Loss), sigma=Mean, size=Simulations)

# Calculate the total loss for each scenario
x = Prob * Impact

# Display a summary of the simulated data
print(np.percentile(x, Reserve * 100))

# Calculate the given percentile of the simulated losses
loss_at_reserve = np.percentile(x, Reserve * 100)
print(f'{Reserve * 100}th Percentile Loss: {loss_at_reserve}')

# Create a histogram of the simulated losses
plt.hist(x, bins=20, density=True, alpha=0.6, color='b', edgecolor='black')
plt.xlabel('Loss')
plt.ylabel('Probability Density')
plt.title('Simulated Losses Histogram')
plt.show()

# Graph a Loss Exceedance Curve
number_sequence = np.arange(0.01, 1.001, 0.001)
y = [np.percentile(x, i * 100) for i in number_sequence]
plt.plot(number_sequence, y, marker='o')
plt.xlabel('Percentile')
plt.ylabel('Loss')
plt.title('Loss Exceedance Curve')
plt.show()

# Graph an Annual Loss Expectancy chart
plt.boxplot(x)
plt.ylabel('Loss')
plt.title('Annual Loss Expectancy')
plt.show()
