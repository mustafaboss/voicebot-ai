import streamlit as st
import pandas as pd
import requests
import os
from dotenv import load_dotenv
import os

load_dotenv()  # This will load .env variables

# ==== ElevenLabs API Configuration ====
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "MF3mGyEYCl7XYWbV9V6O"
# ==== Audio Output Folder ====
OUTPUT_FOLDER = "generated_reports"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ==== Voice Generator Function ====
def generate_voice_elevenlabs(text, filename):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.6
        }
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        file_path = os.path.join(OUTPUT_FOLDER, filename)
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path
    else:
        st.error(f"❌ Voice Generation Failed: {response.status_code} - {response.text}")
        return None

# ==== Urdu Message Creator ====
def create_urdu_message(name, volume_daily, achieved):
    remaining = volume_daily - achieved
    return (
        f"السلام علیکم {name} صاحب، "
        #f"آپ کا آج کا ہدف تھا {int(volume_daily):,}، "
        #f"آپ نے ابھی تک مکمل کیا ہے {int(achieved):,}، "
        #f"تو باقی رہ گیا ہے {int(remaining):,}۔ شکریہ۔"
    )

# ==== Streamlit UI ====
st.set_page_config(page_title="ASM Report Voice Generator", page_icon="📢")
st.title("📊 ASM Urdu Report - ElevenLabs Audio Generator")

uploaded_file = st.file_uploader("📥 اپنی Excel فائل اپلوڈ کریں (جس میں 'ASM', 'Volume Daily', 'Ach 11.59' ہوں)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    required_cols = ['ASM', 'Volume Daily', 'Ach 11.59']
    if not all(col in df.columns for col in required_cols):
        st.error(f"❌ فائل میں یہ کالم موجود ہونے چاہئیں: {', '.join(required_cols)}")
        st.stop()

    st.success(f"✅ {len(df)} ریکارڈز کامیابی سے لوڈ ہو گئے!")

    for index, row in df.iterrows():
        name = row['ASM']
        volume = int(row['Volume Daily'])
        achieved = int(row['Ach 11.59'])
        urdu_text = create_urdu_message(name, volume, achieved)
        filename = f"{name.replace(' ', '_')}_report.mp3"

        with st.expander(f"📢 رپورٹ - {name}", expanded=False):
            st.markdown(f"**🎯 Target:** {volume}")
            st.markdown(f"**✅ Achieved:** {achieved}")
            st.markdown(f"**🧾 Message:** {urdu_text}")

            if st.button(f"🔊 آواز سنیں ({name})", key=f"play_{index}"):
                with st.spinner("🎙️ آواز تیار ہو رہی ہے..."):
                    audio_path = generate_voice_elevenlabs(urdu_text, filename)
                    if audio_path:
                        st.audio(audio_path, format="audio/mp3")
                        st.success(f"💾 آڈیو محفوظ ہو گیا: `{audio_path}`")
else:
    st.info("⏳ براہ کرم اپنی Excel فائل اپلوڈ کریں۔")
