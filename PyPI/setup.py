from setuptools import setup, find_packages

setup(
    name="mlotsawa",
    version="1.0.0",
    author="Jacob Moore",
    description="The purpose of this module is user-friendly translation and transliteration of Classical Tibetan.",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "flask",
        "threading",
        "transformers",
        "torch",
        "waitress",
        "webbrowser"
    ],
)
