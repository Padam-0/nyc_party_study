import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

green_names = ['pickup_datetime', 'dropoff_datetime' ,'pu_long',
                    'pu_lat', 'do_long' ,'do_lat']

df = pd.read_csv('clean_green.csv', names = green_names,
                 index_col='pickup_datetime', parse_dates=True)

x = [i for i in range(480)]

df = df.loc['2015-06-27 11:00:00':]

df = df.resample('T').count()

y = []
for i in range(480):
    y.append(df.ix[i, 'pu_long'])

plot_labels = ['11 pm', '12 am', '1 am', '2 am', '3 am', '4 am', '5 am',
               '6 am', '7 am']

sns.set_style("white")
plt.rc('font', family='Raleway')
fig, ax1 = plt.subplots(figsize=(20, 10))
plt.subplots_adjust(bottom=0.15)

fig.canvas.draw()
plt.xticks([i for i in range(len(plot_labels))])
labels = [item.get_text() for item in ax1.get_xticklabels()]
for i in range(len(plot_labels)):
    labels[i] = plot_labels[i]
ax1.set_xticklabels(labels, rotation=-45)

plt.scatter(x, y, s=8)

sns.despine()
plt.xlabel('Time')
plt.ylabel('Number of rides')
plt.ylim([0, 100])
plt.xlim([-2, 500])
plt.xticks([0, 60, 120, 180, 240, 300, 360, 420, 480])
plt.show()