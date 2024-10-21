#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent

        selection = ui.activeSelections


        if selection.count == 0:
            ui.messageBox('Please select a planar face.')
            return

        selected_face = selection.item(0).entity  # Get the first selected entity
        sketch = rootComp.sketches.add(selected_face)

        num_holes = 6 
        spacing = 2.0  
        hole_radius = 0.5  
        hole_depth = 1.0 

                # Loop to create holes along a straight line
        for i in range(num_holes):
            x_position = i * spacing  # Calculate the x-position of each hole
            centerPoint = adsk.core.Point3D.create(x_position, 0, 0)
            sketch.sketchCurves.sketchCircles.addByCenterRadius(centerPoint, hole_radius)

        prof = sketch.profiles[0]  # Grab the first profile (you may want to modify this later)
        extrudes = rootComp.features.extrudeFeatures
        distance = adsk.core.ValueInput.createByReal(hole_depth)
        extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.CutFeatureOperation)


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
