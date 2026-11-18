"""Copy the entry image to the make.fun output directory.

Stdlib only. The image is generated artwork held in this repository
(entry.png); this program only copies it to the output directory, so
every run writes the same bytes.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(output_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(data)
    # Deterministic check: the output must be byte-identical to the source.
    assert os.path.getsize(dst) == len(data)


if __name__ == "__main__":
    main()
