import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Konfigurasi Halaman Web
st.set_page_config(page_title="Netflix Explorer", page_icon="🎬", layout="wide")

# 2. Judul Aplikasi
st.title("🎬 Netflix Data Explorer & Recommender")
st.markdown("Selamat datang di aplikasi interaktif Netflix! Anda dapat mencari rekomendasi film atau melihat metrik data di bawah ini.")
st.markdown("---")

# 3. Fungsi Load Data 
@st.cache_data
def load_data():
    df = pd.read_csv('NetFlix.csv')
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')
    df = df.dropna(subset=['date_added', 'rating'])
    df['primary_country'] = df['country'].apply(lambda x: x.split(',')[0])
    return df

df = load_data()

# ==========================================
# BAGIAN A: MESIN PENCARI (RECOMMENDER)
# ==========================================
st.header("🔍 Mesin Rekomendasi Film")
st.markdown("Cari film berdasarkan genre favorit dan tahun rilis minimal.")

# Membuat 2 kolom input agar rapi
col1, col2 = st.columns(2)
with col1:
    input_genre = st.text_input("Ketik Genre (Contoh: Action, Horror, Comedies)", value="Action")
with col2:
    # Input angka untuk tahun
    input_tahun = st.number_input("Tahun Rilis Minimal", min_value=1980, max_value=2021, value=2019)

# Logika Filter Pandas (Sama seperti Tantangan 5)
syarat_genre = df['genres'].str.contains(input_genre, case=False, na=False)
syarat_tahun = df['release_year'] >= input_tahun
df_tersaring = df[syarat_genre & syarat_tahun]

st.subheader(f"Rekomendasi Teratas untuk '{input_genre}' (Tahun >= {input_tahun})")
if df_tersaring.empty:
    st.warning("Maaf, tidak ada konten yang cocok dengan pencarian Anda.")
else:
    # Tampilkan 5 teratas
    hasil_pencarian = df_tersaring[['title', 'type', 'release_year', 'genres', 'primary_country']].sort_values(by='release_year', ascending=False).head(5)
    st.dataframe(hasil_pencarian, use_container_width=True)

st.markdown("---")

# ==========================================
# BAGIAN B: VISUALISASI DATA (EDA)
# ==========================================
st.header("📊 Analisis Proporsi Konten per Negara")

# Membuat Sidebar di sebelah kiri web
st.sidebar.header("Filter Analisis ⚙️")
list_negara = sorted(df['primary_country'].unique().tolist())
# Dropdown menu
negara_terpilih = st.sidebar.selectbox("Pilih Negara untuk Dianalisis", ["Global (Semua Negara)"] + list_negara)

# Logika Filter Visualisasi
if negara_terpilih == "Global (Semua Negara)":
    df_visual = df
else:
    df_visual = df[df['primary_country'] == negara_terpilih]

# Membuat Pie Chart (Sama seperti kode EDA Anda sebelumnya)
komposisi = df_visual['type'].value_counts()

if not komposisi.empty:
    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_alpha(0.0) # Membuat background transparan
    
    # Warna Netflix: Merah dan Abu-abu/Hitam
    ax.pie(komposisi, labels=komposisi.index, autopct='%1.1f%%', colors=['#E50914', '#564d4d'], 
           startangle=90, textprops={'fontsize': 12, 'color': 'white', 'fontweight': 'bold'})
    
    st.subheader(f"Proporsi Movie vs TV Show: {negara_terpilih}")
    st.pyplot(fig)
else:
    st.info("Tidak ada data yang cukup untuk divisualisasikan pada negara ini.")