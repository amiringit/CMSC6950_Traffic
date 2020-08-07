from matplotlib import pyplot as plt
from countflights import *

#to make second figure
data["sum"] = data.sum(axis=1)
plt.figure(figsize=(12,12))
plt.plot(data["sum"])
plt.savefig('plot2.png')

