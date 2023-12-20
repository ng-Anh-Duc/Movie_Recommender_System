import streamlit as st
import pickle

movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('MOVIES RECOMMENDATION SYSTEM')

selected_movie = st.selectbox('Select movies from lists', movies.title)

def recommend(movie):
    recommend_movies = []
    id = movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[id])), reverse=True, key=lambda vector: vector[1])
    for i in distance[1:6]:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


if st.button('Show Recommend'):
    recommend_list = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_list[0])
    with col2:
        st.text(recommend_list[1])
    with col3:
        st.text(recommend_list[2])
    with col4:
        st.text(recommend_list[3])
    with col5:
        st.text(recommend_list[4])