import os
from pathlib import Path

from setuptools import setup
from setuptools.command.build_py import build_py

ROOT = Path(__file__).parent
EXCLUDED_DIRS = {".git", ".github", "__pycache__", "build", "dist"}


def discover_packages() -> list[str]:
    packages = {"leadping"}

    for directory in ROOT.rglob("*"):
        if not directory.is_dir():
            continue

        relative = directory.relative_to(ROOT)
        if any(part in EXCLUDED_DIRS or part.startswith(".") for part in relative.parts):
            continue

        if any(child.suffix == ".py" for child in directory.iterdir() if child.is_file()):
            packages.add("leadping." + ".".join(relative.parts))

    return sorted(packages)


class BuildPyWithoutSetupModule(build_py):
    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        return [module for module in modules if module[1] != "setup"]


setup(
    name="leadping",
    version=os.environ.get("PACKAGE_VERSION", "0.0.0"),
    description="Typed Python client for the Leadping API, generated from the Leadping OpenAPI document with Microsoft Kiota.",
    long_description=(ROOT / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/leadpingai/leadping-python",
    author="Leadping",
    license="MIT",
    packages=discover_packages(),
    package_dir={"leadping": "."},
    cmdclass={"build_py": BuildPyWithoutSetupModule},
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "microsoft-kiota-abstractions>=1.10.2,<2.0.0",
        "microsoft-kiota-serialization-form>=1.10.2,<2.0.0",
        "microsoft-kiota-serialization-json>=1.10.2,<2.0.0",
        "microsoft-kiota-serialization-multipart>=1.10.2,<2.0.0",
        "microsoft-kiota-serialization-text>=1.10.2,<2.0.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Typing :: Typed",
    ],
)
