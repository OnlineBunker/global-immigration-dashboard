import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


st.title("World Immigration Data Explorer")
st.markdown(
    """
    #### Explore historical immigration trends across countries with interactive visualizations, statistical summaries, and data filtering.  
    Compare immigration patterns over time and gain insights through intuitive charts and analyses.
    """
)

df = pd.read_csv("data.csv", skiprows=range(0, 3))

st.markdown('---')
st.subheader("Data Preview")
st.write(df.head())
########################################


st.markdown('---')
st.subheader("Data Summary")
st.write(df.describe())

st.markdown('---')
st.subheader("Compare 2 Countries by Immigration Trend")

all_countries = df['Country Name'].unique()
first_country_name = st.selectbox("Select first country", all_countries, key="first")
second_country_name = st.selectbox("Select second country", all_countries, key="second")

if st.button("Compare"):
    st.write(f"Comparing {first_country_name} and {second_country_name}")
    first_country = df.loc[df['Country Name'] == first_country_name].iloc[:, 4:69]
    second_country = df.loc[df['Country Name'] == second_country_name].iloc[:, 4:69]
    years = [i for i in range(1960, 2025)]

    data = pd.DataFrame({
        'Year': years,
        first_country_name: first_country.values.tolist()[0],
        second_country_name: second_country.values.tolist()[0]
    }).set_index('Year')

    st.area_chart(data, color=["#0d76c0", "#ff3a0e"], use_container_width=True)



    # first_country_data = first_country.values.tolist()[0]
    # second_country_data = second_country.values.tolist()[0]
    # years = [i for i in range(1960, 2025)]

    
    # fig, ax = plt.subplots()
    # ax.fill_between(years, first_country_data, color='blue', alpha=0.5, label=first_country_name)
    # ax.fill_between(years, second_country_data, color='red', alpha=0.5, label=second_country_name)
    # ax.set_xlabel("Year")
    # ax.set_ylabel("Number of Immigrants")
    # ax.set_title(f"{first_country_name} vs {second_country_name} Immigration Trend")
    # ax.legend()
    # ax.grid(True)

    # # Show plot in Streamlit
    # st.pyplot(fig)

########################################

st.markdown('---')
st.subheader("Filter Data")
columns = df.columns.tolist()
selected_column = st.selectbox("Select column to filter by", columns)
unique_values = df[selected_column].unique()
selected_value = st.selectbox("Select value", unique_values)

filtered_df = df[df[selected_column] == selected_value]
st.write(filtered_df)

########################################

st.markdown('---')
st.subheader("Plot Data")
x_column = st.selectbox("Select x-axis column", columns)
y_column = st.selectbox("Select y-axis column", columns)
if st.button("Generate Plot"):
    st.line_chart(filtered_df.set_index(x_column)[y_column])

########################################
st.markdown('---')
indian_row = df.loc[df['Country Name'] == 'India'].iloc[: , 4:69]
rows = indian_row.values.tolist()[0]
columns = [i for i in range(1960, 2025)]
st.subheader("Indian Immigration Data")
st.line_chart(pd.DataFrame(rows, index=columns, columns=['Number of immigrants']))

########################################
st.markdown('---')
mean = float(indian_row.mean(axis=1).iloc[0])
std_dev = float(indian_row.std(axis=1).iloc[0])

x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)

cdf = stats.norm.cdf(x, mean, std_dev)
pdf = stats.norm.pdf(x, mean, std_dev)
st.subheader("PDF of Indian Immigrants")
st.write("The PDF graph shows the relative likelihood of the number of Indian immigrants taking on a specific value.")
fig_pdf, ax_pdf = plt.subplots()
ax_pdf.plot(x, pdf, label='PDF')
ax_pdf.axvline(mean, color='r', linestyle=':', label='Mean')
ax_pdf.set_xlabel('Number of immigrants')
ax_pdf.set_ylabel('Probability Density')
ax_pdf.set_title('PDF of Indian immigrants')
ax_pdf.legend()
ax_pdf.grid(True)
st.pyplot(fig_pdf)
st.markdown('---')
st.subheader("CDF of Indian Immigrants")
st.write("The CDF graph shows the probability that the number of Indian immigrants is less than or equal to a specific value on the x-axis")
fig_cdf, ax_cdf = plt.subplots()
ax_cdf.plot(x, cdf, label='CDF')
ax_cdf.axvline(mean, color='r', linestyle=':', label='Mean')
ax_cdf.set_xlabel('Number of immigrants')
ax_cdf.set_ylabel('Probability')
ax_cdf.set_title('CDF of Indian immigrants')
ax_cdf.legend()
ax_cdf.grid(True)
st.pyplot(fig_cdf)

st.markdown('---')
df['Mean Immigrants'] = df.iloc[:, 4:69].mean(axis=1)

top_10 = df.sort_values(by='Mean Immigrants', ascending=False).head(10)
bottom_10 = df.sort_values(by='Mean Immigrants').head(10)

top_10_chart = top_10[['Country Name', 'Mean Immigrants']].set_index('Country Name')
bottom_10_chart = bottom_10[['Country Name', 'Mean Immigrants']].set_index('Country Name')

st.subheader("Top 10 Countries by Mean Immigrants")
st.bar_chart(top_10_chart)

st.markdown("---")

st.subheader("Last 10 Countries by Mean Immigrants")
st.bar_chart(bottom_10_chart)

st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; font-size:14px; color:gray;">
    Made with ❤️ by **Yash Dhankhar** &nbsp;&nbsp;|&nbsp;&nbsp;  
    <a href="https://github.com/OnlineBunker" target="_blank">GitHub</a> &nbsp;|&nbsp;
    <a href="https://www.linkedin.com/in/yash-d-dhankhar/" target="_blank">LinkedIn</a> &nbsp;|&nbsp;  
    <a href="https://www.instagram.com/yash_d_dhankhar/" target="_blank">Instagram</a> &nbsp;|&nbsp;  
    </div>
    """, 
    unsafe_allow_html=True
)
