# 🍿 CineMatch

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cinema-tch.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.9%2B-E50914?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-abbb72)
![API](https://img.shields.io/badge/Data-TMDB_API-E50914)

**CineMatch** is an AI-powered movie discovery engine that bridges the gap between static recommendations and an immersive streaming experience. Built entirely in Python, it leverages the **TMDB Live API** to provide real-time trending data, smart recommendations, and watchable trailers in a streaming-platform style interface.

🔗 **Live Demo:** [Launch App](https://cinema-tch.streamlit.app)

---

## 📸 Preview

| **Trending Dashboard** | **Movie Details & Trailers** |
|:---:|:---:|
| <img src="assets/dashboard.png" width="400" alt="CineMatch Dashboard"> | <img src="assets/details.png" width="400" alt="Movie Details Page"> |
| *Curated dashboard with live trending movies* | *Immersive details page with embedded trailers* |

---

## ✨ Key Features

### 🎬 Cinema Mode
- **Embedded Trailers:** Automatically finds and embeds official YouTube trailers.
- **Rich Metadata:** Displays dynamic backdrops, release years, runtimes, and ratings.
- **Smart Recommendations:** Uses TMDB’s collaborative filtering to suggest similar movies.

### 🔥 Live Trending
- Instantly fetches the **Top 10 Trending Movies** of the week.
- Displays results in a responsive, clickable image grid — streaming-platform styled.

### 🔍 Smart Search
- **Debounced Search** to avoid API rate limits.
- **Auto-complete suggestions** (e.g., typing "Spider" shows “Spider-Man: No Way Home”, etc.).
- Auto-clears input after selection for smoother flow.

### ⚡ Technical Highlights
- **Session State** for persistent navigation.
- **Custom CSS** for a “Dark Mode cinema” look (Bebas Neue).
- Integrates `streamlit-searchbox` and `st-clickable-images`.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit (Python)  
- **Data Source:** TMDB API  
- **Libraries:**  
  - `streamlit-searchbox`  
  - `st-clickable-images`  
  - `requests`  
- **Styling:** Custom CSS Injection

---

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/thanyow/CineMatch.git
   cd CineMatch
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your API Key**
   - Sign up at **The Movie Database (TMDB)**.  
   - Go to *Settings → API* to create your key.

4. **Configure Secrets**  
   Create `.streamlit/secrets.toml`:
   ```toml
   tmdb_key = "YOUR_API_KEY_HERE"
   ```

5. **Run the App**
   ```bash
   streamlit run src/recommender.py
   ```

---

## 📂 Project Structure

```text
CineMatch/
├── .streamlit/
│   └── secrets.toml
├── assets/
│   ├── dashboard.png
│   └── details.png
├── src/
│   └── recommender.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🤝 Credits

- Data from **[The Movie Database (TMDB)](https://www.themoviedb.org/)**  
- Built with **[Streamlit](https://streamlit.io/)**  
- Developed by **[thanyow](https://github.com/thanyow)**  

---

<p align="center">
  <i>This product uses the TMDB API but is not endorsed or certified by TMDB.</i>
</p>
