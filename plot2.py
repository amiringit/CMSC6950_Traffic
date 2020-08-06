#to make second figure
data["sum"] = data.sum(axis=1)
plt.figure(figsize=(12,12))
plt.plot(data.index, data["sum"])
plt.savefig('plot2.png')

