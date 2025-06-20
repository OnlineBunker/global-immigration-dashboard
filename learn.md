# 📘 learn.md

## 🌍 World Immigration Data Explorer – Learning Summary

This project is an interactive dashboard to visualize and analyze global immigration trends using:

* **Streamlit** for the UI and interactivity
* **Pandas** for data manipulation
* **Matplotlib** for custom plots
* **SciPy** for statistical distributions

---

## ✅ What I Learned

### 📊 1. Data Handling with Pandas

* Loaded a dataset using `pd.read_csv("data.csv", skiprows=range(0, 3))` to skip header metadata.
* Previewed data using `df.head()` and summarized it with `df.describe()`.
* Filtered data dynamically based on user-selected column and value via `selectbox`.

### 🎨 2. Interactive Visualizations with Streamlit

* Displayed time-series data using `st.area_chart()` and `st.line_chart()`.
* Rendered top/bottom countries with `st.bar_chart()`.
* Created selection inputs for user interaction (e.g. country comparisons).
* Rendered plots using Matplotlib + `st.pyplot()`.

### 📈 3. Immigration Trend Comparison

* Allowed users to select two countries and compare their immigration trends from 1960 to 2024.
* Constructed a DataFrame for both countries across years and plotted with `area_chart()`.

### 📐 4. Statistical Visualization

* Calculated **mean** and **standard deviation** of Indian immigration data.
* Generated and displayed:

  * **PDF (Probability Density Function)** using `stats.norm.pdf()`
  * **CDF (Cumulative Distribution Function)** using `stats.norm.cdf()`
* Used Matplotlib for custom graphing and highlighted the mean with a vertical line.

### 📊 5. Aggregation Insights

* Calculated mean immigrants for each country across years with:

  ```python
  df['Mean Immigrants'] = df.iloc[:, 4:69].mean(axis=1)
  ```
* Sorted and visualized top and bottom 10 countries.

---

## 📂 Dataset Structure

* Source: `data.csv`
* Format: CSV with metadata in first 3 rows (skipped)
* Each row: A country
* Each column from index 4 to 68: Immigration numbers from 1960 to 2024

---

## 🧪 Libraries Used

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
```

---

## 🧠 Concepts Reinforced

* Streamlit app structure and markdown formatting
* Selectively slicing DataFrames with `.iloc[]` and `.loc[]`
* Interactive UIs in data apps
* Area charts, bar charts, line charts for time-series data
* PDF & CDF graphs using statistical distributions
* Sorting and ranking datasets

---

## 🚀 Future Improvements

* Add download/export functionality for filtered data
* Enable multi-country comparison (more than 2)
* Implement rolling averages or trend lines
* Enhance chart interactivity with tooltips
* Add caching for better performance with large files

---

## ✍️ Author

**Yash Dhankhar**

* 🌐 [GitHub](https://github.com/OnlineBunker)
* 🔗 [LinkedIn](https://www.linkedin.com/in/yash-d-dhankhar/)
* 📷 [Instagram](https://www.instagram.com/yash_d_dhankhar/)

---

> *“Code is a canvas for insight. This project helped me turn raw data into a story.”*
