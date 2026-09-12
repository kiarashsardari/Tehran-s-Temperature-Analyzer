from calculate import describe as d
from dataset_maker import main as m
#تلاش برای اجرای برنامه بر روی یک فایل
try:
    d('Tehran_tmps_dataset.csv')
#اگر فایل وجود نداشت بساز بعد برنامه را اجرا کن
except FileNotFoundError:
    m()
    d('Tehran_tmps_dataset.csv')