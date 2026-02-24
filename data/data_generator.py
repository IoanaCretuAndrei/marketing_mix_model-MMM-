import numpy as np 
import pandas as pd 

np.random.seed(42)

# number of weeks
n_weeks = 208 # 4 years of weekly data

#date range

dates = pd.date_range(start='2021-01-01', periods=n_weeks, freq='W')

# simulate advertising media spend

tv = np.random.uniform(10000, 50000, n_weeks)
youtube = np.random.uniform(500, 3000, n_weeks)
facebook = np.random.uniform(300, 2000, n_weeks)
search = np.random.uniform(2000, 10000, n_weeks)

#adstock function

def adstock(x, alpha=0.5):
    result = np.zeros_like(x)
    for t in range(len(x)):
        if t == 0:
            result[t] = x[t]
        else:
            result[t] = x[t] + alpha * result[t-1]
    return result


#apply adstock transformation

tv_adstock = adstock(tv)
youtube_adstock = adstock(youtube, 0.4)
facebook_adstock = adstock(facebook, 0.3)
search_adstock = adstock(search, 0.2)


# saturation function
def saturation(x, lam):

    return 1 - np.exp(-lam * x)

tv_sat = saturation(tv_adstock, 0.00005)
youtube_sat = saturation(youtube_adstock, 0.0001)
facebook_sat = saturation(facebook_adstock, 0.0001)
search_sat = saturation(search_adstock, 0.0002)


#trend

trend = np.linspace(1, 1000, n_weeks)

# seasonality

seasonality = 2000 * np.sin(np.arange(n_weeks) * 2 * np.pi / 52)

#noise

noise = np.random.normal(0, 1000, n_weeks)

#true coefficients for media channels

sales = (
    5000
    + 8000 * tv_sat
    + 6000 * youtube_sat
    + 5000 * facebook_sat
    + 3000 * search_sat
    + trend
    + seasonality
    + noise
)


df = pd.DataFrame({
    'date': dates,
    'tv': tv,
    'youtube': youtube,
    'facebook': facebook,
    'search': search,
    'sales': sales
})


#save to csv
df.to_csv('mmm_dataset.csv', index=False)

print(df.head())