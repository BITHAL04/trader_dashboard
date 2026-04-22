📊 Trader Performance vs Market Sentiment Analysis

🧠 Overview  
This project analyzes how market sentiment (Fear vs Greed) influences trader behavior and performance. It combines sentiment data with simulated trading activity to evaluate profitability, risk-taking, and trading patterns.  
An interactive Streamlit dashboard is included for visualization.

---

🎯 Objectives  

• Data Preparation  
- Clean and preprocess datasets  
- Align data at daily level  
- Engineer key metrics: PnL, win rate, trade frequency, leverage, long/short ratio  

• Analysis  
- Compare performance across Fear vs Greed  
- Study behavioral changes (frequency, leverage, position size)  
- Segment traders (leverage, frequency, consistency)  

• Actionable Output  
- Design sentiment-based trading strategies  
- Optimize risk and trade execution  

---

📌 Key Insights  

- Greed periods → higher PnL but higher volatility  
- Fear periods → lower PnL but better win rate  
- High leverage → amplified gains and losses  
- Frequent trading → lower efficiency due to overtrading  

---

🛠 Tech Stack  

Python (Pandas, NumPy)  
Visualization: Plotly, Matplotlib, Seaborn  
Machine Learning: Scikit-learn  
Dashboard: Streamlit  

---

📁 Project Structure  

trader-dashboard/  
├── app.py  
├── processed_trader_data.csv  
├── daily_metrics.csv  
├── fear_greed_index.csv  
├── notebook.ipynb  
├── requirements.txt  
└── README.md  

---

⚙️ How to Run  

1. Clone the repository  
2. Install dependencies  
   pip install -r requirements.txt  
3. Run the app  
   streamlit run app.py  

---

📊 Dashboard Features  

- Sentiment filtering  
- KPI metrics (PnL, win rate, leverage)  
- Behavioral visualizations  
- Segment-wise analysis  
- Sentiment gauge  
- Cluster visualization  

---

🔬 Methodology  

- Sentiment encoded from Extreme Fear (0) to Extreme Greed (4)  
- Features engineered for PnL, leverage, and trade behavior  
- Random Forest used for profitability prediction  
- K-Means used for trader segmentation  

---

⚠️ Limitations  

- Uses simulated trading data  
- No transaction cost or slippage modeling  
- Simplified behavioral assumptions  

---

🚀 Future Improvements  

- Integrate real trading data  
- Add live sentiment APIs  
- Enhance predictive models  
- Deploy dashboard online  

---

👤 Author  
Bithal Mohanty
