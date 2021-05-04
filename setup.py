from setuptools import setup

dist = setup(
    name="monopolymath",
    author="Thomas McClintock",
    author_email="mcclintock@bnl.gov",
    description="Tool for simulating Monopoly.",
    license="MIT",
    url="https://github.com/tmcclintock/MonopolyMath",
    python_requires=">=3.5",
    packages=["monopolymath"],
    package_dir={"monopolymath": "monopolymath"},
    package_data={"monopolymath": ["*.txt"]},
    include_package_data=True,
    long_description=open("README.md").read(),
)
