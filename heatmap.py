import streamlit as st
import altair as alt
import queries

def render_heatmap(session):
    st.subheader("🔥 Stock Health Heatmap")

    df = session.sql(queries.HEATMAP_QUERY).to_pandas()
    df.columns = df.columns.str.lower()

    chart = alt.Chart(df).mark_rect().encode(
        x="product_name:N",
        y="warehouse_name:N",
        color=alt.Color(
            "days_left:Q",
            scale=alt.Scale(scheme="redyellowgreen"),
            title="Days Left"
        ),
        tooltip=["warehouse_name", "product_name", alt.Tooltip("days_left:Q", format=".1f")]
    ).properties(height=380)

    st.altair_chart(chart, use_container_width=True)
