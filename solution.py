import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 324047628 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    sum_x2 = sum(x**2)
    q_l = chi2(2*n).ppf(q=alpha/2)
    q_r = chi2(2*n).ppf(q=1-alpha/2)
    return np.sqrt(sum_x2 / q_r / 27), np.sqrt(sum_x2 / q_l / 27)
