import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import joblib
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Klasifikasi Hari di Chinatown, Melbourne",
    page_icon="🔢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- KONSTANTA ---
MODEL_PATH = './models/random_forest_model.pkl'
CLASS_LABELS = { 1: "Weekend (Akhir Pekan)", 2: "Weekday (Hari Kerja)"}

PRESETS = {
    "weekend": [
        394, 264, 140, 144, 104, 28, 28, 25, 70, 153, 401, 649, 1216, 1399, 1249, 1240, 1109, 1137, 1290, 1137, 791, 638, 597, 316
    ],
    "weekday": [
        97,	45,	25,	22,	18,	21,	44,	98,	234, 194,	397,	642,	1392,	1336,	1111,	949,	1012,	1275,	1261,	1282,	966,	792,	380,	251

    ],
}

# --- FUNGSI UPDATE STATE ---
def update_inputs(preset_name):
    """Mengubah nilai semua input field berdasarkan preset"""
    values = PRESETS[preset_name]
    for i, val in enumerate(values):
        # Update session_state dengan key 'input_{i}'
        st.session_state[f"input_{i}"] = val

# --- FUNGSI LOAD MODEL ---
@st.cache_resource
def load_model_strict():
    if not os.path.exists(MODEL_PATH):
        st.error(f"🚨 FATAL ERROR: File model '{MODEL_PATH}' tidak ditemukan!")
        st.stop()
    return joblib.load(MODEL_PATH)

# --- FUNGSI UI INPUT FIELDS ---
def create_time_inputs_with_state():
    """Membuat 24 Input Field yang terhubung ke session state."""
    
    for i in range(24):
        if f"input_{i}" not in st.session_state:
            st.session_state[f"input_{i}"] = 0

    tabs = st.tabs(["Dini Hari (00-05)", "Pagi (06-11)", "Siang (12-17)", "Malam (18-23)"])
    
    current_values = []
    
    for i in range(24):
        tab_idx = i // 6
        with tabs[tab_idx]:
            # Layout Grid 6 Kolom
            col_idx = i % 6
            if col_idx == 0:
                cols = st.columns(6)
            
            with cols[col_idx]:
                # GANTI DI SINI: st.slider -> st.number_input
                st.number_input(
                    label=f"{i:02d}:00",
                    min_value=0,
                    max_value=5000, # Batas wajar
                    step=10,        # Tombol panah nambah 10
                    key=f"input_{i}" # Kunci memori
                )
                current_values.append(st.session_state[f"input_{i}"])

    return np.array([current_values])

# --- MAIN APP ---
def main():
    st.title("Klasifikasi Hari di Chinatown, Melbourne")
    st.info("""
    Aplikasi ini berfungsi untuk mengidentifikasi apakah pola volume pejalan kaki per jam di Chinatown, Melbourne menunjukkan hari kerja (weekday) atau akhir pekan (weekend)
    """)
    st.markdown("---")

    model = load_model_strict()

    col_input, col_result = st.columns([1.5, 1])

    with col_input:
        st.subheader("Input Volume Pejalan Kaki per Jam")
        
        # --- TOMBOL PRESET --- 
        st.info("Gunakan template cepat untuk mencoba pola umum weekday/weekend.")
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            st.button("Coba Pola Weekday", type='primary', on_click=update_inputs, args=("weekday",), use_container_width=True)
        
        with col_btn2:
            st.button("Coba Pola Weekend", type='primary', on_click=update_inputs, args=("weekend",), use_container_width=True)
            
        with col_btn3:
            def reset():
                for i in range(24): st.session_state[f"input_{i}"] = 0
            st.button("🔄 Reset", on_click=reset, use_container_width=True)
        
        st.write("") # Spacer

        # Panggil Fungsi Input Field
        user_input = create_time_inputs_with_state()

    with col_result:
        st.subheader("📊 Analisis Real-time")
        
        # Plotting (Tetap sama biar user bisa visualisasi angka yang diketik)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.axvspan(6, 9, color='yellow', alpha=0.1, label='Rush Hour Pagi')
        ax.axvspan(16, 19, color='orange', alpha=0.1, label='Rush Hour Sore')
        
        ax.plot(user_input[0], marker='o', color='#4F8BF9', linewidth=2, label='Data Input')
        ax.set_title("Visualisasi Data Input")
        ax.set_xlabel("Jam")
        ax.set_ylabel("Volume")
        ax.grid(True, alpha=0.3)
        ax.legend(loc='upper left', fontsize='small')
        st.pyplot(fig)

        # Prediksi
        if st.button("Prediksi Hari", type="primary", use_container_width=True):
            pred = int(model.predict(user_input)[0])
            probs = model.predict_proba(user_input)[0]
            confidence = np.max(probs) * 100

            st.divider()
            if pred == 1:
                st.success(f"### Hasil: {CLASS_LABELS[1]}")
                st.write("Model mendeteksi pola liburan/santai.")
            else:
                st.info(f"### Hasil: {CLASS_LABELS[2]}")
                st.write("Model mendeteksi pola aktivitas kerja.")
            
            st.metric("Confidence Score", f"{confidence:.2f}%")

if __name__ == "__main__":
    main()