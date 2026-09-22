# StaffRegistry-CLI

An interactive Python command-line utility designed to capture employee metadata, process organizational string patterns, and generate standardized profile cards.

##  Features

* **Dynamic Profile Ingestion:** Replaces static assignments with terminal-based `input()` prompts for flexible runtime data entry.
* **String Processing & Slicing:** Demonstrates substring isolation by targeting precise index slices (`[0:3]` and `[9:11]`) within corporate identification codes to pull out department keys.
* **Formatted Console Rendering:** Implements clean terminal spacing by utilizing string formatting expressions along with multi-line print functions (`sep='\n'`).
* **Variable Casting:** Seamlessly integrates standard text objects with type-casted integer and floating-point numeric markers.

##  How it Works

1. **Information Capture:** Prompts the administrator for specific biographical information, regional address units, operational roles, and fiscal parameters.
2. **Parsing Array:** Examines the structured `employee_code` layout to systematically split the corporate initials from the structural code prefix.
3. **Card Assembly:** Packs the localized datasets into an inline template before pushing it down to the final dashboard display.

##  Prerequisites & Execution

You only need Python 3.x installed to run this script.

```bash
python registry.py
```
