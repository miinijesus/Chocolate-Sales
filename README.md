# 🍫 Chocolate Sales Dashboard

An interactive dashboard built with **Python** to analyse and visualise chocolate sales data.
This project focuses on **data cleaning**, **data transformation**, and **interactive data visualisation** using modern Python tools.

---

## 📊 Dataset Source

The dataset used in this project was obtained from **Kaggle**, a widely used platform for open datasets and data science projects.

The data was downloaded locally and processed using **Pandas**.

---

## 🧹 Data Loading & Preparation

The data processing workflow includes the following steps:

### 1. Load the dataset

* The CSV file is loaded using `pandas.read_csv()`.

### 2. Date conversion

* The `Date` column is converted from string format to `datetime`.
* Additional time-based columns are created:

  * `Year`
  * `Month`
  * `Month_num`

### 3. Monetary value cleaning

* The `Amount` column originally contains currency symbols (`$`) and thousands separators.
* These characters are removed.
* The column is converted to `float` to allow numerical analysis and aggregation.

All data preparation logic is handled inside the `dataset.py` file to keep the project modular and maintainable.

---

## 🚀 Dashboard Features

* 📅 Sales analysis by year with interactive filtering
* 👤 Sales performance by seller
* 📦 Sales by product
* 🌍 Sales analysis by country
* 💰 Automatic formatting of large numbers
* 📊 Interactive charts with hover and zoom functionality
* ⚡ User-friendly interface built with Streamlit

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – data manipulation and cleaning
* **Streamlit** – dashboard development
* **Plotly** – interactive visualisations
* **Git & GitHub** – version control

---

## 📂 Project Structure

```
CHOCOLATE-SALES/
│
├── app.py               # Main Streamlit application
├── dataset.py           # Data loading and preprocessing
├── chart.py             # Chart creation functions
├── utils.py             # Helper and formatting functions
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── ChocolateSales.csv
│
└── tabs/
    ├── Overview.py
    ├── Countries.py
    ├── Products.py
    └── Seller.py
```

---

## ▶️ How to Run the Project

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎯 Project Purpose

This project was created to practise and demonstrate skills in:

* Data cleaning and transformation
* Exploratory data analysis
* Building interactive dashboards
* Writing clean, modular Python code
* Preparing portfolio-ready projects

---

## 👨‍💻 Author

Developed by **Vinicius Simoneli**
Python • Data Analysis • Interactive Dashboards
