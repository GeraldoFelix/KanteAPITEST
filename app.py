import requests
import json
import streamlit as st
def letra_musica(banda, musica):
    letra = requests.get(f'https://api.lyrics.ovh/v1/{banda}/{musica}')
    letra = letra.json()['lyrics']
    return letra

st.image('https://upload.wikimedia.org/wikipedia/commons/d/d8/Linkin_Park_-_From_Zero_Lead_Press_Photo_-_James_Minchin_III.jpg')
st.title('AS MELHORES LETRAS')

banda = st.text_input('Nome da banda', key='banda')
musica = st.text_input('Nome da Música', key="musica")
pesquisar = st.button('Pesquisar Música')

if pesquisar:
    letra = letra_musica(banda, musica)
    if letra:
        st.success("Achamos sua letra!")
        st.text(letra)
    else:
        st.error("Erro, digite corretamente o artista ou a musica")