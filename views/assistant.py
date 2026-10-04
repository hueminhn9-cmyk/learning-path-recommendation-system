import streamlit as st
from config import IS_VI

def ai_assistant_page():
    st.markdown(f"""
    <div class="hero-banner">
        <span class="hero-badge">🤖 AI Conversational Assistant</span>
        <h1 style="margin:8px 0; font-size:2.2rem; font-weight:800;">{"Trợ lý AI Hỏi đáp & Tư vấn Học tập Smart" if IS_VI() else "Smart AI Study & Homework Advisor"}</h1>
        <p style="font-size:1.05rem; opacity:0.9; margin:0;">Ask any question about roadmaps, code concepts, algorithms, exam tips</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="bw-card">', unsafe_allow_html=True)
    st.subheader("💡 " + ("Gợi ý câu hỏi nhanh:" if IS_VI() else "Quick Prompts:"))
    q_col1, q_col2, q_col3, q_col4 = st.columns(4)
    
    prompt_text = None
    with q_col1:
        if st.button("🐍 " + ("Lộ trình học Python" if IS_VI() else "Python Roadmap"), use_container_width=True):
            prompt_text = "Cho tôi lộ trình học Python từ cơ bản đến nâng cao?" if IS_VI() else "Give me a step-by-step Python roadmap from beginner to advanced?"
    with q_col2:
        if st.button("🧠 " + ("Cách sửa Overfitting" if IS_VI() else "Fix Overfitting"), use_container_width=True):
            prompt_text = "Overfitting trong AI là gì và cách khắc phục?" if IS_VI() else "What is Overfitting in AI and how to fix it?"
    with q_col3:
        if st.button("🛡️ " + ("Học Cybersecurity" if IS_VI() else "Learn Security"), use_container_width=True):
            prompt_text = "Bắt đầu học Cybersecurity cần những kiến thức gì?" if IS_VI() else "What skills are needed to start learning Cybersecurity?"
    with q_col4:
        if st.button("🌐 " + ("Lộ trình Web Fullstack" if IS_VI() else "Fullstack Web Path"), use_container_width=True):
            prompt_text = "Lập trình Web Fullstack cần học những công nghệ nào?" if IS_VI() else "What technologies to learn for Fullstack Web Development?"

    st.markdown("---")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content": "👋 Xin chào! Tôi là Trợ lý AI Hỏi đáp Học tập. Bạn có thể đặt câu hỏi về kiến thức môn học, cách học hiệu quả hoặc nhờ giải thích các khái niệm khó!" if IS_VI() else "👋 Hello! I am your AI Study Advisor. Ask me anything about programming concepts, study roadmaps, exam preparation, or domain explanations!"}
        ]

    for msg in st.session_state.chat_history:
        st.chat_message(msg["role"]).write(msg["content"])

    user_query = st.chat_input("Đặt câu hỏi cho Trợ lý AI..." if IS_VI() else "Type your question for AI Assistant...")
    if prompt_text:
        user_query = prompt_text

    if user_query:
        st.session_state.chat_history.append({"role": "user", "content": user_query})
        st.chat_message("user").write(user_query)

        query_lower = user_query.lower()
        if "python" in query_lower:
            reply = """🤖 **Lộ trình AI Đề xuất cho Python:**
1. **Cơ bản (Tuần 1-2):** Cú pháp, Biến, Vòng lặp `for/while`, Hàm (`def`), List, Dict, Tuple.
2. **Trung cấp (Tuần 3-4):** Lập trình hướng đối tượng (OOP), Xử lý File, Module & Package.
3. **Chuyên sâu (Tháng 2):** Sử dụng thư viện Pandas, NumPy, Matplotlib cho Phân tích Dữ liệu hoặc Flask/FastAPI cho Web API.
4. **Dự án Thực tế:** Viết Web scraper, Xây dựng Dashboard Streamlit hoặc Mô hình Machine Learning.""" if IS_VI() else """🤖 **AI Recommended Python Roadmap:**
1. **Basics (Week 1-2):** Syntax, Variables, Loops (`for/while`), Functions (`def`), Lists, Dicts, Tuples.
2. **Intermediate (Week 3-4):** Object Oriented Programming (OOP), File I/O, Modules & Packages.
3. **Advanced (Month 2):** Master Pandas, NumPy, Matplotlib for Data Analysis or Flask/FastAPI for Web APIs.
4. **Real Project:** Build a Web Scraper, Streamlit Dashboard, or Machine Learning Model."""
        elif "overfitting" in query_lower:
            reply = """🤖 **Giải thích AI về Overfitting:**
Overfitting xảy ra khi mô hình học quá kỹ dữ liệu huấn luyện (nhiễu), dẫn đến học thuộc lòng thay vì học tổng quát. Khi test dữ liệu mới, độ chính xác bị giảm mạnh.

💡 **4 Cách khắc phục chính:**
1. **Regularization:** Áp dụng L1 (Lasso) hoặc L2 (Ridge) để phạt trọng số lớn.
2. **Dropout:** Thêm lớp Dropout (0.2 - 0.5) ngắt ngẫu nhiên các nơ-ron trong Neural Network.
3. **Early Stopping:** Dừng huấn luyện khi Validation Loss bắt đầu tăng.
4. **Thêm dữ liệu:** Thu thập thêm dữ liệu hoặc dùng kỹ thuật Data Augmentation.""" if IS_VI() else """🤖 **AI Explanation of Overfitting:**
Overfitting occurs when a model learns the training data (and noise) too closely, memorizing rather than generalizing.

💡 **4 Key Fixes:**
1. **Regularization:** Use L1 (Lasso) or L2 (Ridge) to penalize large weights.
2. **Dropout:** Add Dropout layers (0.2 - 0.5) in Deep Neural Networks.
3. **Early Stopping:** Stop training when validation loss begins to increase.
4. **More Data:** Increase sample size or use Data Augmentation."""
        elif "cybersecurity" in query_lower or "security" in query_lower:
            reply = """🤖 **Lộ trình học Cybersecurity từ AI Advisor:**
1. **Nền tảng Mạng (Networking):** Mô hình TCP/IP, OSI, IP Address, Subnetting, DNS, HTTP/HTTPS.
2. **Hệ điều hành & Dòng lệnh:** Sử dụng thành thạo Linux (Ubuntu, Kali Linux), Shell Scripting.
3. **Bảo mật Web:** Nghiên cứu OWASP Top 10 (SQL Injection, XSS, CSRF, Authentication bypass).
4. **Công cụ Thực hành:** Wireshark, Nmap, Burp Suite, Metasploit.""" if IS_VI() else """🤖 **AI Recommended Cybersecurity Roadmap:**
1. **Networking Basics:** TCP/IP, OSI Layers, IP Addressing, DNS, HTTP/HTTPS.
2. **OS & Command Line:** Master Linux CLI (Ubuntu, Kali Linux), Shell Scripting.
3. **Web Security:** Study OWASP Top 10 (SQLi, XSS, CSRF, Auth Bypass).
4. **Practical Tools:** Wireshark, Nmap, Burp Suite, Metasploit."""
        elif "fullstack" in query_lower or "web" in query_lower:
            reply = """🤖 **Lộ trình Học Web Fullstack:**
1. **Frontend:** HTML5, CSS3 (Flexbox/Grid), JavaScript (ES6+), React.js hoặc Next.js.
2. **Backend:** Node.js với Express.js hoặc Python với FastAPI/Django.
3. **Database:** SQL (PostgreSQL/MySQL) và NoSQL (MongoDB).
4. **DevOps:** Git, Docker Containerization, Deploy Vercel/Render/AWS.""" if IS_VI() else """🤖 **Fullstack Web Roadmap:**
1. **Frontend:** HTML5, CSS3, JavaScript (ES6+), React.js / Next.js.
2. **Backend:** Node.js + Express.js or Python + FastAPI/Django.
3. **Database:** SQL (PostgreSQL/MySQL) and NoSQL (MongoDB).
4. **DevOps:** Git, Docker, Vercel / AWS Deployment."""
        else:
            reply = f"🤖 **Tư vấn AI cho '{user_query}':** Để làm chủ chủ đề này, bạn nên chia quá trình học làm 3 bước: 1) Nắm vững lý thuyết nền tảng & khái niệm gốc, 2) Làm bài tập thực hành nhỏ hàng ngày, và 3) Đóng gói thành 1 Mini-project hoàn chỉnh đưa vào Portfolio!" if IS_VI() else f"🤖 **AI Advice for '{user_query}':** To master this subject: 1) Learn the core theory & fundamentals, 2) Solve daily practical exercises, and 3) Build a complete mini-project for your Portfolio!"

        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)
    st.markdown('</div>', unsafe_allow_html=True)
