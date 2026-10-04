import streamlit as st
from datetime import datetime
from config import IS_VI
from database import get_db

def timeline_page():
    st.markdown(f"""
    <div class="hero-banner">
        <span class="hero-badge">🗺️ Interactive Learning Schedule</span>
        <h1 style="margin:8px 0; font-size:2.2rem; font-weight:800;">{"Sơ đồ Lộ trình Học tập Trực quan (Roadmap Timeline)" if IS_VI() else "Interactive Learning Roadmap Timeline"}</h1>
        <p style="font-size:1.05rem; opacity:0.9; margin:0;">Step-by-step milestone schedule from Beginner to Advanced Mastery</p>
    </div>
    """, unsafe_allow_html=True)

    timeline_steps = [
        {"phase": "Giai đoạn 1: Tuần 1 - Tuần 2" if IS_VI() else "Phase 1: Week 1 - Week 2", "title": "Nền tảng & Cấu trúc Dữ liệu" if IS_VI() else "Foundations & Environment Setup", "desc": "Nắm vững lý thuyết cơ bản, cú pháp ngôn ngữ và thiết lập môi trường lập trình."},
        {"phase": "Giai đoạn 2: Tuần 3 - Tuần 4" if IS_VI() else "Phase 2: Week 3 - Week 4", "title": "Phân tích & Xử lý Dữ liệu (EDA)" if IS_VI() else "Data Preprocessing & EDA", "desc": "Thực hành làm sạch dữ liệu, biến đổi thuộc tính và vẽ biểu đồ trực quan hóa."},
        {"phase": "Giai đoạn 3: Tháng thứ 2" if IS_VI() else "Phase 3: Month 2", "title": "Huấn luyện Mô hình & Tối ưu" if IS_VI() else "Model Training & Evaluation", "desc": "Xây dựng thuật toán, đánh giá bằng Cross-Validation và tinh chỉnh tham số."},
        {"phase": "Giai đoạn 4: Tháng thứ 3" if IS_VI() else "Phase 4: Month 3", "title": "Xây dựng Dự án & Triển khai System" if IS_VI() else "Production Project & Deployment", "desc": "Đóng gói ứng dụng web, container hóa Docker và đưa lên môi trường Production."}
    ]

    for step in timeline_steps:
        st.markdown(f"""
        <div class="bw-card">
            <h4 style="margin-top:0; color:#312e81;">📌 {step['phase']} - {step['title']}</h4>
            <p style="color:#475569; margin:0;">{step['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

def export_roadmap_page():
    st.markdown('<div class="bw-card">', unsafe_allow_html=True)
    st.subheader("📄 " + ("Xuất Báo cáo & Chứng nhận Lộ trình Học tập" if IS_VI() else "Export Learning Path Report"))
    st.caption("Generate & download your personalized study certificate & learning roadmap")

    res = None
    if "latest_result" in st.session_state:
        res = st.session_state.latest_result
    else:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM assessments WHERE user_id = ? ORDER BY created_at DESC LIMIT 1", (st.session_state.user_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            res = {
                "name": row["student_name"],
                "subject": row["subject"],
                "marks": row["marks"],
                "interest": row["interest"],
                "time_spent": row["time_spent"],
                "level": row["predicted_level"],
                "confidence": row["confidence"] if row["confidence"] is not None else 85.0
            }

    if not res:
        st.warning("⚠️ Chưa có bài đánh giá nào. Hãy thực hiện Đánh giá AI trước!" if IS_VI() else "⚠️ No assessment history found. Please complete an AI Assessment first!")
        st.markdown('</div>', unsafe_allow_html=True)
        return

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_content = f"""# 🎓 STUDENT LEARNING PATH RECOMMENDATION REPORT
**Issued Date:** {now_str}  
**Student Name:** {res['name']}  
**Subject Analyzed:** {res['subject']}  

---

### 📊 EVALUATION SUMMARY
- **Academic Marks:** {res['marks']} / 100
- **Interest Level:** {res['interest']}
- **Daily Study Commitment:** {res['time_spent']} hours/day
- **AI Predicted Level:** **{res['level']}**
- **Model Confidence Score:** {res['confidence']:.1f}%

---

### 🎯 ACTIONABLE LEARNING MILESTONES & TIPS
1. **Foundation Phase:** Review foundational principles and core concepts of {res['subject']}.
2. **Implementation Phase:** Complete hands-on coding exercises and practical assignments.
3. **Specialization Phase:** Build real-world portfolio projects and analyze high-dimensional data.

---
*AI Student Learning Path Recommendation Platform*
"""

    st.code(report_content, language="markdown")

    st.download_button(
        label="📥 " + ("Tải Báo cáo Lộ trình (.md)" if IS_VI() else "Download Learning Path Report (.md)"),
        data=report_content,
        file_name=f"Learning_Path_Report_{res['name'].replace(' ', '_')}_{res['subject'].replace(' ', '_')}.md",
        mime="text/markdown",
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
