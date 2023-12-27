import pandas as pd
import scipy.stats
from scipy.stats import pearsonr
from functions_ep.base_functions import get_list_of_countries
import numpy as np

def find_correlation(country, table):
    data = table[table.location_key == country]
    new_confirmed = list(data['new_confirmed'])  # кол-во зарегистрированных случаев
    new_recovered = list(data['new_recovered'])  # кол-во выздоровевших
    new_deceased = list(data['new_deceased'])  # кол-во умерших
    i_lst = new_confirmed[0]
    j_lst = new_recovered[0]
    k_lst = new_deceased[0]
    confirmed_cases = [i_lst]
    recovered_cases = [j_lst]
    deceased_cases = [k_lst]

    for i, j, k in zip(new_confirmed, new_recovered, new_deceased):
        i_lst += i
        j_lst += j
        k_lst += k
        confirmed_cases.append(i_lst)
        recovered_cases.append(j_lst)
        deceased_cases.append(k_lst)


    corr_recovered = 0
    corr_deceased = 0
    # коэффициенты корреляции Пирсона
    if not all(x == 0 for x in recovered_cases):
        corr_recovered, _p_value = pearsonr(confirmed_cases, recovered_cases)
    if not all(x == 0 for x in deceased_cases):
        corr_deceased, p_value = pearsonr(confirmed_cases, deceased_cases)

    print("\nМежду числом зарегистрированных случаев и числом выздоровевших:")

    if corr_recovered > 0 and corr_recovered < 1:
        print(
            "Динамика выбывания имеет маленькое запаздывание, это означает, что количество выздоровевших COVID-19 растет примерно в то же время, что и количество зарегистрированных случаев")
    elif corr_recovered == 0:
        print(
            "Динамика выбывания не зависит от числа зарегистрированных случаев, это означает, что количество выздоровевших от COVID-19 не зависит от количества зарегистрированных случаев")
    elif corr_recovered < 0 and corr_recovered > -1:
        print(
            "Динамика выбывания имеет большое запаздывание, это означает, что количество выздоровевших от COVID-19 начинает расти только после того, как количество зарегистрированных случаев достигнет своего пика")
    else:
        print("Коэффициент корреляции вне диапазона.")

    print("\nМежду числом зарегистрированных случаев и числом умерших:")

    if corr_deceased > 0 and corr_deceased < 1:
        print(
            "Динамика выбывания имеет маленькое запаздывание, это означает, что количество умерших COVID-19 растет примерно в то же время, что и количество зарегистрированных случаев")
    elif corr_deceased == 0:
        print(
            "Динамика выбывания не зависит от числа зарегистрированных случаев, это означает, что количество умерших от COVID-19 не зависит от количества зарегистрированных случаев")
    elif corr_deceased < 0 and corr_deceased > -1:
        print(
            "Динамика выбывания имеет большое запаздывание, Это означает, что количество умерших от COVID-19 начинает расти только после того, как количество зарегистрированных случаев достигнет своего пика")
    else:
        print("Коэффициент корреляции вне диапазона.")


def main():
    table = pd.read_csv("new_table_epidemic.csv")
    table.date = pd.to_datetime(table.date, format="%Y-%m-%d")
    set_with_countries = get_list_of_countries(table)
    print("Введите название страны:")
    country = input()
    if country in set_with_countries:
        try:
            find_correlation(country, table)
        except scipy.stats.ConstantInputWarning:
            print("Неверный формат данных")
    else:
        print("Такой страны нет в базе данных")


if __name__ == '__main__':
    main()
