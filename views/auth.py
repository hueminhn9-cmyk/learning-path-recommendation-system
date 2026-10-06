import streamlit as st
import sqlite3
from config import IS_VI
from database import get_db

def login_page():
    st.markdown("""
    <div class="hero-banner">
        <span class="hero-badge">🎓 AI Educational Guidance Platform</span>
        <h1 style="margin:8px 0; font-size:2.4rem; font-weight:800;">Hệ thống Gợi ý Lộ trình Học tập Sinh viên bằng AI</h1>
        <p style="font-size:1.1rem; opacity:0.9; margin:0;">Machine Learning Powered Student Assessment & Personalized Learning Advisor</p>
    </div>
    """, unsafe_allow_html=True)

    c_left, c_center, c_right = st.columns([0.5, 3, 0.5])

    with c_center:
        st.markdown('<div class="bw-card">', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["🔐 " + ("Đăng nhập" if IS_VI() else "Login"), "📝 " + ("Đăng ký" if IS_VI() else "Sign Up")])

        with tab1:
            st.subheader("Welcome Back 👋")
            email = st.text_input("Email Address", placeholder="student@college.edu", key="login_email")
            password = st.text_input("Password", type="password", key="login_pass")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🚀 " + ("Đăng nhập" if IS_VI() else "Login"), use_container_width=True):
                if email and password:
                    conn = get_db()
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
                    user = cursor.fetchone()
                    conn.close()

                    if user:
                        st.session_state.logged_in = True
                        st.session_state.user_id = user["id"]
                        st.session_state.user_email = user["email"]
                        st.session_state.user_name = user["name"]
                        st.session_state.user_role = user["role"]
                        st.success(f"✅ {'Xin chào' if IS_VI() else 'Welcome back'}, {user['name']}!")
                        st.rerun()
                    else:
                        st.error("❌ Email hoặc mật khẩu không chính xác" if IS_VI() else "❌ Invalid email or password")
                else:
                    st.warning("⚠️ Vui lòng điền đầy đủ thông tin" if IS_VI() else "⚠️ Please fill in all fields")

        with tab2:
            st.subheader("Create Student Account ✨")
            reg_name = st.text_input("Full Name / Họ và tên", key="reg_name")
            reg_roll = st.text_input("Roll Number / Mã số Sinh viên (MSSV)", key="reg_roll")
            reg_email = st.text_input("Email Address", key="reg_email")
            reg_pass = st.text_input("Password", type="password", key="reg_pass")

            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("✨ " + ("Đăng ký Tài khoản" if IS_VI() else "Register Account"), use_container_width=True):
                if reg_name and reg_email and reg_pass:
                    try:
                        conn = get_db()
                        cursor = conn.cursor()
                        cursor.execute("INSERT INTO users (name, roll_number, email, password, interest) VALUES (?, ?, ?, ?, ?)",
                                       (reg_name, reg_roll, reg_email, reg_pass, "Medium"))
                        conn.commit()
                        conn.close()
                        st.success("✅ Đăng ký thành công! Hãy chuyển sang thẻ Đăng nhập." if IS_VI() else "✅ Account created successfully! Please switch to Login tab.")
                    except sqlite3.IntegrityError:
                        st.error("❌ Email đã tồn tại trên hệ thống." if IS_VI() else "❌ Email address is already registered.")
                else:
                    st.warning("⚠️ Vui lòng điền đầy đủ Tên, Email và Mật khẩu." if IS_VI() else "⚠️ Please enter Name, Email, and Password.")
        st.markdown('</div>', unsafe_allow_html=True)
