# Monte_Carlo_NPV

## Overview
This financial analysis tool automates Net Present Value (NPV) calculations and risk assessments using Monte Carlo Simulations (MCS). Designed to fetch historical cash flow data and visualize potential outcomes, it aims to facilitate informed investment decisions. The project leverages advanced statistical techniques to improve financial decision-making, optimizing investment strategies through detailed risk assessments and real-time data analysis.

## Features
### Data Retrieval
- Automated extraction of historical cash flow data from Yahoo Finance ensures accuracy and timeliness in financial analysis.

### NPV Calculation
- Calculates the Net Present Value using variable discount rates to determine investment profitability.

### Monte Carlo Simulation
- Employs stochastic modeling to simulate a wide range of financial outcomes, enhancing the reliability of investment analyses.

### Enhanced Risk Analysis
- **Probability of Exceeding Threshold**: Determines the likelihood that NPV exceeds a set benchmark, offering insights into investment reliability.
- **Expected Loss**: Calculates the potential average loss if NPV falls below the threshold, crucial for assessing the financial risk and preparing for adverse outcomes.

### Visualizations
- Generates intuitive charts and histograms to illustrate potential financial scenarios and risk profiles, promoting clearer decision-making.
<p align="center">
 <img width="400" alt="Screenshot 2024-07-17 at 3 16 29 PM" src="https://github.com/user-attachments/assets/f5784f57-c17b-4fa8-a1ca-1fa62e7b385f">
 <img width="400" alt="Screenshot 2024-07-17 at 3 15 50 PM" src="https://github.com/user-attachments/assets/ef237613-1b4b-4c5f-9a82-11703bf17000">
</p>



## Technology Stack
- **Python**: For data handling and computation.
- **NumPy, Pandas**: Core libraries for numerical and data operations.
- **Matplotlib, Seaborn, Pool**: For creating informative and attractive visualizations.

## Enhanced Risk Analysis Details
### Concepts and Implementations
#### Probability of Exceeding Threshold
- **Concept**: Assesses the likelihood that NPV surpasses a predetermined value, reflecting the investment's potential to meet expected returns.
- **Implementation**: Post-simulation, the proportion of scenarios where NPV exceeds the threshold is computed, indicating the investment's risk level.

#### Expected Loss
- **Concept**: Averages losses where NPV is below the threshold, quantifying the downside risk.
- **Implementation**: Calculates mean loss from negative NPV outcomes, essential for understanding the financial stakes and preparing accordingly.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/leiassyun/Monte_Carlo_NPV.git
    cd Monte_Carlo_NPV
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required libraries**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:

    ```bash
    python app.py
    ```

## Usage
1. Run the application by executing `python app.py`.
2. Enter the company's ticker symbol when prompted.
3. View the calculated NPV and Monte Carlo simulation results.
4. Analyze the risk metrics provided by the tool for informed investment decisions.

## API Reference
- **Yahoo Finance API**: Utilized for fetching real-time and historical financial data.
  - [Yahoo Finance API Documentation](https://pypi.org/project/yfinance/)
