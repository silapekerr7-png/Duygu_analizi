import streamlit as st
import pickle
 
model = pickle.load(open('model.pkl', 'rb'))
 
st.title('Film Yorumu Duygu Analizi :movie_camera:')
 
yorum = st.text_area('Film yorumunu İngilizce yazın:', 'This movie was great, I loved it!')
 
if st.button('Analiz Et'):
    olasilik = model.predict_proba([yorum])[0][1]
    if olasilik > 0.5:
        st.success(f'Olumlu 😊 (olumlu olma olasılığı: %{olasilik * 100:.1f})')
    else:
        st.success(f'Olumsuz 😞 (olumlu olma olasılığı: %{olasilik * 100:.1f})')