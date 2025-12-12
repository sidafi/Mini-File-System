from datetime import datetime
from typing import Dict, Optional

class FileNode:
    """Mewakili sebuah node dalam sistem file, bisa berupa file atau direktori."""
    def __init__(self, name: str, is_directory: bool = False):
        self.name = name
        self.is_directory = is_directory
        self.size = 0
        now = datetime.now()
        self.created_at = now
        self.modified_at = now
        self.children: Optional[Dict[str, 'FileNode']] = {} if is_directory else None
        self.content = "" if not is_directory else None

    def get_info(self):
        """Mengembalikan informasi dasar tentang node."""
        return f"Name: {self.name}, Type: {'Directory' if self.is_directory else 'File'}, Size: {self.size} bytes"
    
    def __repr__(self) -> str:
        return f"FileNode(name='{self.name}', is_directory={self.is_directory})"
