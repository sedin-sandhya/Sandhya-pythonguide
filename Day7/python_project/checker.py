import importlib


packages = [
    "requests",
    "pandas",
    "numpy",
    "nonexistent"
]


for package in packages:

    try:

        importlib.import_module(package)

        print(f"OK {package}")

    except ImportError:

        print(f"MISS {package}")