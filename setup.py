import setuptools

setuptools.setup(
    name="better-id3",
    version="DEV",
    url="https://github.com/dAymericBebert/Better-ID3",

    author="Aymeric BERNARD",
    author_email="nope@example.com",

    description="Entity Extractor Module",

    zip_safe=False,
    platforms="any",

    install_requires=[
        "fire>=0.1.2,<0.2",
        "configue>=3.0.3,<3.1",
        "illuin-logging==2.1.1",
        "marshmallow>=3.3.0,<3.4",
        "attrs==19.3.0",
        "tqdm>=4.41.0,<5",
    ],
    python_requires=">=3.6,<4.0",
    packages=setuptools.find_packages(include=["better_id3", "better_id3.*"]),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
