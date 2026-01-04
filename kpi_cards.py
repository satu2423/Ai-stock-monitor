import streamlit as st
import queries

def render_kpis(session):
    df = session.sql(queries.KPI_QUERY).to_pandas()
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="kpi-card" title="Total warehouses monitored">
            <div class="kpi-title">Warehouses</div>
            <div class="kpi-value">{int(df["WAREHOUSES"][0])}</div>
            <div class="kpi-help">Active locations</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="kpi-card" title="Total products tracked">
            <div class="kpi-title">Products</div>
            <div class="kpi-value">{int(df["PRODUCTS"][0])}</div>
            <div class="kpi-help">SKUs monitored</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="kpi-card" title="Stock-out risk before delivery">
            <div class="kpi-title">Critical Items</div>
            <div class="kpi-value">{int(df["CRITICAL_ITEMS"][0])}</div>
            <div class="kpi-help">Immediate action</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="kpi-card" title="Monitor closely">
            <div class="kpi-title">Warning Items</div>
            <div class="kpi-value">{int(df["WARNING_ITEMS"][0])}</div>
            <div class="kpi-help">Reorder soon</div>
        </div>
        """, unsafe_allow_html=True)
