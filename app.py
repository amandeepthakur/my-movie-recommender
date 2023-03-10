import pandas as pd
import streamlit as st
import pickle
import streamlit as st
import requests

movies_list = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))

api_key = '4c1c8eadcc2b3fde4b574c6fd0f65653'
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommended_movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movies = []
    recommended_movies_poster = []
    for i in recommended_movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetching poster using TMDB API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster




st.title(':red[My Movie Recommendation Page]')
st.subheader(':red[-By Amandeep Thakur]')
movies_list = movies['title'].values


selected_movie = st.selectbox(
    'Select a Movie!',
    movies_list)
if st.button('Recommend'):
    movie_name, movie_poster = recommend(selected_movie)

    col1, col2, col3, col4, col5, col6 = st.columns(6, gap="large")


    with col1:
            st.image(movie_poster[0])
            st.subheader(movie_name[0])

    with col2:
            st.image(movie_poster[1])
            st.subheader(movie_name[1])
    with col3:
            st.image(movie_poster[2])
            st.subheader(movie_name[2])
    with col4:
            st.image(movie_poster[3])
            st.subheader(movie_name[3])
    with col5:
            st.image(movie_poster[4])
            st.subheader(movie_name[4])
    with col6:
            st.image(movie_poster[5])
            st.subheader(movie_name[5])
