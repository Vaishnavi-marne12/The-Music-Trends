# SONORA | Music Trends Dashboard
# A simple, pastel-themed front end for the music analysis project.
# Keep this file and data_by_year-selected-columns.csv in the same folder.

from pathlib import Path
import io

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="The Music Trends",
    page_icon="♫",
    layout="wide",
)

# -------------------- Soft pastel theme --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --ink: #35334a;
    --muted: #77758b;
    --lavender: #e9e2f7;
    --pink: #f7e2e8;
    --mint: #dff0e7;
    --blue: #e2edf8;
    --cream: #fffdf9;
    --line: #e9e4ed;
}
.stApp {
    background: #fbf9fc;
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}
.block-container { max-width: 1400px; padding-top: 2rem; padding-bottom: 3rem; }
h1, h2, h3 { color: var(--ink) !important; font-family: 'Playfair Display', serif !important; }
p, label, [data-testid="stMarkdownContainer"] { color: var(--ink); }
[data-testid="stSidebar"] { background: #f1ecf8; border-right: 1px solid #e5dced; }
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p { color: var(--ink) !important; }
[data-testid="stMetric"] {
    background: white;
    border: 1px solid var(--line);
    border-radius: 15px;
    padding: 16px 18px;
    box-shadow: 0 3px 12px rgba(63, 48, 83, .035);
}
[data-testid="stMetricLabel"] { color: var(--muted) !important; }
[data-testid="stMetricValue"] { color: var(--ink) !important; }
[data-testid="stMetricDelta"] { color: #638b7b !important; }
div[data-testid="stPlotlyChart"], div[data-testid="stDataFrame"] {
    background: white;
    border: 1px solid var(--line);
    border-radius: 15px;
    padding: 8px;
}
.stTabs [data-baseweb="tab-list"] { gap: 7px; }
.stTabs [data-baseweb="tab"] {
    background: #f0ebf7;
    border-radius: 9px 9px 0 0;
    padding: 9px 15px;
}
.stTabs [aria-selected="true"] { background: #e1d7f2 !important; }
div.stButton > button, div.stDownloadButton > button {
    background: #e4d9f3;
    color: #35334a;
    border: 1px solid #d7c9eb;
    border-radius: 9px;
}
div.stButton > button:hover, div.stDownloadButton > button:hover {
    background: #d7c8ed;
    color: #35334a;
    border-color: #c8b6e3;
}
.hero {
    background: linear-gradient(110deg, #f3eafa, #fff0f1 58%, #eaf5f0);
    border: 1px solid #eee3ef;
    border-radius: 20px;
    padding: 27px 30px;
    margin-bottom: 18px;
}
.kicker { color: #8b729e; font-size: 12px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; }
.hero p { color: #777187; margin-bottom: 0; }
.note {
    background: #f3eef9;
    border: 1px solid #e6dcef;
    border-radius: 12px;
    padding: 14px 17px;
}
.feature-card {
    background: white;
    border: 1px solid var(--line);
    border-radius: 13px;
    padding: 15px;
    min-height: 105px;
}
div[data-baseweb="select"] > div { border-radius: 9px; }
hr { border-color: #ebe5ef; }
footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# A restrained palette for charts
PALETTE = ["#b9a6d9", "#e8b7c5", "#a9cbbd", "#a9c5df", "#e8d3a8", "#c9bfdc", "#d5b5a9"]
INK = "#49445d"
GRID = "rgba(120, 110, 140, 0.12)"
FEATURES = [
    "danceability", "energy", "valence", "tempo", "loudness",
    "acousticness", "instrumentalness"
]
LABELS = {
    "danceability": "Danceability",
    "energy": "Energy",
    "valence": "Valence",
    "tempo": "Tempo (BPM)",
    "loudness": "Loudness (dB)",
    "acousticness": "Acousticness",
    "instrumentalness": "Instrumentalness",
}

def label_for(column):
    return LABELS.get(column, column.replace("_", " ").title())

def tidy_chart(fig, height=380):
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(family="DM Sans, sans-serif", color=INK, size=12),
        title_font=dict(family="Playfair Display, serif", size=19, color=INK),
        margin=dict(l=18, r=18, t=58, b=25),
        height=height,
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=INK)),
        xaxis=dict(gridcolor=GRID, zerolinecolor=GRID, linecolor="#e8e2ec"),
        yaxis=dict(gridcolor=GRID, zerolinecolor=GRID, linecolor="#e8e2ec"),
        hoverlabel=dict(bgcolor="#fffafc", font_color=INK),
    )
    return fig

# -------------------- Data --------------------
st.sidebar.markdown("# ♫ The MUSIC Trends")
st.sidebar.caption("By, Vaishnavi Marne (125B1F244),Anjali Borse (125B1F236) , Aarya Suryavanshi (125B1F235)")
st.sidebar.divider()

uploaded = st.sidebar.file_uploader("Choose a music CSV or ZIP", type=["csv", "zip"])
# Preferred dataset: the ZIP file already present in the project folder.
zip_path = Path("full_music_data.csv.zip")
csv_candidates = [
    Path("data_by_year-selected-columns.csv"),
    Path("full_music_data.csv"),
    Path("data_by_artist-selected-columns.csv"),
]

@st.cache_data
def read_uploaded_data(content, filename):
    if filename.lower().endswith(".zip"):
        return pd.read_csv(io.BytesIO(content), compression="zip")
    return pd.read_csv(io.BytesIO(content))

try:
    if uploaded is not None:
        raw_df = read_uploaded_data(uploaded.getvalue(), uploaded.name)
        source_name = uploaded.name
    elif zip_path.exists():
        raw_df = pd.read_csv(zip_path, compression="zip")
        source_name = zip_path.name
    else:
        found_csv = next((p for p in csv_candidates if p.exists()), None)
        if found_csv is not None:
            raw_df = pd.read_csv(found_csv)
            source_name = found_csv.name
        else:
            st.markdown("""
            <div class="hero">
              <div class="kicker">Music trends, made easy</div>
              <h1 style="font-size:42px;margin:8px 0">The MUSIC Trends ♫</h1>
              <p>Explore the story behind music through simple charts and audio features....</p>
            </div>
            """, unsafe_allow_html=True)
            st.info("Place `full_music_data.csv.zip` beside `app.py`, or upload a CSV/ZIP using the sidebar.")
            st.code("pip install -r requirements.txt\npython -m streamlit run app.py", language="bash")
            st.stop()
except Exception as error:
    st.error(f"Could not read the data file: {error}")
    st.stop()

raw_df.columns = [str(col).strip() for col in raw_df.columns]
if "year" not in raw_df.columns:
    st.error("The CSV must contain a column named `year`.")
    st.stop()

raw_df["year"] = pd.to_numeric(raw_df["year"], errors="coerce")
features = [f for f in FEATURES if f in raw_df.columns]
for f in features:
    raw_df[f] = pd.to_numeric(raw_df[f], errors="coerce")
if not features:
    st.error("No expected audio-feature columns were found in this CSV.")
    st.stop()

raw_df = raw_df.dropna(subset=["year"]).copy()
raw_df["year"] = raw_df["year"].astype(int)
duplicate_count = int(raw_df.duplicated().sum())
df = raw_df.drop_duplicates().copy()
year_min, year_max = int(df["year"].min()), int(df["year"].max())

st.sidebar.subheader("Explore")
picked_features = st.sidebar.multiselect(
    "Audio features", features, default=features,
    format_func=label_for,
)
if not picked_features:
    picked_features = features
if year_min < year_max:
    year_range = st.sidebar.slider(
        "Choose a year range", year_min, year_max, (year_min, year_max)
    )
    start_year, end_year = year_range
else:
    start_year = end_year = year_min

view = df[df["year"].between(start_year, end_year)].copy()
if view.empty:
    st.warning("There are no records in this year range.")
    st.stop()

# -------------------- Header --------------------
st.markdown(f"""
<div class="hero">
    <div class="kicker">Music trends & audio characteristics</div>
    <h1 style="font-size:42px;margin:8px 0 6px">The MUSIC Trends <span style="font-size:26px">♫</span></h1>
    <p>Every era has its own sound. Explore what the data can tell us.</p>
    <p style="font-size:12px;margin-top:13px">DATA FILE: {source_name} &nbsp; · &nbsp; YEARS: {start_year}–{end_year}</p>
</div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Years covered", f"{view['year'].nunique():,}")
m2.metric("Records", f"{len(view):,}")
m3.metric("Audio features", f"{len(features)}")
m4.metric("Duplicate rows removed", f"{duplicate_count:,}")

tabs = st.tabs(["Overview", "Trends", "Compare periods", "Correlations", "Top years", "Dataset"])

# -------------------- Overview --------------------
with tabs[0]:
    left, right = st.columns([1.3, 1])
    with left:
        st.subheader("One feature, over time")
        overview_feature = st.selectbox(
            "Choose an audio feature", picked_features,
            format_func=label_for, key="overview_feature"
        )
        trend = view.groupby("year", as_index=False)[overview_feature].mean()
        fig = px.line(
            trend, x="year", y=overview_feature, markers=True,
            color_discrete_sequence=["#b49bd5"],
            title=f"{label_for(overview_feature)} by year"
        )
        fig.update_traces(line_width=3, marker_size=5)
        st.plotly_chart(tidy_chart(fig, 390), use_container_width=True)
    with right:
        st.subheader("Average feature values")
        averages = view[picked_features].mean().dropna().sort_values().reset_index()
        averages.columns = ["Feature", "Average"]
        averages["Feature"] = averages["Feature"].map(label_for)
        fig = px.bar(
            averages, x="Average", y="Feature", orientation="h",
            color="Feature", color_discrete_sequence=PALETTE,
            title="A quick snapshot"
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(tidy_chart(fig, 390), use_container_width=True)

    st.markdown("### A few things to know")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="feature-card">🎶 <b>Danceability</b><br><span style="color:#77758b">How suitable a track may be for dancing.</span></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="feature-card">🌿 <b>Acousticness</b><br><span style="color:#77758b">How likely a track is to be acoustic.</span></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="feature-card">☀️ <b>Valence</b><br><span style="color:#77758b">A measure associated with the musical mood.</span></div>', unsafe_allow_html=True)

# -------------------- Trends --------------------
with tabs[1]:
    st.subheader("How has the sound changed?")
    trend_features = st.multiselect(
        "Choose features to compare", picked_features,
        default=picked_features[:min(3, len(picked_features))],
        format_func=label_for, key="trend_features"
    )
    if not trend_features:
        trend_features = picked_features[:1]
    annual = view.groupby("year", as_index=False)[trend_features].mean()
    long_annual = annual.melt(id_vars="year", var_name="Feature", value_name="Value")
    long_annual["Feature"] = long_annual["Feature"].map(label_for)
    fig = px.line(
        long_annual, x="year", y="Value", color="Feature", markers=True,
        color_discrete_sequence=PALETTE, title="Audio features through the years"
    )
    st.plotly_chart(tidy_chart(fig, 440), use_container_width=True)

    st.caption("Some features use different units. The chart below scales each selected feature from 0 to 1 to compare its pattern, not its original value.")
    normalized = annual.copy()
    for f in trend_features:
        low, high = normalized[f].min(), normalized[f].max()
        normalized[f] = (normalized[f] - low) / (high - low) if high != low else 0
    norm_long = normalized.melt(id_vars="year", var_name="Feature", value_name="Normalized value")
    norm_long["Feature"] = norm_long["Feature"].map(label_for)
    fig = px.line(
        norm_long, x="year", y="Normalized value", color="Feature", markers=True,
        color_discrete_sequence=PALETTE, title="Compare patterns on the same scale"
    )
    st.plotly_chart(tidy_chart(fig, 390), use_container_width=True)

    decade_data = view.copy()
    decade_data["Decade"] = decade_data["year"] // 10 * 10
    decade_avg = decade_data.groupby("Decade", as_index=False)[trend_features].mean()
    decade_long = decade_avg.melt(id_vars="Decade", var_name="Feature", value_name="Average")
    decade_long["Feature"] = decade_long["Feature"].map(label_for)
    fig = px.line(
        decade_long, x="Decade", y="Average", color="Feature", markers=True,
        color_discrete_sequence=PALETTE, title="A decade-by-decade view"
    )
    st.plotly_chart(tidy_chart(fig, 390), use_container_width=True)

# -------------------- Compare periods --------------------
with tabs[2]:
    st.subheader("Music then and now")
    midpoint = (start_year + end_year) // 2
    early = view[view["year"] <= midpoint]
    recent = view[view["year"] > midpoint]
    if early.empty or recent.empty:
        st.info("Choose a wider year range to compare two periods.")
    else:
        comparison = pd.DataFrame({
            f"Earlier ({start_year}–{midpoint})": early[picked_features].mean(),
            f"Later ({midpoint + 1}–{end_year})": recent[picked_features].mean(),
        })
        long_comparison = comparison.rename_axis("Feature").reset_index().melt(
            id_vars="Feature", var_name="Period", value_name="Average"
        )
        long_comparison["Feature"] = long_comparison["Feature"].map(label_for)
        fig = px.bar(
            long_comparison, x="Feature", y="Average", color="Period",
            barmode="group", color_discrete_sequence=["#c6b3e2", "#e8b9c8"],
            title="Average feature values by period"
        )
        fig.update_layout(xaxis_tickangle=-25)
        st.plotly_chart(tidy_chart(fig, 430), use_container_width=True)
        st.dataframe(comparison.rename(index=label_for).round(3), use_container_width=True)
        st.download_button(
            "Download period comparison",
            comparison.round(4).to_csv().encode("utf-8"),
            file_name="early_vs_recent_music_comparison.csv",
            mime="text/csv",
        )

    st.subheader("How spread out are the values?")
    box_data = view[picked_features].melt(var_name="Feature", value_name="Value")
    box_data["Feature"] = box_data["Feature"].map(label_for)
    fig = px.box(
        box_data, x="Feature", y="Value", color="Feature",
        color_discrete_sequence=PALETTE, title="Feature distributions"
    )
    fig.update_layout(showlegend=False, xaxis_tickangle=-25)
    st.plotly_chart(tidy_chart(fig, 420), use_container_width=True)

# -------------------- Correlations --------------------
with tabs[3]:
    st.subheader("Which features move together?")
    corr_features = st.multiselect(
        "Features for correlation", picked_features,
        default=picked_features, format_func=label_for, key="corr_features"
    )
    if len(corr_features) >= 2:
        corr = view[corr_features].corr()
        display_names = [label_for(c) for c in corr.columns]
        fig = go.Figure(data=go.Heatmap(
            z=corr.values, x=display_names, y=display_names,
            zmin=-1, zmax=1,
            colorscale=[[0, "#9db8d8"], [0.5, "#fffaf5"], [1, "#d9a5ba"]],
            text=np.round(corr.values, 2), texttemplate="%{text:.2f}",
            hovertemplate="%{x} and %{y}<br>Correlation: %{z:.2f}<extra></extra>",
            colorbar=dict(title="Correlation"),
        ))
        fig.update_layout(title="Correlation heatmap")
        st.plotly_chart(tidy_chart(fig, 500), use_container_width=True)
        st.caption("Values closer to +1 show a positive relationship; values closer to −1 show an inverse relationship. Correlation does not prove cause and effect.")
        st.download_button(
            "Download correlation matrix",
            corr.round(4).to_csv().encode("utf-8"),
            file_name="music_correlation_matrix.csv",
            mime="text/csv",
        )

        year_corr = view[["year"] + corr_features].corr()["year"].drop("year").sort_values()
        corr_frame = year_corr.rename(index=label_for).rename_axis("Feature").reset_index(name="Correlation with year")
        fig = px.bar(
            corr_frame, x="Correlation with year", y="Feature", orientation="h",
            color="Correlation with year",
            color_continuous_scale=["#a9c5df", "#fffaf5", "#e3afc2"],
            range_color=[-1, 1], title="Relationship with year"
        )
        st.plotly_chart(tidy_chart(fig, 350), use_container_width=True)
    else:
        st.info("Select at least two features to view their correlation.")

# -------------------- Top years --------------------
with tabs[4]:
    st.subheader("Years that stand out")
    rank_feature = st.selectbox("Rank by feature", picked_features, format_func=label_for)
    number = st.slider("How many years?", 5, 20, 10)
    ranking = view[["year", rank_feature]].dropna().nlargest(number, rank_feature)
    chart_data = ranking.sort_values(rank_feature)
    fig = px.bar(
        chart_data, x=rank_feature, y=chart_data["year"].astype(str),
        orientation="h", color_discrete_sequence=["#c3b0df"],
        title=f"Top {number} years for {label_for(rank_feature)}",
        labels={rank_feature: label_for(rank_feature), "y": "Year"}
    )
    fig.update_layout(yaxis_title="Year")
    st.plotly_chart(tidy_chart(fig, max(350, number * 29)), use_container_width=True)
    ranking = ranking.rename(columns={rank_feature: label_for(rank_feature)})
    st.dataframe(ranking, hide_index=True, use_container_width=True)
    st.download_button(
        "Download top years",
        ranking.to_csv(index=False).encode("utf-8"),
        file_name=f"top_years_{rank_feature}.csv",
        mime="text/csv",
    )

# -------------------- Dataset --------------------
with tabs[5]:
    st.subheader("Behind the charts")
    a, b = st.columns(2)
    with a:
        st.markdown("#### Dataset details")
        summary = pd.DataFrame({
            "Item": ["Rows in original data", "Rows after removing duplicates",
                     "Duplicate rows", "Missing cells", "Columns", "Distinct years"],
            "Value": [len(raw_df), len(df), duplicate_count, int(df.isna().sum().sum()),
                      len(df.columns), df["year"].nunique()]
        })
        st.dataframe(summary, hide_index=True, use_container_width=True)
    with b:
        st.markdown("#### Descriptive statistics")
        st.dataframe(df[picked_features].describe().T.round(3), use_container_width=True)

    st.markdown("#### Preview the data")
    st.dataframe(view, use_container_width=True, height=320)
    st.download_button(
        "Download selected records",
        view.to_csv(index=False).encode("utf-8"),
        file_name="sonora_filtered_music_data.csv",
        mime="text/csv",
    )

    decade_data = view.copy()
    decade_data["decade"] = decade_data["year"] // 10 * 10
    decade_average = decade_data.groupby("decade")[picked_features].mean()
    st.markdown("#### Decade averages")
    st.dataframe(decade_average.round(3), use_container_width=True)
    st.download_button(
        "Download decade analysis",
        decade_average.round(4).to_csv().encode("utf-8"),
        file_name="decade_wise_music_analysis.csv",
        mime="text/csv",
    )

st.divider()
st.markdown(
    "<p style='text-align:center;color:#858095'>♫ &nbsp; Sonora · Music trends, seen a little differently. &nbsp; ♫</p>",
    unsafe_allow_html=True,
)
