# Library
import streamlit as st

# write
st.title('Software Perkalian')
st.subheader('Aplikasi untuk mengalikan bilangan')

# input bilangan pertama
number1 = st.number_input('Masukkan bilangan pertama')
st.write(f'Bilangan pertama adalah {number1}')

# input bilangan kedua
number2 = st.number_input('Masukkan bilangan kedua')
st.write(f'Bilangan kedua adalah {number2}')

# hasil kali
hasil = number1*number2

if st.button('Hitung'):
    st.write(f'Hasil = {hasil}')
else:
    st.write('Silahkan klik tombol hitung!')

st.balloons()