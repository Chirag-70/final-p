import streamlit as st
import pandas as pd
import numpy as np
import base64
from PIL import Image


img = Image.open("website_logo.jpg")
st.image(img,width=200)
#Background color yaha hai..
st.markdown(
    """
    <style>
    .stApp {
        background-color: #dedbd2;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#page wide ans concise yaha hai..
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    /* Global text color */
    html, body, [class*="css"] {
        color: #0a0908 !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #0a0908 !important;
    }

    /* Paragraphs, labels, widgets */
    p, span, label, div {
        color: #0a0908 !important;
    }

    /* Streamlit inputs text */
    input, textarea {
        color: #0a0908 !important;
    }

    /* Sidebar text */
    section[data-testid="stSidebar"] * {
        color: #0a0908 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#title css change..
st.markdown(
    "<h1 style='text-align: left; color: #0a0908; font-size: 80px;'>Krishi Saarthi</h1>",
    unsafe_allow_html=True
)
st.markdown("<hr style='border: none; height: 3px; background-color: #2c6e49; margin: 20px 0;'>",unsafe_allow_html=True)

def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# -----------------------------
# SESSION STATE
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_scheme" not in st.session_state:
    st.session_state.selected_scheme = None

# -----------------------------
# DATA
# -----------------------------
images_with_info = [
    {
        "img": img_to_base64("img1.jpg"),
        "title": "PM Kisan Samman Nidhi Yojana",
        "points": [
            "Income support: ₹6,000 per year in 3 equal installments.",
            "Eligible farmers: Small and marginal landholding farmer families.",
            "Direct transfer: Amount sent directly to bank account (DBT).",
            "Land record based: Farmer name must be in official land records.",
            "Exclusions: Income-tax payers & government employees not eligible."
        ],
        "link": "https://pmkisan.gov.in/"
    },
    {
        "img": img_to_base64("img2.jpg"),
        "title": "PM Fasal Bima Yojana",
        "points": [
            "Crop insurance against crop loss.",
            "Low premium rates for farmers.",
            "All farmers eligible.",
            "Covers pre & post-harvest losses.",
            "Claims credited directly to bank."
        ],
        "link": "https://pmfby.gov.in/"
    },
    {
        "img": img_to_base64("img3.jpg"),
        "title": "PM Krishi Sinchai Yojana",
        "points": [
            "Expands irrigation coverage.",
            "Promotes micro-irrigation.",
            "Eligible for all farmers.",
            "Efficient water management.",
            "Centre & State funding support."
        ],
        "link": "https://pmksy.gov.in/"
    },
    {
        "img": img_to_base64("img4.jpg"),
        "title": "PM Kisaan Maandhan Yojana",
        "points": [
            "Pension scheme: Provides a minimum pension of ₹3,000 per month after the age of 60.",
            "Eligible farmers: Small and marginal farmers aged 18–40 years.",
            "Contribution based: Farmers contribute ₹55–₹200 per month (based on age).",
            "Government co-contribution: Central Government contributes an equal amount to the pension fund.",
            "Exclusions: Farmers covered under EPFO, NPS, or income-tax payers are not eligible."
            
        ],
        "link": "https://kmy.gov.in/"
    },
    {
        "img": img_to_base64("img5.jpg"),
        "title": "Kisan credit card scheme",
        "points": [
            "Credit support: Provides short-term credit to farmers for crop cultivation and allied activities.",
            "Eligible beneficiaries: Farmers, tenant farmers, sharecroppers, and SHGs/JLGs involved in agriculture.",
            "Flexible usage: Credit can be used for seeds, fertilizers, pesticides, irrigation, and other farm needs.",
            "Interest benefit: Interest subvention available for timely repayment (effective low interest rate).",
            "Easy access: Issued as a card with withdrawal through ATMs / banks for easy and repeated use."
          
        ],
        "link": "https://www.rbi.org.in/"
    },
    {
        "img": img_to_base64("img6.jpg"),
        "title": "Soil Health Card Scheme",
        "points": [
            "Soil testing: Provides farmers with soil test results for their agricultural land.",
            "Nutrient advice: Recommends balanced use of fertilizers based on soil health.",
            "Eligible farmers: All farmers are eligible under the scheme.",
            "Periodic update: Soil Health Cards are issued every 2–3 years.",
            "Improves productivity: Helps reduce input cost and increase crop yield."
          
        ],
        "link": "https://soilhealth.dac.gov.in/"

    },
    {
        "img": img_to_base64("img7.jpg"),
        "title": "eNAM (National Agriculture Market)",
        "points": [
            "Online trading platform: A pan-India electronic market for agricultural commodities.",
            "Better price discovery: Enables transparent bidding and competitive prices for farmers.",
            "Eligible participants: Farmers, traders, and commission agents registered on the platform.",
            "Integrated markets: Links APMC mandis across states into a single national market.",
            "Quality & payments: Supports quality assaying and online payment settlement directly to farmers."
        ],
        "link": "https://www.enam.gov.in/"

    },
    {
        "img": img_to_base64("img8.jpg"),
        "title": "Agri Infrastructure Fund (AIF)",

        "points": [
            "Credit facility: Provides medium to long-term loans for post-harvest and farm infrastructure projects.",
            "Eligible beneficiaries: Farmers, FPOs, PACS, Agri-entrepreneurs, and startups are eligible.",
            "Interest subvention: 3% interest subsidy on loans (up to a specified limit).",
            "Credit guarantee: Loan coverage available under Credit Guarantee Fund to reduce risk.",
            "Infrastructure focus: Supports warehouses, cold storage, grading, sorting, and processing units."
        ],
        "link": "https://agriinfra.dac.gov.in/"
    },
    {
        "img": img_to_base64("img9.jpg"),
        "title": "mKisan SMS Service",
        "points": [
            "Information service: Sends agriculture-related alerts and advisories via SMS to farmers.",
            "Wide coverage: Covers topics like crop management, weather, pests, seeds, and government schemes.",
            "Eligible beneficiaries: All farmers with a registered mobile number can receive messages.",
            "Multi-lingual support: Messages are sent in local languages for better understanding.",
            "Free service: Farmers receive SMS alerts free of cost from the government."
            
        ],
        "link": "https://mkisan.gov.in/"

    },
    {
        "img": img_to_base64("img10.jpg"),
        "title": "National Food Security Mission (NFSM)",
        "points": [
            "Production enhancement: Aims to increase production of rice, wheat, pulses, and coarse cereals.",
            "Eligible beneficiaries: All farmers cultivating targeted crops in identified districts.",
            "Technology support: Provides high-yield seeds, fertilizers, and improved agronomic practices.",
            "Financial assistance: Offers subsidies and incentives to farmers for inputs and activities.",
            "Area focus: Targets districts with potential for crop expansion to ensure food security"
            
        ],
        "link": "https://www.nfsm.gov.in/"

    },


]

# -----------------------------
# GLOBAL CSS
# -----------------------------
st.markdown(
    """
    <style>
    .image-box {
        height: 260px;
        overflow: hidden;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    .image-box img {
        height: 100%;
        width: 100%;
        object-fit: cover;
        transition: transform 0.2s ease;
        cursor: pointer;
    }

    .image-box img:hover {
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# HOME PAGE
# -----------------------------
if st.session_state.page == "home":

    st.markdown("## 🌾 Government Schemes for Farmers")

    cols = st.columns(len(images_with_info))

    for i, scheme in enumerate(images_with_info):
        with cols[i]:

            st.markdown(
                f"""
                <div class="image-box">
                    <img src="data:image/jpeg;base64,{scheme['img']}">
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"View {scheme['title']}",
                key=f"btn_{i}",
                use_container_width=True
            ):
                st.session_state.selected_scheme = scheme
                st.session_state.page = "info"
                st.rerun()

# -----------------------------
# INFO PAGE
# -----------------------------
if st.session_state.page == "info":

    scheme = st.session_state.selected_scheme

    st.markdown(
        """
        <style>
        .info-card {
            background: white;
            padding: 40px;
            border-radius: 18px;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 8px 24px rgba(0,0,0,0.15);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    points_html = "".join(
        [
            f"<li style='font-size:18px; margin-bottom:10px; color:black;'>{p}</li>"
            for p in scheme["points"]
        ]
    )

    st.markdown(
        f"""
        <div class="info-card">
            <h2 style="color:#2f6f3e; text-align:center;">
                {scheme['title']}
            </h2>
            <ul style="margin-top:25px;">
                {points_html}
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

##################

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Back", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

    with col2:
        st.link_button(
            "Continue to Official Website →",
            scheme["link"],
            use_container_width=True
        )

st.markdown("<hr style='border: none; height: 3px; background-color: #2c6e49; margin: 20px 0;'>",unsafe_allow_html=True)
#abhi columns me variaations hai..
cols1, cols2 = st.columns(2)
with cols1:
    with st.expander("Know More About Weather Prediction"):
        st.write("""
        Weather Prediction is a crucial aspect of modern agriculture, enabling farmers to make informed decisions based on anticipated weather conditions. By utilizing advanced meteorological models and data analysis techniques, weather prediction systems can provide accurate forecasts for temperature, rainfall, humidity, and other climatic factors that directly impact crop growth and yield.
        """)

    
    
    APP_URL = "https://weather-prediction-bu7p6nawxu45huhizjyedx.streamlit.app/"

    st.markdown(f"""
    <style>
    .click-card {{
        padding: 30px;
        border-radius: 18px;
        background: linear-gradient(135deg, #e0f2fe, #f8fafc);
        box-shadow: 0 10px 24px rgba(0,0,0,0.12);
        text-align: center;
        font-size: 22px;
        font-weight: 800;
        color: #0a0908;
        transition: 
            transform 0.25s ease,
            box-shadow 0.25s ease,
            background 0.25s ease;
    }}

    .click-card:hover {{
        transform: translateY(-6px) scale(1.02);
        box-shadow: 0 18px 40px rgba(0,0,0,0.18);
        background: linear-gradient(135deg, #d9ed92, #ff9b54);
    }}
    </style>

    <a href="{APP_URL}" target="_blank" style="text-decoration:none">
        <div class="click-card">
            Weather Prediction
        </div>
    </a>

    """, unsafe_allow_html=True)
    st.markdown("<hr style='border: none; height: 3px; background-color: #2c6e49; margin: 20px 0;'>",unsafe_allow_html=True)
    
############################# 
    
    
with cols2:
    with st.expander("Know More About Crop-Disease Detection"):
        st.write("""
        Crop-Disease Detection is an advanced application that leverages machine learning and image processing techniques to identify diseases in various crops. By analyzing images of plant leaves, the system can accurately diagnose common diseases affecting crops such as tomatoes, potatoes, wheat, and more.
        """)

    
    
    APP_URL = "https://crop-disease-detection-r4kvmjzyew58ewgktelgxh.streamlit.app/"

    st.markdown(f"""
    <style>
    .click-card {{
        padding: 30px;
        border-radius: 18px;
        background: linear-gradient(135deg, #e0f2fe, #f8fafc);
        box-shadow: 0 10px 24px rgba(0,0,0,0.12);
        text-align: center;
        font-size: 22px;
        font-weight: 800;
        color: #0a0908;
        transition: 
            transform 0.25s ease,
            box-shadow 0.25s ease,
            background 0.25s ease;
    }}

    .click-card:hover {{
        transform: translateY(-6px) scale(1.02);
        box-shadow: 0 18px 40px rgba(0,0,0,0.18);
        background: linear-gradient(135deg, #d9ed92, #ff9b54);
    }}
    </style>

    <a href="{APP_URL}" target="_blank" style="text-decoration:none">
        <div class="click-card">
            Crop-Disease Detection
        </div>
    </a>

    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: none; height: 3px; background-color: #2c6e49; margin: 20px 0;'>",unsafe_allow_html=True)

#############################
st.markdown(
    "<h1 style='text-align: center; color: #0a0908; font-size: 40px;'>Crop Care/Maintenance advisory</h1>",
    unsafe_allow_html=True
)
APP_URL = "https://aiadvisory-rtmavckgcc5tbzr4nqzunu.streamlit.app/"

st.markdown(f"""
    <style>
    .click-card {{
        padding: 30px;
        border-radius: 18px;
        background: lin
        ear-gradient(135deg, #e0f2fe, #f8fafc);
        box-shadow: 0 10px 24px rgba(0,0,0,0.12);
        text-align: center;
        font-size: 22px;
        font-weight: 800;
        color: #0a0908;
        transition: 
            transform 0.25s ease,
            box-shadow 0.25s ease,
            background 0.25s ease;
    }}

    .click-card:hover {{
        transform: translateY(-6px) scale(1.02);
        box-shadow: 0 18px 40px rgba(0,0,0,0.18);
        background: linear-gradient(135deg, #d9ed92, #ff9b54);
    }}
    </style>

    <a href="{APP_URL}" target="_blank" style="text-decoration:none">
        <div class="click-card">
            Ai Saarthi
        </div>
    </a>

    """, unsafe_allow_html=True)
st.markdown("<hr style='border: none; height: 3px; background-color: #2c6e49; margin: 20px 0;'>",unsafe_allow_html=True)
st.markdown("<hr style='border: none; height: 3px; background-color: #2c6e49; margin: 20px 0;'>",unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center; color: #0a0908; font-size: 40px;'>Others Services by Saarthi</h1>",
    unsafe_allow_html=True
)
coos1,coos2= st.columns(2)
with coos1:
    APP_URL = "https://2pvewgqjzf5ifra57dpsav.streamlit.app/"

    st.markdown(f"""
        <style>
        .click-card {{
            padding: 30px;
            border-radius: 18px;
            background: lin
            ear-gradient(135deg, #e0f2fe, #f8fafc);
            box-shadow: 0 10px 24px rgba(0,0,0,0.12);
            text-align: center;
            font-size: 22px;
            font-weight: 800;
            color: #0a0908;
            transition: 
                transform 0.25s ease,
                box-shadow 0.25s ease,
                background 0.25s ease;
        }}

        .click-card:hover {{
            transform: translateY(-6px) scale(1.02);
            box-shadow: 0 18px 40px rgba(0,0,0,0.18);
            background: linear-gradient(135deg, #d9ed92, #ff9b54);
        }}
        </style>

        <a href="{APP_URL}" target="_blank" style="text-decoration:none">
            <div class="click-card">
                Water requirement Calculator
            </div>
        </a>

        """, unsafe_allow_html=True)
with coos2:
    APP_URL = "https://fcheo9oyypblvtmmm29gtc.streamlit.app/"

    st.markdown(f"""
        <style>
        .click-card {{
            padding: 30px;
            border-radius: 18px;
            background: lin
            ear-gradient(135deg, #e0f2fe, #f8fafc);
            box-shadow: 0 10px 24px rgba(0,0,0,0.12);
            text-align: center;
            font-size: 22px;
            font-weight: 800;
            color: #0a0908;
            transition: 
                transform 0.25s ease,
                box-shadow 0.25s ease,
                background 0.25s ease;
        }}

        .click-card:hover {{
            transform: translateY(-6px) scale(1.02);
            box-shadow: 0 18px 40px rgba(0,0,0,0.18);
            background: linear-gradient(135deg, #8ecae6, #e3d5ca);
        }}
        </style>

        <a href="{APP_URL}" target="_blank" style="text-decoration:none">
            <div class="click-card">
                Crop cost-profit Calculator
            </div>
        </a>

        """, unsafe_allow_html=True)




    



