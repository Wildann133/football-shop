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


