"""Charts for the dashboard."""
import streamlit as st
import altair as alt


# ====================== Altair charts ======================
        
def draw_chart(chart_title: str = None, chart_data=None, y_axis_title: str = None, x_axis_title: str = "Datetime",topRange:int=50,bottomRange:int=0):
    if chart_title:
        st.subheader(chart_title)
    if chart_data is None:
        st.error("No Data Available")
        return
    elif chart_data.empty:
        st.error("No Data Available")
        return

        
    temperature_chart_an = (
            alt.Chart(data=chart_data)
            .mark_area( # type: ignore
                line={"color": "#1fa2ff"},
                color=alt.Gradient(
                    gradient="linear",
                    stops=[
                        alt.GradientStop(color="#1fa2ff", offset=1),
                        alt.GradientStop(color="rgba(255,255,255,0)", offset=0),
                    ],
                    x1=1,
                    x2=1,
                    y1=1,
                    y2=0,
                ),
                interpolate="monotone",
                cursor="crosshair",
            )
            .encode(  # type: ignore
                x=alt.X(
                    shorthand="Datetime:T",
                    axis=alt.Axis(
                        format="%Y-%m-%d %H:%M:%S",
                        title=x_axis_title,
                        tickCount=10,
                        grid=True,
                        tickMinStep=5,
                    ),
                ),  # T indicates temporal (time-based) data
                y=alt.Y(
                    "value:Q",
                    # scale=alt.Scale(domain=[0, 100]),
                    scale=alt.Scale(zero=False, domain=[bottomRange, topRange]),
                    axis=alt.Axis(
                        title=y_axis_title, grid=True, tickCount=30
                    ),
                ),  # Q indicates quantitative data
                tooltip=[
                    alt.Tooltip(
                        "Datetime:T",
                        format="%Y-%m-%d %H:%M:%S",
                        title="Time",
                    ),
                    alt.Tooltip("value:Q", format="0.2f", title="Value"),
                ],
            )
            .properties(height=350)
            .interactive()
        )  # type: ignore

    st.altair_chart(temperature_chart_an, use_container_width=True)
