import pickle
import streamlit as st
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=enteryourapikey&language=en-US'.format(movie_id))
    
    data=response.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500"+poster_path
    return full_path
    

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances=similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    
    recommended_movie=[]
    recommended_movie_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].title)
        
        #fetch poster from api
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_poster   
        
movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')


selected_movie = st.selectbox("Type or select a movie from the dropdown",movies['title'].values)

if st.button('Show Recommendation'):
    names,posters=recommend(selected_movie)
    col1,col2,col3,col4,col5 =st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
st.text('Developed by Prathamesh Jadhav')            
