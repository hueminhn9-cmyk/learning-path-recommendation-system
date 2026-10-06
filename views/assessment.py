import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from config import IS_VI, translate_subject_vi_to_en, render_kpi_card
from database import get_db, get_all_subjects
from models import load_models, interest_to_number

def assessment_page():
    model, model_type, scaler, level_map, model_metrics = load_models()

    st.markdown(f"""
    <div class="hero-banner">
        <span class="hero-badge">📝 AI Evaluation Module</span>
        <h1 style="margin:8px 0; font-size:2.2rem; font-weight:800;">{"Đánh giá Lộ trình Học tập bằng AI" if IS_VI() else "AI Student Learning Path Assessment"}</h1>
        <p style="font-size:1.05rem; opacity:0.9; margin:0;">Machine Learning Powered Level Prediction & Custom Subject Roadmaps</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="bw-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")
    all_subjects = get_all_subjects()
    custom_option = "✏️ " + ("Môn học khác (Tự nhập tên tùy chỉnh)..." if IS_VI() else "Custom Subject (Type new name)...")
    select_options = all_subjects + [custom_option]

    with col1:
        st.subheader("👤 " + ("Thông tin Sinh viên & Môn học" if IS_VI() else "Student & Subject Details"))
        student_name = st.text_input("Họ và Tên" if IS_VI() else "Full Name", value=st.session_state.user_name)
        
        selected_subject_choice = st.selectbox(
            "📘 " + ("Chọn môn học hoặc tự nhập môn mới:" if IS_VI() else "Select or Type Subject:"), 
            options=select_options,
            key="catalog_subj_select"
        )

        if selected_subject_choice == custom_option:
            subject = st.text_input(
                "✏️ " + ("Nhập tên môn học tùy chỉnh:" if IS_VI() else "Enter custom subject name:"), 
                placeholder="vd: Blockchain, Flutter, Golang, DevOps, Rust...",
                key="custom_subj_text_input"
            )
        else:
            subject = selected_subject_choice

    with col2:
        st.subheader("📊 " + ("Chỉ số Năng lực Học tập" if IS_VI() else "Performance Metrics"))
        marks = st.slider("Điểm số môn học (0 - 100)" if IS_VI() else "Academic Marks Obtained (0 - 100)", 0, 100, 75)
        interest = st.selectbox("Mức độ hứng thú" if IS_VI() else "Interest Level", ["Low", "Medium", "High"], index=2)
        time_spent = st.slider("Thời gian tự học (giờ/ngày)" if IS_VI() else "Daily Study Time (hours/day)", 0.5, 8.0, 3.5)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🤖 " + ("Tạo Lộ trình Học tập bằng AI" if IS_VI() else "Generate Learning Path Recommendation"), use_container_width=True):
        if not subject or not subject.strip():
            st.error("❌ Vui lòng nhập hoặc chọn tên môn học." if IS_VI() else "❌ Please select or enter a subject name.")
            return

        raw_subject = subject.strip()
        translated_subject = translate_subject_vi_to_en(raw_subject)

        if raw_subject.lower() != translated_subject.lower():
            st.info(f"🌐 AI Auto-Translation: **'{raw_subject}'** ➔ **'{translated_subject}'** (Mapped for English Video & Learning Resources)")

        subject = translated_subject

        input_data = np.array([[marks, interest_to_number(interest), time_spent]])
        if scaler is not None:
            input_scaled = scaler.transform(input_data)
        else:
            input_scaled = input_data

        if model_type == "keras" and model is not None:
            prediction = model.predict(input_scaled, verbose=0)
            predicted_class = int(np.argmax(prediction[0]))
            confidence = float(np.max(prediction[0]) * 100)
        elif model_type == "sklearn" and model is not None:
            proba = model.predict_proba(input_scaled)
            predicted_class = int(np.argmax(proba[0]))
            confidence = float(np.max(proba[0]) * 100)
        else:
            if marks <= 45:
                predicted_class = 0
            elif marks <= 75:
                predicted_class = 1
            else:
                predicted_class = 2
            confidence = 88.5

        level = level_map.get(predicted_class, "Beginner")

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO assessments (user_id, student_name, subject, marks, interest, time_spent, predicted_level, confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (st.session_state.user_id, student_name, subject, marks, interest, time_spent, level, confidence))
        
        cursor.execute("UPDATE users SET current_level = ? WHERE id = ?", (level, st.session_state.user_id))
        conn.commit()
        conn.close()

        st.session_state.latest_result = {
            "name": student_name,
            "subject": subject,
            "marks": marks,
            "interest": interest,
            "time_spent": time_spent,
            "level": level,
            "confidence": confidence
        }

        st.success(f"✅ AI Analysis Complete for subject: **{subject}**!")

    st.markdown('</div>', unsafe_allow_html=True)

    if "latest_result" in st.session_state:
        res = st.session_state.latest_result
        st.markdown('<div class="bw-card">', unsafe_allow_html=True)
        st.subheader("🎯 " + ("Kết quả Đánh giá AI & Lộ trình Học tập Đề xuất" if IS_VI() else "Assessment Results & Recommended Learning Path"))

        c1, c2, c3, c4 = st.columns(4, gap="medium")
        with c1:
            render_kpi_card("Sinh viên" if IS_VI() else "Student", res["name"], icon="👤")
        with c2:
            render_kpi_card("Môn học" if IS_VI() else "Subject", res["subject"], icon="📘")
        with c3:
            render_kpi_card("Trình độ AI" if IS_VI() else "Level", res["level"], icon="🎯")
        with c4:
            render_kpi_card("Độ tin cậy" if IS_VI() else "Confidence", f"{res['confidence']:.1f}%", icon="📊")

        st.progress(int(res["confidence"]) / 100)

        target_next_level = "Advanced Mastery" if res["level"] == "Advanced" else ("Intermediate" if res["level"] == "Beginner" else "Advanced")
        hours_needed = max(15, int((100 - res["marks"]) * 1.4))
        est_weeks = max(1.0, round(hours_needed / (res["time_spent"] * 7), 1))

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #e0e7ff 0%, #fae8ff 100%); border:1px solid #c7d2fe; border-radius:14px; padding:22px; margin:22px 0;">
            <h4 style="margin-top:0; color:#312e81;">⏱️ <b>Dự đoán AI về Thời gian Học tập (AI Time Estimator):</b></h4>
            <p style="color:#1e1b4b; font-size:1.05rem; margin:0;">Dựa trên thời gian học <b>{res['time_spent']} giờ/ngày</b> và điểm hiện tại <b>{res['marks']}/100</b>, AI tính toán bạn cần khoảng <b>{est_weeks} tuần</b> ({hours_needed} giờ học tổng cộng) để làm chủ hoàn toàn cấp độ <b>{target_next_level}</b> của môn <b>{res['subject']}</b>.</p>
        </div>
        """, unsafe_allow_html=True)

        col_radar, col_tips = st.columns([1, 1], gap="large")

        with col_radar:
            st.subheader("🕸️ " + ("Phân tích Năng lực Skill Radar" if IS_VI() else "Skill Radar Breakdown"))
            
            categories = ['Lý thuyết' if IS_VI() else 'Theory', 
                          'Thực hành Code' if IS_VI() else 'Coding', 
                          'Tư duy Thống kê' if IS_VI() else 'Statistics', 
                          'Giải quyết BTVN' if IS_VI() else 'Problem Solving', 
                          'Kiến trúc Hệ thống' if IS_VI() else 'System Design']
            
            m_factor = res["marks"] / 100.0
            t_factor = min(res["time_spent"] / 6.0, 1.0)
            
            values = [
                round(m_factor * 95, 1),
                round(m_factor * 90 + t_factor * 10, 1),
                round(m_factor * 85, 1),
                round(m_factor * 88 + t_factor * 12, 1),
                round(m_factor * 80 + t_factor * 15, 1)
            ]
            values += values[:1]
            angles = [n / float(len(categories)) * 2 * np.pi for n in range(len(categories))]
            angles += angles[:1]

            fig_radar, ax_r = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True), facecolor='#ffffff')
            ax_r.set_facecolor('#f8fafc')
            ax_r.plot(angles, values, color='#4f46e5', linewidth=2.5)
            ax_r.fill(angles, values, color='#6366f1', alpha=0.25)
            ax_r.set_xticks(angles[:-1])
            ax_r.set_xticklabels(categories, color='#1e293b', fontsize=10, fontweight='bold')
            ax_r.set_rlabel_position(0)
            plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="#64748b", size=8.5)
            plt.ylim(0, 100)
            st.pyplot(fig_radar)

        with col_tips:
            st.subheader("💡 " + ("Lời khuyên & Phân tích Điểm yếu từ AI" if IS_VI() else "AI Skill Gap Analysis & Next Steps"))
            tips = {
                "Beginner": [
                    f"📖 Nắm vững lý thuyết cơ bản, thuật ngữ và cú pháp cốt lõi của **{res['subject']}**.",
                    "🎥 Xem video bài giảng hướng dẫn nhập môn từ cơ bản.",
                    "✏️ Giải 3-5 bài tập thực hành nhỏ mỗi ngày."
                ],
                "Intermediate": [
                    f"🛠️ Thực hành xây dựng các Mini-Project thực tế cho **{res['subject']}**.",
                    "💡 Giải quyết các bài toán tối ưu và Case Study trung cấp.",
                    "🔍 Phân tích lỗi và cải thiện hiệu năng chương trình."
                ],
                "Advanced": [
                    f"🚀 Thiết kế Kiến trúc Hệ thống Production hoàn chỉnh cho **{res['subject']}**.",
                    "🔬 Nghiên cứu các tài liệu kỹ thuật nâng cao và thư viện Mã nguồn mở trên GitHub.",
                    "🎓 Đóng gói sản phẩm đưa vào Portfolio chuyên nghiệp."
                ]
            }
            for tip in tips.get(res["level"], []):
                st.write(f"• {tip}")

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses WHERE subject LIKE ? AND level = ?", (f"%{res['subject']}%", res["level"]))
        courses = cursor.fetchall()
        if len(courses) < 4:
            cursor.execute("SELECT * FROM courses WHERE level = ? LIMIT 6", (res["level"],))
            courses = cursor.fetchall()
        conn.close()

        st.markdown("---")
        st.subheader(f"🗺️ {'Sơ đồ Lộ trình Học tập Tích hợp Video & Web Link cho' if IS_VI() else 'Integrated Learning Roadmap with Video & Web Links for'} {res['subject']}")

        phases = [
            {"phase": "Giai đoạn 1 (Tuần 1-2)", "title": f"Nền tảng & Cú pháp cơ bản {res['subject']}", "desc": "Nắm vững lý thuyết cơ bản, thiết lập môi trường và chạy thử bài tập hello world."},
            {"phase": "Giai đoạn 2 (Tuần 3-4)", "title": f"Thực hành Kỹ năng & Thư viện {res['subject']}", "desc": "Thực hành sử dụng thư viện cốt lõi, viết hàm và xử lý dữ liệu thực tế."},
            {"phase": "Giai đoạn 3 (Tháng thứ 2)", "title": f"Tối ưu & Xây dựng Mini-Project {res['subject']}", "desc": "Giải quyết bài toán nâng cao, sửa lỗi Overfitting/Bottleneck và đóng gói module."},
            {"phase": "Giai đoạn 4 (Tháng thứ 3)", "title": f"Triển khai System Production {res['subject']}", "desc": "Đưa sản phẩm lên môi trường Cloud, container hóa Docker và hoàn thiện Portfolio."}
        ]

        for i, p in enumerate(phases):
            course_item = courses[i % len(courses)] if courses else None
            video_link = course_item['url'] if course_item else "https://www.youtube.com"
            course_title = course_item['title'] if course_item else f"Học {res['subject']} Toàn tập"
            
            st.markdown(f"""
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:14px; padding:20px; margin-bottom:16px;">
                <h4 style="margin-top:0; color:#1e1b4b; font-size:1.15rem;">📌 <b>{p['phase']}</b> - {p['title']}</h4>
                <p style="color:#475569; font-size:0.98rem;">{p['desc']}</p>
                <div style="margin-top:10px; padding: 14px; background-color:#f8fafc; border:1px solid #cbd5e1; border-radius:10px;">
                    <p style="margin:0; color:#0f172a;">🎬 <b>Video Bài giảng Đề xuất:</b> <a href="{video_link}" target="_blank" style="font-weight:bold; color:#4f46e5;">{course_title}</a></p>
                    <p style="margin:6px 0 0 0; color:#0f172a;">🌐 <b>Liên kết Học tập:</b> <a href="{video_link}" target="_blank" style="font-weight:bold; color:#4f46e5;">▶️ Click để Xem Video / Tài liệu Web Trực tiếp</a></p>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader(f"📚 {'Tất cả Video Bài giảng & Tài nguyên Khóa học' if IS_VI() else 'All Recommended Video Courses & Resources'}")
        if courses:
            for row_idx in range(0, min(len(courses), 6), 3):
                row_courses = courses[row_idx:row_idx+3]
                c_cols = st.columns(len(row_courses), gap="medium")
                for idx, c in enumerate(row_courses):
                    with c_cols[idx]:
                        st.markdown(f"""
                        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:14px; padding:20px; height:100%;">
                            <h4 style="margin-top:0; font-size:1.1rem;"><a href="{c['url']}" target="_blank" style="text-decoration:none; color:#1e1b4b;">🎬 {c['title']}</a></h4>
                            <p style="color:#64748b; font-size:0.875rem;">📌 <b>Level:</b> {c['level']} | <b>Subject:</b> {c['subject']}</p>
                            <p style="color:#334155; font-size:0.925rem;">{c['description']}</p>
                            <a href="{c['url']}" target="_blank" style="font-weight: bold; color: #4f46e5;">▶️ Mở Link Video / Khóa học</a>
                        </div>
                        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
