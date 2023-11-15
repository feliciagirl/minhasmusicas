import streamlit as st

st.header('minhas musicas')
happy = 'https://www.youtube.com/watch?v=RnyPNdBWwVw'
ideo = 'https://www.youtube.com/watch?v=KyDov-QJFGE'
oi = 'https://www.youtube.com/watch?v=EBWzgb1Xeis'
hi = 'https://www.youtube.com/watch?v=uceKnghZ9NU'

st.subheader(':standing_person: strangers ')
st.video(happy)
st.subheader(':radio: stereo hearts ')
st.video(ideo)
st.subheader(':eyes: mix ')
st.video(oi)
st.subheader(':wave: mix 2 ')
st.video(hi,start_time=194)
