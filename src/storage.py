# d:\POLMAN\Kuliah Polman\Arsitektur dan Organisasi Komputer (Semester 3)\MiniFileSystem\src\storage.py
import pickle
from typing import Optional

from .filesystem import FileSystem

def save_filesystem(fs: FileSystem, path: str):
    """Menyimpan objek FileSystem ke file biner menggunakan pickle."""
    try:
        with open(path, 'wb') as f:
            pickle.dump(fs, f)
        print(f"Sistem file berhasil disimpan ke {path}")
    except IOError as e:
        print(f"Error saat menyimpan file: {e}")

def load_filesystem(path: str) -> Optional[FileSystem]:
    """Memuat objek FileSystem dari file biner."""
    try:
        with open(path, 'rb') as f:
            fs = pickle.load(f)
            print(f"Sistem file berhasil dimuat dari {path}")
            return fs
    except FileNotFoundError:
        print("File penyimpanan tidak ditemukan. Membuat sistem file baru.")
        return FileSystem()
    except (IOError, pickle.UnpicklingError) as e:
        print(f"Error saat memuat file: {e}. Membuat sistem file baru.")
        return FileSystem()
