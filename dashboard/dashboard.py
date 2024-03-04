import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set_theme(style='dark')

df = pd.read_csv("main_data.csv")

st.header('Dashboard ku :D')

st.markdown("""
Pertanyaan 1 : Urutan musim yang paling berpengaruh terhadap peminjaman sepeda\n
Pertanyaan 2 : Urutan cuaca yang paling berpengaruh terhadap peminjaman sepeda\n
Pertanyaan 3 : Tren peminjaman sepeda\n
Pertanyaan 4 : Rentang jam yang paling sering digunakan untuk meminjam sepeda\n
Pertanyaan 5 : Rentang temperature yang paling sering digunakan untuk meminjam sepeda\n
""")

df_pertanyaan_1 = df.groupby('season')['cnt'].mean().to_frame().reset_index()
df_pertanyaan_2 = df.groupby('weathersit')['cnt'].mean().to_frame().reset_index()
df_pertanyaan_3 = df.groupby('dteday')['cnt'].sum().to_frame().reset_index()
df_pertanyaan_3['dteday'] = pd.to_datetime(df_pertanyaan_3['dteday'], format='%Y-%m-%d')
df_pertanyaan_4 = df.groupby('hr')['cnt'].mean().to_frame().reset_index()
df_pertanyaan_5 = df.groupby('atemp')['cnt'].mean().to_frame().reset_index()

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3","Pertanyaan 4","Pertanyaan 5"])

with tab1:
    df_pertanyaan_1.plot(x='season', y='cnt', kind='bar', legend=False)
    plt.xlabel('Season')
    plt.ylabel('Mean Count')
    plt.title('Mean Count by Season')
    st.pyplot(plt)
    st.markdown("""
Berdasarkan gambar sebelumnya, 3 merupakan season yang paling banyak dalam hal perentalan sepeda, lalu 2, lalu 4, lalu 1.
                
3 Merupakan season yang paling banyak dirental sepedanya. Dimana season ini merupakan season fall.\n
2 Merupakan season kedua paling banyak dirental sepedanya. Dimana season ini merupakan season summer.\n
4 merupakan season ketiga paling banyak dirental sepedanya. Dimana season ini merupakan season winter.\n
1 merupakan season yang paling sedikit dirental sepedanya. Dimana season ini merupakan season spring.\n
                
Menurut saya, seharusnya winter dan summer merupakan season yang memiliki sepeda yang dirental sedikit karena temperatur yang ekstrim tetapi berdasarkan data ini, sepertinya dugaan saya dibantah. Untuk alasannya mungkin saja season-season tersebut memiliki daya tarik tersendiri untuk bersepeda atau pada season-season tersebut memiliki hari kerja yang lebih banyak.
""")
    
with tab2:
    df_pertanyaan_2.plot(x='weathersit', y='cnt', kind='bar', legend=False)
    plt.xlabel('Weather Situation')
    plt.ylabel('Mean Count')
    plt.title('Mean Count by Weather Situation')
    st.pyplot(plt)
    st.markdown("""
Berdasarkan gambar sebelumnya, weather situation paling banyak dirental sepedanya adalah weather situation 1 lalu 2 lalu 3 lalu 4.

Hal ini sudah sesuai dengan dugaan saya karena weather situation 1 merupakan cuaca yang paling mendukung untuk bersepeda karena tidak hujan sama sekali sedangkan weather situation 4 merupakan cuaca yang paling tidak mendukung untuk bersepeda karena cuacanya sedang hujan deras, salju, hujan es, dan badai.
""")
    
with tab3:
    fig, ax = plt.subplots()
    ax.plot(df_pertanyaan_3['dteday'], df_pertanyaan_3['cnt'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Count')
    ax.set_title('Count Trend Over Time')
    ax.tick_params(axis="x",rotation=45)
    st.pyplot(fig)
    st.markdown("""
Jika dilihat pada gambar sebelumnya, terdapat hari dimana perentalan sepeda sangat sedikit. Dan juga bulan 4 sampai 10 merupakan bulan yang paling sering dirental sepeda. Tahun 2012 memiliki rental sepeda yang lebih banyak daripada rental 2011.
""")
    
with tab4:
    fig, ax = plt.subplots()
    ax.bar(df_pertanyaan_4['hr'], df_pertanyaan_4['cnt'])
    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Count')
    ax.set_title('Count by Hour of the Day')
    ax.set_xticks(df_pertanyaan_4['hr'])
    st.pyplot(fig)
    st.markdown("""
Jika dilihat pada gambar sebelumnya, terdapat dua "gunung" yaitu pada sekitar jam 8 pagi dan sekitar jam 5 sore. Hal ini dapat terjadi karena pada waktu tersebut merupakan waktu masuk kerja dan waktu pulang kerja.
""")

with tab5:
    fig, ax = plt.subplots()
    ax.plot(df_pertanyaan_5['atemp'], df_pertanyaan_5['cnt'], marker='o', color='skyblue', linestyle='-')
    ax.set_xlabel('Apparent Temperature')
    ax.set_ylabel('Count')
    ax.set_title('Continuous Line Graph of Count by Apparent Temperature')
    ax.grid(True)
    st.pyplot(fig)
    st.markdown("""
Jika dilihat pada gambar sebelumnya, rentang 0.6 sampai 0.85 merupakan rentang yang paling banyak digunakan untuk bersepda berdasarkan temperatur yang dirasakan. Hal ini dapat dijelaskan karena temperatur tersebut merupakan temperatur yang pas dimana temperatur tersebut tidak terlalu tinggi dan tidak terlalu rendah.
""")



