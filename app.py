import streamlit as st
import plotly.express as px
import pandas as pd

st.write("Hello World!")
df = px.data.gapminder()

fig  = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

st.plotly_chart(fig)
st.balloons()
