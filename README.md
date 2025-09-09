# 🏥 Digital Health Card System

A smart, QR-based medical data system designed for quick access to essential health information—built using **Python (Flask)** and **PostgreSQL**, deployed via **Render**.  
This project bridges the gap between healthcare and digital accessibility, enabling users to securely store and retrieve patient records in real-time.

---

## 🚨 Problem Statement
In critical situations, delays in accessing a patient’s medical information can result in improper care or life-threatening decisions. Traditional health records are paper-based, fragmented, or inaccessible when most needed.

This project solves that by:
- 📱 Generating a Digital Health Card with a QR code  
- 📤 Storing data like blood group, allergies, emergency contacts, etc., in a secure PostgreSQL database  
- ⚡ Enabling instant access to records by scanning the QR code from any device  

---

## 🎯 Objectives
- ✅ Digitize health records for easy retrieval  
- ✅ Ensure real-time access to medical details during emergencies  
- ✅ Offer a simple UI for both data input and display  
- ✅ Use QR codes for fast, secure, and shareable patient identification  

---

## 🧰 Tech Stack

| Layer       | Technologies |
|-------------|--------------|
| 🔙 Backend  | Python (Flask Framework) |
| 🖼️ Frontend | HTML, CSS (Jinja2 templates) |
| 🗃️ Database | PostgreSQL |
| 🔲 QR Codes | `qrcode` Python library |
| 🚀 Hosting  | Render |
| 🔧 Dev Tools| Git, GitHub, VS Code, Jupyter Notebook |

---

## 🔑 Key Features
- 📝 Form-based health data submission  
- 🧾 Unique QR code generation for each card  
- 🧠 Information includes: name, blood group, emergency contact, allergies, etc.  
- 🔒 Secure storage using PostgreSQL  
- 🌐 Works across desktop and mobile browsers  
- 🔗 QR codes contain secure, route-based identifiers (`/display/<card_id>`)  

---

## 🏗️ System Architecture
User ➝ Flask Form ➝ PostgreSQL ➝ QR Generation ➝ QR Code Output
↓ QR Scan ↓
/display/<card_id> ➝ Fetch & Render Details


---

## 🧪 How It Works
1. User fills out a form with health details  
2. Unique card ID is generated, QR code is created  
3. Data is saved in PostgreSQL with the associated `card_id`  
4. QR code displays a URL like `/display/<card_id>`  
5. Scanning the QR shows the health details securely  

---

## ✅ Results
- 🔐 Unique, scannable QR for each patient  
- 📱 Works seamlessly on both mobile and desktop  
- 🧪 Fully tested on Render and localhost deployments  

---

## 🧩 Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| QR showing old data | Refactored routes to fetch dynamic IDs |
| Localhost-only QR scanning | Deployed on Render for public access |
| QR overwriting on new card generation | Used `card_id` as QR image filename |

---

## 🚀 Deployment (Render)
1. Pushed code to GitHub  
2. Used `requirements.txt` and `Procfile` for setup  
3. Set Python version to 3.10+  
4. Public QR scanning enabled with hosted URL  

---

## 🔮 Future Improvements
- 🔐 Add login for verified healthcare professionals  
- 📋 Include prescriptions and full medical history  
- 📊 Admin dashboard for hospital use  
- 🧾 Export health card as downloadable PDF  

---

## 🧠 Conclusion
The **Digital Health Card System** offers a reliable and scalable solution to access and manage patient data, especially useful in emergency care.  
It demonstrates how technology can simplify and enhance healthcare workflows through smart integration of software and real-world needs.  

📌 Built with a vision to **combine data + devices = impact**  

---

## 👨‍💻 Author
**Vishwanath Kulal**

