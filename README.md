# Scam Message Detector

A machine learning model that checks whether an SMS or message looks like a scam. Built to help people spot fake KYC updates, UPI refund links, fake job offers and lottery scams.

## Model
- Base model: DistilBERT (Hugging Face Transformers, PyTorch)
- Data: UCI SMS Spam Collection plus 40 hand-written Indian-style messages
- Trained on Google Colab (T4 GPU)
- Model on Hugging Face: https://huggingface.co/laaduvansh/scam-detector-model

## Results
| Test set | Accuracy | F1 |
|---|---|---|
| SMS Spam held-out set (1,115 messages) | 99.2% | 96.9% |
| Hand-made Indian messages (16), before adding Indian data | 68.8% | - |
| Hand-made Indian messages (16), after adding Indian data | 87.5% | - |

## Limitations
- The Indian test set is very small (16 messages), so those numbers are only indicative.
- The main dataset is older English SMS, so new scam styles and other languages (Hindi, Hinglish) may be missed.
- This is a screening aid, not a guarantee. Never share OTPs or PINs, even if the tool says a message is safe.

## Demo
live demo:
https://scam-detector-hvc3sh9hkdwntd2tj6vwic.streamlit.app/

