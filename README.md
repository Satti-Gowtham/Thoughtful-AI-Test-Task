# Package Sorting System

This repository contains the code for test task from Thoughtful AI. It implements a **package sorting system** to sort packages based on their dimensions and mass. The packages can be dispatched into three different stacks: **STANDARD**, **SPECIAL**, or **REJECTED**, depending on the criteria for bulkiness and heaviness.

## Sorting Logic

Packages are sorted based on the following criteria:

- **Bulky Package**: Volume is greater than or equal to 1,000,000 cm³, or Any dimension (width, height, or length) is greater than or equal to 150 cm.
- **Heavy Package**: Mass is greater than or equal to 20 kg.
- **Stack Criteria**: 
    - **STANDARD**: If the package is neither bulky nor heavy.
    - **SPECIAL**: If the package is either bulky or heavy.
    - **REJECTED**: If the package is both bulky and heavy.

## How to Use

### Command-Line Interface (CLI)

The CLI interface allows you to sort packages directly from the command line.

**To use the CLI interface**:

1. Ensure that you have Python installed on your system.
2. Run the following command in your terminal, passing the dimensions and mass as arguments:

```bash
python cli.py <width> <height> <length> <mass>
```

Replace `<width>`, `<height>`, `<length>`, and `<mass>` with the actual values for the package.