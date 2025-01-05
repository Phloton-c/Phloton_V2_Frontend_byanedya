"""Charts for the dashboard."""
import streamlit as st
import altair as alt


# ====================== Altair charts ======================
        
def draw_chart(chart_title:str=None,chart_data=None,y_axis_title:str=None,x_axis_title:str="Datetime"):
    if chart_data is None :
        st.error("No data found")
        return
    elif chart_data.empty:
        st.error("Data is empty")
        return
    else:
        if chart_title is not None:
            st.subheader(chart_title)
        chart_an = (
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
                    "aggregate:Q",
                    # scale=alt.Scale(domain=[0, 100]),
                    scale=alt.Scale(zero=False, domain=[10, 50]),
                    axis=alt.Axis(
                        title=y_axis_title, grid=True, tickCount=10
                    ),
                ),  # Q indicates quantitative data
                tooltip=[
                    alt.Tooltip(
                        "Datetime:T",
                        format="%Y-%m-%d %H:%M:%S",
                        title="Time",
                    ),
                    alt.Tooltip("aggregate:Q", format="0.2f", title="Value"),
                ],
            )
            .properties(height=400)
            .interactive()
        )  # type: ignore

        st.altair_chart(chart_an, use_container_width=True)

    