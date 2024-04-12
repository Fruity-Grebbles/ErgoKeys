import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        design = app.activeProduct
        rootComp = design.rootComponent
        
        # Get the sketch for the top label.
        top_sketch_name = next(sketch for sketch in rootComp.sketches if sketch.name.startswith('Top_Label'))
        top_sk = rootComp.sketches.itemByName(top_sketch_name)
        # Get the plane for the top label.
        top_plane = top_sk.referencePlane
        # Create a new sketch for our new text.
        new_top_sketch = rootComp.sketches.add(top_plane)
        # Copy the existing sketch contents to the new sketch.
        top_sk.copy(top_sk.sketchCurves, adsk.core.Vector3D.create(), new_top_sketch)
        # Get the first sketch text on the top label.
        top_skText_main = top_sk.sketchTexts.item(0)
        
        # Change the first text on the top label.
        top_skText_main.text = returnValue

        # Get the second sketch text on the top label.
        top_skText_sub = top_sk.sketchTexts.item(1)

        # Change the second text on the top label.
        top_skText_sub.text = returnValue
        

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))