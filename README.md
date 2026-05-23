# ShadowFox
# ShadowFox Python Development Internship Tasks 🚀

This repository contains all the tasks completed during the ShadowFox Python Development Internship.

## 👩‍💻 Intern Details
- Name: Velidindi Mounika
- Internship Domain: Python Development
- Organization: ShadowFox

# 📂 Repository Structure

> Beginner Level Tasks
1. Variables:
     * Topics Covered:
          Variables,
          Data Types,
          Keywords,
          Simple Interest Calculation.
     * Programs:
          Store value of pi,
          Check datatype,
          Keyword error example,
          Calculate simple interest.
2. Numbers:
     * Topics Covered:
          Number formatting,
          Area calculation,
          Speed calculation.
     * Programs:
          Octal representation,
          Area of pond,
          Water quantity calculation,
          Speed in meters/second.
3. List:
     * Topics Covered:
          List operations,
          Insert,
          Append,
          Remove,
          Sort.
     * Programs:
          Justice League operations,
          Add members,
          Rearrange members,
          Sort list alphabetically.
4. If Condition:
      * Topics Covered:
          Conditional statements,
          BMI Calculator,
          Country finder using cities.
      * Programs:
          BMI Category checker,
          City to country finder,
          Same country checker.
5. For Loop:
      * Topics Covered:
          Loops,
          Random module,
          Counters,
          Conditions inside loops.
      * Programs:
          Dice rolling simulator,
          Jumping jacks workout tracker.
🛠 Technologies Used:
      Python,
      VS Code,
      GitHub.

> Intermediate Level Tasks
>  🌟 ShadowFox Internship – Intermediate Level Projects 🦊✨

This repository contains my Intermediate Level internship projects completed as part of the ShadowFox Internship Program. These projects helped me improve my Python programming, problem-solving, and automation skills. 🚀

# 🌐 Project 1: Web Scraper using Python 🕸️🐍

## 📌 Description
This project is a simple Web Scraper developed using Python. It extracts data from a website automatically and stores the collected information into a CSV file.

The project demonstrates:
- 🌐 Web Scraping
- 🏗️ HTML Parsing
- 📥 Data Extraction
- 📄 CSV File Handling

## 🛠️ Technologies Used
- Python 🐍
- Requests Library 🌍
- BeautifulSoup 🥣
- CSV Module 📄

## 📂 Files Included
- `webscraper.py` 💻
- `scraped_data.csv` 📊
- `README.md` 📝

## ▶️ How to Run the Project

### 1️⃣ Install Required Libraries
```bash
pip install requests beautifulsoup4

# 🎮 Project 2 : Hangman game using python 🐍*

## 📌 Description
This project is a simple Hangman Game developed using Python. The player has to guess the hidden word letter by letter before all attempts are completed.

The project demonstrates:
- 🔁 Loops
- ⚡ Conditional Statements
- 📋 Lists
- 🔤 String Handling
- 🎮 Game Logic Development

## 🛠️ Technologies Used
- Python 🐍

## 📂 Files Included
- `hangman.py` 💻
- `README.md` 📝

## ▶️ How to Run the Project

### 1️⃣ Open Terminal
Navigate to the project folder.

### 2️⃣ Run the Python File
```bash
python hangman.py


** Advanced Cricket Fielding Analysis using IPL Sample Data**

## 🏏 Advanced Cricket Fielding Analysis - IPL

### Overview
This project performs advanced-level analysis of fielding performance in IPL matches using Python. It evaluates players on metrics like runs saved, catch efficiency, run-out impact, and pressure situations to generate a comprehensive fielding impact score.

### 📊 Features
- *Fielding Metrics Calculated*:
    1. *Runs Saved/Conceded*: Based on fielding position, distance covered, ball speed
    2. *Catch Efficiency*: $CE = \frac{Catches\ Taken}{Catch\ Opportunities} \times Difficulty\ Weight$
    3. *Run-Out Impact*: Direct hits, assists, and opportunities missed
    4. *Pressure Index*: Performance in death overs, close matches, playoffs
    5. *Fielding Impact Score*: Weighted composite of all metrics

- *Visualizations*:
    - Heatmaps of fielder positions and success rates
    - Player-wise fielding rankings
    - Team fielding comparison
    - Over-by-over runs saved trends

### 📁 Dataset
Uses sample IPL ball-by-ball data with fielding columns:
| Match_ID | Innings | Over | Ball | Fielder | Action | Outcome | Distance_Covered | Ball_Speed | Catch_Difficulty | Match_Situation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_01 | 1 | 5.2 | Jadeja | Stop | Run_Saved | 12m | 85kmph | NA | Powerplay |
| 2024_01 | 2 | 18.5 | Kohli | Catch | Out | 22m | 110kmph | High | Death_Overs |
Sample data included: `ipl_fielding_sample_2023_2024.csv`

### ⚙️ Tech Stack
- *Language*: Python 3.10+
- *Libraries*: Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-learn
- *Data*: Sample IPL 2023-2024 fielding data

### 🧠 Code Explanation

*1. Data Preprocessing - `preprocess.py`*
# Clean and engineer features
df['Difficulty_Score'] = df['Distance_Covered'] * df['Ball_Speed'] * df['Catch_Difficulty']
df['Pressure_Weight'] = df['Match_Situation'].map({'Death_Overs': 1.5, 'Powerplay': 1.2, 'Middle': 1.0})
Handles missing values, creates difficulty weights based on physics of fielding.

*2. Metrics Engine - `metrics.py`*
def calculate_runs_saved(row):
    expected_runs = model.predict([[row['Distance'], row['Ball_Speed']]])
    actual_runs = row['Runs_Conceded']
    return expected_runs - actual_runs

def fielding_impact_score(player_df):
    return 0.4*Runs_Saved + 0.3*Catch_Efficiency + 0.2*Runout_Points + 0.1*Pressure_Index
Uses a regression model to find expected runs vs actual runs saved by each fielder.

*3. Visualization - `plots.py`*
Generates interactive Plotly heatmaps showing best fielding zones for each player and team comparisons.

*4. Main Analysis - `main.py`*
Runs the full pipeline: load → preprocess → calculate metrics → rank players → export results + plots.

### 🚀 How to Run
1. Clone repo: `git clone <repo-url>`
2. Install deps: `pip install -r requirements.txt`
3. Run analysis: `python main.py --season 2024`
4. View results: Check `/output` for CSV rankings and `/plots` for visualizations

### 📈 Sample Output
Player | Runs_Saved | Catch_Eff | Runout_Points | Impact_Score | Rank
Jadeja | 28.5 | 0.92 | 12 | 94.3 | 1
Kohli | 15.2 | 0.88 | 8 | 82.1 | 2

### 🔮 Future Scope
1. Add computer vision to track player movement from video
2. Integrate player fatigue and ground conditions
3. Real-time fielding impact during live matches
