# Aplikasi Penilaian Otomatis Ujian UKK Cloud Computing

Aplikasi ini digunakan untuk menilai keberhasilan deployment siswa di AWS secara otomatis pada ujian kompetensi SMK jurusan TKJ bidang Cloud Computing.

## 🚀 Fitur Utama
- Mengecek status deployment aplikasi siswa di AWS.
- Memverifikasi konfigurasi domain dan HTTPS.
- Menampilkan hasil penilaian secara otomatis.

## 📦 Persyaratan
- **Node.js** versi 18 atau lebih baru
- **npm** (Node Package Manager)
- Akses internet untuk menguji deployment siswa

## 🔧 Cara Instalasi

1. **Clone repository**
   ```bash
   git clone https://github.com/<username>/<repo-name>.git
   cd <repo-name>
2. **Install Dependensi**
   ```bash
   npm install
3. **Konfigurasi Environment**
   Buat file .env dan isi dengan konfigurasi berikut:
   ```env
   PORT=3000
   AWS_ACCESS_KEY_ID=your_aws_key
   AWS_SECRET_ACCESS_KEY=your_aws_secret

3. **Jalankan Aplikasi**
   ```bash
   npm start
4. **Testing**
   ```bash
   npm test
