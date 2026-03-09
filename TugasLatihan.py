# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
# membaca data
data = pd.read_csv("tips.csv")

# %%
# menghitung jumlah laki-laki dan perempuan
gender_count = data['sex'].value_counts()

# %%
# membuat pie chart
plt.title("Persentase Pelanggan yang Memberikan Tips")

plt.pie(
    gender_count,
    labels=gender_count.index,
    autopct='%1.1f%%'
)

# %%
plt.show()

# %%
