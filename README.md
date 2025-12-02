
````markdown
# 🍿 CineMatch

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cinematch.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.9%2B-E50914?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-abbb72)
![API](https://img.shields.io/badge/Data-TMDB_API-E50914)

**CineMatch** is an AI-powered movie discovery engine that bridges the gap between static recommendations and an immersive streaming experience. Built entirely in Python, it leverages the **TMDB Live API** to provide real-time trending data, smart recommendations, and watchable trailers in a Streaming platform-style interface.

🔗 **Live Demo:** [Launch App](https://cinematch.streamlit.app)

---

## 📸 Preview

| **Trending Dashboard** | **Movie Details & Trailers** |
|:---:|:---:|
| <img src="assets/dashboard.png" width="400" alt="CineMatch Dashboard"> | <img src="assets/details.png" width="400" alt="Movie Details Page"> |
| *Curated dashboard with live trending movies* | *Immersive details page with embedded trailers* |

---

## ✨ Key Features

### 🎬 **Cinema Mode**
- **Embedded Trailers:** Automatically finds and embeds the official YouTube trailer for every movie directly in the dashboard.
- **Rich Metadata:** Displays dynamic backdrops, release years, runtimes, and ratings.
- **Smart Recommendations:** Provides "More Like This" suggestions using TMDB's collaborative filtering algorithm.

### 🔥 **Live Trending**
- Instantly fetches the **Top 10 Trending Movies** of the week from TMDB.
- Displays results in a responsive, **clickable image grid** Streaming platform-style rather than a boring list.

### 🔍 **Smart Search**
- Implements **Debounced Search** to prevent API rate limiting.
- Features **Auto-complete suggestions**: Type "Spider" and instantly see "Spider-Man: No Way Home", "Spider-Man: Across the Spider-Verse", etc.
- Auto-clears input upon selection for a smooth user flow.

### ⚡ **Technical Highlights**
- **Session State Management:** Preserves user navigation history without reloading the entire app.
- **Custom CSS:** Overrides Streamlit defaults to create a "Dark Mode" cinema aesthetic with custom fonts (Bebas Neue).
- **Component Integration:** Seamlessly integrates `streamlit-searchbox` and `st-clickable-images`.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit (Python)
* **Data Source:** The Movie Database (TMDB) API
* **Key Libraries:**
  * `streamlit-searchbox` (Real-time search)
  * `st-clickable-images` (Interactive Grid)
  * `requests` (API Handling)
* **Styling:** Custom CSS Injection

---

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/thanyow/CineMatch.git](https://github.com/thanyow/CineMatch.git)
   cd CineMatch
````

2.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Get your API Key**

      - Sign up at [The Movie Database (TMDB)](https://www.themoviedb.org/).
      - Go to Settings \> API to generate your key.

4.  **Configure Secrets**
    Create a file named `.streamlit/secrets.toml` in the root directory:

    ```toml
    tmdb_key = "YOUR_API_KEY_HERE"
    ```

5.  **Run the App**

    ```bash
    streamlit run src/recommender.py
    ```

-----

## 📂 Project Structure

```text
CineMatch/
├── .streamlit/
│   └── secrets.toml      # API Keys (GitIgnored)
├── assets/               # Screenshots for Readme
│   ├── dashboard.png     # App Screenshot
│   └── details.png       # App Screenshot
├── src/
│   └── recommender.py    # Main Application Logic
├── .gitignore            # Security rules
├── README.md             # Documentation
└── requirements.txt      # Dependencies
```

-----

## 🤝 Credits

  * Data provided by **[The Movie Database (TMDB)](https://www.themoviedb.org/)**.
  * Built with **[Streamlit](https://streamlit.io/)**.
  * Developed by **[thanyow](https://github.com/thanyow)**.

-----

\<p align="center"\>
\<i\>This product uses the TMDB API but is not endorsed or certified by TMDB.\</i\>
\</p\>

```
```