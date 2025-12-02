# 🍿 CineMatch

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cinema-tch.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![API](https://img.shields.io/badge/API-TMDB-green)

**CineMatch** is an interactive movie discovery engine that bridges the gap between static data projects and immersive streaming experiences. Built entirely in Python, it leverages the **TMDB Live API** to provide real-time trending data, smart recommendations, and watchable trailers in a Netflix-style interface.

🔗 **Live Demo:** [View App](https://cinema-tch.streamlit.app)

---

## 📸 Screenshots

| **Trending Dashboard** | **Movie Details & Trailer** |
|:---:|:---:|
| <img src="assets/dashboard.png?v=2" width="400"> | <img src="assets/details.png?v=2" width="400"> |

---

## ✨ Key Features

### 🔥 **Live Trending Dashboard**
- Instantly fetches the **Top 10 Trending Movies** of the week from TMDB.
- Displays results in a responsive, **clickable image grid** (Netflix-style) rather than a boring list.

### 🔍 **Smart Search Engine**
- Implements **Debounced Search** to prevent API rate limiting.
- Features **Auto-complete suggestions**: Type "Spider" and instantly see "Spider-Man: No Way Home", "Spider-Man: Across the Spider-Verse", etc.
- Auto-clears input upon selection for a smooth user flow.

### 🎬 **Cinema Mode**
- **Embedded Trailers:** Automatically finds and embeds the official YouTube trailer for every movie.
- **Rich Metadata:** Displays dynamic backdrops, release years, runtimes, and ratings.
- **Smart Recommendations:** Provides "More Like This" suggestions using TMDB's collaborative filtering algorithm.

### ⚡ **Technical Highlights**
- **Session State Management:** Preserves user navigation history without reloading the entire app.
- **Custom CSS:** Overrides Streamlit defaults to create a "Dark Mode" cinema aesthetic with custom fonts (Bebas Neue).
- **Component Integration:** seamlessly integrates `streamlit-searchbox` and `st-clickable-images`.

---

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/thanyow/CineMatch.git
   cd CineMatch
