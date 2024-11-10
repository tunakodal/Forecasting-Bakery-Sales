# Correlation Analysis of Items
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Veriyi yükleme
df = pd.read_csv('bakery_sales_dataset_4.5.csv')

# Korelasyonu analiz edilecek sütunlar
columns = ['Brent Price','WTI Price','Average Price','tmin',
           'tmax','tavg','wspd','pres','filter coffee', 'bread', 'croissant', 'angbutter',
           'tea', 'cake', 'cookie',
           'plain bread', 'pastry', 'sandwich', 'hot chocolate', 'orange pound', 'latte',
           'americano', 'cacao deep', 'wiener', 'pandoro', 'brownie', 'jam', 'farm house bread',
           'juice', 'muffin', 'scone', 'soup', 'toast', 'scandinavian', 'gateau chocolat',
           'truffles', 'coke', 'spanish brunch', 'fudge', 'baguette bread', 'tiffin', 'milk tea',
           'chicken stew', 'jammie dodgers', 'mineral water', 'hearty & seasonal', 'cheesecake',
           'salad', 'frittata', 'smoothies', 'the nomad', 'vegan mincepie', 'berry ade', 'focaccia']

# Korelasyon matrisini hesaplama
matrix = df[columns].corr()

# Grafik boyutunu büyütme ve çözünürlüğü artırma
plt.figure(figsize=(24, 30), dpi=200)  # Boyut ve çözünürlük artırıldı

# Korelasyon matrisinin ısı haritasını oluşturma
sns.heatmap(matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.7,
            cbar_kws={'shrink': 0.75}, annot_kws={'size': 8}, xticklabels=1, yticklabels=1)

# Etiketlerin döndürülmesi
plt.xticks(rotation=90)
plt.yticks(rotation=0)

# Başlık ekleme
plt.title('Correlation Matrix of Bakery Items', fontsize=18)

    # Görselleştirmeyi gösterme
plt.tight_layout()  # Kenarlıkların düzgün olmasını sağlar
plt.show()