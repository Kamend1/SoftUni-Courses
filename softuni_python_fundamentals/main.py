import yfinance as yf
import numpy as np
from scipy.stats import norm
from datetime import datetime


def calculate_probability_of_exercise(ticker_symbol, option_strike_price, option_expiry_date):
    # Retrieve historical price data for the underlying asset
    ticker = yf.Ticker(ticker_symbol)
    historical_data = ticker.history(period="1y")

    # Calculate historical returns
    historical_returns = historical_data['Close'].pct_change().dropna()

    # Estimate volatility of the underlying asset
    volatility = np.std(historical_returns) * np.sqrt(252)  # Annualized volatility

    # Calculate time to expiry in years
    expiry_date = datetime.strptime(option_expiry_date, '%Y-%m-%d')
    current_date = datetime.now()
    time_to_expiry = (expiry_date - current_date).days / 365.0

    # Calculate parameters for Black-Scholes formula
    d1 = (np.log(historical_data['Close'].iloc[-1] / option_strike_price) + (0.5 * volatility ** 2)\
          * time_to_expiry) / (volatility * np.sqrt(time_to_expiry))
    d2 = d1 - volatility * np.sqrt(time_to_expiry)

    # Calculate cumulative distribution function values using normal distribution
    cdf_d1 = norm.cdf(d1)
    cdf_d2 = norm.cdf(d2)

    # Calculate probability of exercise
    probability_of_exercise = cdf_d2

    return probability_of_exercise


# Example usage:
ticker_symbol = 'MSFT'
option_strike_price = 455
option_expiry_date = '2024-03-01'
probability = calculate_probability_of_exercise(ticker_symbol, option_strike_price, option_expiry_date)
print(f"Probability of option exercise at maturity: {(probability * 100):.10f}%")

