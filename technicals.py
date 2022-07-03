import numpy as np

# Calculates moving average line
# INPUT: x=PriceArray, n=LookbackPeriod

def moving_average(x, n=50):
    k = [np.nan for u in range(n)] + [np.mean(x[v-n:v]) for v in range(n, len(x))]
    return k


# Calculates vwap
# INPUT: x=PriceArray, v=VolumeArray, n=LookbackPeriod

def vwap(x, v, n=50):
    k = [np.nan for u in range(n)] + [np.sum([j*k for j, k in zip(x[i-n:i], v[i-n:i])])/np.sum(v[i-n:i]) for i in range(n, len(x))]
    return k


# Calculate bollinger bands
# INPUT: x=PriceArray, n=LookBackPeriod, d=StandardDeviationMultiplier

def bollinger(x, n=50, d=2):
    up_k = [np.nan for u in range(n)] + [x[i] + d*np.std(x[i-n:i]) for i in range(n, len(x))]
    down_k = [np.nan for u in range(n)] + [x[i] - d*np.std(x[i-n:i]) for i in range(n, len(x))]
    return up_k, down_k


# Calculates relative strength index (RSI)
# INPUT: x=PriceArray, n=LookBackPeriod

def rsi(x, n=50):
    y = x[:n]
    up = np.sum([i - j if i - j >= 0 else 0 for i, j in zip(y[:-1], y[1:])])/n
    down = np.sum([abs(i - j) if i - j < 0 else 0 for i, j in zip(y[:-1], y[1:])])/n
    return 100 - 100 / (1 + (up/down))
