import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    from scipy.stats import chi2
    alpha = 1 - p
    return sum(x ** 2) / (chi2.ppf(1 - alpha / 2) * np.sqrt(27)), \
           sum(x ** 2) / (chi2.ppf(alpha / 2) * np.sqrt(27))
