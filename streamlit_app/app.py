import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from fpdf import FPDF
import streamlit.components.v1 as components



# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Customer Churn Predictor",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    @media (max-width: 768px) {
        div[data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Global CSS
# ---------------------------
st.markdown("""
<style>
body {
    background-color: #020617;
    color: #e5e7eb;
}

h1, h2, h3 {
    margin-bottom: 8px;
}

/* Card container */
.card {
    background: linear-gradient(135deg, #0f172a, #020617);
    border: 1px solid #1e293b;
    border-radius: 16px;
    padding: 20px 24px;
    box-shadow: 0 0 30px rgba(0,0,0,0.45);
}

/* Result number */
.big-number {
    font-size: 46px;
    font-weight: 700;
    margin: 4px 0;
}

/* Risk labels */
.risk-low {
    color: #22c55e;
    font-size: 18px;
    font-weight: 600;
}

.risk-high {
    color: #ef4444;
    font-size: 18px;
    font-weight: 600;
}

/* Section divider */
.divider {
    margin: 14px 0;
    border-top: 1px solid #1e293b;
}

/* Compact bullets */
.reason {
    margin: 4px 0;
    font-size: 15px;
}

/* Summary rows */
.summary-row {
    display: flex;
    justify-content: space-between;
    margin: 6px 0;
    font-size: 15px;
}
.summary-key {
    color: #94a3b8;
}
.summary-value {
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------
# Session State
# ---------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------------------
# Header
# ---------------------------
st.markdown("""
<h1 style="text-align:center;">Customer Churn Prediction System</h1>
<p style="text-align:center; color:#94a3b8;">
Predict churn risk and understand key drivers behind customer behavior
</p>
""", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

#PDF
def generate_pdf_report(result, payload):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, "Customer Churn Prediction Report", ln=True)
    pdf.ln(4)

    pdf.cell(0, 10, f"Churn Probability: {result['churn_probability']*100:.2f}%", ln=True)
    pdf.cell(0, 10, f"Risk Level: {result['risk_level']}", ln=True)

    pdf.ln(4)
    pdf.cell(0, 10, "Top Churn Drivers:", ln=True)

    for reason in result["top_reasons"]:
        pdf.multi_cell(0, 8, f"- {reason}")

    pdf.ln(4)
    pdf.cell(0, 10, "Customer Summary:", ln=True)

    for k, v in payload.items():
        pdf.multi_cell(0, 8, f"{k}: {v}")

    return pdf.output(dest="S").encode("latin-1")

# ---------------------------
# Layout
# ---------------------------
input_col, output_col = st.columns(
    [1.25, 1],
    gap="large"
)


# ===========================
# INPUT SECTION
# ===========================
with input_col:
    st.subheader("Customer Information")

    gender = st.selectbox("Gender",["Female","Male"])
    SeniorCitizen = st.selectbox("Senior Citizen",[0,1])
    Partner = st.selectbox("Partner",["Yes","No"])
    Dependents = st.selectbox("Dependents",["Yes","No"])
    tenure = st.number_input("Tenure(months)",0,72,12)

    st.markdown("<div class='divider></div>",unsafe_allow_html=True)

    PhoneService = st.selectbox("Phone Service",["Yes","No"])
    MultipleLines = st.selectbox(
        "Multiple Lines",
        ["No phone service"] if PhoneService == "No" else ["Yes","No"]
    )

    InternetService = st.selectbox("Internet Service",["DSL","Fiber optic","No"])
    internet_opts = ["No internet service"] if InternetService == "No" else ["Yes","No"]
    OnlineSecurity = st.selectbox("Online Security",internet_opts)
    OnlineBackup = st.selectbox("Onliine Backup",internet_opts)
    DeviceProtection = st.selectbox("Device Protection", internet_opts)
    TechSupport = st.selectbox("Tech Support", internet_opts)
    StreamingTV = st.selectbox("Streaming TV", internet_opts)
    StreamingMovies = st.selectbox("Streaming Movies", internet_opts)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
    TotalCharges = st.text_input("Total Charges (optional)")

    predict_clicked = st.button(
    "Predict Churn",
    use_container_width=True
)


# ===========================
# API CALL
# ===========================
if predict_clicked:
    payload = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    try:
        response = requests.post(
            "https://customer-churn-api.onrender.com/predict",
            json=payload,
            timeout=5
        )

        if response.status_code == 200:
            result = response.json()
            st.session_state.history.append({
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "probability": result["churn_probability"],
                "risk": result["risk_level"]
            })
        else:
            st.error("API error. Please check backend logs.")
            st.stop()

    except Exception:
        st.error("Could not connect to prediction service.")
        st.stop()

# ===========================
# OUTPUT SECTION
# ===========================
with output_col:
    if predict_clicked and response.status_code == 200:
        risk_class = "risk-low" if result["risk_level"] == "Low" else "risk-high"

        # Build reasons HTML safely
        if result["top_reasons"]:
            reasons_html = "".join(
                f"<div class='reason'>• {r}</div>"
                for r in result["top_reasons"]
            )
        else:
            reasons_html = "<div class='reason'>No dominant churn drivers detected.</div>"

        # ---- Prediction Card ----
        
        prediction_card = f"""
        <div class="card">
            <h3>Churn Probability</h3>
            <div class="big-number">{result['churn_probability']*100:.2f}%</div>
            <div class="{risk_class}">{result['risk_level']} Risk</div>
            <div class="divider"></div>
        </div>
        """

         # 🔽 SCROLL TARGET
        st.markdown("<div id='prediction-result'></div>", unsafe_allow_html=True)

        st.markdown(prediction_card, unsafe_allow_html=True)

        # 🔽 AUTO SCROLL
        components.html(
            """
            <script>
            const scrollToResult = () => {
                const el = window.parent.document.getElementById("prediction-result");
                if (el) {
                    el.scrollIntoView({ behavior: "smooth", block: "start" });
                }
            };
            setTimeout(scrollToResult, 100);
            </script>
            """,
            height=0,
        )


        # ---- Top Churn Drivers Card ----
        drivers_card = f"""
        <div class="card">
            <h3>Top Churn Drivers</h3>
            <div class="divider"></div>
            {reasons_html}
        </div>
        """

        st.markdown(drivers_card, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)


        # ---- Customer Summary Card ----
        summary_card = f"""
        <div class="card">
            <h3>Customer Summary</h3>
            <div class="summary-row"><span class="summary-key">Tenure</span><span class="summary-value">{tenure} months</span></div>
            <div class="summary-row"><span class="summary-key">Contract</span><span class="summary-value">{Contract}</span></div>
            <div class="summary-row"><span class="summary-key">Monthly Charges</span><span class="summary-value">${MonthlyCharges:.2f}</span></div>
            <div class="summary-row"><span class="summary-key">Payment Method</span><span class="summary-value">{PaymentMethod}</span></div>
        </div>
        """

        st.markdown(summary_card, unsafe_allow_html=True)


        pdf_bytes = generate_pdf_report(result, payload)
        st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)

        st.download_button(
         label="📄 Download PDF Report",
         data=pdf_bytes,
         file_name="churn_prediction_report.pdf",
         mime="application/pdf"
     )



# ===========================
# HISTORY SECTION
# ===========================
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.subheader("Prediction History (Session)")

if st.session_state.history:
    st.dataframe(pd.DataFrame(st.session_state.history), use_container_width=True)
else:
    st.write("No predictions yet.")

components.html(
    """
    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <style>
    .footer {
        margin-top: 40px;
        padding: 16px 0;
        border-top: 1px solid #1e293b;
        text-align: center;
        color: #94a3b8;
        font-size: 14px;
    }
    .footer a {
        color: #94a3b8;
        margin: 0 12px;
        font-size: 20px;
        text-decoration: none;
        transition: color 0.2s ease;
    }
    .footer a:hover {
        color: #38bdf8;

        .footer {
    text-align: center;
    padding: 12px;
}

.footer a {
    margin: 0 8px;
    font-size: 22px;
}

@media (max-width: 480px) {
    .footer a {
        font-size: 20px;
        margin: 0 6px;
    }
}

    }

    /* ---------------------------
   RESPONSIVE FIXES
--------------------------- */

/* Tablets & small laptops */
@media (max-width: 1024px) {
    .big-number {
        font-size: 36px;
    }

    .card {
        padding: 16px 18px;
    }
}

/* Mobile phones */
@media (max-width: 768px) {

    /* Stack columns vertically */
    section.main > div {
        padding-left: 0.5rem;
        padding-right: 0.5rem;
    }

    /* Reduce card padding */
    .card {
        padding: 14px 16px;
        border-radius: 12px;
    }

    /* Reduce headings */
    h1 {
        font-size: 26px;
        text-align: center;
    }

    h2 {
        font-size: 20px;
    }

    h3 {
        font-size: 18px;
    }

    /* Probability number scaling */
    .big-number {
        font-size: 32px;
    }

    /* Reduce bullet spacing */
    .reason {
        font-size: 14px;
        margin: 2px 0;
    }

    /* Summary rows stack */
    .summary-row {
        flex-direction: column;
        align-items: flex-start;
    }

    .summary-value {
        margin-top: 2px;
    }
}

/* Extra small devices */
@media (max-width: 480px) {
    .big-number {
        font-size: 28px;
    }

    .risk-low,
    .risk-high {
        font-size: 16px;
    }
}

    </style>

    <div class="footer">
        <div>Built by <b>Shaivi Srivastava</b> • Machine Learning Project</div>
        <div style="margin-top:8px;">
            <a href="https://github.com/ShaiviSri04" target="_blank">
                <i class="fab fa-github"></i>
            </a>
            <a href="https://www.linkedin.com/in/shaivisri04" target="_blank">
                <i class="fab fa-linkedin"></i>
            </a>
        </div>
    </div>
    """,
    height=120,
)

