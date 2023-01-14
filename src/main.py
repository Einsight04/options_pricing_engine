from libs.get_oanda_price import get_oanda_price
from libs.monte_carlo_option_pricing import monte_carlo_option_pricing

# Get current spot price from Oanda API
S = get_oanda_price('EUR_USD')

# Get current strike price from Oanda API
K = get_oanda_price('EUR_USD')

# Define other parameters
r = 0.03
sigma = 0.2
T = 1
n_sim = 10000

# Calculate call and put option prices
call_price, put_price = monte_carlo_option_pricing(S, K, r, sigma, T, n_sim)

print("Call price: ", call_price)
print("Put price: ", put_price)
