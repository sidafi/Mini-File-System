import os
from src.filesystem import FileSystem
from src.storage import save_filesystem, load_filesystem

def test_save_and_load_cycle(tmp_path):
    """
    Test siklus lengkap: buat data -> simpan -> muat -> verifikasi data.
    `tmp_path` adalah fixture dari pytest yang menyediakan direktori sementara.
    """
    storage_file = tmp_path / "test_fs.dat"

    fs_original = FileSystem()
    fs_original.mkdir("data")
    fs_original.cd("data")
    fs_original.write("report.txt", "Ini adalah laporan rahasia.")

    save_filesystem(fs_original, str(storage_file))

    fs_loaded = load_filesystem(str(storage_file))

    assert fs_loaded is not None
    assert fs_loaded.cat("data/report.txt") == "Ini adalah laporan rahasia."