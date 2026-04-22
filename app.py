import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components

# ===============================
# 🚀 CONFIG
# ===============================
st.set_page_config(layout="wide", page_title="Trader Intelligence Dashboard")

# ===============================
# 🌌 PARTICLE BACKGROUND
# ===============================
components.html("""
<div id="particles-js"></div>

<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>

<script>
particlesJS("particles-js", {
  "particles": {
    "number": { "value": 70 },
    "color": { "value": "#00f5d4" },
    "shape": { "type": "circle" },
    "opacity": { "value": 0.4 },
    "size": { "value": 3 },
    "line_linked": {
      "enable": true,
      "distance": 130,
      "color": "#00f5d4",
      "opacity": 0.3,
      "width": 1
    },
    "move": {
      "enable": true,
      "speed": 2
    }
  }
});
</script>

<style>
#particles-js {
  position: fixed;
  width: 100%;
  height: 100%;
  z-index: -1;
  top: 0;
  left: 0;
}
</style>
""", height=0)

# ===============================
# 🎨 DARK + GLASS UI
# ===============================
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #000000;
    color: white;
}

section[data-testid="stSidebar"] {
    background: rgba(20,20,20,0.95);
    border-right: 1px solid rgba(255,255,255,0.1);
}

.glass {
    background: rgba(255,255,255,0.05);
    border-radius: 15px;
    padding: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    transition: transform 0.3s;
}

.glass:hover {
    transform: scale(1.05);
}

.metric {
    font-size: 28px;
    font-weight: bold;
    color: #00f5d4;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #00f5d4;
}

.fade {
    animation: fadeIn 1.2s ease-in;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# ===============================
# 📂 LOAD DATA
# ===============================
@st.cache_data
def load_data():
    df = pd.read_csv("processed_trader_data.csv")
    daily = pd.read_csv("daily_metrics.csv")
    df["pnl_size"] = df["pnl"].abs() + 1
    return df, daily

df, daily = load_data()
# ===============================
# 🎛️ SIDEBAR (UPGRADED)
# ===============================
st.sidebar.markdown("## ⚙️ Control Panel")

st.sidebar.markdown("---")

sentiment_range = st.sidebar.slider(
    "📊 Sentiment Range",
    min_value=0,
    max_value=4,
    value=(0,4)
)

segment = st.sidebar.selectbox(
    "👥 Select Segment",
    ["leverage_group", "freq_group", "consistency_group"]
)

st.sidebar.markdown("---")

st.sidebar.markdown("### 📘 About")
st.sidebar.info(
    "This dashboard analyzes trader behavior using market sentiment data.\n\n"
    "Includes ML modeling, clustering, and performance insights."
)

filtered = df[(df['sentiment_score'] >= sentiment_range[0]) &
              (df['sentiment_score'] <= sentiment_range[1])]

# ===============================
# 📊 KPI CARDS
# ===============================
col1, col2, col3, col4 = st.columns(4)

def card(col, title, val):
    col.markdown(f"""
    <div class="glass fade">
        <h4>{title}</h4>
        <div class="metric">{val}</div>
    </div>
    """, unsafe_allow_html=True)

card(col1, "💰 Avg PnL", f"{filtered['pnl'].mean():.2f}")
card(col2, "📈 Win Rate", f"{filtered['win'].mean():.2f}")
card(col3, "⚡ Avg Leverage", f"{filtered['leverage'].mean():.2f}")
card(col4, "📊 Trades", len(filtered))

# ===============================
# ⚡ GAUGE
# ===============================
st.markdown("### ⚡ Market Sentiment")

avg_sentiment = filtered['sentiment_score'].mean()

fig_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=avg_sentiment,
    gauge={
        'axis': {'range': [0, 4]},
        'bar': {'color': "#00f5d4"},
        'steps': [
            {'range': [0, 1], 'color': "#ff4d4d"},
            {'range': [1, 2], 'color': "#ff944d"},
            {'range': [2, 3], 'color': "#ffd11a"},
            {'range': [3, 4], 'color': "#00ff99"}
        ]
    }
))

fig_gauge.update_layout(template="plotly_dark")
st.plotly_chart(fig_gauge, use_container_width=True)

# ===============================
# 📈 PnL DISTRIBUTION
# ===============================
st.markdown("### 📈 PnL Distribution")

fig1 = px.violin(
    filtered,
    x="sentiment_score",
    y="pnl",
    color="sentiment_score",
    template="plotly_dark"
)
st.plotly_chart(fig1, use_container_width=True)

# ===============================
# 🔥 SCATTER (FIXED)
# ===============================
st.markdown("### 🔥 Trader Behavior Map")

neon_colors = ["#00f5d4", "#ff00ff", "#00ff00", "#ffea00", "#ff4d4d"]

fig2 = px.scatter(
    filtered,
    x="leverage",
    y="trade_size",
    size="pnl_size",
    color="cluster",
    hover_data=['trader_id'],
    template="plotly_dark",
    color_discrete_sequence=neon_colors
)

fig2.update_traces(marker=dict(line=dict(width=1, color='white')))

st.plotly_chart(fig2, use_container_width=True)

# ===============================
# 📅 TREND
# ===============================
st.markdown("### 📅 Daily Trend")

fig3 = go.Figure()

fig3.add_trace(go.Scatter(
    x=daily['date'],
    y=daily['pnl'],
    mode='lines+markers',
    line=dict(color='#00f5d4', width=3)
))

fig3.update_layout(template="plotly_dark")

st.plotly_chart(fig3, use_container_width=True)

# ===============================
# 🎯 SEGMENT ANALYSIS
# ===============================
st.markdown("### 🎯 Segment Analysis")

fig4 = px.box(
    filtered,
    x=segment,
    y="pnl",
    color=segment,
    template="plotly_dark"
)

st.plotly_chart(fig4, use_container_width=True)

# ===============================
# 🧠 3D CLUSTERS
# ===============================
st.markdown("### 🧠 Trader Clusters")

fig5 = px.scatter_3d(
    filtered,
    x='leverage',
    y='trade_size',
    z='pnl',
    color='cluster',
    template="plotly_dark"
)

st.plotly_chart(fig5, use_container_width=True)

# ===============================
# ⚡ INSIGHTS
# ===============================
st.markdown("### ⚡ Key Insights")

st.markdown("""
<div class="glass fade">
<ul>
<li>🚀 Higher sentiment → higher leverage</li>
<li>⚠️ High leverage clusters → volatile PnL</li>
<li>📉 Fear = safer trades</li>
<li>📈 Greed = aggressive trading</li>
</ul>
</div>
""", unsafe_allow_html=True)