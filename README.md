# Netflix Movies & TV Shows Dashboard

[![Live Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://kcube-netflix-dashboard.streamlit.app)

An interactive data exploration dashboard built with Python and Streamlit, analyzing Netflix's content library.

## Features

- Filter content by Movies, TV Shows, or both
- KPI cards: total titles, movies, TV shows, and countries represented
- Movies vs TV Shows breakdown (pie chart)
- Content added per year trend (line chart)
- Top 10 genres (bar chart)
- Top 10 countries producing content (bar chart)
- Rating distribution — G, PG, TV-MA, etc. (bar chart)

## Tech Stack

- **Python**
- **pandas** — data loading and cleaning
- **Plotly** — interactive charts
- **Streamlit** — web app UI

## Dataset

[Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows) from Kaggle (~8,800 titles).

## Getting Started

1. Clone the repo
   ```bash
   git clone https://github.com/KKK-Cube/netflix-dashboard.git
   cd netflix-dashboard
   ```

2. Install dependencies
   ```bash
   python -m pip install -r requirements.txt
   ```

3. Run the app
   ```bash
   python -m streamlit run app.py
   ```

4. Open your browser at `http://localhost:8501`

## License

MIT
