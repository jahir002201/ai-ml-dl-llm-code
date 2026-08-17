from scipy.stats import norm

mean = 100
std = 15
x = 130

z_score = (x - mean) / std

probability = norm.cdf(x, mean, std)

print("Z-score:", z_score)
print("P(X <= 130):", probability)