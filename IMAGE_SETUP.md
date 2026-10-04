# 🖼️ How to Add Your College Logo/Images

## Quick Setup Guide

### **Step 1: Prepare Your Image**

1. **Get your college logo/image**
   - Format: PNG, JPG, or JPEG
   - Size: Recommended 400x400 pixels or larger
   - File name: `college_logo.png`

2. **Location to save:**
   ```
   AI_Student_Learning_Path/
   └── assets/
       └── college_logo.png
   ```

---

## 📂 Adding Your College Logo

### **Method 1: Simple Copy-Paste (Recommended)**

1. **Create folder** (Already created ✅)
   - Go to: `C:\Users\CHANDHAN M\Desktop\AI_Student_Learning_Path\assets\`

2. **Add your image**
   - Place your college logo as: `college_logo.png`
   - File format: PNG, JPG, or JPEG

3. **Restart the app**
   ```bash
   python -m streamlit run dataset/app.py
   ```

4. **The logo will appear** on the login page!

---

## 🎨 Where Images Will Display

### **1. Login Page**
- Your college logo appears as a banner
- Size: 200px width
- Caption: "Your College Logo"

### **2. Can Add More Images**

You can add additional images for:

**Profile Section** (Update app.py):
```python
# Add this in profile_page() function:
profile_img_path = os.path.join(BASE_DIR, "..", "assets", "profile.png")
if os.path.exists(profile_img_path):
    st.image(profile_img_path, width=200)
```

**Header Section**:
```python
header_img_path = os.path.join(BASE_DIR, "..", "assets", "header.png")
if os.path.exists(header_img_path):
    st.image(header_img_path, use_column_width=True)
```

---

## 📋 Supported Image Formats

| Format | Extension | Quality | Size |
|--------|-----------|---------|------|
| PNG | .png | ⭐⭐⭐⭐⭐ | Small |
| JPEG | .jpg, .jpeg | ⭐⭐⭐⭐ | Medium |
| GIF | .gif | ⭐⭐⭐ | Varies |
| BMP | .bmp | ⭐⭐ | Large |

**Recommendation**: Use PNG with transparent background for best results

---

## 🎯 Image Recommendations

### **College Logo**
- **Size**: 400x400 to 600x600 pixels
- **Format**: PNG with transparency
- **Aspect Ratio**: Square or landscape
- **File Size**: < 500 KB

### **Background Images** (Advanced)
- **Size**: 1920x1080 or higher
- **Format**: JPG (smaller file size)
- **File Size**: < 2 MB

---

## 🛠️ Step-by-Step Instructions

### **To Add College Logo:**

**Step 1: Find your college logo**
- Check your college website
- Download as PNG/JPG
- Or use any logo image you have

**Step 2: Save to correct location**
```
C:\Users\CHANDHAN M\Desktop\AI_Student_Learning_Path\assets\college_logo.png
```

**Step 3: Verify installation**
- Folder exists: `C:\...\assets\` ✅
- Image file: `college_logo.png` ✅
- Format: PNG or JPG ✅

**Step 4: Restart app**
```bash
python -m streamlit run dataset/app.py
```

**Step 5: Check login page**
- Logo should appear above login form
- If not, check file name and format

---

## ❓ Troubleshooting

### **Logo Not Showing?**

**Check 1: File Location**
```
Correct path:
C:\Users\CHANDHAN M\Desktop\AI_Student_Learning_Path\assets\college_logo.png

Wrong path:
C:\Users\CHANDHAN M\Desktop\assets\college_logo.png  ❌
C:\Users\CHANDHAN M\Desktop\AI_Student_Learning_Path\college_logo.png  ❌
```

**Check 2: File Name**
- Must be exactly: `college_logo.png`
- Case-sensitive on some systems
- No spaces in filename

**Check 3: File Format**
- Use: PNG, JPG, or JPEG
- Not: GIF, BMP, TIFF, etc.

**Check 4: Restart App**
- Sometimes Streamlit caches files
- Stop app (Ctrl+C)
- Restart: `python -m streamlit run dataset/app.py`

### **Image Size Issues**

**Too large:**
- Resize to 400-600 pixels
- Use online image resizer
- Or use Python PIL:
```python
from PIL import Image
img = Image.open("logo.jpg")
img.thumbnail((500, 500))
img.save("logo_resized.png")
```

**Too small:**
- Resize to at least 200 pixels
- Increase dimensions

---

## 🎨 Advanced: Add More Images

### **Step 1: Prepare images**
- Logo: `college_logo.png`
- Header: `header_banner.png`
- Footer: `footer_logo.png`
- Profile: `profile_icon.png`

### **Step 2: Save to assets folder**
```
assets/
├── college_logo.png
├── header_banner.png
├── footer_logo.png
└── profile_icon.png
```

### **Step 3: Update app.py to display them**

**In home_page() - Add header banner:**
```python
header_path = os.path.join(BASE_DIR, "..", "assets", "header_banner.png")
if os.path.exists(header_path):
    st.image(header_path, use_column_width=True)
```

**In profile_page() - Add profile icon:**
```python
profile_path = os.path.join(BASE_DIR, "..", "assets", "profile_icon.png")
if os.path.exists(profile_path):
    st.image(profile_path, width=100)
```

**In footer() - Add footer logo:**
```python
footer_path = os.path.join(BASE_DIR, "..", "assets", "footer_logo.png")
if os.path.exists(footer_path):
    st.image(footer_path, width=80)
```

---

## 📸 Current Image Locations

### **Login Page**
- Location in code: `login_page()` function
- File looked for: `assets/college_logo.png`
- Display size: 200px width
- Status: ✅ Ready to display

### **Future Enhancement Locations**
- Home page header
- Profile page avatar
- Footer section
- Resource section

---

## 💡 Pro Tips

✅ **Use PNG format** for logos (best quality)

✅ **Use JPG format** for photos (smaller size)

✅ **Keep aspect ratio** when resizing

✅ **Test on login page** first

✅ **Use high resolution** images (won't downsize bad)

✅ **Transparent background** looks professional

✅ **Consistent branding** across all pages

---

## 🎬 Visual Preview

### **With College Logo:**
```
┌─────────────────────────────────────┐
│                                     │
│      [Your College Logo Here]       │  ← Your image here!
│                                     │
│  🎓 AI Student Learning Path        │
│                                     │
│  Email: [____________]              │
│  Password: [____________]           │
│                                     │
│  [🔐 Login]  [📝 Sign Up]          │
└─────────────────────────────────────┘
```

---

## ✅ Checklist

- [ ] Image file ready (PNG/JPG)
- [ ] Saved as: `college_logo.png`
- [ ] Location: `assets/` folder
- [ ] File size: < 500 KB
- [ ] Image resolution: 400x400+ pixels
- [ ] App restarted
- [ ] Logo visible on login page

---

## 🎓 Next Steps

1. **Add your college logo** following steps above
2. **Restart the app** to see changes
3. **Check login page** for your logo
4. **Customize colors** in CSS (optional)
5. **Add more images** as needed

---

## 📞 Issues?

**Not working?**
1. Check file path and name
2. Check file format (PNG/JPG)
3. Restart Streamlit app
4. Check browser cache (Ctrl+Shift+Delete)
5. Try with different image file

---

**Your assets folder is ready!** 🎉

Just add your images and restart the app.

Updated: March 17, 2026
