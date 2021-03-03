from setuptools import find_packages, setup


setup(
    name="job_application_task",
    description="Installer user interface to be able to install new software on devices",
    url="https://stash.draeger.com/projects/SVC_SW/repos/job_application_task/browse",
    author="Draeger",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    install_requires=[
      "falcon==2.0.0",
      "falcon-cors==1.1.7",
      "falcon-multipart==0.2.0",
      "waitress==1.4.4"
    ],
    extras_require={
        "test": [
            "pylint==2.6.*"
        ]
    }
)
