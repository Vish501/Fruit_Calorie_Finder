# Requires lxml installed

import pandas as pd
import requests


def main():
    fruit = get_string("Item: ")
    fruit = fruit.strip().lower()

    # Building dictionary
    url = "https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/raw-fruits-poster-text-version-accessible-version"

    dict_fruit = get_dict_html(url)

    # Printing result
    if fruit in dict_fruit:
        print(f"Calories: {dict_fruit[fruit]}")


# Getting a string from the user
def get_string(x):
    while True:
        try:
            user_string = input(x)
            if user_string != "":
                return user_string
        except:
            pass
        print(f"Enter a valid string")


# Building a dictionary using the html passed to the fuction and cleaning un-needed data
def get_dict_html(url):
    dataframe_fruit = pd.read_html(requests.get(url).content)[0]
    dataframe_fruit = dataframe_fruit.iloc[:, :2]

    # Cleaning the table to only return back fruit names as keys in our final dictionary
    text = ""
    for i in range(len(dataframe_fruit)):
        for char in dataframe_fruit.iat[i, 0]:
            if char.isnumeric() is True:
                break
            elif char == ",":
                text = text.split(" ")[0]
                break
            else:
                text += char
        dataframe_fruit.iat[i, 0] = text.strip().lower().replace("  ", " ")
        text = ""

    # Renaming the table headers to allow for easier zipping
    dataframe_fruit= dataframe_fruit.set_axis(["fruit", "calories"], axis=1)
    dict_fruit = dict(zip(dataframe_fruit.fruit, dataframe_fruit.calories))
    return dict_fruit


if __name__ == "__main__":
    main()