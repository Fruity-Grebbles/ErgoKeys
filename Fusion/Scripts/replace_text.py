import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        
        design = app.activeProduct
        rootComp = design.rootComponent
        
        # Get the sketch for the top label.
        top_sk = rootComp.sketches.itemByName("Top_Label")
        # Get the plane for the top label.
        top_plane = top_sk.referencePlane
        # Create a new sketch for our new text.
        new_top_sketch = rootComp.sketches.add(top_plane)
        # Copy the existing sketch contents to the new sketch.
        top_sk.copy(top_sk.sketchCurves, adsk.core.Vector3D.create(), new_top_sketch)



        # Add suppress feature columns to the configuration table for the labels. 

        # Get the sketch for the front label
        front_sk = rootComp.sketches.itemByName("Front_Label")
        # Get the plane for the front label.
        front_plane = front_sk.referencePlane
        # Create a new sketch for our new text.
        new_front_sketch = rootComp.sketches.add(front_plane)
        # Copy the existing sketch contents to the new sketch.
        front_sk.copy(front_sk.sketchCurves, adsk.core.Vector3D.create(), new_front_sketch)

        # Set the new text for the top label's main text.
        new_top_sketch.sketchTexts.item(0).text = returnValue
        # Set the new text for the top label's sub text.
        top_sk.sketchTexts.item(1) = returnValue

        # Set the new text for the front label's text.
        new_front_sketch.sketchTexts.item(0).text = returnValue

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def copySketchByName(baseFeature, sketchName, newSketchName):
    # Get the original sketch
    sketch = baseFeature.sketches.itemByName(sketchName)
    # Get the plane for the original sketch.
    plane = sketch.referencePlane
    # Create a new sketch on the same plane.
    new_sketch = baseFeature.sketches.add(plane)
    # Create an object collection to hold the existing sketch contents.
    sketchObjects = adsk.core.ObjectCollection.create()
    # Add the existing sketch contents to the object collection.
    sketchObjects.add(sketch.sketchCurves)
    sketchObjects.add(sketch.sketchPoints)
    sketchObjects.add(sketch.sketchTexts)
    sketchObjects.add(sketch.sketchDimensions)
    sketchObjects.add(sketch.sketchConstraints)
    # Copy the existing sketch contents to the new sketch.
    sketch.copy(sketchObjects, adsk.core.Vector3D.create(), new_sketch)
    # 
    return new_sketch


def copyExtrudefeatureByName(baseFeature, extrudeFeatureName, newFeatureName, sketchProfiles):
    # Get the original extrude feature
    extrudes = baseFeature.features.extrudeFeatures
    extrudeFeature = extrudes.itemByName(extrudeFeatureName)
    # Get the face from which the original extrude feature was created.
    startDef = adsk.fusion.FromEntityStartDefinition.cast(extrudeFeature.startExtent)
    # Get the face to which the original extrude feature extrudes.
    toDef = adsk.fusion.ToEntityExtentDefinition.cast(extrudeFeature.extentOne)
    # Create a new extrude feature using the extents of the original extrude feature and the given sketch.
    extrudeInput = extrudes.createInput(sketchProfiles, adsk.fusion.FeatureOperations.CutFeatureOperation)
    new_extrude = extrudes.add(extrudeInput)
    return new_extrude