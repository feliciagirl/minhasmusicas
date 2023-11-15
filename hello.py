import streamlit as st

st.header('minhas musicas')
happy = 'https://www.youtube.com/watch?v=RnyPNdBWwVw'
ideo = 'https://www.youtube.com/watch?v=KyDov-QJFGE'
oi = 'https://www.youtube.com/watch?v=EBWzgb1Xeis'

if st.button('quero ver mais'):
    st.subheader(':standing_person: strangers ')
    st.video(happy)
    st.subheader(':radio: stereo hearts ')
    st.video(ideo)
    st.subheader(':eyes: mix ')
    st.video(oi)
else:
    st.write('(para ver mais musicas, clique no botao acima:)')