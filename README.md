# ForestLens India

A Streamlit-based analytics dashboard for exploring forest cover change, tree cover loss, and carbon emissions across India from 2001–2020.

ForestLens India helps translate large-scale environmental datasets into clear visual insights for policymakers, researchers, and decision-makers who want to understand deforestation patterns and identify vulnerable regions.

## Overview

This project analyzes forest-related data across multiple geographic levels:

- Country-level trends
- State-wise comparisons
- District-level hotspots
- Yearly forest loss progression
- AI-based prediction of future deforestation patterns

The dashboard is designed to make complex environmental data easier to interpret through interactive charts, maps, and summary insights.

## Key Features

- Interactive India-wide forest loss dashboard
- State-wise comparison and ranking
- Trend analysis across multiple years
- District-level exploration for localized hotspots
- AI/ML-based forecasting of forest loss patterns
- Clean, research-friendly data preprocessing pipeline
- Responsive Streamlit UI for quick exploration

## Project Structure

```text
Forestlens-india/
├── .streamlit/
│   └── config.toml
├── data/
│   ├── raw/
│   └── processed/
├── pages/
│   ├── 1_India_Overview.py
│   ├── 2_State_wise_Analysis.py
│   ├── 3_Trend_Analysis.py
│   ├── 4_AI_Prediction.py
│   ├── 5_Insights.py
│   └── 6_District_Explorer.py
├── deforestation-dashboard/
├── Project_Overview.py
├── preprocess.py
├── requirements.txt
├── theme.py
├── .gitignore
└── README.md
```

## Dashboard Pages

1. India Overview
   - Overall forest cover and loss across the country
2. State-wise Analysis
   - Comparison of states by forest loss and carbon impact
3. Trend Analysis
   - Temporal changes in forest loss over the years
4. AI Prediction
   - ML-based prediction and comparison with actual values
5. Insights
   - High-impact states, years, and key findings
6. District Explorer
   - Detailed examination of district-level forest loss hotspots

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- scikit-learn
- Excel-based environmental datasets

## Data Sources

This project uses forest and carbon data aligned with Global Forest Watch (GFW) and University of Maryland datasets, including:

- Tree cover loss
- Forest extent
- Carbon emissions data
- Geographic breakdowns by country, state, and district

## Data Processing Workflow

The repository includes a preprocessing script, `preprocess.py`, which:

- Reads raw Excel datasets
- Filters for the standard canopy threshold (30%)
- Reshapes long-form time series data
- Saves processed CSV files under `data/processed/`

This makes the dashboard faster and easier to analyze by converting raw tabular data into cleaner, structured formats.

## Installation

### Prerequisites

- Python 3.9+
- pip
- Virtual environment (recommended)

### Setup

```bash
git clone https://github.com/DhananiParita/Forestlens-india.git
cd Forestlens-india
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the App

From the project root, start the dashboard with:

```bash
streamlit run Project_Overview.py
```

This launches the project overview page and provides access to the multi-page dashboard experience.

## Usage

After launching the app:

- Open the sidebar navigation to move between pages
- Select regions, years, or metrics of interest
- Review the interactive visualizations and summaries
- Use the AI prediction page to compare observed versus forecasted patterns

## Project Goals

The main objective of ForestLens India is to:

- highlight patterns of deforestation and forest loss
- make forest-change analysis more accessible
- support environmental monitoring with data-driven insight
- provide a clear framework for examining India's changing forest landscape

## Future Enhancements

Potential areas for future improvement include:

- integration of more recent forest datasets
- geospatial mapping with interactive India map overlays
- exportable reports and CSV downloads
- improved model validation and forecasting accuracy
- public deployment for wider stakeholder access

## Contributing

Contributions are welcome. If you'd like to enhance the dashboard, improve visualizations, or expand the analysis:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request with a clear summary of the update

## Contact

For questions, collaborations, or project discussions, please connect through the repository owner or project maintainer on GitHub.

## Note

This project is actively oriented around environmental analytics and data storytelling. It is best suited for local exploration and research use cases, and is designed as a practical dashboard for understanding deforestation patterns in India.
