import streamlit as st

def app():
    st.title('Hypothesis testing')

    st.header('Hypothesis statement')
    st.write('Apakah rata-rata pembelian gender female bertype member sama dengan rata-rata pembelian total?')

    st.markdown('Saya ingin mencari tahu bagaimana pengaruh dari keanggotaan seorang customer dan dari gender manakah yang berpengaruh terhadap pembelian di supermarket')
    st.markdown('Pertama saya melakukan Measure of Central Tendency untuk mengetahui nilai mean, median, dan modus dari data tersebut')
    st.markdown('Didapatkan nilai mean dari pembelian gender female bertype member sebesar : 337.7277528735631, median : 266.028, dan modus : 93.7440, 189.0945, dan 216.8460')
    st.markdown('Kemudian saya lakukan penghitung nilai skewness untuk mengetahui apakah data terdistrbusi normal atau tidak')
    st.markdown('Didapatkan nilai skewness sebesar : 0.8258619418349009')
    st.markdown('Karena nilai skewness lebih besar dari 0.5, maka data tesebut termasuk positif skewed atau tidak terdistribusi normal')
    st.markdown('Karena data tidak tedistribusi secara normal, maka akan dilakukan pencarian outlier menggunakan IQR')
    st.markdown('Dilakukan pencarian terhadap Q1 dan Q3 dari data, didapatkan nilai Q1 : 118.9020 dan Q3 : 506.6355')
    st.markdown('Setelah itu dilakukan pencarian IQR dengan menggunakan rumus IQR= Q3-Q1')
    st.markdown('Kemudian ditentukan limit atas dan limit bawahnya')
    st.markdown('Mencari limit atas menggunakan rumus :Q3 + 1.5*IQR dan limit bawah menggunakan rumus :Q1 - 1.5*IQR')
    st.markdown('Setelah dilakukan penentuan limit atas dan bawah, kemudian dilakukan pencarian outlier')
    st.markdown('Pencarian outlier menggunakan persamaan outlier_iqr= data_product_female_member[(data_product_female_member.Total > upper_limit) | (data_product_female_member.Total < lower_limit)]')
    st.markdown('Dari hasil persamaan di atas tidak didapatkan outlier, maka data sudah bisa digunakan untuk melakukan hypothesis testing')
    st.markdown('Pada proses hypothesis testing saya menggunakan single sample hypothesis testing, karena data yang dimasukkan hanya terdapat 1 sample')
    st.markdown('Pada Proses ini saya menentukan H0: μ total member female = μ total customer all type and gender dan H1: μ total member female != μ total customer all type and gender')
    st.markdown('Sebagai data pembanding saya menggunakan rata-rata total dari seluruh pembelian')
    st.markdown('Dari proses penggunaan single sample hypothesis testing didapatkan nilai P-value : 0.3572784040547631')
    st.markdown('Pada proses hypothesis testing ini saya menggunakan signifikansi level sebesar 0.05 atau 5%')
    st.markdown('Karena nilai P-value lebih besar dari signifikansi level, maka H0 gagal ditolak')
    st.markdown('Saya menyarankan untuk pemilik supermarket, karena rata-rata pembelian oleh member female sama dengan rata-rata pembeian seluruh customer, maka dapat dilakukan pemberian promo terhadap member female agar pembelian yang dilakukan lebih meningkat')

st.write('This is outside function')