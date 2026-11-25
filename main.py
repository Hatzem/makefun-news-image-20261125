"""Copy entry.png to the output directory, verifying it on the way.

Reads the image shipped next to this file, checks it is a PNG no larger
than 1 MiB and no bigger than 1024x1024, copies it to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output), and confirms the copy
is byte-identical by SHA-256. Standard library only, no network.
"""

import hashlib
import os
import struct
import sys

MAX_BYTES = 1048576
MAX_SIDE = 1024


def png_dimensions(data):
    """Return (width, height) from a PNG header, or None if not a PNG."""
    if len(data) < 33 or data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    if data[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    with open(source, "rb") as handle:
        blob = handle.read()

    if len(blob) > MAX_BYTES:
        print(f"entry.png is {len(blob)} bytes, over the 1048576 limit",
              file=sys.stderr)
        return 1
    dims = png_dimensions(blob)
    if dims is None:
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    width, height = dims
    if width > MAX_SIDE or height > MAX_SIDE:
        print(f"entry.png is {width}x{height}, over the 1024x1024 limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(blob)

    with open(target, "rb") as handle:
        copied = handle.read()
    digest = hashlib.sha256(blob).hexdigest()
    if hashlib.sha256(copied).hexdigest() != digest:
        print("copy does not match the source", file=sys.stderr)
        return 1

    print(f"entry.png: {len(blob)} bytes, {width}x{height}, sha256 {digest}")
    print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
