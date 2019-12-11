import pandas as pd
import numpy as np


def pumping_cost(H, year, state):
    P = pd.read_excel('MAP_energy_prices.xlsx', index_col=0)
    # constants
    A = 1.36127

    # Nebraska Pumping Standard (assumign 50-50 diesel and electric
    NPSd = 18  # diesel
    NPSe = 1.15  # electric

    k_d = A / NPSd

    k_e = A / NPSe

    # H (pumping lift) is in feet
    # calculate pumping cost in units of dollars per acre-foot
    cyear = P.loc[year]
    P_e = cyear['{}_elec'.format(state)]
    P_d = cyear['{}_dies'.format(state)]

    return np.mean(((k_d * H * P_d), (k_e * H * P_e)))