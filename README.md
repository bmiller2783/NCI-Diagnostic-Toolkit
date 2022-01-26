# NCI Diagnostic Toolkit

{Insert blurb about what the tool does and leave space for publication citation}

*Version v2.1_beta (Jan 5, 2021)*

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
 - pandas (v
 - numpy (v
 - matplotlib (v
 - adjusttext (v

*All Python modules can be installed via pip or conda from the terminal:*
```
pip install pandas
```
*To automatically install all Python modules, run the setup script in the terminal:*
```
pip install -r setup.txt
```

# Preparing Input Data

The NCI Diagnostic Tool takes input in excel (.xlsx) format (see SampleInput.xlsx as an example). Two columns are required:
  - Functional group names (column A)
  - Experimental values (column B)

And at least two rows are required:
  - Header line (Row 1)
  - Beginning of data (Row 2 ...)
  
  <img width="735" alt="input_format_img" src="https://user-images.githubusercontent.com/84196711/151250658-0ab72212-a41a-4931-84ca-7b1458521193.png">

*NOTE: The input excel file must be in the same directory as {FINAL-NAME-TBD}.ipynb*
  
### Functional Group Naming
  
Functional group names with data available for each energy type can be listed by running a function in the Jupyter Notebook prior to analysis
  1. In the second cell of the Jupyter Notebook, uncomment (delete the # in front of) line 6.
  2. Type in desired data workbook (default: NAME-OF-DATA-TBD) and energy type.
  3. Click in cell 1 of the notebook, then hold the ```shift``` key and press ```enter``` to run.
  4. Click in cell 2 of the notebook, then hold the ```shift``` key and press ```enter``` to run. A list of functional group names for each NCI interaction type will print onscreen. Copy the desired funcional group name EXACTLY AS PRINTED into your input excel file.
  
 ### Walkthrough for running this function:
  ![running_naming_function](https://user-images.githubusercontent.com/84196711/151255270-ae1b8aed-2252-4490-b1ee-b8c3c0dc8a13.gif)

  ***IMPORTANT:The code can not currently handle synonomous names for functional groups, be sure to check the names recognized***
  
*Comment out (add the # back to the beginning of) line 6 to suppress output during analysis*

# Explanation of Code Input Options

```
reference_excel_data # Name of data workbook (Default: NAME-OF-DATA-TBD)
input_excel_workbook # Name of input excel workbook
input_excel_sheetname # Name of input excel sheet
interaction_type # Specify type of NCI interaction to analyze (Options: all (recommended), Cation-pi, Anion-pi, Anion-pi fixed, pi-pi, or CH-pi)
energy_type # Specify type of energy to analyze (Options: Total Interaction Energy, Electrostatic, Repulsion, Induction, or Dispersion)
yaxis_data_label # Y-Axis experimental data label for plots

# OPTIONAL:
write_correlation_to_excel # Name of excel file to export correlation data (Default: no, meaning 'no output')
export_graphs_as_png # Basename for graphs to be exported as .png (Default: no, meaning 'no output')
```

Type desired input IN BETWEEN the hyphens ''. DO NOT DELETE THE HYPHENS

See the following publications for guidance on selecting interaction and energy types:

{LIST SELECTED PUBLICATIONS}

# Running the Notebook

After selecting input options as descibed above, run the Jupyter Notebook:
 1. Click in cell 1 of the notebook, then hold the ```shift``` key and press ```enter``` to run.
 2. Click in cell 3 of the notebook, then hold the ```shift``` key and press ```enter``` to run. Correlation coefficients will be printed quickly below, followed slowly by all corresponding graphs.
 
### Walkthrough for running analysis tool:
 
 {INSERT WHEN OUTPUT AESTHETIC IS FINALIZED}

# Adding to/Using Custom Data Workbooks

This Toolkit is designed to handle the addition of custom data into NAME-OF-DATA-TBD.xlsx calculated by the user. The naming conventions for adding data are as follows:

### Excel Data Worksheets

The code only recognizes sheets named Cation-pi, Anion-pi, Anion-pi Fixed, pi-pi, and CH-pi. 

*IMPORTANT: DO NOT add/remove sheets OR change their names*

### Naming Probe Groups

Data for distinct probes must be grouped together under a PROBE header cell. New probes can be added by declaring a new PROBE header in the desired excel sheet.

Naming probe headers:
```
PROBE: [ProbeName] (Description)
```

<img width="187" alt="probe_header_cell" src="https://user-images.githubusercontent.com/84196711/151257662-bb835f9f-6d23-4f66-a61d-69af722fc8f8.png">

If included, the description will take the place of the probe name as graph titles in output. 

*IMPORTANT: The description MUST be in parentheses, and the probe name cannot include parentheses*

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
  - Ex: Data in this row   <img width="186" alt="het" src="https://user-images.githubusercontent.com/84196711/151258734-55143905-2452-477c-b0c7-54c33ef59930.png">   will be indentified as ```2OMe_styrene_BA``` in the excel input

Data for each entry must be added to the corresponding column (e.g. Total Interaction Energy, Electrostatic, Repulsion, Induction, Dispersion). At least one of these columns must contain data.

*IMPORTANT: DO NOT add/remove columns OR change their names*

## Contact Information

For code-related inquiries, contact beck.miller@utah.edu
