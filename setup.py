from setuptools import setup, find_packages

setup(
    name = 'survival-datasets', 
    version = '0.1.2',
    description = 'Data loader for common datasets in Survival Analysis.',
    packages = find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    author = 'Christian Marius Lillelund',
    author_email = 'chr1000@gmail.com',
    
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",

    url='https://github.com/thecml/survival-datasets',

    classifiers  = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Operating System :: OS Independent',
    ],
    
    install_requires = [
        'scikit-survival ~= 0.17.2',
        'pandas ~= 1.4.3',
        'numpy ~= 1.22.4',
        'shap ~= 0.41.0',
        'pyarrow ~= 11.0.0',
    ],
    
    keywords = ['Survival Analysis', 'Datasets'],
    
)
