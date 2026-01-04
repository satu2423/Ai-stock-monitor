import streamlit as st
from snowflake.snowpark.context import get_active_session

from styles import load_styles
from kpi_cards import render_kpis
from heatmap import render_heatmap
from tables import render_alerts, render_reorders

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="AI Stock Health Monitor",
    layout="wide"
)

session = get_active_session()


# -----------------------------------
# LOAD GLOBAL STYLES
# -----------------------------------
load_styles()

# -----------------------------------
# HEADER
# -----------------------------------
st.title("📦 AI-Powered Stock Health Monitor")
st.markdown(
    "A centralized dashboard to monitor inventory, "
    "detect shortages early, and guide reorder decisions."
)

st.divider()

# -----------------------------------
# KPI CARDS
# -----------------------------------
render_kpis(session)

st.divider()

# -----------------------------------
# HEATMAP
# -----------------------------------
render_heatmap(session)

st.divider()

# -----------------------------------
# ALERTS & ACTIONS
# -----------------------------------
render_alerts(session)
st.divider()
render_reorders(session)
