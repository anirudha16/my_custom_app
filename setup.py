from setuptools import setup, find_packages

setup(
    name='my_custom_app',
    version='0.0.1',
    description='Custom app for Frappe',
    author='Your Name',
    author_email='your-email@example.com',
    author='Anirudha Landage',
    author_email='anirudhalandage16@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe'],
)

