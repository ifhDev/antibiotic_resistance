# Antibiotic Resistance Trends in Europe: Prototype Analysis

## Purpose

* **Goal:** Prototype a workflow for analyzing antibiotic resistance trends.
* **Scope:** Start with one bacterium and one antibiotic to ensure data and methods are viable before scaling up.

## Project Overview

This project explores resistance rates of *Escherichia coli* (E. coli) to fluoroquinolone antibiotics in Europe, using surveillance data from 2000–2018 (EARS-Net / ECDC).
The main objective is to establish a reproducible, modular data science workflow that can be expanded to other bacteria, antibiotics, or regions.

### What’s Included

* **Code & Data Handling**

  * Prototype Jupyter notebook (`prototype.ipynb`): Data exploration and initial visualizations.
  * Modular starter scripts (`main.py`, `dataset.py`): Structure for future development and scaling.
* **Figures**

  * `bar_resistance.png`: Bar plot of *E. coli* fluoroquinolone resistance across European countries in 2018.
  * `trends.png`: Line plot of resistance trends (2000–2018) for six representative European countries (SE, DE, FR, GR, PL, SI).
* **Documentation**

  * This README.

## **Column Descriptions**

* **Distribution**: Indicates whether the data is grouped by gender or by age group.
* **Unit**: The measurement unit (typically percentage, %).
* **Time**: The year in which the data was reported.
* **RegionCode**: Abbreviation/code for the reporting country.
* **RegionName**: Name of the country reporting the data.
* **Category**: The specific age group or gender category, as specified in the Distribution column.
* **Value**: Percentage of bacterial isolates found to be resistant to the specified antibiotic group.
* **Bacteria**: The bacterial species or group being monitored for resistance.
* **Antibiotic**: The class or group of antibiotics tested against the bacteria.

## Key Visualizations

* **Country Comparison (2018):**
  ![Bar plot of resistance rates by country](bar_resistance.png)
  *Shows wide variation in resistance rates across Europe, from <15% (Finland, Norway) to nearly 40% (Bulgaria).*

* **Trends Over Time (2000–2018):**
  ![Line plot of resistance trends for selected countries](trends.png)
  *Highlights regional differences and rising resistance in certain countries over the last two decades.*

## Methods Summary

* **Data filtering:** Focused on *E. coli* and fluoroquinolones only for this prototype.
* **Country selection:** Six countries chosen to represent a range of European regions and climates (Sweden, Germany, France, Greece, Poland, Slovenia).
* **Visualization:** Used pandas and matplotlib/seaborn for quick exploratory plots.

## Notes

* This is an early-stage prototype; many modules are placeholders for future development.
* Data files are ignored by git as per `.gitignore`.

---

**Next steps:** Expand analysis to more bacteria/antibiotic pairs, integrate basic statistical testing, and refactor notebook code into functions/modules.