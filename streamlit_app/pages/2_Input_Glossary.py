import streamlit as st

st.set_page_config(
    page_title="Input Glossary | Customer Churn System",
    layout="wide"
)

# ---------------------------
# Global CSS (COMPACT)
# ---------------------------
st.markdown("""
<style>
body {
    background-color: #020617;
    color: #e5e7eb;
}

/* Card */
.card {
    background: linear-gradient(135deg, #0f172a, #020617);
    border: 1px solid #1e293b;
    border-radius: 16px;
    padding: 20px 24px;
    margin-bottom: 18px;
}

/* Titles */
.section-title {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 10px;
}

/* Compact rows */
.row {
    display: flex;
    gap: 12px;
    margin-bottom: 6px;
    font-size: 15px;
    line-height: 1.4;
}

.key {
    min-width: 160px;
    font-weight: 600;
    color: #93c5fd;
}

.value {
    color: #cbd5f5;
}

/* Compact list */
ul {
    margin: 6px 0 6px 20px;
    padding: 0;
}
li {
    margin-bottom: 4px;
    font-size: 15px;
}

/* Helper text */
.note {
    margin-top: 6px;
    font-size: 14px;
    color: #a5b4fc;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Input Glossary</h1>", unsafe_allow_html=True)

# ---------------------------
# Customer Profile
# ---------------------------
st.markdown("""
<div class="card">
  <div class="section-title">Customer Profile</div>

  <div class="row">
    <div class="key">Gender</div>
    <div class="value">Customer gender as recorded.</div>
  </div>

  <div class="row">
    <div class="key">Senior Citizen</div>
    <div class="value">Binary indicator (1 = senior, 0 = non-senior).</div>
  </div>

  <div class="row">
    <div class="key">Partner</div>
    <div class="value">Whether the customer has a partner.</div>
  </div>

  <div class="row">
    <div class="key">Dependents</div>
    <div class="value">Whether the customer supports dependents.</div>
  </div>

  <div class="row">
    <div class="key">Tenure</div>
    <div class="value">Number of months the customer has stayed with the company.</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Services
# ---------------------------
st.markdown("""
<div class="card">
  <div class="section-title">Services</div>

  <div class="row">
    <div class="key">Phone Service</div>
    <div class="value">Whether phone service is active.</div>
  </div>

  <div class="row">
    <div class="key">Multiple Lines</div>
    <div class="value">Multiple phone lines (disabled if no phone service).</div>
  </div>

  <div class="row">
    <div class="key">Internet Service</div>
    <div class="value">DSL, Fiber optic, or No internet.</div>
  </div>

  <div class="row">
    <div class="key">Internet Features</div>
    <div class="value">
      <ul>
        <li>Online Security</li>
        <li>Online Backup</li>
        <li>Device Protection</li>
        <li>Tech Support</li>
        <li>Streaming TV</li>
        <li>Streaming Movies</li>
      </ul>
      <div class="note">
        Automatically set to <b>No internet service</b> when Internet Service is "No",
        matching the original dataset structure.
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Billing
# ---------------------------
st.markdown("""
<div class="card">
  <div class="section-title">Billing Information</div>

  <div class="row">
    <div class="key">Contract</div>
    <div class="value">Month-to-month, One year, or Two year.</div>
  </div>

  <div class="row">
    <div class="key">Paperless Billing</div>
    <div class="value">Whether billing is digital.</div>
  </div>

  <div class="row">
    <div class="key">Payment Method</div>
    <div class="value">Customer payment type.</div>
  </div>

  <div class="row">
    <div class="key">Monthly Charges</div>
    <div class="value">Monthly cost of services.</div>
  </div>

  <div class="row">
    <div class="key">Total Charges</div>
    <div class="value">Total billed amount (optional for flexibility).</div>
  </div>
</div>
""", unsafe_allow_html=True)
