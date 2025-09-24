# football-shop
Tugas 2
Nama:Wildan Muhammad Hafidz
NPM: 2406495962
🔗link deployment: https://wildan-muhammad41-footballshop.pbp.cs.ui.ac.id/

---

## Implementasi Step-by-Step
Berikut ini adalah langkah-langkah yang saya lakukan untuk menyelesaikan checklist tugas:

1. **Membuat Proyek Django**

   Memulai dengan membuat virtual environment agar library yang digunakan terisolasi:
   ```bash
   python -m venv env
   env\Scripts\activate     # di Windows
   source env/bin/activate  # di Mac/Linux
   ```
   Kemudian membuat project Django baru:
   ```bash
   django-admin startproject footballshop
   cd footballshop
   ```
2. **Membuat Aplikasi main**
   ```bash
   python manage.py startapp main
   ```
   Lalu, menambahkan 'main' ke dalam INSTALLED_APPS di peakperformance/settings.py.
   
3. **Routing Proyek ke Aplikasi main**

   Menambahkan path('', include('main.urls')) di football_shop/urls.py

4. **Membuat Model Product**

   Mengisi main/models.py dengan:
   ```bash
   name = models.CharField(max_length=255)
   price = models.IntegerField(default=0)
   description = models.TextField(blank=True, null=True)
   thumbnail = models.URLField(blank=True, null=True)
   category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='update')
   is_featured = models.BooleanField(default=False)
   shop_views = models.PositiveIntegerField(default=0)
   ```
   Lalu menjalankan:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   untuk melakukan migration

5. **Routing di main/urls.py**
   
   Menambahkan path('', include('main.urls')) di main/urls.py

6. **Deployment ke PWS**
   -Menambahkan requirements.txt
   -Mengatur ALLOWED_HOSTS di settings.py agar sesuai domain PWS.
   -Menambahkan environment variable untuk SECRET_KEY dan DEBUG.
   -Push ke PWS:
   
    ```bash
    git add .
    git commit -m " "
    git push pws master
    ```
       
---

##📊 Bagan Alur Request & Response Django


   <img width="900" height="450" alt="image" src="https://github.com/user-attachments/assets/65158c85-3515-4235-a83b-1d2753c87d85" />
   
   **Penjelasan Alur**:

 1. Client mengirim permintaan (request) ke server Django, misalnya:
    shttp://localhost:8000/produk/.
    
 2. urls.py akan memetakan URL yang diminta ke fungsi view yang sesuai.
    
 3. views.py berisi fungsi/kelas yang memproses request:
    -Mengambil data dari models.py (database) bila perlu.
    -Memilih template HTML untuk merender data.

 4. models.py berisi representasi tabel database dalam bentuk model Python.
    -Views akan memanggil model ini untuk query data.

 5. Data yang diambil dari models.py dikirim kembali ke views.py, lalu views menggabungkan data dengan HTML Template menggunakan Django Template Engine.

 6. Django mengirimkan response berupa halaman HTML lengkap kembali ke Client (Browser).

    
## 🗄️ Cara Kerja Migrasi Database di Django
 Migrasi database di Django dilakukan dalam dua tahap:
1. Membuat migrasi (generate migration file):
   ```bash
   python manage.py makemigrations
   ```
   -Django memeriksa perubahan pada models.py.
   
   -Membuat file migrasi di folder migrations/ untuk mencatat perubahan
   
 2. Menerapkan migrasi ke database::
   ```bash
   python manage.py migrate
   ```
   -Django mengeksekusi file migrasi ke database.
   
   -Membuat/mengubah tabel sesuai model.
   Migrasi ini membuat database tetap sinkron sama kode yang ada.

---

## ❓ Kenapa Django Cocok Jadi Framework Pertama?

   Django dijadikan titik awal pembelajaran pengembangan perangkat lunak karena menawarkan kecepatan pengembangan dan struktur yang siap pakai, menggunakan Python yang mudah dipelajari, menyediakan dokumentasi      dan komunitas yang kuat untuk bantuan, memiliki fitur keamanan bawaan, dan bersifat sumber terbuka (gratis) sehingga memudahkan pengembang untuk fokus pada fitur unik tanpa mengulang kode umum seperti            autentikasi pengguna dan administrasi konten. 

## Feedback untuk asisten dosen
Pada saat sesi tutorial 1 di minggu ke-dua, asisten dosen sudah sangat baik dalam membantu mahasiswa saat ada masalah lewat discord ketika mengerjakan tutorial 1. Jadi sudah cukup baik.

# TUGAS 3 - Implementasi Form dan Data Delivery pada Django

---

## ❓ Mengapa Kita Memerlukan Data Delivery?

Aplikasi web modern memerlukan pengiriman data karena fungsinya lebih dari sekadar menampilkan halaman statis. Agar interaktif, aplikasi harus memungkinkan pertukaran informasi antara client dan server. Misalnya, saat pengguna mendaftar, data formulir dikirim ke server, diproses, dan server memberikan respons kembali. Tanpa mekanisme ini, aplikasi web tidak akan bisa berinteraksi dengan pengguna dan hanya bersifat pasif seperti dokumen HTML biasa.

## ⚖️ XML vs JSON

Untuk hampir semua kebutuhan pengembangan web modern (API, aplikasi mobile, website interaktif), JSON adalah pilihan yang lebih baik dan lebih benar.
JSON lebih unggul karena lebih sederhana, lebih ringan, dan lebih cepat. XML masih sangat berguna, tetapi untuk kasus penggunaan yang lebih spesifik dan seringkali bersifat legacy (sudah usang tetapi masih dibutuhkan).

Sintaks yang Jauh Lebih Sederhana: JSON lebih mudah dibaca dan ditulis oleh manusia. Strukturnya yang berupa kunci:nilai sangat intuitif dan mirip dengan objek pada bahasa pemrograman populer, terutama JavaScript.

"Bahasa Asli" JavaScript: JSON (JavaScript Object Notation) pada dasarnya adalah format objek JavaScript. Di dunia web di mana JavaScript ada dimana mana, mengubah data JSON menjadi objek yang bisa langsung dipakai hanya butuh satu baris kode (JSON.parse()), tanpa perlu library eksternal

## 📝 Fungsi is_valid() pada Django Form

Method is_valid() dipakai untuk memvalidasi data yang dikirim lewat form. Django akan otomatis mengecek apakah input sesuai aturan field di model atau form.
Contoh: kalau ada field price (IntegerField) lalu user isi dengan teks "wildan", is_valid() akan mengembalikan False dan Django akan menampilkan error ke user.
jadi dengan is_valid() kita bisa lebih mudah menghandle input tidak sesuai agar tidak terjadi bug.

## 🔒 Mengapa Perlu csrf_token?

Tanpa proteksi CSRF, request berbahaya bisa dikirim dari situs lain menggunakan cookie tersebut, tanpa sepengetahuan user.Lalu server memverifikasi apakah token itu cocok dengan yang disimpan di sesi user.
→ Kalau tidak cocok, request ditolak.

Kalau tidak ada token ini, penyerang bisa bikin user tanpa sadar mengirim request berbahaya ke server (misalnya klik link di website palsu yang ternyata mengirim request POST ke aplikasi kita).
Dengan csrf_token, setiap form punya token unik yang harus cocok dengan token di server. Jadi penyerang tidak bisa sembarangan submit data karena tokennya tidak valid.



## 📌 Alur Pengerjaan Tugas 3

1. **Membuat Layout Utama (`base.html`)**

   * Membuat file `base.html` sebagai layout utama untuk dipakai di file file html lain.
   * File ini berisi struktur dasar seperti header, navbar, dan footer.
   * Menambahkan block `{% block content %}{% endblock %}` agar halaman lain bisa mewarisi struktur dasar ini.
  
2. **Memperbarui main.html**
   * Menambahkan beberapa tombol untuk tambah barang dan melihat deskripsi barang
   * Halaman ini menggunakan `{% extends 'base.html' %}` untuk mewarisi layout utama.

3. **Membuat Form di `forms.py`**

   * Membuat file `forms.py` dan mendefinisikan `ShopForm` berbasis `ModelForm`.
   * Form ini menggunakan model `Shop` dan mengambil semua field yang sudah didefinisikan di model.
   * Form ini dipakai pada halaman tambah produk (`add_product.html`).
     
4. **Membuat Halaman Detail Produk (`product_detail.html`)**

   * Halaman ini menampilkan detail informasi dari setiap produk yang dipilih.
   * Data produk diambil berdasarkan `pk` yang dikirim melalui URL.
   * Halaman ini juga extends dari `base.html`.
     
5. **Membuat Halaman Form (`add_product.html`)**

   * Halaman ini digunakan untuk menambahkan produk baru.
   * Form yang ditampilkan berasal dari `ShopForm`.
   * Halaman ini juga extends dari `base.html`.

6. **Menambahkan Fungsi Views untuk JSON dan XML**

   * Menambahkan empat fungsi baru di `views.py`:

     * `show_json` → menampilkan semua produk dalam format JSON.
     * `show_xml` → menampilkan semua produk dalam format XML.
     * `show_json_by_id` → menampilkan detail satu produk berdasarkan ID dalam format JSON.
     * `show_xml_by_id` → menampilkan detail satu produk berdasarkan ID dalam format XML.
   
7. **Menambahkan Routing URL di `urls.py`**

   * Menambahkan path baru untuk mengakses data dalam format JSON dan XML.
   * Contoh:

     * `/products/json/` → semua produk dalam format JSON.
     * `/products/xml/<int:pk>/` → produk berdasarkan ID dalam format XML.
     * 
<img width="1919" height="1014" alt="image" src="https://github.com/user-attachments/assets/76bc9858-01cd-4b60-b486-f9e8a52b65bb" />
<img width="1410" height="925" alt="image" src="https://github.com/user-attachments/assets/110aefc7-b2a9-4f89-90e9-623660ddfddf" />
<img width="1919" height="1017" alt="image" src="https://github.com/user-attachments/assets/0ba4142b-6a56-4773-9752-44e756951701" />
<img width="1446" height="914" alt="image" src="https://github.com/user-attachments/assets/2e833944-8452-4613-8b2c-b7ee08c4ac79" />



## 👩‍🏫 Feedback untuk asisten dosen Tutorial 2
untuk tutorial 2 sendiri saya tidak mengalami masalah sehingga semua berjalan lancar, jadi saya tidak punya feedback untuk asdos

## ❓ Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya !
Django AuthenticationForm adalah sebuah formulir bawaan dari Django yang dirancang khusus untuk menangani proses login pengguna.

**Kelebihan:**
- Keamanannya Terjamin, Formulir ini sudah dirancang dengan praktik keamanan terbaik.
- Menangani validasi login secara otomatis, termasuk pengecekan akun yang tidak aktif.
- Mudah digunakan

**Kekurangan:**
- Terbatas pada field username dan password.
- Pesan errornya terlalu generik jadi susah untuk debugging


---
## 2. 🔑 Perbedaan Autentikasi dan Otorisasi

- **Autentikasi (Authentication)**: proses memverifikasi identitas seseorang.   
  📌 Contoh: Anda membuktikan bahwa Anda adalah orang yang Anda klaim.

- **Otorisasi (Authorization)**:  proses menentukan hak akses atau izin yang dimiliki oleh pengguna yang telah diautentikasi.  
  📌 Contoh: Setelah sistem tahu siapa Anda, ia akan menentukan apa saja yang boleh Anda lihat atau lakukan.

**Implementasi di Django:**
- ✅ **Autentikasi**:  
  Django menyediakan `django.contrib.auth`, yang mana di dalamnya ada `authenticate()` dan `login()` untuk memverifikasi identitas.
- ✅ **Otorisasi**:  
  Django memiliki sistem *permissions* dan *groups*  Setiap model secara otomatis mendapatkan izin add, change, delete, dan view. Anda bisa mengelompokkan izin-izin ini ke dalam Groups dan menetapkannya ke         pengguna.
---

## 3. 🍪 Session vs Cookies dalam Menyimpan State

**Cookies**: data kecil yang disimpan di sisi *client* (browser).  
**Session**: data pengguna yang disimpan di server, sementara browser hanya menyimpan *session ID* di dalam cookies.

### ⚡ Kelebihan Cookies:
- Mudah diimplementasikan, tidak membebani server.

### ⚠️ Kekurangan Cookies:
- Tidak aman untuk data sensitif, ukuran terbatas, dan memperlambat request jika datanya besar.

### ⚡ Kelebihan Session:
- Jauh lebih aman karena data ada di server, kapasitas besar.


### ⚠️ Kekurangan Session:
- Membebani memori dan penyimpanan server, bisa menjadi rumit untuk dikelola dalam arsitektur terdistribusi (load balancing).

## 4. 🔐 Apakah Cookies Aman Secara Default?

Secara default, cookies tidak aman. Mereka rentan terhadap beberapa serangan umum jika tidak ditangani dengan benar.

**Penanganan di Django:**
-  Opsi `HttpOnly` untuk mencegah akses cookie melalui JavaScript.  
-  Mendukung `Secure` flag agar cookies hanya dikirim melalui HTTPS.  
-  Mekanisme **CSRF protection** untuk mencegah serangan berbasis form.  
-  Konfigurasi `SESSION_COOKIE_AGE`, `SESSION_COOKIE_SECURE`, dan `SESSION_COOKIE_SAMESITE` di `settings.py` untuk meningkatkan keamanan.


---
# 📋 Implementasi Autentikasi, Relasi User–Product, & Cookies

## 1. Fitur Autentikasi

- Buat view register, login_user, dan logout_user.
- Gunakan UserCreationForm (untuk register) & AuthenticationForm (untuk login).
- Saat login berhasil, simpan cookie last_login.
- Saat logout, hapus cookie last_login.

## 2. Relasi User–Product

- Pada model Product, tambahkan field: user = models.ForeignKey(User, on_delete=models.CASCADE).
- Di view create produk, set produk.user = request.user sebelum disimpan.

## 3. Tampilan & filter

- Di halaman utama, tampilkan request.user.username dan cookie last_login.
- Buat tombol filter "All" (semua produk) dan "My" (hanya produk milik user).
  
## 4. Dummy Data
- Registrasi 2 akun pengguna langsung melalui form `register`.
- Login dengan masing-masing akun dan buat 3 data `Product` menggunakan form input yang sudah ada.
- Dengan demikian, setiap akun memiliki 3 data dummy secara manual melalui antarmuka aplikasi.

## 5. Penyesuaian Form
- `login.html` dan `register.html` disusun dengan struktur dan class CSS yang konsisten dengan `home.html`.

## 6. Verifikasi
- Login: Cek username & cookie last_login muncul.
- Tambah Produk: Pastikan produk terhubung dengan user yang login.
- Filter: Uji tombol "All" dan "My", pastikan data tampil sesuai.
- Logout: Pastikan cookie last_login terhapus.

---

## 👩‍🏫 Feedback untuk asisten dosen Tutorial 3

saya tidak mengalami masalah dalam mengerjakan tutorial kemarin, jadi aman aman saja dan tidak ada feedback dari saya untuk sesi tutorial kali ini

---



