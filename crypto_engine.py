from pathlib import Path
from cryptography.fernet import Fernet


def load_or_create_key(base_dir: Path) -> Fernet:
    key_dir = base_dir / ".secureai"
    key_dir.mkdir(parents=True, exist_ok=True)
    key_path = key_dir / "fernet.key"

    if key_path.exists():
        key = key_path.read_bytes()
    else:
        key = Fernet.generate_key()
        key_path.write_bytes(key)

    return Fernet(key)


def encrypt_file(source: Path, target: Path, fernet: Fernet) -> None:
    data = source.read_bytes()
    encrypted = fernet.encrypt(data)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(encrypted)
