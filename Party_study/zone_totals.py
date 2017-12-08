import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_change(pdict, names):
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

    x = [30, 90, 150, 210, 270, 330, 390, 450]

    labs = []

    for zone, zlist in pdict.items():
        name = names.loc[zone,'nta_name'] + ", " + names.loc[zone, 'borough']
        labs.append(name)
        plt.plot(x, zlist, '-o')

    colors = ['brown red', 'tree green', 'slime green', 'greeny blue',
              'dark navy', 'pale lilac', 'wheat', 'watermelon']
    for i, j in enumerate(ax1.lines):
        j.set_color(sns.xkcd_rgb[colors[i]])

    plt.legend(labels=labs,
               bbox_to_anchor=(0.05, .7, 0., 0.), loc=3, mode="expand",
               borderaxespad=0., markerscale=1)

    sns.despine()
    plt.xlabel('Time')
    plt.ylabel('Rank')
    plt.ylim([0, 15])
    plt.xlim([-2, 500])
    plt.xticks([0, 60, 120, 180, 240, 300, 360, 420, 480])
    plt.show()


def get_demo():
    demo = pd.read_csv('../Original Data/demographics.csv')

    demo['u19'] = (demo['under_5_years'] + demo['5-9_years'] +
                   demo['10-14_years'] + demo['15-19_years']) / demo[
                      'population']

    demo['20s'] = (demo['20-24_years'] + demo['25-29_years']) / demo[
        'population']
    demo['30s'] = (demo['30-34_years'] + demo['35-39_years']) / demo[
        'population']
    demo['40s'] = (demo['40-44_years'] + demo['45-49_years']) / demo[
        'population']
    demo['50s'] = (demo['50-54_years'] + demo['55-59_years']) / demo[
        'population']
    demo['o60'] = (demo['60-64_years'] + demo['over_65_years']) / demo[
        'population']
    demo['total'] = demo['u19'] + demo['20s'] + demo['30s'] + demo['40s'] + \
                    demo['50s'] + demo['o60']

    demo_pop = demo[['nta_code', 'population', 'nta_name', 'borough']]
    demo_age = demo[['nta_name', 'borough', 'nta_code', 'u19', '20s', '30s',
                     '40s', '50s', 'o60']]

    names = demo[['nta_name', 'borough']]
    names.index = demo['nta_code']

    return demo_pop, demo_age, names


def find_top_5(df, demo, n=-1):
    zones = list(pd.read_csv('../Original Data/geographic.csv').columns)

    pop_dict = {}

    for zone in zones:
        try:
            pop = demo.loc[demo['nta_code'] == zone]['population'].iloc[0]
        except:
            pop = 0
        pop_dict[zone] = pop

    vc = df['do_zone'].value_counts()

    party_dict = {}

    for zone in vc.index:
        if pop_dict[zone] != 0:
            party_dict[zone] = vc[zone] / pop_dict[zone]
        else:
            party_dict[zone] = 0

    sorted_p = sorted(party_dict, key=party_dict.get, reverse=True)[:n]

    return sorted_p


def main():
    df_names = ['pickup_datetime','dropoff_datetime','pu_long','pu_lat','do_long',
                'do_lat','pu_zone','do_zone']

    df11 = pd.read_csv('./11pm_data.csv', index_col='pickup_datetime',
                       names=df_names)

    df12 = pd.read_csv('./12am_data.csv', index_col='pickup_datetime',
                       names=df_names)

    df01 = pd.read_csv('./01am_data.csv', index_col='pickup_datetime',
                       names=df_names)
    df02 = pd.read_csv('./02am_data.csv', index_col='pickup_datetime',
                       names=df_names)
    df03 = pd.read_csv('./03am_data.csv', index_col='pickup_datetime',
                       names=df_names)
    df04 = pd.read_csv('./04am_data.csv', index_col='pickup_datetime',
                       names=df_names)
    df05 = pd.read_csv('./05am_data.csv', index_col='pickup_datetime',
                       names=df_names)
    df06 = pd.read_csv('./06am_data.csv', index_col='pickup_datetime',
                       names=df_names)

    dp, da, names = get_demo()
    top_5_all = []
    for hour in [df11, df12, df01, df02, df03, df04, df05, df06]:
        top_5 = find_top_5(hour, dp, 5)
        top_5_all.extend(top_5)

    top_5_all = set(top_5_all)
    plot_dict = {}
    for zone in top_5_all:
        plot_dict[zone] = []

    for hour in [df11, df12, df01, df02, df03, df04, df05, df06]:
        for j, k in enumerate(find_top_5(hour, dp)):
            if k in top_5_all:
                plot_dict[k].append(j + 1)

    plot_change(plot_dict, names)


if __name__ == "__main__":
    main()
