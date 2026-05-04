markdown_content = """# 📸 SnapClass 🎙️
**Next-Gen Biometric Attendance System for Classrooms**

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Database](https://img.shields.io/badge/Database-Supabase-3ECF8E.svg)](https://supabase.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

## 📖 Introduction
Welcome to **SnapClass**! Taking attendance is a fundamental part of classroom management, but it doesn't have to be a chore. SnapClass is a smart, web-based tool designed to help teachers capture attendance in seconds using advanced Face ID and Voice Recognition technology. 

## ❓ The Problem
In a typical classroom, teachers waste anywhere from 5 to 15 minutes manually calling out names or passing around an attendance sheet. 
* **It wastes time:** Time that could be spent teaching.
* **It breaks momentum:** Disrupts the flow at the beginning of a lecture.
* **It's prone to errors:** "Proxy" attendance (students answering for friends) is a common headache.

## 💡 The Solution
SnapClass eliminates manual roll calls. Teachers simply create a subject and generate a QR code. Students scan the QR code to register their facial and voice profiles. When it's time for class, the teacher can either:
1. Take a single **group photo** of the class.
2. Record a quick audio clip of students saying "Present."

SnapClass does the heavy lifting: identifying the students, marking them present, and logging the exact timestamp in the database. Fast, secure, and proxy-proof!

---

## ✨ Key Features
* **👨‍🏫 Teacher Dashboard:** Easy registration and subject management for educators.
* **📱 QR Code Onboarding:** Frictionless student registration. Students scan a QR code to enroll their face or voice under a specific subject.
* **🖼️ Group Photo Face ID:** Snap a picture of the classroom; the app detects faces, generates embeddings, matches them, and marks attendance instantly.
* **🗣️ Voice Recognition Roll Call:** Teachers can record students saying "present," and the app will verify their identity based on voice embeddings.
* **⏱️ Timestamped Logs:** Every attendance record is securely stored with exact timestamps to maintain academic integrity.

---

## 🛠️ Tech Stack

This project is powered by a robust stack of Python libraries and modern tools:

**Frontend & UI**
* **[Streamlit](https://streamlit.io/):** For building the fast, interactive web application interface.

**Database & Security**
* **[Supabase](https://supabase.com/):** For reliable, scalable database management.
* **[Bcrypt](https://pypi.org/project/bcrypt/):** For secure password hashing and protection.

**Face Recognition & Image Processing**
* **[Scikit-learn](https://scikit-learn.org/):** Used for face classification.
* **[Dlib (dlib-bin)](http://dlib.net/):** For detecting facial landmarks and shapes.
* **[Face Recognition Models](https://github.com/ageitgey/face_recognition_models):** For extracting precise facial embeddings.
* **[Pillow (PIL)](https://python-pillow.org/):** For image preprocessing, resizing, scaling, and transformation.

**Voice Recognition & Audio Processing**
* **[Librosa](https://librosa.org/):** For loading, cutting, and partitioning audio files.
* **[Resemblyzer](https://github.com/resemble-ai/Resemblyzer):** For creating deep voice embeddings to compare and verify student voices.

**Utilities**
* **NumPy & Pandas:** For heavy data manipulation and array calculations.
* **Segno:** For generating QR codes for student registration.
* **Setuptools:** For managing non-Python package dependencies.

---

## 🚀 How It Works (The Flow)

### For Teachers:
1. **Sign Up / Login:** Register on the platform.
2. **Create a Subject:** Set up the class you are teaching.
3. **Share QR Code:** Generate and display the subject-specific QR code on the projector or screen.
4. **Take Attendance:** Choose either the *Camera* mode (snap a group photo) or *Voice* mode (record audio). 

### For Students:
1. **Scan & Register:** Scan the teacher's QR code.
2. **Provide Biometrics:** Upload a photo or voice sample to register for that specific subject.
3. **Attend Class:** Just show up! Your face or voice will do the rest.

---

## 💻 Local Setup & Installation

```bash
# Clone the repository
git clone [https://github.com/Jayanthravi16/AI-SnapClass.git](https://github.com/Jayanthravi16/AI-SnapClass.git)

# Navigate into the directory
cd AI-SnapClass

# Install the required dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py