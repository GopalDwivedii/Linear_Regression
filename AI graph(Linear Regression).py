from scipy import stats
import matplotlib.pyplot as plt


x = [10, 20, 30, 89, 56, 90, 78, 65, 44]
y = [10, 20, 30, 34, 54, 2, 99, 101, 34]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def func(x):
    return slope * x + intercept


model = list(map(func, x))

plt.scatter(x, y)
plt.plot(x, model)
plt.show()
