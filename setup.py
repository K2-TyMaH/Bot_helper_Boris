from setuptools import setup, find_namespace_packages

setup(
    name="Best bot",
    version="1.0.0",
    author="Best team",
    url="https://github.com/LevytskyiS/t_bot",
    license="MIT License",
    packages=find_namespace_packages(),
    entry_points={"console_scripts": ["best_bot = t_bot.main:main"]}
)