import pandas as pd

df = pd.read_csv('bakery_sales.csv')

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

edinburgh = [
    (22, 10),  # 22 Ekim
    (27, 10),  # 27 Ekim
    (20, 12),  # 20 Aralık
    (25, 12),  # 25 Aralık
    (26, 12),  # 26 Aralık
    (1, 1),  # 1 Ocak
    (2, 1),  # 2 Ocak
    (19, 1),  # 19 Ocak
    (25, 1)  # 25 Ocak
]

korea = [
    (1, 1),  # 1 Ocak
    (7, 2),  # 7 Şubat
    (8, 2),  # 8 Şubat
    (9, 2),  # 9 Şubat
    (10, 2),  # 10 Şubat
    (1, 3),  # 1 Mart
    (1, 5),  # 1 Mayıs
    (5, 5),  # 5 Mayıs
    (14, 5),  # 14 Mayıs
    (6, 6),  # 6 Haziran
    (14, 9),  # 14 Eylül
    (15, 9),  # 15 Eylül
    (16, 9),  # 16 Eylül
    (9, 10),  # 9 Ekim
    (25, 12)  # 25 Aralık
]


def isHoliday(row):
    if row['Place'] == 'edinburgh':
        return 1 if (row['Date'].day, row['Date'].month) in edinburgh else 0
    else:
        return 1 if (row['Date'].day, row['Date'].month) in korea else 0


df['isHoliday'] = df.apply(isHoliday, axis=1)

df.to_csv('bakery_sales_2.csv', index=False)
