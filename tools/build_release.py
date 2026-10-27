"""Package the two native pet files without account-specific data. Python 3 stdlib."""
from pathlib import Path
import hashlib
import json
import struct
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PET = ROOT / "pet" / "sandrone-refined"
VERSION = "1.0.0"


def main():
    manifest = json.loads((PET / "pet.json").read_text(encoding="utf-8"))
    assert manifest["id"] == "sandrone-refined"
    assert manifest["spriteVersionNumber"] == 2
    assert manifest["spritesheetPath"] == "spritesheet.png"
    sprite = (PET / "spritesheet.png").read_bytes()
    assert sprite[:8] == b"\x89PNG\r\n\x1a\n"
    assert struct.unpack(">II", sprite[16:24]) == (1536, 2288)
    assert len(sprite) <= 20 * 1024 * 1024
    summary = json.loads((ROOT / "docs" / "validation.json").read_text(encoding="utf-8"))
    assert hashlib.sha256(sprite).hexdigest() == summary["sha256"], "Revalidate changed art before release"
    out = ROOT / "downloads"
    out.mkdir(exist_ok=True)
    package = out / f"Sandrone-Refined-v{VERSION}.zip"
    entries = {
        "sandrone-refined/pet.json": (PET / "pet.json").read_bytes(),
        "sandrone-refined/spritesheet.png": sprite,
        "INSTALL.md": (ROOT / "INSTALL.md").read_bytes(),
        "ASSET-LICENSE.md": (ROOT / "ASSET-LICENSE.md").read_bytes(),
    }
    with zipfile.ZipFile(package, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, contents in entries.items():
            info = zipfile.ZipInfo(name, (2026, 10, 27, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, contents)
    with zipfile.ZipFile(package) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == set(entries)
        assert archive.read("sandrone-refined/spritesheet.png") == sprite
    hashes = [
        f"{hashlib.sha256(package.read_bytes()).hexdigest()}  {package.name}",
        f"{hashlib.sha256(sprite).hexdigest()}  ../pet/sandrone-refined/spritesheet.png",
    ]
    (out / "SHA256SUMS.txt").write_text("\n".join(hashes) + "\n", encoding="utf-8")
    print(json.dumps({"package": package.name, "bytes": package.stat().st_size, "verified": True}))


if __name__ == "__main__":
    main()
