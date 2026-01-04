import streamlit as st

def load_styles():
    st.markdown("""
    <style>
    .kpi-card {
        background-color: #0e1117;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #262730;
        transition: all 0.2s ease-in-out;
    }
    .kpi-card:hover {
        border-color: #3b82f6;
        transform: translateY(-4px);
    }
    .kpi-title {
        font-size: 14px;
        color: #9ca3af;
    }
    .kpi-value {
        font-size: 42px;
        font-weight: 600;
        color: #e5e7eb;
    }
    .kpi-help {
        font-size: 12px;
        color: #6b7280;
    }
    </style>
    """, unsafe_allow_html=True)
