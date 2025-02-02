# Personalized Quiz Performance Analyzer

## Overview

The **Personalized Quiz Performance Analyzer** is a Python-based tool designed to analyze student quiz performance and provide personalized recommendations for improvement. It processes both current and historical quiz data to generate insights into a student's performance, test-taking strategies, and areas for improvement.

### Key Features:
- **Performance Analysis**: Analyzes accuracy, speed, final score, and other metrics for the current quiz.
- **Historical Trends**: Tracks performance over time using historical quiz data.
- **Personalized Recommendations**: Provides actionable recommendations based on the student's performance.
- **Exploratory Data Analysis (EDA)**: Visualizes trends, correlations, and topic-wise performance.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/riddhima29/personalized_quiz_performance_analyzer.git
   cd personalized_quiz_performance_analyzer

2. **Install Dependencies**:
Install the required Python packages using requirements.txt:
    ```bash
    pip install -r requirements.txt

3. **Install the Package:**:
Install the package locally using setup.py:
    ```bash
    pip install .

# Usage

**Command-Line Interface**
The tool can be run from the command line using the following syntax:
    ```bash
    python quiz_performance_analyser.py --current <current_quiz.json> --historical <historical_quizzes.json>

## Output
The tool will generate the following outputs:
1. **Performance Analysis**: Detailed metrics for the current quiz.
2. **Test Strategy Analysis**: Insights into the student's test-taking strategy.
3. **Personalized Recommendations**: Actionable recommendations for improvement.
4. **Student Persona**: A summary of the student's performance level and learning potential.

# Project Approach
## Data Processing
1. **Current Quiz Data**:
- The tool processes the current quiz data to calculate metrics such as accuracy, speed, final score, and negative marking impact.
- It also extracts the quiz topic and analyzes the student's rank and percentile.

2. **Historical Quiz Data**:
- The historical quiz data is filtered to include only records for the current user.
- Key metrics (accuracy, speed, final score, etc.) are extracted and analyzed to identify trends over time.

## Analysis
1. **Performance Analysis**:
- The tool calculates metrics such as time per question, attempt rate, and score rate to evaluate the student's performance.

2. **Test Strategy Analysis**:
- It analyzes the student's test-taking strategy, including time management, accuracy, and attempt patterns.

3. **Personalized Recommendations**:
- Based on the analysis, the tool generates recommendations to improve accuracy, speed, and overall performance.

4. **Exploratory Data Analysis (EDA)**:
- The tool visualizes historical trends, correlations, and topic-wise performance using plots and charts.

## Visualization
- **Line Plots**: For accuracy trends and negative marking impact over time.
- **Histograms**: For the distribution of final scores.
- **Heatmaps**: For correlations between key metrics.
- **Bar Charts**: For topic-wise performance.

# Example Data
**Current Quiz Data (SubmissionData.json)**
```javascript
{
  "user_id": "YcDFSO4ZukTJnnFMgRNVwZTE4j42",
  "started_at": "2025-01-17T15:18:30.000+05:30",
  "ended_at": "2025-01-17T15:30:15.000+05:30",
  "accuracy": "90 %",
  "speed": "100",
  "score": 108,
  "final_score": "105.0",
  "negative_score": "3.0",
  "correct_answers": 27,
  "incorrect_answers": 3,
  "total_questions": 100,
  "quiz": {
    "topic": "Body Fluids and Circulation",
    "correct_answer_marks": "4.0",
    "negative_marks": "1.0"
  },
  "mistakes_corrected": 9,
  "initial_mistake_count": 12,
  "response_map": {
    "2523": 10109,
    "2529": 10130
  },
  "rank_text": "Topic Rank - #-171",
  "better_than": 107,
  "trophy_level": 2
}
```
**Historical Quiz Data (HistoricalQuizeData.json)**
```javascript
[
  {
    "user_id": "YcDFSO4ZukTJnnFMgRNVwZTE4j42",
    "accuracy": "85 %",
    "speed": "95",
    "final_score": "90.0",
    "negative_score": "2.0",
    "score": 92,
    "quiz": {
      "topic": "Body Fluids and Circulation",
      "correct_answer_marks": "4.0",
      "negative_marks": "1.0"
    }
  },
  {
    "user_id": "YcDFSO4ZukTJnnFMgRNVwZTE4j42",
    "accuracy": "88 %",
    "speed": "98",
    "final_score": "95.0",
    "negative_score": "1.0",
    "score": 96,
    "quiz": {
      "topic": "Body Fluids and Circulation",
      "correct_answer_marks": "4.0",
      "negative_marks": "1.0"
    }
  }
]
```
