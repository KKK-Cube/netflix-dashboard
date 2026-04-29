import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Netflix EDA Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/netflix_titles.csv")
    df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors="coerce")
    df["year_added"] = df["date_added"].dt.year
    return df

df = load_data()

# Sidebar filter
st.sidebar.title("Filter")
content_type = st.sidebar.radio("Content Type", ["All", "Movie", "TV Show"])

min_year = int(df["year_added"].dropna().min())
max_year = int(df["year_added"].dropna().max())
year_range = st.sidebar.slider("Year Added", min_year, max_year, (min_year, max_year))

if content_type != "All":
    df = df[df["type"] == content_type]
df = df[(df["year_added"].isna()) | (df["year_added"].between(year_range[0], year_range[1]))]

# Title
st.title("Netflix Movies & TV Shows Dashboard")
st.markdown("Exploratory analysis of Netflix content library.")

# KPI cards
total = len(df)
movies = len(df[df["type"] == "Movie"])
shows = len(df[df["type"] == "TV Show"])
countries = df["country"].dropna().str.split(",").explode().str.strip().nunique()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Titles", total)
col2.metric("Movies", movies)
col3.metric("TV Shows", shows)
col4.metric("Countries", countries)

st.divider()

# Row 1: Pie chart + Content added per year
col1, col2 = st.columns(2)

with col1:
    st.subheader("Movies vs TV Shows")
    type_counts = df["type"].value_counts().reset_index()
    type_counts.columns = ["type", "count"]
    fig = px.pie(type_counts, names="type", values="count", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Content Added Per Year")
    year_counts = df["year_added"].dropna().astype(int).value_counts().sort_index().reset_index()
    year_counts.columns = ["year", "count"]
    fig = px.line(year_counts, x="year", y="count", markers=True)
    st.plotly_chart(fig, use_container_width=True)

# Row 2: Top genres + Top countries
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Genres")
    genres = df["listed_in"].dropna().str.split(",").explode().str.strip()
    genre_counts = genres.value_counts().head(10).reset_index()
    genre_counts.columns = ["genre", "count"]
    fig = px.bar(genre_counts, x="count", y="genre", orientation="h",
                 category_orders={"genre": genre_counts["genre"].tolist()})
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Top 10 Countries")
    country_series = df["country"].dropna().str.split(",").explode().str.strip()
    country_counts = country_series.value_counts().head(10).reset_index()
    country_counts.columns = ["country", "count"]
    fig = px.bar(country_counts, x="country", y="count")
    st.plotly_chart(fig, use_container_width=True)

# Row 3: World map
st.subheader("Content by Country (World Map)")
all_countries = df["country"].dropna().str.split(",").explode().str.strip()
map_counts = all_countries.value_counts().reset_index()
map_counts.columns = ["country", "count"]
fig = px.choropleth(map_counts, locations="country", locationmode="country names",
                    color="count", color_continuous_scale="Reds",
                    labels={"count": "Titles"})
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
st.plotly_chart(fig, use_container_width=True)

# Row 4: Rating distribution
st.subheader("Rating Distribution")
rating_counts = df["rating"].dropna().value_counts().reset_index()
rating_counts.columns = ["rating", "count"]
fig = px.bar(rating_counts, x="rating", y="count")
st.plotly_chart(fig, use_container_width=True)
