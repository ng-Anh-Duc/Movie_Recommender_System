import streamlit as st
import pickle
import requests

movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('MOVIES RECOMMENDATION SYSTEM')

selected_movie = st.selectbox('Select movies from lists', movies.title)

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=3510d39b603dffcf0ab967ac7edfb7c6'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path


def recommend(movie):
    recommend_movies = []
    posters = []
    id = movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[id])), reverse=True, key=lambda vector: vector[1])
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return recommend_movies, posters


if st.button('Show Recommend'):
    recommend_list, posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_list[0])
        st.image(posters[0])
    with col2:
        st.text(recommend_list[1])
        st.image(posters[1])
    with col3:
        st.text(recommend_list[2])
        st.image(posters[2])
    with col4:
        st.text(recommend_list[3])
        st.image(posters[3])
    with col5:
        st.text(recommend_list[4])
        st.image(posters[4])