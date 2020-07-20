import numpy as np
from typing import List, Union


def current_value(cash_flow: np.array, interest_rate: float):
    interest_rate_flow = np.array(
        [interest_rate**i for i in range(len(cash_flow))])
    print(cash_flow*interest_rate_flow)
    return np.sum(cash_flow*interest_rate_flow)


if __name__ == "__main__":
    sa = current_value(np.array([3, 4, 5,12]), 0.2)
    print(sa)
    print(type(sa))