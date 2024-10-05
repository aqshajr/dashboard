import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

orderpayments_df = pd.read_csv('orderpayments_df.csv')
orders_df = pd.read_csv('orders_df.csv')

st.title("Rata-rata Nilai Transaksi Berdasarkan Metode Pembayaran")

orderpayments_df = orderpayments_df.groupby('payment_type')['payment_value'].mean().sort_values()

fig, ax = plt.subplots()
ax.bar(orderpayments_df.index, orderpayments_df.values, color='#72BCD4')
ax.set_title('Rata-rata Nilai Transaksi Berdasarkan Metode Pembayaran', fontsize=15)
ax.set_xlabel('Metode Pembayaran', fontsize=12)
ax.set_ylabel('Rata-rata Nilai Transaksi', fontsize=12)
plt.xticks(rotation=45)

st.pyplot(fig)

st.write("Data Rata-rata Nilai Transaksi Berdasarkan Metode Pembayaran")
st.table(orderpayments_df)

orders_df=orders_df.groupby(by="purchase_day_of_week").agg({
    "delivery_time": ["max", "min", "mean", "std"]
})
orders_df = orders_df.reset_index()

st.title(" Kecepatan Pengiriman Berdasarkan Hari")

ordered_days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
orders_df["purchase_day_of_week"] = pd.Categorical(orders_df["purchase_day_of_week"], categories=ordered_days, ordered=True)
orders_df = orders_df.sort_values(by="purchase_day_of_week")

fig, ax = plt.subplots()
ax.plot(orders_df["purchase_day_of_week"], orders_df["delivery_time"]["mean"], marker='o', color='#72BCD4')
ax.set_title('Kecepatan Pengiriman Berdasarkan Hari')
ax.set_xlabel('Hari')
ax.set_ylabel('Rata-Rata Waktu Pengiriman (Hari)')
ax.invert_yaxis()

st.pyplot(fig)

st.write("Data Pengiriman")
st.table({
    'Hari': ordered_days,
    'Rata-Rata Waktu Pengiriman': orders_df["delivery_time"]["mean"]
})
