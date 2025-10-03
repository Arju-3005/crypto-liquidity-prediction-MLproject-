from setuptools import setup, find_packages

setup(
    name='Crypto-Liquidity-Prediction',
    version='1.0.0',
    description='Machine Learning project to predict cryptocurrency liquidity for market stability',
    author='[Your Name]',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'xgboost',
        'matplotlib',
        'seaborn',
        'streamlit'
    ],
    entry_points={
        'console_scripts': [
            'run_prediction=src.train:main',  # example script to run training
        ],
    },
)
