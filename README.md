# Federal Highway Accident Observatory

Data analysis project developed to explore accidents occurring on Brazilian federal highways using public data provided by the Brazilian Federal Highway Police (PRF).

The project aims to build a complete data workflow, from raw data collection and preparation to data analysis and dashboard development, integrating different tools commonly used in the Data field.

## Objective

Build an observatory of accidents on Brazilian federal highways using PRF data from **2024 and 2025**.

The analysis will explore topics such as:

- distribution of accidents over time;
- accident locations by state, municipality, and highway;
- main causes of accidents;
- accident types and classifications;
- number of injured people and fatalities;
- characteristics of the vehicles and people involved;
- road conditions, weather conditions, and time of day;
- differences between accidents recorded in 2024 and 2025.

The project also aims to develop a pipeline that integrates different tools commonly used in real-world data analysis projects.

---

##  Data Source

The data used in this project comes from the **Brazilian Federal Highway Police (PRF) Open Data**.

The datasets used contain accident records grouped by person, including all accident causes and types.

Files used:

```text
acidentes2024_todas_causas_tipos.csv
acidentes2025_todas_causas_tipos.csv
```

The original files are preserved without modifications in the project's raw data layer.

---

## Technologies

The project was designed to integrate different technologies throughout the data processing, storage, analysis, and visualization stages:

**Languages and Data Analysis**
- Python
- Pandas
- SQL

**Data Visualization and Business Intelligence**
- Power BI
- Tableau

**Additional Analysis**
- Excel
- Google Sheets

**Version Control**
- Git
- GitHub

---

## Project Pipeline

The planned project workflow is:

```text
PRF Open Data
       │
       ▼
CSV Files
       │
       ▼
Python + Pandas
       │
       ├── Validation
       ├── Cleaning
       ├── Processing
       └── Transformation
       │
       ▼
SQL Database
       │
       ▼
SQL Analysis
       │
       ├──────────────┬──────────────┐
       ▼              ▼              ▼
   Power BI        Tableau      Excel / Sheets
       │              │              │
       └──────────────┴──────────────┘
                      │
                      ▼
             Analysis & Insights
```

---

### `data/raw`

Contains the original files provided by the PRF.

The data in this directory is not modified, preserving the original source and ensuring the traceability of transformations performed throughout the project.

### `documentacao`

Contains supporting materials and documentation related to the datasets used in the project.

---

##  Data Preparation

The first stage of the project consists of analyzing the structure and quality of the data using **Python and Pandas**.

The checks performed include:

- number of records and columns;
- variable names;
- data types;
- null values;
- empty values;
- date and time standardization;
- conversion of numerical variables;
- validation of the 2024 and 2025 datasets.

Some variables require specific processing before the analysis.

Examples:

```text
data_inversa            → datetime
horario                 → datetime
km                      → decimal
br                      → integer
ano_fabricacao_veiculo  → integer
```

Missing values are preserved during the initial stage so they can be analyzed before defining any treatment strategy.

---

##  Project Stages

The project development is divided into the following stages:

- [x] Obtain official PRF data
- [x] Initial project organization
- [x] Load datasets using Pandas
- [x] Validate dataset structure
- [x] Analyze and adjust initial data types
- [x] Analyze missing values
- [x] Clean and standardize the data
- [x] Exploratory Data Analysis (EDA)
- [ ] SQL database modeling and data storage
- [ ] Data analysis using SQL
- [ ] Power BI dashboard development
- [ ] Tableau visualization development
- [ ] Additional analysis using Excel and Google Sheets
- [ ] Comparison between 2024 and 2025
- [ ] Documentation of key insights

---

##  Planned Analyses

After preparing the data, different aspects of the accidents recorded on Brazilian federal highways will be investigated.

The planned analyses include:

**Temporal Trends**

Analysis of the number of accidents by month, day of the week, and time.

**Geographic Distribution**

Identification of the states, municipalities, and highways with the highest concentration of accidents.

**Causes of Accidents**

Investigation of the most frequent causes and their relationship with accident severity.

**Severity**

Analysis of accidents considering uninjured people, minor injuries, serious injuries, and fatalities.

**Accident Conditions**

Evaluation of factors such as weather conditions, time of day, road type, and road layout.

**Vehicles and People Involved**

Exploration of the characteristics of the vehicles and people involved in the accidents.

**Annual Comparison**

Comparison of accident indicators between **2024 and 2025**, allowing variations and patterns between the two periods to be identified.

---

##  Dashboards

The results of the analyses will be used to develop dashboards and visualizations using:

- Power BI;
- Tableau;
- Excel;
- Google Sheets.

This section will be updated with dashboard images and links as the project progresses.

---

##  How to Run the Project

Clone the repository:

```bash
git clone <https://github.com/gomesmc/Federal-Highway-Accident-Observatory>
```

Navigate to the project directory:

```bash
cd observatorio_de_acidentes_nas_rodovias_2024_2025
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```
