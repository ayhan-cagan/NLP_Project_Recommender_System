import streamlit as st 
import pickle
import pandas as pd 
import requests

def fetch_poster(movie_id):  
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=b35eea4944a34e2e5071860edf2c1d2c'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# API https://www.themoviedb.org/settings/api sitesinden apı key alıyoruz. daha sonrasında aşağıda olan requerest url ile döngüye girip sırayla json formatından posterleri çektik 



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
         # film posterlerini listeye ekliyoruz. 
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title) # film indexine göre title çekiyoruz ve boş listeye append ediyoruz. 

    return recommended_movie_names,recommended_movie_posters


movies =pickle.load(open("movies.pkl", "rb")) # fonksiyon için gerekli olan dosyaları yüklüyoruz

similarity = pickle.load(open("similarity.pkl", "rb")) # vektörlerin açılarını yani benzerliklerini  yüklüyoruz. 

movies_list = movies["title"].values 

st.title("MOVİE RECOMMENDER SYSTEM")

selected_movie = option = st.selectbox(" Film Seçiniz  :) ",
                     movies_list)


if st.button('Tavsiye et'):
    st.markdown(f"**'{selected_movie}'** filmini izlediyseniz, aşağıdaki filmleri de sevebilirsiniz.")
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0]) # hem film ismini hem de posterini sütünlar ile gösteriyoruz. 
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])


## _____ THE END _______ 




