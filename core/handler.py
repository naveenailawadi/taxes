from core import settings
import pandas as pd
import os


# create a class to handle all csvs
class BaseHandler:
    def __init__(self, filename):
        self.filename = filename

        # load the initial csv
        self.load_csv()

    # create a loading function
    def load_csv(self):
        # check if the filename exists
        if os.path.exists(self.filename):
            self.df = pd.read_csv(self.filename)
        else:
            # create the csv and notify the user
            self.df = pd.DataFrame(settings.BASE_STRUCTURE)

    # create a function to save the csv
    def save_csv(self):
        self.df.to_csv(self.filename, index=False)

    def drop_nulls(self, column):
        # get most recent data
        self.load_csv()

        self.df = self.df[self.df[column].notna()]

        self.save_csv()

    # make a function to keep only types in a particular list
    def keep_only(self, column, keep_list):
        # load the csv
        self.load_csv()

        # filter for what's in the column
        bool_df = self.df[column].isin(keep_list)

        self.df = self.df[bool_df]

        self.save_csv()


# create a class to handle revenue
class RevenueHandler(BaseHandler):
    # change the loading function
    def load_csv(self):
        # check if the filename exists
        if os.path.exists(self.filename):
            self.df = pd.read_csv(self.filename)
        else:
            # create the csv and notify the user
            self.df = pd.DataFrame(settings.REVENUE_STRUCTURE)

    # get only the positive numbers (mainly for getting rid of negative numbers)
    def filter_amounts(self, column, greater_than_cutoff=0):
        # load the most recent csv
        self.load_csv()

        # strip the column of commas
        self.df.replace(',', '', regex=True, inplace=True)

        # translate the column to floats
        self.df[column] = self.df[column].astype(float)

        # filter the rows
        self.df[[column]] = self.df[self.df[[column]]
                                    > greater_than_cutoff][[column]]

        # save the csv
        self.save_csv()

        # drop the nulls (will save by default)
        self.drop_nulls(column)
