from setuptools import setup

dist = setup(name="monopolymath",
             author="Thomas McClintock",
             author_email="mcclintock@bnl.gov",
             description="Tool for simulating Monopoly.",
             license="MIT",
             url="https://github.com/tmcclintock/MonopolyMath",
             python_requires='>=3.5',
             packages=['monopolymath'],
             long_description=open("README.md").read()
)
