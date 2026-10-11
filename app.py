import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("text-classification", model="laaduvansh/scam-detector-model")

clf = load_model()

st.title("Scam Message Detector")
st.write("Paste any SMS or message to check if it looks like a scam.")

text = st.text_area("Paste a message here", height=150)

if st.button("Check"):
    if text.strip():
        result = clf(text)[0]
        label, score = result["label"], result["score"]
        if label == "SCAM":
            st.error(f"SCAM ({score:.1%} confident)")
        else:
            st.success(f"NORMAL ({score:.1%} confident)")
    else:
        st.warning("Please paste a message first.")
    st.caption("This is a screening aid, not a guarantee. Never share OTPs or PINs.")
