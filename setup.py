from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="student_quiz_analyzer",  # Name of your package
    version="1.0.0",  # Version of your package
    author="Riddhima Yadav",  # Your name
    author_email="riddhima9898@gmail.com",  # Your email
    description="A tool to analyze student quiz performance and provide personalized recommendations.",  # Short description
    long_description=open("README.md").read(),  # Long description from README.md
    long_description_content_type="text/markdown",  # Type of long description
    url="https://github.com/riddhima29/personalized_quiz_performance_analyzer",  # Project URL
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=requirements,  # Dependencies from requirements.txt
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires=">=3.8",  # Minimum Python version required
    entry_points={
        "console_scripts": [
            "personalised_quiz_performance_analyzer=quiz_performance_analyser:main",  # Command-line tool
        ],
    },
)