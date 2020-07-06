from setuptools import setup

APP_NAME = "bukdjango_captcha"

setup(
    name=APP_NAME,
    zip_safe=False,
    version="0.1",
    include_package_data=True,
    packages=[APP_NAME],
    python_requires=">=3.8",
    install_requires=[x for x in open('requirements.txt', 'r').readlines()],
)
