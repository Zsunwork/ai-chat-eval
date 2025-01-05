from setuptools import setup, find_packages

setup(
    name="AIChatEval",
    version="0.1.0",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Zhendong Sun",
    author_email="zsunforwork@outlook.com",
    url="https://github.com/Zsunwork/ai-chat-eval",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy",  # Add your dependencies here
        "openai"
    ],
)
