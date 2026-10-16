# ================================================================
# MUSIC TRENDS AND AUDIO CHARACTERISTICS ANALYSIS
# ================================================================
# Project Title:
# Analysis of Music Trends and Audio Characteristics
# Over the Years Using Python
#
# Dataset:
# data_by_year-selected-columns.csv
#
# This project analyzes how different characteristics of music
# have changed over the years.
# ================================================================


# ================================================================
# 1. IMPORT REQUIRED LIBRARIES
# ================================================================

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# pandas       -> Used for reading and analyzing tabular data
# numpy        -> Used for numerical operations
# matplotlib   -> Used for creating graphs
# seaborn      -> Used for attractive statistical visualizations


# ================================================================
# 2. VISUALIZATION SETTINGS
# ================================================================

sns.set_theme(style="whitegrid")

# Sets the default size of graphs
plt.rcParams["figure.figsize"] = (10, 6)

# Sets the default title and label sizes
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 12


# ================================================================
# 3. LOAD DATASET
# ================================================================

file_path = "data_by_year-selected-columns.csv"

# read_csv() reads the CSV file and stores it as a DataFrame
# A DataFrame is a table-like structure provided by pandas
df = pd.read_csv(file_path)


print("\n")
print("=" * 75)
print("        MUSIC TRENDS AND AUDIO CHARACTERISTICS ANALYSIS")
print("=" * 75)


# ================================================================
# 4. DISPLAY FIRST FEW RECORDS
# ================================================================

print("\n1. FIRST 5 RECORDS")
print("-" * 75)

# head() displays the first 5 rows of the dataset
# It helps us check whether the data has loaded correctly
print(df.head())


# ================================================================
# 5. DATASET SHAPE
# ================================================================

print("\n2. DATASET SHAPE")
print("-" * 75)

# shape returns (number of rows, number of columns)
print("Number of Rows    :", df.shape[0])
print("Number of Columns :", df.shape[1])


# ================================================================
# 6. COLUMN NAMES
# ================================================================

print("\n3. COLUMN NAMES")
print("-" * 75)

# df.columns gives the names of all columns
for column in df.columns:
    print("-", column)


# ================================================================
# 7. DATA TYPES
# ================================================================

print("\n4. DATA TYPES")
print("-" * 75)

# dtypes tells us the type of data stored in each column
# Example: int64, float64, object, etc.
print(df.dtypes)


# ================================================================
# 8. DATASET INFORMATION
# ================================================================

print("\n5. DATASET INFORMATION")
print("-" * 75)

# info() displays:
# - number of rows
# - column names
# - non-null values
# - data types
# - memory usage
df.info()


# ================================================================
# 9. CHECK MISSING VALUES
# ================================================================

print("\n6. MISSING VALUE ANALYSIS")
print("-" * 75)

# isnull() checks whether each value is missing
# sum() counts the missing values in each column
missing_values = df.isnull().sum()

print(missing_values)

# If the total number of missing values is 0,
# the dataset does not require missing-value treatment
if missing_values.sum() == 0:
    print("\nNo missing values found in the dataset.")
else:
    print("\nMissing values are present.")


# ================================================================
# 10. CHECK DUPLICATES
# ================================================================

print("\n7. DUPLICATE ANALYSIS")
print("-" * 75)

# duplicated() identifies repeated rows
# sum() gives the total number of duplicate rows
duplicates = df.duplicated().sum()

print("Number of duplicate rows:", duplicates)


# ================================================================
# 11. REMOVE DUPLICATES
# ================================================================

# drop_duplicates() removes repeated rows
# This helps prevent duplicate records from affecting analysis
df = df.drop_duplicates()

print("Duplicates removed successfully.")


# ================================================================
# 12. BASIC STATISTICAL DESCRIPTION
# ================================================================

print("\n8. DESCRIPTIVE STATISTICS")
print("-" * 75)

# describe() gives important statistical values such as:
# count, mean, standard deviation, minimum,
# maximum and quartiles
print(
    df.describe().round(3)
)

# round(3) displays numerical values up to 3 decimal places


# ================================================================
# 13. DATASET TIME PERIOD
# ================================================================

print("\n9. TIME PERIOD")
print("-" * 75)

# min() finds the earliest year
# max() finds the latest year
# nunique() counts the number of unique years
print("Starting Year :", int(df["year"].min()))
print("Ending Year   :", int(df["year"].max()))
print("Total Years   :", df["year"].nunique())


# ================================================================
# 14. AUDIO FEATURES
# ================================================================

# Store the names of important audio-feature columns
# in a list so that we can analyze them together
audio_features = [
    "danceability",
    "energy",
    "valence",
    "tempo",
    "loudness",
    "acousticness",
    "instrumentalness"
]


# ================================================================
# 15. AVERAGE VALUES OF AUDIO FEATURES
# ================================================================

print("\n10. AVERAGE AUDIO FEATURES")
print("-" * 75)

# mean() calculates the average value of every audio feature
average_values = df[audio_features].mean()

print(
    average_values.round(3)
)


# ================================================================
# 16. GRAPH 1
# DANCEABILITY OVER THE YEARS
# ================================================================

plt.figure(figsize=(12, 6))

# plot() creates a line graph
# X-axis -> year
# Y-axis -> danceability
plt.plot(
    df["year"],
    df["danceability"],
    marker="o",
    linewidth=2
)

plt.title("Danceability of Music Over the Years")
plt.xlabel("Year")
plt.ylabel("Danceability")

# tight_layout() automatically adjusts spacing
plt.tight_layout()

# show() displays the graph
plt.show()


# ================================================================
# 17. GRAPH 2
# ENERGY OVER THE YEARS
# ================================================================

plt.figure(figsize=(12, 6))

plt.plot(
    df["year"],
    df["energy"],
    marker="o",
    linewidth=2
)

plt.title("Energy of Music Over the Years")
plt.xlabel("Year")
plt.ylabel("Energy")

plt.tight_layout()
plt.show()


# ================================================================
# 18. GRAPH 3
# VALENCE OVER THE YEARS
# ================================================================

plt.figure(figsize=(12, 6))

plt.plot(
    df["year"],
    df["valence"],
    marker="o",
    linewidth=2
)

plt.title("Valence of Music Over the Years")
plt.xlabel("Year")
plt.ylabel("Valence")

plt.tight_layout()
plt.show()


# ================================================================
# 19. GRAPH 4
# TEMPO OVER THE YEARS
# ================================================================

plt.figure(figsize=(12, 6))

plt.plot(
    df["year"],
    df["tempo"],
    marker="o",
    linewidth=2
)

plt.title("Tempo of Music Over the Years")
plt.xlabel("Year")
plt.ylabel("Tempo (BPM)")

plt.tight_layout()
plt.show()


# ================================================================
# 20. GRAPH 5
# LOUDNESS OVER THE YEARS
# ================================================================

plt.figure(figsize=(12, 6))

plt.plot(
    df["year"],
    df["loudness"],
    marker="o",
    linewidth=2
)

plt.title("Loudness of Music Over the Years")
plt.xlabel("Year")
plt.ylabel("Loudness (dB)")

plt.tight_layout()
plt.show()


# ================================================================
# 21. GRAPH 6
# ACOUSTICNESS OVER THE YEARS
# ================================================================

plt.figure(figsize=(12, 6))

plt.plot(
    df["year"],
    df["acousticness"],
    marker="o",
    linewidth=2
)

plt.title("Acousticness of Music Over the Years")
plt.xlabel("Year")
plt.ylabel("Acousticness")

plt.tight_layout()
plt.show()


# ================================================================
# 22. GRAPH 7
# INSTRUMENTALNESS OVER THE YEARS
# ================================================================

plt.figure(figsize=(12, 6))

plt.plot(
    df["year"],
    df["instrumentalness"],
    marker="o",
    linewidth=2
)

plt.title("Instrumentalness of Music Over the Years")
plt.xlabel("Year")
plt.ylabel("Instrumentalness")

plt.tight_layout()
plt.show()


# ================================================================
# 23. GRAPH 8
# COMPARISON OF NORMALIZED AUDIO FEATURES
# ================================================================

# Different features have different numerical scales.
# For example, tempo is measured in BPM while
# danceability is usually between 0 and 1.
#
# Normalization converts values to a common range of 0 to 1.
# This makes different features easier to compare.

normalized_df = df.copy()

for feature in audio_features:

    # Find minimum and maximum values of the feature
    minimum = df[feature].min()
    maximum = df[feature].max()

    # Min-Max Normalization formula:
    #
    # normalized value =
    # (value - minimum) / (maximum - minimum)
    #
    # The result is generally between 0 and 1.
    normalized_df[feature] = (
        (df[feature] - minimum)
        /
        (maximum - minimum)
    )


plt.figure(figsize=(14, 7))

# Plot the normalized features so that they
# can be compared on the same scale
plt.plot(
    df["year"],
    normalized_df["danceability"],
    label="Danceability"
)

plt.plot(
    df["year"],
    normalized_df["energy"],
    label="Energy"
)

plt.plot(
    df["year"],
    normalized_df["valence"],
    label="Valence"
)

plt.plot(
    df["year"],
    normalized_df["acousticness"],
    label="Acousticness"
)

plt.plot(
    df["year"],
    normalized_df["instrumentalness"],
    label="Instrumentalness"
)

plt.title("Comparison of Music Characteristics Over the Years")
plt.xlabel("Year")
plt.ylabel("Normalized Value")

# legend() displays the names of the lines
plt.legend()

plt.tight_layout()
plt.show()


# ================================================================
# 24. GRAPH 9
# CORRELATION HEATMAP
# ================================================================

# corr() calculates the correlation between numerical columns.
#
# Correlation values range from -1 to +1:
# +1 -> strong positive relationship
#  0 -> little/no linear relationship
# -1 -> strong negative relationship
correlation_matrix = df[audio_features].corr()


print("\n11. CORRELATION MATRIX")
print("-" * 75)

print(
    correlation_matrix.round(3)
)


plt.figure(figsize=(10, 8))

# heatmap() represents correlation values using colors
# annot=True displays the actual correlation values
# fmt=".2f" displays values up to 2 decimal places
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap of Music Audio Features")

plt.tight_layout()
plt.show()


# ================================================================
# 25. GRAPH 10
# DISTRIBUTION OF AUDIO FEATURES
# ================================================================

plt.figure(figsize=(12, 7))

# A boxplot shows the distribution of numerical data.
# It helps identify:
# - median
# - spread
# - possible outliers
df[audio_features].boxplot()

plt.title("Distribution of Music Audio Features")
plt.xlabel("Audio Features")
plt.ylabel("Values")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ================================================================
# 26. HIGHEST AND LOWEST VALUES
# ================================================================

print("\n12. HIGHEST AND LOWEST VALUES")
print("-" * 75)


for feature in audio_features:

    # idxmax() returns the index of the row
    # containing the highest value
    highest_index = df[feature].idxmax()

    # idxmin() returns the index of the row
    # containing the lowest value
    lowest_index = df[feature].idxmin()

    # loc[] is used to access data using row index
    highest_year = df.loc[
        highest_index,
        "year"
    ]

    lowest_year = df.loc[
        lowest_index,
        "year"
    ]

    highest_value = df.loc[
        highest_index,
        feature
    ]

    lowest_value = df.loc[
        lowest_index,
        feature
    ]

    print("\nFeature:", feature)

    print(
        "Highest:",
        round(highest_value, 3),
        "in",
        int(highest_year)
    )

    print(
        "Lowest :",
        round(lowest_value, 3),
        "in",
        int(lowest_year)
    )


# ================================================================
# 27. MOST DANCEABLE YEARS
# ================================================================

print("\n13. TOP 10 MOST DANCEABLE YEARS")
print("-" * 75)

# Select only year and danceability columns
# sort_values() arranges rows according to danceability
# ascending=False means highest values come first
# head(10) selects the first 10 rows
top_danceable = (
    df[
        ["year", "danceability"]
    ]
    .sort_values(
        "danceability",
        ascending=False
    )
    .head(10)
)

print(
    top_danceable.to_string(index=False)
)


# ================================================================
# 28. MOST ENERGETIC YEARS
# ================================================================

print("\n14. TOP 10 MOST ENERGETIC YEARS")
print("-" * 75)

top_energy = (
    df[
        ["year", "energy"]
    ]
    .sort_values(
        "energy",
        ascending=False
    )
    .head(10)
)

print(
    top_energy.to_string(index=False)
)


# ================================================================
# 29. MOST ACOUSTIC YEARS
# ================================================================

print("\n15. TOP 10 MOST ACOUSTIC YEARS")
print("-" * 75)

top_acoustic = (
    df[
        ["year", "acousticness"]
    ]
    .sort_values(
        "acousticness",
        ascending=False
    )
    .head(10)
)

print(
    top_acoustic.to_string(index=False)
)


# ================================================================
# 30. CORRELATION WITH YEAR
# ================================================================

print("\n16. CORRELATION OF AUDIO FEATURES WITH YEAR")
print("-" * 75)

# Here, year is included in the correlation calculation.
# This helps us understand whether a feature tends to
# increase or decrease as the years progress.
year_correlation = (
    df[
        ["year"] + audio_features
    ]
    .corr()["year"]
    .drop("year")
    .sort_values(
        ascending=False
    )
)

print(
    year_correlation.round(3)
)


# ================================================================
# 31. BAR CHART OF YEAR CORRELATIONS
# ================================================================

plt.figure(figsize=(10, 6))

# Bar plot displays the correlation of every audio feature
# with the year.
sns.barplot(
    x=year_correlation.values,
    y=year_correlation.index
)

plt.title(
    "Correlation of Music Features with Year"
)

plt.xlabel("Correlation with Year")
plt.ylabel("Audio Feature")

plt.tight_layout()
plt.show()


# ================================================================
# 32. EARLY VS RECENT MUSIC COMPARISON
# ================================================================

# Divide the dataset into two time periods:
#
# Early Period  : 1921–1970
# Recent Period : 1971–2020
#
# Boolean conditions are used to filter the DataFrame.

early_music = df[
    df["year"] <= 1970
]

recent_music = df[
    df["year"] > 1970
]


# Calculate the average of each audio feature
# separately for the two periods.
early_average = (
    early_music[audio_features]
    .mean()
)

recent_average = (
    recent_music[audio_features]
    .mean()
)


# Create a new DataFrame containing both averages
# so that the two periods can easily be compared.
comparison = pd.DataFrame({

    "Early Period (1921-1970)":
        early_average,

    "Recent Period (1971-2020)":
        recent_average

})


print("\n17. EARLY VS RECENT MUSIC")
print("-" * 75)

print(
    comparison.round(3)
)


# ================================================================
# 33. EARLY VS RECENT COMPARISON GRAPH
# ================================================================

# plot(kind="bar") creates a bar chart
# comparing early and recent music.
comparison.plot(
    kind="bar",
    figsize=(14, 7)
)

plt.title(
    "Comparison of Music Characteristics: Early vs Recent Period"
)

plt.xlabel("Audio Feature")
plt.ylabel("Average Value")

plt.xticks(rotation=45)

plt.legend(
    title="Period"
)

plt.tight_layout()
plt.show()


# ================================================================
# 34. DECADE ANALYSIS
# ================================================================

# Convert each year into its corresponding decade.
#
# Example:
# 1921 -> 1920
# 1937 -> 1930
# 1985 -> 1980
#
# // performs integer division and *10 gives the decade.
df["decade"] = (
    df["year"] // 10
) * 10


# groupby() groups all rows belonging to the same decade.
# mean() then calculates the average of each feature
# for every decade.
decade_average = (
    df.groupby("decade")[audio_features]
    .mean()
)


print("\n18. DECADE-WISE AVERAGE")
print("-" * 75)

print(
    decade_average.round(3)
)


# ================================================================
# 35. DANCEABILITY BY DECADE
# ================================================================

plt.figure(figsize=(12, 6))

plt.plot(
    decade_average.index,
    decade_average["danceability"],
    marker="o",
    linewidth=2
)

plt.title("Average Danceability by Decade")
plt.xlabel("Decade")
plt.ylabel("Average Danceability")

plt.tight_layout()
plt.show()


# ================================================================
# 36. ENERGY BY DECADE
# ================================================================

plt.figure(figsize=(12, 6))

plt.plot(
    decade_average.index,
    decade_average["energy"],
    marker="o",
    linewidth=2
)

plt.title("Average Energy by Decade")
plt.xlabel("Decade")
plt.ylabel("Average Energy")

plt.tight_layout()
plt.show()


# ================================================================
# 37. ACOUSTICNESS BY DECADE
# ================================================================

plt.figure(figsize=(12, 6))

plt.plot(
    decade_average.index,
    decade_average["acousticness"],
    marker="o",
    linewidth=2
)

plt.title("Average Acousticness by Decade")
plt.xlabel("Decade")
plt.ylabel("Average Acousticness")

plt.tight_layout()
plt.show()


# ================================================================
# 38. SAVE IMPORTANT ANALYSIS RESULTS
# ================================================================

# to_csv() saves a DataFrame as a CSV file.
#
# These files can later be opened in Excel or used
# for preparing tables and reports.

comparison.to_csv(
    "early_vs_recent_music_comparison.csv"
)

decade_average.to_csv(
    "decade_wise_music_analysis.csv"
)

correlation_matrix.to_csv(
    "music_correlation_matrix.csv"
)


# ================================================================
# 39. FINAL SUMMARY
# ================================================================

print("\n")
print("=" * 75)
print("                     FINAL SUMMARY")
print("=" * 75)

print("""
The Music Trends Analysis has been successfully completed.

The analysis included:

1. Dataset inspection
2. Data cleaning
3. Missing value analysis
4. Duplicate analysis
5. Descriptive statistics
6. Danceability analysis
7. Energy analysis
8. Valence analysis
9. Tempo analysis
10. Loudness analysis
11. Acousticness analysis
12. Instrumentalness analysis
13. Feature comparison
14. Correlation analysis
15. Correlation heatmap
16. Distribution analysis
17. Highest and lowest values
18. Top danceable years
19. Top energetic years
20. Top acoustic years
21. Correlation with year
22. Early vs recent music comparison
23. Decade-wise analysis

The generated CSV files are:

- early_vs_recent_music_comparison.csv
- decade_wise_music_analysis.csv
- music_correlation_matrix.csv
""")

print("=" * 75)
print("                  END OF ANALYSIS")
print("=" * 75)


