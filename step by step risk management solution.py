import numpy as np
import pandas as pd
import plotly.graph_objs as go
import matplotlib.pyplot as plt

# Define the risk management function
def risk_management(returns, weights, cov_matrix):
    # Calculate portfolio returns
    portfolio_returns = np.dot(weights, returns)
    
    # Calculate portfolio standard deviation
    portfolio_std_dev = np.sqrt(np.dot(weights, np.dot(cov_matrix, weights)))
    
    return portfolio_returns, portfolio_std_dev

# Generate random returns data
n_assets = 5
n_simulation = 500
returns = np.random.randn(n_assets, n_simulation)

# Calculate weights
rand = np.random.rand(n_assets)
weights = rand / sum(rand)

# Calculate covariance matrix
cov_matrix = np.cov(returns.T, aweights=weights, ddof=1)

# Calculate portfolio returns and standard deviation
portfolio_returns, portfolio_std_dev = risk_management(returns, weights, cov_matrix)

# Print results
print("Portfolio Returns:", portfolio_returns)
print("Portfolio Standard Deviation:", portfolio_std_dev)

# Visualize the risk-return relationship
portfolio = np.array([risk_management(np.random.randn(n_assets, i), weights, cov_matrix) for i in range(1, 101)])
best_fit = np.polyfit(portfolio[:, 0], portfolio[:, 1], 1)
fig = go.Figure()
fig.add_trace(go.Scatter(name='Risk-Return Relationship', x=portfolio[:, 0], y=portfolio[:, 1], mode='markers'))
fig.add_trace(go.Scatter(name='Best Fit Line', x=portfolio[:, 0], y=best_fit[0] * portfolio[:, 0] + best_fit[1], mode='lines'))
fig.update_layout(xaxis_title='Return', yaxis_title='Standard Deviation', width=900, height=470)
fig.show()
