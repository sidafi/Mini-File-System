# d:\POLMAN\Kuliah Polman\Arsitektur dan Organisasi Komputer (Semester 3)\MiniFileSystem\src\cli.py
from .filesystem import FileSystem
import shlex
from src.storage import save_filesystem, load_filesystem

STORAGE_FILE = "minifs.dat"

class CLI:
    """Command Line Interface untuk berinteraksi dengan sistem file mini."""
    def __init__(self):
        self.fs = load_filesystem(STORAGE_FILE)
        if self.fs is None:
            self.fs = FileSystem()

    def run(self):
        """Menjalankan loop utama CLI."""
        print("Selamat datang di Mini File System!")
        print("Ketik 'help' untuk melihat daftar perintah.")
        
        while True:
            current_path_prompt = self.fs.pwd()
            
            try:
                command_line = input(f"minifs:{current_path_prompt}$ ").strip()
                if not command_line:
                    continue

                try:
                    parts = shlex.split(command_line)
                except ValueError:
                    print("Error: Kutipan tidak ditutup dengan benar.")
                    continue
                command = parts[0]
                args = parts[1:]

                if command == "exit":
                    save_filesystem(self.fs, STORAGE_FILE)
                    print("Selamat tinggal!")
                    break
                
                self.handle_command(command, args)

            except KeyboardInterrupt:
                save_filesystem(self.fs, STORAGE_FILE)
                print("\nInterupsi diterima. Menyimpan state dan keluar.")
                break
            except Exception as e:
                print(f"Terjadi error tak terduga: {e}")


    def handle_command(self, command: str, args: list):
        """Memproses dan mengeksekusi perintah yang diberikan."""
        if command == "help":
            self.show_help()
        elif command == "ls":
            path = args[0] if args else "."
            result = self.fs.ls(path)
            if result:
                print("\n".join(result))
        elif command == "mkdir":
            if not args:
                print("Penggunaan: mkdir <nama_direktori>")
            else:
                print(self.fs.mkdir(args[0]))
        elif command == "touch":
            if not args:
                print("Penggunaan: touch <nama_file>")
            else:
                print(self.fs.touch(args[0]))
        elif command == "cd":
            if not args:
                print("Penggunaan: cd <path>")
            else:
                print(self.fs.cd(args[0]))
        elif command == "cat":
            if not args:
                print("Penggunaan: cat <nama_file>")
            else:
                print(self.fs.cat(args[0]))
        elif command == "write":
            if len(args) < 2:
                print('Penggunaan: write <nama_file> "konten file"')
            else:
                print(self.fs.write(args[0], args[1]))
        elif command == "append":
            if len(args) < 2:
                print('Penggunaan: append <nama_file> "konten tambahan"')
            else:
                print(self.fs.append(args[0], args[1]))
        elif command == "replace":
            if len(args) < 3:
                print('Penggunaan: replace <nama_file> "teks_lama" "teks_baru"')
            else:
                file_name = args[0]
                old_text = args[1]
                new_text = args[2]
                print(self.fs.replace(file_name, old_text, new_text))
        elif command == "pwd":
            print(self.fs.pwd())
        elif command == "rm":
            if not args:
                print("Penggunaan: rm <nama_file_atau_direktori>")
            else:
                print(self.fs.rm(args[0]))
        elif command == "cp":
            if len(args) < 2:
                print("Penggunaan: cp <sumber> <tujuan>")
            else:
                print(self.fs.cp(args[0], args[1]))
        elif command == "mv":
            if len(args) < 2:
                print("Penggunaan: mv <sumber> <tujuan>")
            else:
                print(self.fs.mv(args[0], args[1]))
        elif command == "stat":
            if not args:
                print("Penggunaan: stat <nama_file_atau_direktori>")
            else:
                print(self.fs.stat(args[0])) 
        elif command == "tree":
            path = args[0] if args else "."
            print(self.fs.tree(path)) 
        elif command == "find":
            if not args:
                print("Penggunaan: find <nama_file_atau_direktori>")
            else:
                results = self.fs.find(args[0])
                if results:
                    print("Ditemukan:")
                    for r in results:
                        print(r)
                else:
                    print("Tidak ditemukan.")
        elif command == "save":
            save_filesystem(self.fs, STORAGE_FILE)
        elif command == "load":
            self.fs = load_filesystem(STORAGE_FILE)
            if self.fs is None: 
                self.fs = FileSystem()
        elif command == "clear":
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print(f"Perintah tidak dikenal: {command}")


    def show_help(self):
        """Menampilkan pesan bantuan."""
        print("\nPerintah yang tersedia:")
        print("\n--- Navigasi & Inspeksi ---")
        print("  ls [path]         - Tampilkan isi direktori")
        print("  cd <path>         - Pindah ke direktori lain")
        print("  cd ..             - Kembali ke root/direktori sebelumnya")
        print("  pwd               - Tampilkan path direktori saat ini")
        print("  find <nama>       - Cari file atau direktori di seluruh sistem")
        print("  stat <path>       - Tampilkan informasi detail (metadata)")
        print("  tree              - Tampilkan struktur direktori dalam bentuk pohon")
        
        print("\n--- Manipulasi File & Direktori ---")
        print("  mkdir <dir_name>    - Buat direktori baru")
        print("  touch <file_name>   - Buat file kosong baru")
        print("  cat <file_name>     - Tampilkan isi file")
        print("  write <file> \"...\"- Tulis konten ke file")
        print("  append <file> \"...\" - Tambahkan konten ke akhir file")
        print("  replace <file> \"A\" \"B\" - Ganti semua teks \"A\" menjadi \"B\" di file")
        print("  rm <path>           - Hapus file atau direktori kosong")
        print("  cp <src> <dest>     - Salin file ke lokasi baru")
        print("  mv <src> <dest>     - Pindahkan atau ubah nama file")

        print("\n--- Utilitas ---")
        print("  save              - Simpan state sistem file")
        print("  load              - Muat state sistem file")
        print("  clear             - Bersihkan layar konsol")
        print("  help              - Tampilkan pesan ini")
        print("  exit(= ctrl+c)    - Keluar dari program dan simpan state")
        print()
