# Sensitive Information Detector

This utility package is designed to detect sensitive information or secrets within a given content, typically stored in a text file. It provides a simple interface to check whether any sensitive information is present in the content.

## Features

- **Input Options**: Accepts a file path or content string as input.
- **Detection**: Scans the input content for known patterns configured in a separate configuration file included in the utility package.
- **Pattern Configurations**: Examples of patterns include strings starting with `SECRET_`, ending with `_KEY` or `_PASSWORD`, and other variations.
- **Output**: Returns `True` if sensitive information or secrets are found, and `False` otherwise.
- **Test Cases**: Includes several test cases to demonstrate the utility's functionality, leveraging pytest for testing.
- **Code Hygiene**: Utilizes tools like Black or similar code scanning tools to ensure code meets basic hygiene standards, and runs these checks before every commit, preferably via pre-commit hooks.
- **Build as Wheel File**: Learn how to build the package as a wheel file locally for distribution and installation.
- **Release to PyPI**: Learn how to release the package to the Python Package Index (PyPI) repository publicly for broader usage.
- **Automated Release**: Utilizes GitHub Actions to automate the release process. Whenever a pull request is merged into the main branch, a new package is created and released with a new version on PyPI.

## Setup and Installation

### Clone the Repository

1. Clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/SaxenaSim/utility-package.git

2. Navigate to the repository directory:
   ```bash
   cd your-repository

3. Install the required packages from the requirements.txt file:
   ```bash
   pip install -r requirements.txt


## Usage

Once the package is installed, you can use the utility package as follows:

1. **Run the utility:**

   a. Importing the packages:
   ```bash
   import package_name
   from package_name.module_name import className
   ```
   b. Creating objects:
   ```bash
   obj = className()
   ```
   c. Call methods or access attributes of object:
   ```bash
   result = obj.method_name()
   print(result)
   ```

## Testing

The repository includes some test cases to demonstrate the utility's functionality. You can run the test suite using pytest:

```bash
 pytest
 ```

## Code Hygiene and Pre-commit Hooks

The repository employs tools such as Black which is a code scanning tools to enforce code hygiene standards. These checks are executed automatically before each commit, typically through pre-commit hooks.

## Building the package locally

To build the package as a wheel file locally for distribution and installation, you can use the following command:

```bash
 python setup.py sdist bdist_wheel
 ```

## Releasing to PyPI

To release the package to the Python Package Index (PyPI) repository publicly for broader usage, follow these steps:

1. Sign up for an account on PyPI ([https://pypi.org/](https://pypi.org/)).
2. Install twine if not already installed:

    ```bash
    pip install twine
    ```

3. Upload your package to PyPI using twine:

    ```bash
    twine upload dist/*
    ```