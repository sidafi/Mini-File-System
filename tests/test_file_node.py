from src.file_node import FileNode
from datetime import datetime

def test_create_file_node():
    """Test pembuatan node untuk sebuah file."""
    file = FileNode("test.txt", is_directory=False)
    assert file.name == "test.txt"
    assert not file.is_directory
    assert file.content == ""
    assert file.children is None
    assert isinstance(file.created_at, datetime)

def test_create_directory_node():
    """Test pembuatan node untuk sebuah direktori."""
    directory = FileNode("docs", is_directory=True)
    assert directory.name == "docs"
    assert directory.is_directory
    assert directory.content is None
    assert directory.children == {}

def test_repr():
    """Test representasi string dari node."""
    file = FileNode("image.jpg")
    assert repr(file) == "FileNode(name='image.jpg', is_directory=False)"