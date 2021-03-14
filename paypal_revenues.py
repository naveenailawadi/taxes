from core.handlers import RevenueHandler
import sys

NAME_COL = 'Name'
NET_REVENUE_COL = 'Net'
TRANSACTION_STATUS_COL = 'Status'

RELEVANT_STATUSES = ['Completed']


def main(filename):
    # make a revenue handler
    handler = RevenueHandler(filename)

    # drop all the nulls in the name column
    handler.drop_nulls(NAME_COL)

    # only keep positive numbers
    handler.filter_amounts(NET_REVENUE_COL)

    # filter for only completed transactions
    handler.keep_only(TRANSACTION_STATUS_COL, RELEVANT_STATUSES)


# inquire for the filename and get the revenues
if __name__ == '__main__':
    filename = sys.argv[1]

    main(filename)
