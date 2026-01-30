import streamlit as st

st.set_page_config(
    page_title="How It Works | Customer Churn System",
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
    margin-bottom: 6px;
    font-size: 15px;
    line-height: 1.4;
    color: #cbd5f5;
}

/* Highlight text */
.highlight {
    font-weight: 600;
    color: #93c5fd;
}

/* Lists */
ul {
    margin: 6px 0 6px 20px;
    padding: 0;
}
li {
    margin-bottom: 4px;
    font-size: 15px;
}

/* Notes */
.note {
    margin-top: 6px;
    font-size: 14px;
    color: #a5b4fc;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>How the Customer Churn Prediction System Works</h1>", unsafe_allow_html=True)

# ---------------------------
# Problem Statement
# ---------------------------
st.markdown("""
<div class="card">
  <div class="section-title">Problem This System Solves</div>

  <div class="row">
    Customer churn refers to customers discontinuing a service in subscription-based businesses.
  </div>

  <div class="row">
    This directly impacts <span class="highlight">revenue, growth, and customer lifetime value</span>.
  </div>

  <div class="row">
    This system predicts <span class="highlight">how likely a customer is to churn</span> and explains
    <span class="highlight">why that risk exists</span>, enabling proactive retention strategies.
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Data
# ---------------------------
st.markdown("""
<div class="card">
  <div class="section-title">Data Used</div>

  <div class="row">
    The model is trained on the <span class="highlight">Telecom Customer Churn dataset</span>,
    where each row represents a real customer snapshot.
  </div>

  <ul>
    <li>Customer demographics</li>
    <li>Service subscriptions</li>
    <li>Contract and billing information</li>
    <li>Historical churn outcomes</li>
  </ul>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Workflow
# ---------------------------
st.markdown("""
<div class="card">
  <div class="section-title">Prediction Workflow</div>

  <div class="row"><b>Step 1:</b> User inputs customer data using controlled dropdowns.</div>
  <div class="row"><b>Step 2:</b> Inputs are validated and aligned with the training schema.</div>
  <div class="row"><b>Step 3:</b> Feature engineering ensures training–prediction consistency.</div>
  <div class="row"><b>Step 4:</b> A machine learning model predicts churn probability.</div>
  <div class="row"><b>Step 5:</b> Probability is mapped to a business-friendly risk level.</div>
  <div class="row"><b>Step 6:</b> Human-readable churn explanations are generated.</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Risk Explanation
# ---------------------------
st.markdown("""
<div class="card">
  <div class="section-title">Risk Levels Explained</div>

  <div class="row">
    The model outputs a <span class="highlight">probability</span>, not a binary decision.
  </div>

  <ul>
    <li><b>Low Risk:</b> Low likelihood of churn</li>
    <li><b>Medium Risk:</b> Moderate likelihood</li>
    <li><b>High Risk:</b> High likelihood of churn</li>
  </ul>

  <div class="note">
    A customer may have churned historically but still appear as low or medium risk
    due to overlapping behavioral patterns.
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Trust & Limitations
# ---------------------------
st.markdown("""
<div class="card">
  <div class="section-title">Transparency & Limitations</div>

  <ul>
    <li>Predicts likelihood, not certainty</li>
    <li>Uses historical patterns, not future guarantees</li>
    <li>Supports decision-making, not replaces it</li>
  </ul>

  <div class="note">
    This behavior mirrors real-world production machine learning systems.
  </div>
</div>
""", unsafe_allow_html=True)
