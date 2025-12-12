# d:\POLMAN\Kuliah Polman\Arsitektur dan Organisasi Komputer (Semester 3)\MiniFileSystem\src\filesystem.py
from datetime import datetime
from typing import List, Optional

from .file_node import FileNode

class FileSystem:
    """Mengelola seluruh struktur sistem file, termasuk operasi file."""
    def __init__(self):
        self.root = FileNode("/", is_directory=True)
        self.current_directory = self.root

    def _get_path(self, target_node: FileNode) -> str:
        """
        Helper untuk mendapatkan path lengkap dari sebuah node."""
        if target_node == self.root:
            return "/"

        path_parts = []
        current = target_node
        
        def find_path_recursive(node: FileNode, target: FileNode, current_path_parts: List[str]) -> Optional[List[str]]:
            if node == target:
                return current_path_parts
            if node.is_directory and node.children:
                for name, child in node.children.items():
                    result = find_path_recursive(child, target, current_path_parts + [name])
                    if result:
                        return result
            return None

        found_path_parts = find_path_recursive(self.root, target_node, [])
        if found_path_parts:
            return "/" + "/".join(found_path_parts)
        return "" 

    def pwd(self) -> str:
        """Mendapatkan path lengkap dari direktori saat ini."""
        return self._get_path(self.current_directory)

    def _resolve_path(self, path: str) -> Optional[FileNode]:
        """
        Mengurai path (absolut atau relatif) dan mengembalikan node yang sesuai.
        Menangani '.' dan '..'.
        Ini adalah helper internal untuk _find_node.
        """
        if not path:
            return self.current_directory
        if path == "/":
            return self.root

        if path.startswith('/'):
            start_node = self.root
            path_parts = path.strip('/').split('/')
        else:
            
            start_node = self.current_directory
            path_parts = path.split('/')

        if not path_parts or (len(path_parts) == 1 and path_parts[0] == ''): 
            return self.root
        if path == '.': 
            return start_node

        
        path_stack = []
        if path.startswith('/'):
            
            pass
        else:
            
            path_stack.extend(self._get_path(self.current_directory).strip('/').split('/'))

        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            if part == '..':
                if path_stack:
                    path_stack.pop()
            else:
                path_stack.append(part)

        
        final_path = "/" + "/".join(filter(None, path_stack))
        
        current = self.root 
        for part in final_path.strip('/').split('/'):
            if part and current.is_directory and part in current.children: # type: ignore
                current = current.children[part] # type: ignore
            else:
                
                if final_path == "/" and part == '':
                    return self.root
                return None 
        return current if final_path != "/" else self.root

    def _find_node(self, path: str) -> Optional[FileNode]:
        """Mencari node berdasarkan path. Mendukung path absolut dan relatif."""
        return self._resolve_path(path)

    def ls(self, path: str = ".") -> List[str]:
        """Menampilkan isi dari sebuah direktori."""
        target_node = self._find_node(path)
        if target_node is None:
            return [f"Error: Path '{path}' tidak ditemukan."]
        if not target_node.is_directory:
            return [f"Error: '{path}' bukan direktori."]
        
        output = []
        if target_node.children:
            for name, node in target_node.children.items():
                if node.is_directory:
                    output.append(f"{name}/") 
                else:
                    output.append(name)
        return sorted(output)

    def mkdir(self, dir_name: str) -> str:
        """Membuat direktori baru."""
        if '/' in dir_name:
            return "Error: Nama direktori tidak boleh mengandung '/'."
        if dir_name in self.current_directory.children:
            return f"Error: Direktori '{dir_name}' sudah ada."
        
        new_dir = FileNode(dir_name, is_directory=True)
        self.current_directory.children[dir_name] = new_dir # type: ignore
        self.current_directory.modified_at = datetime.now()
        return f"Direktori '{dir_name}' berhasil dibuat."

    def touch(self, file_name: str) -> str:
        """Membuat file kosong baru."""
        if '/' in file_name:
            return "Error: Nama file tidak boleh mengandung '/'."
        if file_name in self.current_directory.children:
            return f"Error: File '{file_name}' sudah ada."

        new_file = FileNode(file_name, is_directory=False) 
        self.current_directory.children[file_name] = new_file # type: ignore
        self.current_directory.modified_at = datetime.now()
        return f"File '{file_name}' berhasil dibuat."

    def cat(self, file_name: str) -> str:
        """Membaca isi file."""
        node = self._find_node(file_name)
        if node and not node.is_directory:
            return node.content # type: ignore
        return f"Error: File '{file_name}' tidak ditemukan atau adalah direktori."

    def write(self, file_name: str, content: str) -> str:
        """Menulis konten ke file. Akan menimpa konten yang ada."""
        node = self._find_node(file_name)
        if node and not node.is_directory:
            node.content = content
            node.size = len(content.encode('utf-8')) # type: ignore
            node.modified_at = datetime.now()
            return f"Konten berhasil ditulis ke '{file_name}'."
        return f"Error: File '{file_name}' tidak ditemukan atau adalah direktori."

    def append(self, file_name: str, content: str) -> str:
        """Menambahkan konten ke akhir file yang sudah ada."""
        node = self._find_node(file_name)
        if node and not node.is_directory:
            node.content += content # type: ignore
            node.size = len(node.content.encode('utf-8')) # type: ignore
            node.modified_at = datetime.now()
            return f"Konten berhasil ditambahkan ke '{file_name}'."
        return f"Error: File '{file_name}' tidak ditemukan atau adalah direktori."

    def replace(self, file_name: str, to_find: str, to_replace: str) -> str:
        """Mengganti semua kemunculan sebuah string di dalam file."""
        node = self._find_node(file_name)
        if not (node and not node.is_directory):
            return f"Error: File '{file_name}' tidak ditemukan atau adalah direktori."

        original_content = node.content
        if to_find not in original_content: # type: ignore
            return f"Info: Teks '{to_find}' tidak ditemukan di dalam file '{file_name}'. Tidak ada yang diubah."

        node.content = original_content.replace(to_find, to_replace) # type: ignore
        node.size = len(node.content.encode('utf-8')) # type: ignore
        node.modified_at = datetime.now()
        return f"Konten di dalam '{file_name}' berhasil diubah."

    def cd(self, path: str) -> str:
        """Mengubah direktori saat ini."""
        target_node = self._resolve_path(path)

        if target_node and target_node.is_directory:
            self.current_directory = target_node
            return f"Berpindah ke direktori: {self._get_path(self.current_directory)}"
        return f"Error: Direktori '{path}' tidak ditemukan."

    def find(self, name: str) -> List[str]:
        """Mencari file atau direktori berdasarkan nama di seluruh sistem file."""
        results = []

        def _find_recursive(node: FileNode, current_path: str):
            if node.name == name and node != self.root:
                results.append(current_path)

            if node.is_directory and node.children:
                for child_name, child_node in node.children.items():
                    child_path = f"{current_path.rstrip('/')}/{child_name}"
                    _find_recursive(child_node, child_path)

        _find_recursive(self.root, "/")
        return results

    def stat(self, path: str) -> str:
        """Menampilkan metadata dari sebuah file atau direktori."""
        node = self._find_node(path)
        if not node:
            return f"Error: '{path}' tidak ditemukan."

        node_type = "Directory" if node.is_directory else "File"
        info = [
            f"  File: {node.name}",
            f"  Type: {node_type}",
            f"  Size: {node.size} bytes",
            f"  Created: {node.created_at.strftime('%Y-%m-%d %H:%M:%S')}",
            f"  Modified: {node.modified_at.strftime('%Y-%m-%d %H:%M:%S')}"
        ]
        return "\n".join(info)

    def tree(self, path: str = ".") -> str:
        """Menampilkan struktur direktori dalam format pohon."""
        start_node = self._find_node(path)
        if not start_node:
            return f"Error: Path '{path}' tidak ditemukan."
        if not start_node.is_directory:
            return f"Error: '{path}' bukan direktori."

        tree_lines = [start_node.name]
        
        def _tree_recursive(node: FileNode, prefix: str):
            children = sorted(node.children.keys()) # type: ignore
            for i, name in enumerate(children):
                connector = "└── " if i == len(children) - 1 else "├── "
                tree_lines.append(f"{prefix}{connector}{name}")
                child_node = node.children[name] # type: ignore
                if child_node.is_directory:
                    extension = "    " if i == len(children) - 1 else "│   "
                    _tree_recursive(child_node, prefix + extension)

        _tree_recursive(start_node, "")
        return "\n".join(tree_lines)

    def _find_parent_and_name(self, path: str) -> tuple[Optional[FileNode], Optional[str]]:
        """Helper untuk menemukan node parent dan nama dari item di path."""
        if not path or '/' in path:
            parts = path.rstrip('/').split('/')
            name = parts[-1]
            parent_path = "/".join(parts[:-1])
            if not parent_path and path.startswith('/'): 
                parent_path = "/"
            elif not parent_path: 
                parent_path = "."
            parent_node = self._find_node(parent_path)
        else:
            name = path
            parent_node = self.current_directory

        if not parent_node or not parent_node.is_directory:
            return None, None
        return parent_node, name

    def rm(self, path: str) -> str:
        """Menghapus file atau direktori kosong."""
        node_to_delete = self._find_node(path)
        if not node_to_delete:
            return f"Error: '{path}' tidak ditemukan."
        if node_to_delete == self.root:
            return "Error: Tidak dapat menghapus direktori root."
        if node_to_delete.is_directory and node_to_delete.children:
            return f"Error: Direktori '{path}' tidak kosong."

        parent, name = self._find_parent_and_name(path)
        if parent and name and name in parent.children: # type: ignore
            del parent.children[name] # type: ignore
            parent.modified_at = datetime.now()
            return f"'{path}' berhasil dihapus."
        return f"Error: Gagal menghapus '{path}' (parent tidak ditemukan)."

    def cp(self, source_path: str, dest_path: str) -> str:
        """Menyalin file. Penyalinan direktori belum didukung."""
        source_node = self._find_node(source_path)
        if not source_node:
            return f"Error: Sumber '{source_path}' tidak ditemukan."
        if source_node.is_directory:
            return "Error: Penyalinan direktori belum didukung."

        dest_parent_node = self._find_node(dest_path)
        if dest_parent_node and dest_parent_node.is_directory:
            dest_name = source_node.name
            if dest_name in dest_parent_node.children: # type: ignore
                return f"Error: File '{dest_name}' sudah ada di tujuan '{dest_path}'."
        else: 
            dest_parent_node, dest_name = self._find_parent_and_name(dest_path)
            if not dest_parent_node or not dest_name:
                return f"Error: Path tujuan '{dest_path}' tidak valid."

        new_file = FileNode(dest_name, is_directory=False)
        new_file.content = source_node.content
        new_file.size = source_node.size
        
        dest_parent_node.children[dest_name] = new_file # type: ignore
        dest_parent_node.modified_at = datetime.now()
        return f"File '{source_path}' berhasil disalin ke '{dest_path}'."

    def mv(self, source_path: str, dest_path: str) -> str:
        """Memindahkan atau mengubah nama file/direktori."""
        source_node = self._find_node(source_path)
        if not source_node:
            return f"Error: Sumber '{source_path}' tidak ditemukan."

        dest_node_check = self._find_node(dest_path)
        if dest_node_check and dest_node_check.is_directory:
            dest_parent_node = dest_node_check
            dest_name = source_node.name
            if dest_name in dest_parent_node.children: # type: ignore
                return f"Error: '{dest_name}' sudah ada di direktori tujuan '{dest_path}'."
        else:
            dest_parent_node, dest_name = self._find_parent_and_name(dest_path)
            if not dest_parent_node or not dest_name:
                return f"Error: Path tujuan '{dest_path}' tidak valid."

        source_parent, source_name = self._find_parent_and_name(source_path)
        if not source_parent or not source_name:
            return f"Error: Gagal menemukan parent dari '{source_path}'."
        del source_parent.children[source_name] # type: ignore
        source_parent.modified_at = datetime.now()

        source_node.name = dest_name
        dest_parent_node.children[dest_name] = source_node # type: ignore
        dest_parent_node.modified_at = datetime.now()
        
        return f"Berhasil memindahkan/mengubah '{source_path}' ke '{dest_path}'."
