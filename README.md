# PLP-Python-Assignment-Week-7

## Basic Data Analysis

---

### Description

**Objective for this Assignment:**
- To load and analyze a dataset using the pandas library in Python.
- To create simple plots and charts with the matplotlib library for visualizing the data.

---

### Submission Requirements

Submit a Jupyter notebook (`.ipynb` file) or Python script (`.py` file) containing:
- Data loading and exploration steps.
- Basic data analysis results.
- Visualizations.
- Any findings or observations.

---

### Task 1: Load and Explore the Dataset

- Choose a dataset in CSV format (e.g., Iris dataset, a sales dataset, or any dataset of your choice).
- Load the dataset using pandas.
- Display the first few rows of the dataset using `.head()` to inspect the data.
- Explore the structure of the dataset by checking the data types and any missing values.
- Clean the dataset by either filling or dropping any missing values.

---

### Task 2: Basic Data Analysis

- Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using `.describe()`.
- Perform groupings on a categorical column (e.g., species, region, or department) and compute the mean of a numerical column for each group.
- Identify any patterns or interesting findings from your analysis.

---

### Task 3: Data Visualization

Create at least four different types of visualizations:
1. Line chart showing trends over time (e.g., a time-series of sales data).
2. Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species).
3. Histogram of a numerical column to understand its distribution.
4. Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).

Customize your plots with:
- Titles
- Labels for axes
- Legends (where necessary)

---

### Additional Instructions

#### Dataset Suggestions
- You can use publicly available datasets from sites like Kaggle or UCI Machine Learning Repository.
- The **Iris dataset** (a classic dataset for classification problems) can be accessed via `sklearn.datasets.load_iris()` for analysis.

#### Plot Customization
- Customize the plots using the matplotlib library to add titles, axis labels, and legends.
- Use **seaborn** for additional plotting styles, which can make your charts more visually appealing.

#### Error Handling
- Handle possible errors during the file reading (e.g., file not found), missing data, or incorrect data types by using exception-handling mechanisms (`try`, `except`).

#### Submission
- Ensure your submission is complete with all necessary code and explanations.
- Make sure that each plot is properly labeled and provides insights into the dataset.

---

### Dataset Used for This Assignment

** Demographic and Socioeconomic Data Sample**  

---

### Dataset Information

This synthetic dataset contains information on 100 randomly generated individuals representing a fictional population. The data is designed for exploratory data analysis (EDA), data visualization, and practice with data science tools and techniques. It includes both demographic and socioeconomic variables.

## Columns Overview

- **name**: Full name of the individual.  
- **age**: Age in years (ranging from 18 to 90).  
- **national id**: A unique 8-digit identifier simulating a national ID.  
- **sex**: Gender of the individual (Male/Female).  
- **occupation**: Job title or profession.  
- **residence**: Full residential address (synthetic).  
- **town**: The main town/city of residence.  
- **nationality**: National identity (e.g., Kenyan, Ugandan).  
- **disability status**: Indicates whether the person has a disability ("Yes"/"No").  
- **if disabled, specify**: Type of disability, if any (e.g., "Visual Impairment").  
- **salary**: Monthly salary (in local currency), ranging approximately between 20,000 and 300,000.  
- **number of kids**: Number of children (ranging from 0 to 6).

---

## Author

**Denis Macharia Ndiritu**  
[GitHub](https://github.com/seaSharkDenis) • [LinkedIn](https://www.linkedin.com/in/denis-ndiritu-15b6a5341/) • [Email](mailto:denisndiritu1@gmail.com)