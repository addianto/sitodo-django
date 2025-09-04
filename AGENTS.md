# Work Guidelines for Agent

## Testing

- Always run the test suite before and after making changes to the project.

## Code Writing Style

- Try to follow [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/) when writing Python code in this project.
- This project uses `ruff` as linter and autoformatter.
  Therefore, follow these instructions when making changes to the project:
    - Always run `ruff format --diff` to check for any lint violations.
    - If there are any lint violations, run `ruff format` without any additional options to autoformat the project.
- Ensure all declared variables and parameters to have type hints.
