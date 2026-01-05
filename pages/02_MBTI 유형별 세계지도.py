import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 MBTI 유형별 세계지도")
df = pd.read_csv('countriesMBTI_16types.csv')
mbti_list = df.columns[1:].tolist()

target = st.selectbox("지도로 보고 싶은 MBTI를 선택하세요", mbti_list)

fig = px.choropleth(df, 
                    locations="Country", 
                    locationmode='country names',
                    color=target,
                    hover_name="Country",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title=f"전 세계 {target} 분포도")

st.plotly_chart(fig, use_container_width=True)
st.write(f"💡 색이 밝을수록 해당 국가에 {target} 성향의 사람이 많다는 뜻입니다.")
