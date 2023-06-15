from setuptools import setup, find_packages

setup(
    name="resimpyx",
    # version="0.0.1",
    version="0.0.0.7",
    keywords=("pip", "resimpy"),
    description="REad SIMulation PY",
    long_description="sequencing read simulation python interface",
    license="MIT",

    url="https://github.com/cribbslab; https://github.com/2003100127",
    author="Jianfeng Sun",
    author_email="jianfeng.sun@ndorms.ox.ac.uk",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires='>3.6',
    install_requires=[
        'numpy==1.22.1',
        'scipy==1.7.2',
        'pyfastx==0.8.4',
        'pandas==1.4.1',
        'pyfiglet',
    ],
    entry_points={
        'console_scripts': [
            'resimpy_general=resimpy.simulate.dispatcher.batch.General:run',
            'resimpy_umi_transloc=resimpy.simulate.dispatcher.batch.UMIDouble:run',
            'resimpy_umi_sc=resimpy.simulate.dispatcher.batch.SingleCell:run',
        ],
    }
)