import pytest # type: ignore
from src.filesystem import FileSystem

@pytest.fixture
def fs():
    """Menyediakan instance FileSystem yang baru untuk setiap test."""
    return FileSystem()


def test_initial_state(fs: FileSystem):
    """Test bahwa filesystem dimulai dengan benar di root."""
    assert fs.current_directory == fs.root
    assert fs.root.name == "/"
    assert fs.pwd() == "/"


def test_mkdir(fs: FileSystem):
    """Test fungsionalitas membuat direktori."""
    result = fs.mkdir("docs")
    assert "berhasil dibuat" in result
    assert "docs" in fs.current_directory.children
    assert fs.current_directory.children["docs"].is_directory

    result_fail = fs.mkdir("docs")
    assert "sudah ada" in result_fail


def test_touch_and_ls(fs: FileSystem):
    """Test membuat file dan menampilkannya dengan ls."""
    fs.touch("file1.txt")
    fs.mkdir("mydir")

    contents = fs.ls()
    assert "file1.txt" in contents
    assert "mydir" in contents
    assert sorted(contents) == ["file1.txt", "mydir"]

def test_rm_file(fs: FileSystem):
    """Test menghapus file."""
    fs.touch("deleteme.txt")
    assert "deleteme.txt" in fs.ls()
    
    result = fs.rm("deleteme.txt")
    assert "berhasil dihapus" in result
    assert "deleteme.txt" not in fs.ls()

def test_rm_empty_directory(fs: FileSystem):
    """Test menghapus direktori kosong."""
    fs.mkdir("emptydir")
    assert "emptydir" in fs.ls()

    result = fs.rm("emptydir")
    assert "berhasil dihapus" in result
    assert "emptydir" not in fs.ls()

def test_rm_non_empty_directory_fails(fs: FileSystem):
    """Test bahwa rm gagal pada direktori yang tidak kosong."""
    fs.mkdir("fulldir")
    fs.cd("fulldir")
    fs.touch("somefile.txt")
    fs.cd("..")

    result = fs.rm("fulldir")
    assert "tidak kosong" in result
    assert "fulldir" in fs.ls()

def test_mv_file(fs: FileSystem):
    """Test memindahkan (mengubah nama) file."""
    fs.touch("original.txt")
    fs.write("original.txt", "test content")
    
    result = fs.mv("original.txt", "renamed.txt")
    assert "berhasil dipindahkan" in result
    assert "original.txt" not in fs.ls()
    assert "renamed.txt" in fs.ls()
    assert fs.cat("renamed.txt") == "test content"