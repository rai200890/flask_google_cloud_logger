from setuptools import setup

setup(
    name="flask_google_cloud_logger",
    version="0.0.1",
    description="Google Cloud Log Formatter for Flask",
    url="http://github.com/rai200890/flask_google_cloud_logger",
    author="Raissa Ferreira",
    author_email="rai200890@gmail.com",
    license="MIT",
    packages=["flask_google_cloud_logger"],
    install_requires=[
        "google_cloud_logger>=0.0.2",
        "flask>=1.0",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: System :: Logging"
    ],
    zip_safe=False)
