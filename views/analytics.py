import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from config import IS_VI
from database import get_db
from models import load_models

def progress_page():
    st.markdown(f"""
    <div class="hero-banner">
        <span class="hero-badge">📈 Historical Performance Dashboard</span>
        <h1 style="margin:8px 0; font-size:2.2rem; font-weight:800;">{"Bảng theo dõi Tiến độ & Thống kê" if IS_VI() else "Progress & Analytics Dashboard"}</h1>
        <p style="font-size:1.05rem; opacity:0.9; margin:0;">Track your learning evaluation history over time</p>
    </div>
    """, unsafe_allow_html=True)

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assessments WHERE user_id = ? ORDER BY created_at ASC", (st.session_state.user_id,))
    records = cursor.fetchall()
    conn.close()

    if not records:
        st.warning("⚠️ Chưa có dữ liệu đánh giá lịch sử nào." if IS_VI() else "⚠️ No historical data available yet. Please complete an assessment first.")
        return

    df = pd.DataFrame([dict(r) for r in records])

    st.markdown('<div class="bw-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("📊 " + ("Biến động Điểm số theo Thời gian" if IS_VI() else "Marks Progression Over Time"))
        fig, ax = plt.subplots(figsize=(6.5, 4), facecolor='#ffffff')
        ax.set_facecolor('#f8fafc')
        ax.plot(df['created_at'], df['marks'], marker='o', color='#4f46e5', linewidth=2.5)
        ax.tick_params(colors='#0f172a')
        ax.xaxis.label.set_color('#0f172a')
        ax.yaxis.label.set_color('#0f172a')
        ax.set_ylabel("Marks (0-100)", color='#0f172a', fontweight='bold')
        ax.set_ylim(0, 100)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)

    with col2:
        st.subheader("🎯 " + ("Phân bố Trình độ Học tập" if IS_VI() else "Learning Level Distribution"))
        level_counts = df['predicted_level'].value_counts()
        fig2, ax2 = plt.subplots(figsize=(6.5, 4), facecolor='#ffffff')
        ax2.set_facecolor('#f8fafc')
        pie_colors = ['#fca5a5', '#fcd34d', '#6ee7b7']
        ax2.pie(level_counts, labels=level_counts.index, autopct='%1.1f%%', colors=pie_colors, textprops={'color': '#0f172a', 'fontweight': 'bold'})
        plt.tight_layout()
        st.pyplot(fig2)

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📋 " + ("Nhật ký Đánh giá Chi tiết" if IS_VI() else "Complete Assessment Log"))
    st.dataframe(df[["id", "subject", "marks", "interest", "time_spent", "predicted_level", "confidence", "created_at"]], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def ai_analytics_page():
    model, model_type, scaler, level_map, model_metrics = load_models()

    st.markdown(f"""
    <div class="hero-banner">
        <span class="hero-badge">📊 Machine Learning Benchmarking</span>
        <h1 style="margin:8px 0; font-size:2.2rem; font-weight:800;">{"Phân tích & So sánh Mô hình AI / Machine Learning" if IS_VI() else "AI / ML Model Analytics & Benchmarking"}</h1>
        <p style="font-size:1.05rem; opacity:0.9; margin:0;">Neural Network (ANN), Random Forest, Decision Tree, Support Vector Machine (SVM)</p>
    </div>
    """, unsafe_allow_html=True)

    if not model_metrics:
        st.warning("⚠️ No model evaluation metrics found. Please run train_model.py first!")
        return

    df_metrics = pd.DataFrame(model_metrics)
    best_model = df_metrics.loc[df_metrics['accuracy'].idxmax()]

    model_names = [m['model'].replace("Classifier", "").replace("Artificial Neural Network ", "").strip() for m in model_metrics]
    best_name = best_model['model'].replace("Classifier", "").replace("Artificial Neural Network ", "").strip()

    c1, c2, c3, c4 = st.columns(4, gap="medium")
    c1.metric("🥇 Best Performing Model", best_name)
    c2.metric("🎯 Top Accuracy Score", f"{best_model['accuracy']:.1f}%")
    c3.metric("⭐ Weighted F1-Score", f"{best_model['f1_score']:.1f}%")
    c4.metric("⚙️ Total Trained Models", len(df_metrics))

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="bw-card">', unsafe_allow_html=True)

    st.subheader("📋 " + ("Bảng So sánh Chỉ số Mô hình Machine Learning" if IS_VI() else "Machine Learning Models Comparative Metrics Table"))
    st.dataframe(df_metrics[["model", "accuracy", "precision", "recall", "f1_score"]], use_container_width=True)

    st.subheader("📈 " + ("Biểu đồ So sánh Độ chính xác & F1-Score" if IS_VI() else "Accuracy & F1-Score Comparison Chart"))
    fig_bm, ax_bm = plt.subplots(figsize=(8.5, 4.2), facecolor='#ffffff')
    ax_bm.set_facecolor('#f8fafc')
    
    x = np.arange(len(df_metrics))
    width = 0.35
    
    rects1 = ax_bm.bar(x - width/2, df_metrics['accuracy'], width, label='Accuracy (%)', color='#4f46e5')
    rects2 = ax_bm.bar(x + width/2, df_metrics['f1_score'], width, label='F1-Score (%)', color='#a855f7')
    
    ax_bm.set_ylabel('Percentage (%)', color='#0f172a', fontweight='bold')
    ax_bm.set_xticks(x)
    ax_bm.set_xticklabels(model_names, color='#0f172a', fontweight='bold')
    ax_bm.tick_params(colors='#0f172a')
    ax_bm.set_ylim(0, 110)
    ax_bm.legend(facecolor='#ffffff', edgecolor='#cbd5e1', labelcolor='#0f172a')
    plt.tight_layout()
    st.pyplot(fig_bm)
    st.markdown('</div>', unsafe_allow_html=True)
