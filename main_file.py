import time
import os
import pandas  # Third party module

while True:
    # Checks is the file exists.
    if os.path.exists("temps_today.csv"):

        # Gets the data from the csv file
        data = pandas.read_csv("temps_today.csv")

        # Calculates and prints out the average of each tolumn from the file.
        print(data.mean())
    else:
        print("File doesnt exist")

    # Puts a 5 second sleep on the loop.
    time.sleep(10)
