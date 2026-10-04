import streamlit as st
import pandas as pd
from database import get_db

def admin_page():
    st.markdown("""
    <div class="hero-banner">
        <span class="hero-badge">🛡️ Administration Console</span>
        <h1 style="margin:8px 0; font-size:2.2rem; font-weight:800;">System Administration Console</h1>
        <p style="font-size:1.05rem; opacity:0.9; margin:0;">Manage students, dynamic subject courses, and view system statistics</p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.user_role != "admin":
        st.error("⛔ Access Denied. Administrator privileges required.")
        return

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'student'")
    student_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM assessments")
    assessment_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM courses")
    course_count = cursor.fetchone()[0]
    conn.close()

    c1, c2, c3 = st.columns(3)
    c1.metric("👥 Total Students", student_count)
    c2.metric("📝 Total Assessments", assessment_count)
    c3.metric("📚 Total Courses in Catalog", course_count)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="bw-card">', unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["👥 Student Directory", "➕ Add New Resource", "🗑️ Manage Catalog Courses"])

    with tab1:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, roll_number, email, interest, current_level, role FROM users")
        users_df = pd.DataFrame([dict(u) for u in cursor.fetchall()])
        conn.close()
        st.dataframe(users_df, use_container_width=True)

    with tab2:
        with st.form("add_course_form"):
            c_subj = st.text_input("Subject Name", value="Machine Learning")
            c_lvl = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])
            c_title = st.text_input("Course Title")
            c_url = st.text_input("Course URL / Video Link")
            c_desc = st.text_area("Course Description")

            if st.form_submit_button("✨ Save Resource to Database"):
                if c_title and c_url and c_subj:
                    conn = get_db()
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO courses (subject, level, title, url, description) VALUES (?, ?, ?, ?, ?)",
                                   (c_subj.strip(), c_lvl, c_title.strip(), c_url.strip(), c_desc.strip()))
                    conn.commit()
                    conn.close()
                    st.success(f"✅ Course '{c_title}' added successfully!")
                    st.rerun()

    with tab3:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses ORDER BY id DESC")
        courses_list = cursor.fetchall()
        conn.close()

        if courses_list:
            for course in courses_list:
                c_col1, c_col2 = st.columns([4, 1])
                with c_col1:
                    st.markdown(f"**{course['title']}** ({course['subject']} - {course['level']})")
                    st.caption(course['url'])
                with c_col2:
                    if st.button("🗑️ Delete", key=f"del_course_{course['id']}"):
                        conn = get_db()
                        cursor = conn.cursor()
                        cursor.execute("DELETE FROM courses WHERE id = ?", (course['id'],))
                        conn.commit()
                        conn.close()
                        st.success("✅ Course deleted!")
                        st.rerun()
                st.markdown("---")
        else:
            st.info("No courses currently in catalog.")
    st.markdown('</div>', unsafe_allow_html=True)
