# fusionScriptHolePattern

## Description

This is a Python script designed for Autodesk Fusion 360 that automates the process of creating a hole pattern on a selected face of an existing solid body. This script simplifies the repetitive task of manually sketching and extruding holes.

## Features

- **Automated Hole Creation:** Easily generate a specified number of holes with adjustable spacing and radius.
- **Customizable Parameters:** Modify the number of holes, spacing, radius, and depth directly in the script to suit your design needs.

## Prerequisites

- Autodesk Fusion 360 installed on your computer.
- Basic understanding of how to navigate the Fusion 360 interface.
- Familiarity with running scripts in Fusion 360.

## Usage

1. **Create a Solid Body:** Use the modeling tools in Fusion 360 to create a solid body (e.g., a box or cylinder).
2. **Select a Planar Face:** Choose the face of the solid body where you want the hole pattern to be applied.
3. **Run the Script:** Execute the script within Fusion 360. The hole pattern will automatically be generated on the selected face.

## Installation

To use the script, follow these steps:

1. Download the script file from the repository.
2. Open Autodesk Fusion 360.
3. Go to the "Scripts and Add-Ins" option under the "Tools" menu.
4. Click on the "+" icon to add a new script and select the downloaded script file.
5. Select the face of the body you want to implement the hole pattern on.
6. Run the script.


## Current Error ==> Uppon running the script the following error will appear: 
///
Failed:
Traceback (most recent call last):
  File "/Users/vukperovic/Library/Application Support/Autodesk/Autodesk Fusion 360/API/Scripts/Hole Pattern Script/Hole Pattern Script.py", line 38, in run
    extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.CutFeatureOperation)
  File "/Users/vukperovic/Library/Application Support/Autodesk/webdeploy/production/8be4e0864ac1dd09db77f83fc912ee24df879da2/Autodesk Fusion 360.app/Contents/Api/Python/packages/adsk/fusion.py", line 23692, in addSimple
    return _fusion.ExtrudeFeatures_addSimple(self, profile, distance, operation)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: 3 : No target body found to cut or intersect!
///


If you have experience with Fusion 360 scripting and know how to resolve this issue, 
your contributions to fixing this error would be greatly appreciated. Please feel free
to submit a pull request or provide suggestions in an issue!




