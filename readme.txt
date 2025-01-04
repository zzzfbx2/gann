Gann Levels Calculator

The Gann Levels Calculator is a powerful tool designed to help traders and investors analyze Gann levels for any stock ticker. By visualizing these levels, users can better understand price action and make informed trading decisions. This app is implemented in two versions: Streamlit (Python) and SwiftUI (iOS).

Features

Core Functionalities:

Input Ticker and Timeframe:

Users can input a stock ticker (e.g., AAPL, TSLA) and select a timeframe (e.g., 6 months, 1 year).

Custom timeframes are also supported.

Calculate Gann Levels:

Automatically calculates the key Gann levels: 0%, 25%, 50%, 75%, and 100%.

Displays price levels on the chart for better interpretation.

Interactive Chart:

Visualize historical stock prices along with Gann levels.

Zoom, pan, and hover over the chart for detailed analysis (in the Python version).

Download Chart:

Download the chart as a PNG file for offline reference.

Additional Features:

Light and Dark Mode Support: Switch between themes for a comfortable viewing experience.

Real-Time Price Updates (Future Integration): Enable live price tracking for intraday traders.

Error Handling: Provides actionable feedback for invalid inputs.

How It Works

Gann Levels Calculation:

Identify the highest and lowest price points in the selected timeframe.

Calculate intermediate levels based on the Gann percentage ratios:

0%: Lowest price

25%: Low + 25% of the price range

50%: Midpoint of the range

75%: Low + 75% of the price range

100%: Highest price

Supported Platforms:

Python (Streamlit):

Uses Yahoo Finance for fetching historical data.

Visualizes data with Plotly for an interactive experience.

SwiftUI (iOS):

Implements a native app for iPhones using the Charts framework.

Installation and Usage

For Streamlit (Python):

Prerequisites:

Install Python 3.8 or above.

Install required libraries:

pip install streamlit yfinance plotly

Run the App:

streamlit run app.py

Open in Browser:

The app will launch in your default browser at http://localhost:8501.

For SwiftUI (iOS):

Requirements:

Install Xcode (latest version).

Clone the project to your local machine.

Run on Simulator:

Open the project in Xcode.

Select an iPhone simulator and run the app.

Usage Guide

Input Stock Ticker:

Enter the stock symbol (e.g., AAPL for Apple) in the input field.

Select Timeframe:

Choose a predefined timeframe (e.g., 1 month, 6 months) or enter a custom timeframe.

Analyze the Chart:

View historical prices along with the Gann levels displayed as horizontal lines.

Use the interactive features (zoom, pan, hover) in the Python version for detailed insights.

Download Chart:

Click the "Download Chart as PNG" button to save the chart.

Future Enhancements

Real-Time Data Updates:

Enable live updates for intraday trading.

Custom Gann Levels:

Allow users to define their own percentage levels.

Volume Overlay:

Add volume data as a secondary chart for deeper analysis.

Alerts:

Notify users when prices cross specific Gann levels.

Contributing

We welcome contributions to improve the Gann Levels Calculator. Please feel free to fork the repository and submit a pull request for any features or fixes.

License

This project is licensed under the MIT License. Feel free to use and modify the code for personal or commercial purposes.

Contact

For questions or suggestions, please contact:

Raj: [Email/Contact Info]

Made with ❤️ by Raj

