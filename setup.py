import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    README = f.read()

setup(
    name="wflow",
    description="wflow hydrological modeling framework",
    long_description=README,
    author="J. Schellekens",
    author_email="wflow@deltares.nl",
    url="http://wflow.readthedocs.io/",
    license="GPL",
    use_scm_version = {'write_to': 'wflow/version.py', 'fallback_version': '2018.1.dev'},
    setup_requires=["setuptools_scm"],
    python_requires=">=3.6",
    install_requires=[
        "pcraster",
        "numpy",
        "scipy",
        "gdal",
        "netCDF4",
        "xarray",
        "cftime",
        "numba",
        "pyproj",
        "python-dateutil",
    ],
    extras_require={
        "docs": ["sphinx", "sphinx_rtd_theme"],
    },
    packages=["wflow", "wflow.pcrglobwb", "wflow.sphy", "wflow.wrappers.rtc"],
    package_dir={"wflow": "wflow"},
    test_suite="tests",
    zip_safe=False,
    scripts=[
        "Scripts/pcr2netcdf.py",
        "Scripts/tss2xml.py",
        "Scripts/wflow_subcatch.py",
        "wflow/wflow_extract.py",
        "wflow/wflow_sceleton.py",
        "wflow/wflow_gr4.py",
        "wflow/plottss.py",
        "wflow/wflow_wave.py",
        "wflow/wflow_topoflex.py",
        "wflow/wflow_cqf.py",
        "wflow/wflow_floodmap.py",
        "wflow/wflow_upscale.py",
        "wflow/wflow_fit.py",
        "wflow/wflow_adapt.py",
        "wflow/wflow_delwaq.py",
        "Scripts/wflow_prepare_step1.py",
        "Scripts/wflow_prepare_step2.py",
        "wflow/wflow_sbm.py",
        "wflow/wflow_hbv.py",
        "wflow/wflow_w3ra.py",
        "wflow/wflow_upscale.py",
        "wflow/wflow_routing.py",
        "Scripts/bmi2runner.py",
    ],
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
    ],
    keywords="wflow hydrology modeling framework pcraster",
)
