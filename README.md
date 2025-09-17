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

## 👩‍🏫 Feedback untuk asisten dosen Tutorial 2
untuk tutorial 2 sendiri saya tidak mengalami masalah sehingga semua berjalan lancar, jadi saya tidak punya feedback untuk asdos



