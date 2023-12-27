from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def plot_country_confirmed_stats(country, low, high, table, path):
    current_contry_table = table[table.location_key == country]
    current_contry_table = current_contry_table[
        (current_contry_table.date >= low) & (current_contry_table.date <= high)]
    current_contry_table = current_contry_table[["date", "new_confirmed"]]
    a = list(current_contry_table.date)
    b = list(current_contry_table.new_confirmed)
    plt.bar(a, b)
    plt.title(country)
    plt.xlabel("dates")
    plt.xticks(rotation='vertical')
    plt.ylabel("confirmed")
    plt.ylim(0)
    plt.savefig(path + "/" + country + '_cnf_stats' + ".png")


def plot_country_deceased_stats(country, low, high, table, path):
    current_contry_table = table[table.location_key == country]
    current_contry_table = current_contry_table[
        (current_contry_table.date >= low) & (current_contry_table.date <= high)]
    current_contry_table = current_contry_table[["date", "new_deceased"]]
    a = list(current_contry_table.date)
    b = list(current_contry_table.new_deceased)
    plt.bar(a, b)
    plt.title(country)
    plt.xlabel("dates")
    plt.xticks(rotation='vertical')
    plt.ylabel("deceased")
    plt.ylim(0)
    plt.savefig(path + "/" + country + '_dcs_stats' + ".png")


def absolute_growth(country, low, high, table, path):
    current_contry_table = table[table.location_key == country]
    current_contry_table = current_contry_table[
        (current_contry_table.date >= low) & (current_contry_table.date <= high)]
    current_contry_table = current_contry_table[["date", "new_confirmed"]]
    a = list(current_contry_table.date)
    b = list(current_contry_table.new_confirmed)
    new_a = []
    new_b = []
    for idx in range(0, len(b)):
        if b[idx] != 0:
            new_a.append(a[idx])
            new_b.append(b[idx])
    absolute = []
    for idx in range(1, len(new_b)):
        absolute.append(new_b[idx] - new_b[idx - 1])
    print(np.mean(absolute))
    plt.plot(new_a[1:], absolute)
    plt.title(country)
    plt.xlabel("dates")
    plt.xticks(rotation='vertical')
    plt.ylabel("confirmed absolute growth")
    plt.savefig(path + "/" + country + '_abs_growth' + ".png")


def rate_growth(country, low, high, table, path):
    current_contry_table = table[table.location_key == country]
    current_contry_table = current_contry_table[
        (current_contry_table.date >= low) & (current_contry_table.date <= high)]
    current_contry_table = current_contry_table[["date", "new_confirmed"]]
    a = list(current_contry_table.date)
    b = list(current_contry_table.new_confirmed)
    absolute = []
    new_a = []
    new_b = []
    for idx in range(0, len(b)):
        if b[idx] != 0:
            new_a.append(a[idx])
            new_b.append(b[idx])
    for idx in range(1, len(new_b)):
        absolute.append(new_b[idx] / new_b[idx - 1] * 100)
    new_a = new_a[1:]
    mean_value = np.mean(absolute)
    print(mean_value)
    plt.plot(new_a, absolute)
    plt.plot(new_a, [mean_value for i in range(len(new_a))])
    plt.plot(new_a, [100 for i in range(len(new_a))])
    plt.title(country)
    plt.xlabel("dates")
    plt.xticks(rotation='vertical')
    plt.yticks(range(0, int(max(absolute)) + 1, 50))
    plt.ylabel("confirmed rate growth")
    plt.legend(["rate growth", "mean == " + str(mean_value)[:5], "100%"])
    plt.savefig(path + "/" + country + "_rate_gr" + ".png")


def increase_rate_growth(country, low, high, table, path):
    current_country_table = table[table.location_key == country]
    current_country_table = current_country_table[
        (current_country_table.date >= low) & (current_country_table.date <= high)]
    current_country_table = current_country_table[["date", "new_confirmed"]]
    a = list(current_country_table.date)
    b = list(current_country_table.new_confirmed)
    absolute = []
    new_a = []
    new_b = []
    for idx in range(0, len(b)):
        if b[idx] != 0:
            new_a.append(a[idx])
            new_b.append(b[idx])
    for idx in range(1, len(new_b)):
        absolute.append(new_b[idx] / new_b[idx - 1] * 100 - 100)
    new_a = new_a[1:]
    print(np.mean(absolute))
    plt.plot(new_a, absolute)
    plt.title(country)
    plt.xlabel("dates")
    plt.xticks(rotation='vertical')
    plt.yticks(range(0, int(max(absolute)) + 1, 50))
    plt.ylabel("confirmed rate growth")
    plt.ylim(0, 500)
    plt.savefig(path + "/" + country + '_inc_rate' + ".png")


def deceased_absolute_growth(country, low, high, table, path):
    current_country_table = table[table.location_key == country]
    current_country_table = current_country_table[
        (current_country_table.date >= low) & (current_country_table.date <= high)]
    current_country_table = current_country_table[["date", "new_deceased"]]
    a = list(current_country_table.date)
    b = list(current_country_table.new_deceased)
    absolute = []
    new_a = []
    new_b = []
    for idx in range(0, len(b)):
        if b[idx] != 0:
            new_a.append(a[idx])
            new_b.append(b[idx])
    for idx in range(1, len(new_b)):
        absolute.append(new_b[idx] - new_b[idx - 1])
    print(np.mean(absolute))
    plt.plot(new_a[1:], absolute)
    plt.title(country)
    plt.xlabel("dates")
    plt.xticks(rotation='vertical')
    plt.ylabel("deceased absolute")
    plt.savefig(path + "/" + country + '_dcs_abs_growth' + ".png")


def deceased_rate_growth(country, low, high, table, path):
    current_country_table = table[table.location_key == country]
    current_country_table = current_country_table[
        (current_country_table.date >= low) & (current_country_table.date <= high)]
    current_country_table = current_country_table[["date", "new_deceased"]]
    a = list(current_country_table.date)
    b = list(current_country_table.new_deceased)
    absolute = []
    new_a = []
    new_b = []
    for idx in range(0, len(b)):
        if b[idx] != 0:
            new_a.append(a[idx])
            new_b.append(b[idx])
    for idx in range(1, len(new_b)):
        absolute.append(new_b[idx] / new_b[idx - 1] * 100)
    new_a = new_a[1:]
    mean_value = np.mean(absolute)
    print(mean_value)
    plt.plot(new_a, absolute)
    plt.plot(new_a, [mean_value for i in range(len(new_a))])
    plt.plot(new_a, [100 for i in range(len(new_a))])

    plt.title(country)
    plt.xlabel("dates")
    plt.xticks(rotation='vertical')
    plt.yticks(range(0, int(max(absolute)) + 1, 50))
    plt.ylabel("deceased rate growth")
    plt.legend(["rate growth", "mean == " + str(mean_value)[:5], "100%"])
    plt.savefig(path + "/" + country + "_dcs_rate_gr" + ".png")


def plot_vaccine_stats(country, low, high, table, path):
    current_country_table = table[table.location_key == country]
    current_country_table = current_country_table[
        (current_country_table.date >= low) & (current_country_table.date <= high)]
    current_country_table = current_country_table[["date", "new_persons_vaccinated"]]
    a = list(current_country_table.date)
    b = list(current_country_table.new_persons_vaccinated)
    plt.bar(a, b)
    plt.title(country)
    plt.xlabel("dates")
    plt.xticks(rotation='vertical')
    plt.ylabel("number of new vaccinated people")
    plt.ylim(0)
    plt.savefig(path + "/" + country + '_vaccine_stats' + ".png")


def plot_anxiety(path):
    file = pd.read_csv("anxiety.csv")
    file.Date = pd.to_datetime(file.Date)
    plt.plot(file.Date, file.Count)
    plt.title("anxiety")
    plt.xlabel("dates")
    plt.xticks(rotation='vertical')
    plt.ylabel("number of patients")
    plt.savefig(path + "/" + "anxiety" + ".png")


def plot_depression(path):
    file = pd.read_csv("depression.csv")
    file.Date = pd.to_datetime(file.Date)
    plt.plot(file.Date, file.Count)
    plt.title("depression")
    plt.xlabel("dates")
    plt.xticks(rotation='vertical')
    plt.ylabel("number of patients")
    plt.savefig(path + "/" + "depression" + ".png")


def waves(country, low, high, table, path):
    chosen_country = country
    start = low
    end = high
    stats_of_country = table[(table['location_key'] == chosen_country)][['date', 'new_confirmed']]
    stats_of_country = stats_of_country[(stats_of_country['date'] >= start) & (stats_of_country['date'] <= end)]
    stats_of_country = stats_of_country[stats_of_country['new_confirmed'] >= 0.0]
    # выкинул все отрицательные значения, остались даты и new confirmed нужной страны в нужный период
    dates = list(stats_of_country.date)
    confirmeds = list(stats_of_country.new_confirmed)
    # [i][0] - ind of new_conf, [i][1] - behavour: 0 - const, 1 - increasing, -1 - decreasing
    dynamic = [[0, 0]]
    increasing = 0
    for j in range(0, len(dates) - 1):
        if increasing == 0:
            if confirmeds[j] != confirmeds[j + 1]:
                dynamic.append([j, increasing])
                increasing = (1 if confirmeds[j] < confirmeds[j + 1] else -1)
        elif increasing == 1:
            if confirmeds[j] >= confirmeds[j + 1]:
                dynamic.append([j, increasing])
                increasing = (-1 if confirmeds[j] > confirmeds[j + 1] else 0)
        else:
            if confirmeds[j] <= confirmeds[j + 1]:
                dynamic.append([j, increasing])
                increasing = (1 if confirmeds[j] < confirmeds[j + 1] else 0)

    if dynamic[-1][0] != len(confirmeds):
        dynamic.append([len(confirmeds) - 1, increasing])

    if dynamic[0] == dynamic[1]:
        dynamic.pop(0)

    coords_x = []
    coords_y = []
    max_decrease = [0, 0]
    max_increase = [0, 0]
    for i in range(1, len(dynamic)):
        if dynamic[i][1] == -1:
            if dynamic[i][0] - dynamic[i - 1][0] > max_decrease[0]:
                max_decrease = [dynamic[i][0] - dynamic[i - 1][0], i]
        elif dynamic[i][1] == 1:
            if dynamic[i][0] - dynamic[i - 1][0] > max_increase[0]:
                max_increase = [dynamic[i][0] - dynamic[i - 1][0], i]

    for i in range(0, len(dynamic)):
        coords_x.append(dynamic[i][0])
        coords_y.append(confirmeds[dynamic[i][0]])
    plt.plot(coords_x, coords_y)
    plt.plot([coords_x[max_increase[1] - 1], coords_x[max_increase[1]]],
             [coords_y[max_increase[1] - 1], coords_y[max_increase[1]]], color='red')
    plt.plot([coords_x[max_decrease[1] - 1], coords_x[max_decrease[1]]],
             [coords_y[max_decrease[1] - 1], coords_y[max_decrease[1]]], color='purple')
    plt.xlabel("Дни")
    plt.ylabel("Количество новых заражений")
    plt.savefig(path + "/" + country + "_waves" + ".png")
