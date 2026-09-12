import numpy as np
import pandas as pd
#شبیه سازی تاریخ و دمای هرروز یکسال تهران
def main():
    (pd.DataFrame({
        'Date' : np.arange('2025-01-01', '2026-01-01', dtype='datetime64[D]'),
        'Tmps' : (np.round(np.random.normal(30, 5, 365))).astype(int)
    })).to_csv('Tehran_tmps_dataset.csv', index=False, encoding='utf-8-sig')
