import adsk.core, adsk.fusion, adsk.cam, traceback

def export_configurations():
    ui = None 
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
    try:
        # Get the active design
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the configuration table
        configTable = design.configurationTopTable

        if configTable is None:
            ui.messageBox('No configuration table found.')
            return

        # Iterate through each configuration row
        for row in configTable.rows:
            # Activate the configuration
            row.activate()

            # Generate the file name and path for the export
            filename = f'{row.name}.f3d'
            path = f'/Users/Josh/Documents/{filename}'

            # Create export options for Fusion design
            exportMgr = design.exportManager
            options = exportMgr.createFusionArchiveExportOptions(path, design.rootComponent)

            # Execute the export
            exportMgr.execute(options)
            ui.messageBox(f'Exported {row.name} to {path}')

    except Exception as e:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def export_active_configuration():
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
    try:
        # Get the active design
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the configuration table
        configTable = design.configurationTopTable

        if configTable is None:
            ui.messageBox('No configuration table found.')
            return

        # Get the active configuration
        config = configTable.activeRow

        if config is None:
            ui.messageBox('No active configuration found.')
            return

        # Generate the file name and path for the export
        filename = f'{config.name}.f3d'
        path = f'/Users/Josh/Documents/{filename}'

        # Create export options for Fusion design
        exportMgr = design.exportManager
        options = exportMgr.createFusionArchiveExportOptions(path, design.rootComponent)

        # Execute the export
        exportMgr.execute(options)
        ui.messageBox(f'Exported {config.name} to {path}')

    except Exception as e:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def run():
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        # export_configurations()
        export_active_configuration()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

run()
