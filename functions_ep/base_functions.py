import pandas as pd


def read_two_dates():
    print("Please enter two dates in the format YYYY-MM-DD")
    date_1 = input()
    if date_1 == "":
        date_1 = "2020-01-01"
    elif len(date_1) == 4:
        date_1 = date_1 + "-01-01"
    date_2 = input()
    if date_2 == "":
        date_2 = "2022-12-31"
    elif len(date_2) == 4:
        date_2 = date_2 + "-01-01"

    date_1 = pd.to_datetime(date_1, format="%Y-%m-%d")
    date_2 = pd.to_datetime(date_2, format="%Y-%m-%d")
    if date_2 < date_1:
        date_1, date_2 = date_2, date_1
    return date_1, date_2


def get_list_of_countries(table):
    set_with_countries = table['location_key']
    set_with_countries = sorted(list(set_with_countries.drop_duplicates()))
    return set_with_countries

