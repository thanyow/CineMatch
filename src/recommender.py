import streamlit as st
import requests
from streamlit_searchbox import st_searchbox
from st_clickable_images import clickable_images

# --- PAGE CONFIG ---
st.set_page_config(page_title="CineMatch", page_icon="🍿", layout="wide")

# --- SESSION STATE ---
if 'current_movie_id' not in st.session_state:
    st.session_state.current_movie_id = None
if 'search_key_version' not in st.session_state:
    st.session_state.search_key_version = 0

# --- CONSTANTS: GENRE MAP ---
GENRE_MAP = {
    "All Genres": None,
    "Action": 28,
    "Adventure": 12,
    "Animation": 16,
    "Comedy": 35,
    "Crime": 80,
    "Drama": 18,
    "Fantasy": 14,
    "Horror": 27,
    "Mystery": 9648,
    "Romance": 10749,
    "Sci-Fi": 878,
    "Thriller": 53
}

# --- CUSTOM CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@300;400;700&display=swap');
    
    h1 { 
        font-family: 'Bebas Neue', sans-serif; 
        font-size: 4rem !important; 
        margin-bottom: 0px; 
    }
    h1 a, h1 a:visited, h1 a:hover, h1 a:active { 
        text-decoration: none !important; 
        color: #E50914 !important; 
        border-bottom: none !important;
    }
    h1 a:hover { color: #b20710 !important; }
    
    h2 { font-family: 'Bebas Neue', sans-serif; font-size: 2.5rem !important; }
    
    .movie-title { font-weight: bold; font-size: 1.0rem; margin-top: 5px; margin-bottom: 0px; line-height: 1.2;}
    .movie-year { color: #aaa; font-size: 0.85rem; margin-top: 0px; margin-bottom: 10px; }
    
    .stButton>button { background-color: #333; color: white; border: 1px solid #555; }
    .stButton>button:hover { border-color: #E50914; color: #E50914; }

    /* GENRE TAGS */
    .genre-tag {
        display: inline-block;
        background-color: #333;
        color: #ddd;
        padding: 2px 10px;
        border-radius: 15px;
        font-size: 0.8rem;
        margin-right: 5px;
        margin-bottom: 10px;
        border: 1px solid #555;
    }
    
    .footer {
        text-align: center;
        color: #666;
        padding: 20px;
        font-size: 0.9rem;
        border-top: 1px solid #333;
        margin-top: 50px;
    }
    .footer a { color: #E50914; text-decoration: none; font-weight: bold; }
    .footer a:hover { text-decoration: underline; }
</style>
""", unsafe_allow_html=True)

# --- API FUNCTIONS ---
def get_api_key():
    try: return st.secrets["tmdb_key"]
    except: return None

def search_tmdb(searchterm: str):
    if not searchterm: return []
    api_key = get_api_key()
    if not api_key: return []
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={searchterm}"
    try:
        response = requests.get(url).json()
        results = response.get('results', [])
        suggestions = []
        for m in results:
            year = m.get('release_date', '')[:4]
            label = f"{m['title']} ({year})"
            suggestions.append((label, m['id']))
        return suggestions
    except: return []

def get_details(movie_id):
    api_key = get_api_key()
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&append_to_response=credits,recommendations,videos"
    return requests.get(url).json()

def get_trending_movies():
    api_key = get_api_key()
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}"
    try: return requests.get(url).json().get('results', [])
    except: return []

# --- NEW: GET MOVIES BY GENRE ---
def get_movies_by_genre(genre_id):
    api_key = get_api_key()
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}&sort_by=popularity.desc"
    try: return requests.get(url).json().get('results', [])
    except: return []

# --- NAVIGATION HELPER ---
def go_to_movie(movie_id):
    st.session_state.current_movie_id = movie_id
    st.session_state.search_key_version += 1
    st.rerun()

# --- APP LAYOUT ---
st.markdown("<h1><a href='.' target='_self'>CINEMATCH</a></h1>", unsafe_allow_html=True)

user_selection = st_searchbox(
    search_tmdb,
    key=f"search_{st.session_state.search_key_version}",
    placeholder="🔍 Search for a movie...",
)
if user_selection:
    go_to_movie(user_selection)

if st.session_state.current_movie_id is None:
    # --- DASHBOARD (Trending or Filtered) ---
    
    # 1. Filter UI
    col_header, col_filter = st.columns([3, 1])
    with col_filter:
        selected_genre_name = st.selectbox("Filter by Genre", list(GENRE_MAP.keys()))
    
    # 2. Logic to switch data source
    if selected_genre_name == "All Genres":
        movie_list = get_trending_movies()[:10]
        with col_header:
            st.subheader("🔥 Trending This Week")
    else:
        genre_id = GENRE_MAP[selected_genre_name]
        movie_list = get_movies_by_genre(genre_id)[:10]
        with col_header:
            st.subheader(f"🍿 Top {selected_genre_name} Movies")

    # 3. Display Grid
    cols = st.columns(5)
    for i, movie in enumerate(movie_list):
        col_index = i % 5
        with cols[col_index]:
            poster = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get('poster_path') else "https://via.placeholder.com/500x750"
            
            clicked = clickable_images(
                paths=[poster], 
                titles=[movie['title']],
                div_style={"display": "flex", "justify-content": "center", "width": "100%"},
                img_style={"cursor": "pointer", "border-radius": "10px", "width": "100%"},
                key=f"home_{movie['id']}" # Changed key prefix to avoid conflicts
            )
            
            year = movie.get('release_date', '')[:4]
            st.markdown(f"<p class='movie-title'>{movie['title']}</p><p class='movie-year'>{year}</p>", unsafe_allow_html=True)
            
            if clicked > -1:
                go_to_movie(movie['id'])

else:
    # --- MOVIE DETAILS PAGE ---
    data = get_details(st.session_state.current_movie_id)
    
    if st.button("⬅ Back to Dashboard"):
        st.session_state.current_movie_id = None
        st.session_state.search_key_version += 1
        st.rerun()

    trailer_key = None
    if 'videos' in data and 'results' in data['videos']:
        for video in data['videos']['results']:
            if video['site'] == "YouTube" and video['type'] == "Trailer":
                trailer_key = video['key']
                break
    
    c1, c2 = st.columns([1, 3]) 
    
    with c1:
        poster_url = f"https://image.tmdb.org/t/p/w500{data['poster_path']}" if data.get('poster_path') else "https://via.placeholder.com/500x750"
        st.image(poster_url, use_container_width=True)
    
    with c2:
        st.markdown(f"## {data['title']}")
        st.caption(f"{data.get('release_date', '')[:4]} • {data.get('runtime', 'N/A')} min • {data.get('status', '')}")
        
        # Display Genres
        if 'genres' in data:
            genre_html = "".join([f"<span class='genre-tag'>{g['name']}</span>" for g in data['genres']])
            st.markdown(f"<div>{genre_html}</div>", unsafe_allow_html=True)

        st.write(data.get('overview', ''))
        st.markdown(f"### ⭐ {data.get('vote_average', 0):.1f}/10")
        
        if trailer_key:
            st.markdown("#### 🎥 Watch Trailer")
            st.video(f"https://www.youtube.com/watch?v={trailer_key}")
        else:
            st.info("No trailer available.")

    st.write("---")

    tab1, tab2 = st.tabs(["🎬 Cast", "🍿 Recommendations"])
    
    with tab1:
        if 'credits' in data:
            cast = data['credits']['cast'][:6]
            cols = st.columns(6)
            for i, actor in enumerate(cast):
                with cols[i]:
                    if actor.get('profile_path'):
                        st.image(f"https://image.tmdb.org/t/p/w200{actor['profile_path']}")
                    st.caption(actor.get('name'))

    with tab2:
        if 'recommendations' in data and data['recommendations']['results']:
            recs = data['recommendations']['results'][:5]
            cols = st.columns(5)
            for i, rec in enumerate(recs):
                with cols[i]:
                    poster = f"https://image.tmdb.org/t/p/w500{rec['poster_path']}" if rec.get('poster_path') else "https://via.placeholder.com/500x750"
                    
                    clicked_rec = clickable_images(
                        paths=[poster], 
                        titles=[rec['title']],
                        div_style={"display": "flex", "justify-content": "center", "width": "100%"},
                        img_style={"cursor": "pointer", "border-radius": "10px", "width": "100%"},
                        key=f"rec_{rec['id']}"
                    )
                    
                    year = rec.get('release_date', '')[:4]
                    st.markdown(f"<p class='movie-title'>{rec['title']}</p><p class='movie-year'>{year}</p>", unsafe_allow_html=True)
                    
                    if clicked_rec > -1:
                        go_to_movie(rec['id'])
        else:
            st.info("⚠️ No similar movies found.")

# --- FOOTER ---
st.markdown("""
<div class="footer">
    <p>
        Made with ❤️ by <a href="https://github.com/thanyow" target="_blank">thanyow</a>
        <br>
        © 2025 CineMatch • Data provided by <a href="https://www.themoviedb.org/" target="_blank">TMDB</a>
    </p>
</div>
""", unsafe_allow_html=True)