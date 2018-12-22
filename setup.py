from setuptools import setup

dist = setup(name="monopolymath",
             author="Thomas McClintock",
             author_email="mcclintock@bnl.gov",
             description="Tool for simulating Monopoly.",
             license="MIT",
             url="https://github.com/tmcclintock/MonopolyMath",
             packages=['monopolymath'],
             long_description=open("README.md").read()
)
