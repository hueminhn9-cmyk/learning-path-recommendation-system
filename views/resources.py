import streamlit as st
from config import IS_VI
from database import get_db

def resources_page():
    st.markdown(f"""
    <div class="hero-banner">
        <span class="hero-badge">📚 Educational Content Catalog</span>
        <h1 style="margin:8px 0; font-size:2.2rem; font-weight:800;">{"Thư viện Tài nguyên Học tập" if IS_VI() else "Learning Resources Library"}</h1>
        <p style="font-size:1.05rem; opacity:0.9; margin:0;">Explore & search curated educational courses, tutorials, and documentation</p>
    </div>
    """, unsafe_allow_html=True)

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses ORDER BY subject, level")
    all_courses = cursor.fetchall()
    conn.close()

    all_subjects = sorted(list(set([c["subject"] for c in all_courses])))

    st.markdown('<div class="bw-card">', unsafe_allow_html=True)
    search_query = st.text_input("🔍 " + ("Tìm kiếm Khóa học theo Từ khóa:" if IS_VI() else "Search Courses by Keyword:"), placeholder="e.g. Python, Machine Learning, Web, Security, Cloud, SQL, Docker...")

    col1, col2 = st.columns(2, gap="large")
    with col1:
        selected_subj = st.selectbox("Lọc theo Môn học" if IS_VI() else "Filter by Subject", ["All Subjects"] + all_subjects)
    with col2:
        selected_lvl = st.selectbox("Lọc theo Trình độ" if IS_VI() else "Filter by Level", ["All Levels", "Beginner", "Intermediate", "Advanced"])

    filtered = []
    for c in all_courses:
        match_subj = (selected_subj == "All Subjects" or c["subject"] == selected_subj)
        match_lvl = (selected_lvl == "All Levels" or c["level"] == selected_lvl)
        
        match_query = True
        if search_query and search_query.strip():
            q = search_query.strip().lower()
            match_query = (q in c["title"].lower() or q in c["subject"].lower() or q in c["description"].lower() or q in c["level"].lower())
            
        if match_subj and match_lvl and match_query:
            filtered.append(c)

    st.markdown("---")
    st.write(f"{'Hiển thị' if IS_VI() else 'Showing'} **{len(filtered)}** {'tài nguyên học tập:' if IS_VI() else 'learning resources:'}")

    if filtered:
        for c in filtered:
            st.markdown(f"""
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:14px; padding:22px; margin-bottom:18px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);">
                <h3 style="margin-top:0; font-size:1.25rem;"><a href="{c['url']}" target="_blank" style="text-decoration:none; color:#312e81;">🔗 {c['title']}</a></h3>
                <p style="color:#64748b; font-size:0.925rem;">📌 Subject: <b>{c['subject']}</b> | Level: <b>{c['level']}</b></p>
                <p style="color:#334155; font-size:0.975rem;">{c['description']}</p>
                <a href="{c['url']}" target="_blank" style="display:inline-block; background:linear-gradient(135deg, #4f46e5, #6366f1); color:#ffffff; padding:10px 20px; border-radius:10px; font-weight:700; text-decoration:none;">▶️ Access Learning Material Link</a>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
