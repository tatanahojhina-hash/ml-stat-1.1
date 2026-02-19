import pandas as pd
import statistics as st
import matplotlib.pyplot as plt


df = pd.read_excel('FPS_hw_1_df_1_bank_customer.xlsx')


mean_age = st.mean(df['Age'])
std_dev_age = st.stdev(df['Age'])
min_age = df['Age'].min()
quartiles = df['Age'].quantile([0.25, 0.5, 0.75])
max_age = df['Age'].max()


print(f'Среднее значение возраста: {mean_age:.2f}')
print(f'Стандартное отклонение возраста: {std_dev_age:.2f}')
print(f'Минимальное значение возраста: {min_age}')
print(f'квартиль (0,25): {quartiles[0.25]:.2f}, квартиль (0,5): {quartiles[0.5]:.2f}, квартиль (0,75): {quartiles[0.75]:.2f}')
print(f'Mаксимальное значение возраста: {max_age}')


plt.hist(df['Age'], bins=20)
plt.title('Гистограмма распределения возрастов клиентов банка')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.show()