# Mini File System

Sebuah simulator sistem file berbasis command-line yang dibuat dengan Python. Proyek ini merupakan implementasi praktis dari konsep-konsep dasar Arsitektur dan Organisasi Komputer, khususnya mengenai cara sistem file mengelola data, direktori, dan path.

## Fitur Utama

- **Navigasi Direktori:** `ls`, `cd`, `pwd`
- **Manipulasi File & Direktori:** `mkdir`, `touch`, `rm`, `cp`, `mv`
- **Inspeksi Konten & Metadata:** `cat`, `stat`, `tree`, `find`
- **Modifikasi Konten File:** `write` (timpa), `append` (tambah), `replace` (ganti)
- **Persistensi Data:** Keadaan sistem file secara otomatis disimpan ke `minifs.dat` saat keluar dan dimuat saat dimulai.

---

## Struktur Proyek

```
MiniFileSystem/
├── src/
│   ├── cli.py          # Layer Antarmuka: Menerima input & menampilkan output.
│   ├── filesystem.py   # Layer Logika: Otak dari semua operasi sistem file.
│   ├── file_node.py    # Layer Model Data: Mendefinisikan struktur file & direktori.
│   └── storage.py      # Layer Persistensi: Menangani simpan/muat state.
├── tests/
│   └── test_*.py       # Layer Jaminan Kualitas: Tes otomatis untuk setiap komponen.
├── main.py             # Titik masuk (entry point) untuk menjalankan aplikasi.
├── requirements.txt    # Daftar dependensi proyek.
└── README.md           # Anda sedang membacanya.
```

---

## Instalasi & Setup

1.  **Clone Repositori**
    ```bash
    git clone <url_repositori_anda>
    cd MiniFileSystem
    ```

2.  **Buat dan Aktifkan Virtual Environment**
    ```bash
    # Buat environment
    python -m venv venv

    # Aktifkan di Windows
    .\venv\Scripts\activate

    # Aktifkan di macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependensi**
    ```bash
    pip install -r requirements.txt
    ```

---

## Cara Penggunaan

1.  **Jalankan Aplikasi**
    ```bash
    python main.py
    ```
    Anda akan disambut dengan prompt `minifs:/$`.

2.  **Interaksi**
    Gunakan perintah-perintah yang tersedia untuk berinteraksi dengan sistem file.

3.  **Keluar**
    Ketik `exit` atau tekan `Ctrl+C`. Keadaan sistem file Anda akan otomatis tersimpan dalam file `minifs.dat`. Saat Anda menjalankan aplikasi lagi, semua file dan direktori Anda akan ada kembali.

---

## Panduan Perintah

### Navigasi & Inspeksi
| Perintah | Contoh Penggunaan | Deskripsi |
|---|---|---|
| `ls [path]` | `ls`, `ls /polman` | Menampilkan isi direktori. Direktori ditandai dengan `/`. |
| `cd <path>` | `cd polman`, `cd ../` | Pindah ke direktori lain. |
| `pwd` | `pwd` | Menampilkan path direktori saat ini. |
| `find <nama>` | `find profil.txt` | Mencari file atau direktori di seluruh sistem. |
| `stat <path>` | `stat /polman/profil.txt` | Menampilkan informasi detail (metadata) dari file/direktori. |
| `tree [path]` | `tree`, `tree /polman` | Menampilkan struktur direktori dalam bentuk pohon. |

### Manipulasi File & Direktori
| Perintah | Contoh Penggunaan | Deskripsi |
|---|---|---|
| `mkdir <dir>` | `mkdir tugas` | Membuat direktori baru. |
| `touch <file>` | `touch catatan.txt` | Membuat file kosong baru. |
| `cat <file>` | `cat catatan.txt` | Menampilkan isi konten sebuah file. |
| `write <file> "..."` | `write file.txt "Halo Dunia"` | Menimpa seluruh isi file dengan konten baru. |
| `append <file> "..."` | `append file.txt " Baris baru."` | Menambahkan konten ke akhir file yang sudah ada. |
| `replace <file> "A" "B"` | `replace file.txt "Halo" "Hai"` | Mengganti semua teks "A" menjadi "B" di dalam file. |
| `rm <path>` | `rm catatan.txt` | Menghapus file atau direktori **kosong**. |
| `cp <src> <dest>` | `cp file.txt /tugas/` | Menyalin file ke lokasi baru. |
| `mv <src> <dest>` | `mv file.txt file_baru.txt` | Memindahkan atau mengubah nama file. |

### Utilitas
| Perintah | Deskripsi |
|---|---|
| `save` | Menyimpan state sistem file secara manual. |
| `load` | Memuat state sistem file secara manual dari `minifs.dat`. |
| `clear` | Membersihkan layar konsol. |
| `help` | Menampilkan daftar semua perintah yang tersedia. |
| `exit` | Keluar dari aplikasi dan menyimpan state. |

---

## Pengujian (Testing)

Proyek ini dilengkapi dengan unit test untuk memastikan setiap fungsi berjalan dengan benar. Untuk menjalankan tes:

```bash
# Jalankan semua tes
pytest

# Jalankan tes dengan laporan cakupan (coverage)
pytest --cov=src
```

---

## Kontributor

- Azfa Hafshiam Dilaga (2224443002)
- Bintang Shobri Al Chakim (224443003)
- Lukita Falencia Marjan (224443009)
- Muhammad Basit Rozak Akbar S.P (224443012)
- Muhammad Daffi Izzuddin (224443013)
- Raden Aryo Dwiputra Permana (224443017)


