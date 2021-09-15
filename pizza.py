# !/usr/bin/env python3

# Created by Trent Hodgins
# Created on 09/15/2020
# This program calculates the price of pizza

import pizza_constants


def main():
    # this function calculates the cost of pizza

    # input
    diameter = int(
        input("Enter the diameter of the pizza you would " + "like (inch): ")
    )

    # process
    sub_total = (
        pizza_constants.LABOR
        + pizza_constants.RENT
        + (diameter * pizza_constants.COST_PER_INCH)
    )
    total = sub_total * pizza_constants.HST

    # output
    print("")
    print("The cost for a {0} inch pizza is ${1:,.2f}".format(diameter, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
