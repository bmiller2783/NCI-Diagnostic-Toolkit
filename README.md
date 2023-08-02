# NCI Diagnostic Toolkit

A data science tool for correlating user data with noncovalent interaction (NCI) energies, using substituent effect patterns and statistical analyses to suggest the most likely NCI. Cation–π, anion–π, CH–π, and π–π interactions are currently available for analysis along with 54 differently substituted arenes and heteroarenes.

Citation: Pending

*Version v3.3.1_beta (July 2023)*

What this document covers:
 - Software and Module Requirements
 - Preparing Input Data
 - Explanation of Code Input Options
 - Running the Notebook
 - Adding to/Using Custom Data Workbooks

## Software and module requirements

Software Required:
 - Jupyter Notebook
 - Python3

Python Modules Required:
 - pandas
 - numpy
 - plotly
 - scipy.stats

*All Python modules can be installed via pip or conda from the terminal:*
```
pip install pandas
```
*To automatically install all Python modules, run the setup script in the terminal:*
```
pip install -r setup.txt
```

# Preparing Input Data

The NCI Diagnostic Tool takes input in excel (.xlsx) format (see Input.xlsx as an example). Two columns are required:
  - Arene Fragment or Substituent
  - Experimental Data

The input excel file must be in the same directory as NCI Analysis.ipynb
*Note: Additional data in the same excel sheet as input may lead to errors*

### Functional Group Naming
  
Functional group names with data available for each energy type can be listed by running a function in the Jupyter Notebook prior to analysis
<img width="773" alt="Screen Shot 2023-08-02 at 2 28 48 PM" src="https://github.com/SigmanGroup/NCI-Diagnostic-Toolkit/assets/84196711/671620f4-5a5a-4268-8463-a191b694c74e">

A list of functional group names for selected NCI interaction type will print onscreen. Copy the desired funcional group name EXACTLY AS PRINTED into your input excel file as needed.

# Explanation of Code Input Options

```
NCI_reference_data # Name of NCI data workbook (Default: NAME-OF-DATA-TBD)
input_excel_workbook # Name of input excel workbook
input_excel_sheetname # Name of input excel sheet
interaction_type # Specify type of NCI interaction to analyze (Options: all (recommended), Cation-pi, Anion-pi, Anion-pi fixed, pi-pi, or CH-pi)
energy_type # Specify type of energy to analyze (Options: Total Interaction Energy, Electrostatic, Repulsion, Induction, or Dispersion)
```

# Adding to Current/Using Custom Data Workbooks

This Toolkit is designed to accomodate the addition of custom data into the NCI reference workbook calculated by the user. The naming conventions for adding data are as follows:

### Excel Data Worksheets

The code only recognizes reference sheets named BA'd Library, ESP, Fixed Distance Anion-pi, and Hammett. 
*DO NOT add/remove sheets OR change their names*
### Naming Data Entries Within Probe Groups

For benzene substituents:
```
[ProbeName]_[FunctionalGroup]_benzene
```
  - Ex: Data in this row   <img width="185" alt="probe_header_cell" src="https://user-images.githubusercontent.com/84196711/151258088-2a362923-25e9-4f60-8572-1c99215f09e6.png">   will be indentified as ```12diMe``` in the excel input

For other heteroaromatics:
```
[ProbeName]_[FunctionalGroup]
```
  - Ex: Data in this row   <img width="186" alt="het" src="https://user-images.githubusercontent.com/84196711/151258734-55143905-2452-477c-b0c7-54c33ef59930.png">   will be indentified as ```2OMe_styrene``` in the excel input

Data for each entry must be added to the corresponding column (e.g. Total Interaction Energy, Electrostatic, Repulsion, Induction, Dispersion). At least one of these columns must contain data.

*IMPORTANT: DO NOT add/remove columns OR change their names*

## Contact Information

For code-related inquiries, contact beck.miller@utah.edu
