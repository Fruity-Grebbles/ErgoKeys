import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        design = app.activeProduct
        rootComp = design.rootComponent
        
        # Get the sketch named "ChangeText"
        sk = rootComp.sketches.itemByName('ChangeText')
        
        # Get the first sketch text.
        skText = sk.sketchTexts.item(0)

        #Prompts the user for the new Text   
        (returnValue, cancelled) = ui.inputBox('What text?', 'New text:', )
        
        # Grab the sketch and first text entity 
        sk = rootComp.sketches.itemByName('ChangeText') 
        skText = sk.sketchTexts.item(0)

        # Change the text.
        skText.text = returnValue

        # Write in the path to the folder where you want to save STL‘s
        folder = 'C:/Users/Desktop/etc...'
        
        # Construct the output filename. Name will be the same as you‘ve changed    the text into.
        filename = folder + skText.text + '.stl'

        # Save the file as STL.
        exportMgr = adsk.fusion.ExportManager.cast(design.exportManager)
        stlOptions = exportMgr.createSTLExportOptions(rootComp)
        stlOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementMedium
        stlOptions.filename = filename
        exportMgr.execute(stlOptions)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))