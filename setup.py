from setuptools import setup, find_namespace_packages

setup(
    name="Bot-helper Boris",
    version="2.0.0",
    author="MRTeam",
    url="https://github.com/K2-TyMaH/Bot_helper_Boris",
    license="MIT License",
    packages=find_namespace_packages(),
    entry_points={"console_scripts": ["boris = t_bot.main:main"]}
)