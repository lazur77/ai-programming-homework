import matplotlib.pyplot as plt
from sklearn import datasets

def plotiris(y, X, w=None, addhline=None, addvline=None):
    iris = datasets.load_iris()
    plt.figure(figsize=(8, 6))
    if w is not None:
        plt.scatter(X[y == -1][:, 0], X[y == -1][:, 1], s=(w[y == -1]*3000), color='blue', label='-1')
        plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], s=(w[y == 1]*3000), color='red', label='1')
    else:
        plt.scatter(X[y == -1][:, 0], X[y == -1][:, 1], color='blue', label='-1')
        plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='red', label='1')
    plt.xlabel(f'{iris.feature_names[0]}')
    plt.ylabel(f'{iris.feature_names[1]}')
    plt.title('iris data')
    if addvline:
        plt.axvline(x = addvline, color = 'b', label = 'axvline - full height')
    if addhline:
        plt.axhline(y = addhline, color = 'b', label = 'axvline - full height')
    plt.legend()
    plt.show()