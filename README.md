# Sistem Autentikasi Pengguna

[![Python CI](https://github.com/gracej88/sistemautentikasipengguna/actions/workflows/test.yml/badge.svg)](https://github.com/gracej88/sistemautentikasipengguna/actions/workflows/test.yml)
![Coverage](https://img.shields.io/badge/coverage-96%25-brightgreen)

---

## 📌 Deskripsi

Aplikasi sederhana berbasis Python dan Flask untuk melakukan registrasi pengguna dengan validasi input.  
Proyek ini dibuat sebagai bagian dari Final Project mata kuliah Software Testing.

Aplikasi ini menerapkan:

- Unit Testing
- Integration Testing
- Test Coverage
- Continuous Integration (CI)

---

## 🚀 Fitur Utama

- Registrasi user
- Validasi email, password, dan nomor telepon
- Penyimpanan data ke file JSON
- Web interface menggunakan Flask

---

## 🧱 Arsitektur Aplikasi

- Frontend → HTML (Flask Template)
- Backend → Flask
- Business Logic → user_service.py
- Validation → validation.py
- Storage → users.json

---

## ▶️ Cara Menjalankan Aplikasi

Install dependency: pip install flask
Jalankan : py main.py
Buka di browser:http://127.0.0.1:5000

---

## 🧪 Cara Menjalankan Testing

py -m unittest discover

---

## 📊 Test Coverage

py -m coverage run -m unittest discover
py -m coverage report

Coverage saat ini: **96%**

---

## ⚙️ Continuous Integration (CI)

Menggunakan GitHub Actions.

Pipeline berjalan saat:

- push
- pull request

Langkah CI:

- install dependencies
- menjalankan seluruh test
- generate coverage report

---

## 📂 Struktur Project

project/
│
├── main.py
├── user_service.py
├── validation.py
├── test_validation.py
├── test_integration.py
├── templates/
│ └── index.html
├── users.json
├── README.md
└── .github/workflows/

---

## 🎯 Strategi Pengujian

### Unit Testing

Digunakan untuk menguji:

- Validasi email
- Validasi password
- Validasi nomor telepon

### Integration Testing

Digunakan untuk menguji:

- Proses registrasi user secara end-to-end

---

## 💡 Teknologi

- Python
- Flask
- unittest
- coverage
- GitHub Actions
