import streamlit as st
import queries

def render_alerts(session):
    st.subheader("⚠ Items Requiring Immediate Attention")
    df = session.sql(queries.ALERTS_QUERY).to_pandas()
    st.dataframe(df, use_container_width=True)

def render_reorders(session):
    st.subheader("📦 Recommended Reorder Actions")
    df = session.sql(queries.REORDER_QUERY).to_pandas()
    st.dataframe(df, use_container_width=True)

    st.download_button(
        "⬇ Download Reorder Plan",
        df.to_csv(index=False),
        "reorder_plan.csv",
        "text/csv"
    )
