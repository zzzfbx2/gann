import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from io import BytesIO

# App title
st.markdown("<h1 style='color: green; font-weight: bold;'>📈 Gann Levels Calculator</h1>", unsafe_allow_html=True)

# App description
st.markdown("<p style='font-family: Arial, sans-serif; font-size: 16px;'>Use this app to calculate and visualize Gann levels for any stock ticker. Simply enter the stock ticker and a custom timeframe (e.g., 6 months, 1 year), and the app will generate a chart displaying key Gann levels along with the stock's historical price data.</p>", unsafe_allow_html=True)

# Input section
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL or MSFT):", value="AAPL")
timeframe_options = ["1mo", "3mo", "6mo", "1y", "2y"]
timeframe = st.selectbox("Select a Timeframe:", options=timeframe_options, index=2)
custom_timeframe = st.text_input("Or enter a custom timeframe (e.g., 6mo, 1y, 2y):")

# Use custom timeframe if provided, otherwise use dropdown selection
timeframe = custom_timeframe if custom_timeframe else timeframe

if st.button("Get Gann Levels"):
    try:
        # Fetch data
        stock = yf.Ticker(ticker)
        history = stock.history(period=timeframe)

        if history.empty:
            st.error("No data found for the given ticker!")
        else:
            # Calculate Gann Levels
            high_price = history['High'].max()
            low_price = history['Low'].min()

            gann_levels = [
                low_price,
                low_price + (high_price - low_price) * 0.25,
                low_price + (high_price - low_price) * 0.5,
                low_price + (high_price - low_price) * 0.75,
                high_price,
            ]

            # Plot data
            st.markdown("<h2 style='color: green; font-weight: bold;'>Stock Price Chart with Gann Levels</h2>", unsafe_allow_html=True)

            # Create Plotly chart
            fig = go.Figure()

            # Add close price line
            fig.add_trace(go.Scatter(
                x=history.index,
                y=history['Close'],
                mode='lines',
                name='Close Prices',
                line=dict(color='blue')
            ))

            # Add Gann levels
            colors = ["red", "green", "purple", "orange", "cyan"]
            labels = ["0%", "25%", "50%", "75%", "100%"]
            for value, color, label in zip(gann_levels, colors, labels):
                fig.add_hline(
                    y=value,
                    line_dash="dash",
                    annotation_text=f"{value:.2f}",
                    annotation_position="right",
                    line_color=color
                )

            # Customize layout
            fig.update_layout(
                title=f"{ticker} Close Prices and Gann Levels",
                xaxis_title="Date",
                yaxis_title="Price",
                template="plotly_white",
                font=dict(color="green", size=14),
                margin=dict(r=100)  # Add extra margin on the right
            )

            # Display chart
            st.plotly_chart(fig)

            # Option to download chart as image
            buf = BytesIO()
            fig.write_image(buf, format="png")
            buf.seek(0)
            st.download_button(
                label="Download Chart as PNG",
                data=buf,
                file_name=f"{ticker}_gann_levels.png",
                mime="image/png",
            )

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("<div style='text-align: center; margin-top: 20px;'>Made with ❤️ by Raj</div>", unsafe_allow_html=True)
