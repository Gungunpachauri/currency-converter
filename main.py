import streamlit as st
import requests

st.set_page_config(page_title="Currency Converter 💱", page_icon="💰", layout="centered")

st.title("💰 Currency Converter")
st.markdown("Convert between world currencies using live exchange rates 🌍")

st.markdown("---")

CURRENCIES = [
    "USD", "INR", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "SGD",
    "NZD", "HKD", "KRW", "SEK", "NOK", "ZAR", "MXN", "THB", "AED"
]

col1, col2, col3 = st.columns(3)

with col1:
    amount = st.number_input("💵 Amount", min_value=0.0, value=1.0, step=0.5)

with col2:
    from_currency = st.selectbox("From Currency", options=CURRENCIES, index=CURRENCIES.index("USD"))

with col3:
    to_currency = st.selectbox("To Currency", options=CURRENCIES, index=CURRENCIES.index("INR"))

st.markdown("")

if st.button("🔁 Convert", use_container_width=True):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        
        if response.status_code != 200:
            st.error("⚠️ Error fetching exchange rate data. Try again later.")
        else:
            data = response.json()
            if to_currency not in data["rates"]:
                st.error(f"❌ Currency code '{to_currency}' not found.")
            else:
                rate = data["rates"][to_currency]
                converted_amount = amount * rate
                
                st.success(f"✅ {amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
                st.caption(f"Exchange Rate: **1 {from_currency} = {rate:.4f} {to_currency}**")

                # Optional styling with a progress bar animation
                st.progress(100)
    except Exception as e:
        st.error(f"Something went wrong 😢\n{e}")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit and ExchangeRate API")

