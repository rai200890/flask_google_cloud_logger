from setuptools import setup

__VERSION__ = "0.1.0"

setup(
    name="flask_google_cloud_logger",
    version=__VERSION__,
    description="Google Cloud Log Formatter for Flask",
    url="http://github.com/rai200890/flask_google_cloud_logger",
    author="Raissa Ferreira",
    author_email="rai200890@gmail.com",
    license="MIT",
    packages=["flask_google_cloud_logger"],
    install_requires=[
        "google_cloud_logger>=0.1.0",
        "flask>=1.0",
    ],
    classifiers=[
        "Environment :: Web Environment", "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English", "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: System :: Logging"
    ],
    zip_safe=False)
