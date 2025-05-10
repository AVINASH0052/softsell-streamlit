import streamlit as st
from openai import OpenAI
import json
from datetime import datetime

# Configure Streamlit page
st.set_page_config(
    page_title="SoftSell - Software License Marketplace",
    page_icon="💻",
    layout="wide"
)

# Initialize NVIDIA client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

# Initialize session state for chat history and user info
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_info" not in st.session_state:
    st.session_state.user_info = {}

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif !important;
        background: #f7f9fb;
        color: #22223b;
    }
    .main {
        padding: 2rem;
        background: #f7f9fb;
    }
    h1, h2, h3, h4 {
        color: #22223b;
        font-weight: 700;
        letter-spacing: -1px;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #4f8cff 0%, #38b6ff 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        transition: background 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #38b6ff 0%, #4f8cff 100%);
    }
    .stTextInput > div > input,
    .stTextArea > div > textarea,
    .stSelectbox > div,
    .stSelectbox > div > div {
        color: #22223b !important;
        background: #fff !important;
    }
    .stSelectbox div[role="combobox"] {
        color: #22223b !important;
        background: #fff !important;
    }
    .stForm {
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 16px rgba(80, 80, 120, 0.07);
        padding: 2rem;
        margin-bottom: 2rem;
    }
    .stMarkdown {
        font-size: 1.1rem;
    }
    .chat-message {
        padding: 1.2rem;
        border-radius: 0.7rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
        background: #e9f1fb;
    }
    .chat-message.user {
        background-color: #d1e7ff;
        align-self: flex-end;
    }
    .chat-message.assistant {
        background-color: #f1f3f8;
        align-self: flex-start;
    }
    @media (max-width: 768px) {
        .main, .stForm {
            padding: 1rem !important;
        }
        h1 {
            font-size: 2rem !important;
        }
        h2 {
            font-size: 1.3rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div style="display: flex; align-items: center; gap: 1rem;">
        <img src="https://img.icons8.com/color/48/000000/software.png" width="48"/>
        <h1 style="margin-bottom: 0;">SoftSell</h1>
    </div>
""", unsafe_allow_html=True)
st.subheader("Your Trusted Software License Marketplace")
st.write("Sell your unused software licenses quickly and securely")

# How It Works Section
st.header("How It Works")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://img.icons8.com/fluency/48/upload.png")
    st.markdown("### 1. Upload License")
    st.write("Upload your software license details securely")
with col2:
    st.image("https://img.icons8.com/fluency/48/money.png")
    st.markdown("### 2. Get Valuation")
    st.write("Receive an instant market-based valuation")
with col3:
    st.image("https://img.icons8.com/fluency/48/receive-cash.png")
    st.markdown("### 3. Get Paid")
    st.write("Complete the sale and receive payment")

# Why Choose Us Section
st.header("Why Choose Us")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### Secure Transactions")
    st.write("Bank-grade security for all transactions")
with col2:
    st.markdown("### Best Market Rates")
    st.write("Get the best value for your licenses")
with col3:
    st.markdown("### Fast Process")
    st.write("Complete the sale in as little as 24 hours")

# Testimonials Section
st.header("What Our Customers Say")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div style="background:#fff; border-radius:10px; box-shadow:0 2px 8px #e0e1e6; padding:1rem; margin-bottom:1rem;">
    <b>"SoftSell made selling our unused licenses incredibly easy. The process was smooth and we got great value."</b>
    <br><br>
    <span style="color:#4f8cff;">John Smith</span><br>
    CTO, TechCorp
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style="background:#fff; border-radius:10px; box-shadow:0 2px 8px #e0e1e6; padding:1rem; margin-bottom:1rem;">
    <b>"The platform is intuitive and the support team is always helpful. Highly recommended!"</b>
    <br><br>
    <span style="color:#4f8cff;">Sarah Johnson</span><br>
    IT Manager, Innovate Inc
    </div>
    """, unsafe_allow_html=True)

# Contact Form
st.header("Get Started")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    company = st.text_input("Company")
    license_type = st.selectbox(
        "License Type",
        ["Microsoft Office", "Adobe Creative Suite", "Windows OS", "Other"]
    )
    if license_type == "Other":
        license_type = st.text_input("Please specify your license type")
    message = st.text_area("Message")
    submit = st.form_submit_button("Get a Quote")

    if submit:
        if name and email and company and message:
            # Store user info in session state
            st.session_state.user_info = {
                "name": name,
                "email": email,
                "company": company,
                "license_type": license_type
            }
            
            # Save form submission to a file (you can modify this to store in a database)
            submission = {
                "timestamp": datetime.now().isoformat(),
                "name": name,
                "email": email,
                "company": company,
                "license_type": license_type,
                "message": message
            }
            
            try:
                with open("submissions.json", "a") as f:
                    json.dump(submission, f)
                    f.write("\n")
                st.success("Thank you for your submission! We'll contact you shortly.")
            except Exception as e:
                st.error("There was an error saving your submission. Please try again.")
        else:
            st.error("Please fill in all required fields.")

# Chat Widget
st.header("Chat with Us")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("How can we help you?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare system message with user context
    system_message = "You are a helpful assistant for SoftSell, a software license marketplace. "
    if st.session_state.user_info:
        system_message += f"The user's name is {st.session_state.user_info.get('name', 'User')}. "
        system_message += f"They are from {st.session_state.user_info.get('company', 'their company')}. "
        system_message += f"They are interested in {st.session_state.user_info.get('license_type', 'software licenses')}. "

    # Get AI response using NVIDIA API
    try:
        completion = client.chat.completions.create(
            model="nvidia/llama-3.1-nemotron-ultra-253b-v1",
            messages=[
                {"role": "system", "content": system_message},
                *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            ],
            temperature=0.6,
            top_p=0.95,
            max_tokens=4096,
            frequency_penalty=0,
            presence_penalty=0
        )
        assistant_response = completion.choices[0].message.content
    except Exception as e:
        assistant_response = "I apologize, but I'm having trouble connecting to the chat service. Please try again later."

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

st.markdown(
    '<link rel="shortcut icon" href="https://img.icons8.com/color/48/000000/software.png">',
    unsafe_allow_html=True
) 