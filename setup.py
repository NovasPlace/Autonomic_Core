from setuptools import setup, find_packages

setup(
    name="autonomic_core",
    version="1.0.0",
    description="Autonomic immune system and cognitive routing substrate for autonomous LLM agents.",
    author="frost",
    packages=find_packages(),
    install_requires=[
        "pydantic",
        "requests",
        "scikit-learn",
        # Dependencies imported from Sovereign Engine Core that are strictly required for the organs
    ],
    python_requires=">=3.10",
    include_package_data=True,
    package_data={
        "autonomic_core": ["anchors/*.pt"],
    },
)
