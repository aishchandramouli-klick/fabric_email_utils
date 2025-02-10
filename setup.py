from setuptools import setup, find_packages

setup(
    name="fabric_email_utils",
    version="0.1.0",
    author="achandramouli@klick.com",
    packages=find_packages(),
    description="A package to send emails using smtplib",
    url=" https://github.com/aishchandramouli-klick/fabric_email_utils",
    install_requires=[
        "smtplib",
        "email"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)