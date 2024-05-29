#Blizard Lizard's 3 Light Turntable Setup Script
#Email questions to Blizardlizardscripts@gmail.com

import maya.cmds as cmds
    
object_vals = ('Directional', 'Area', 'Arnold_Area')
def blizard_lizard_turntablescript() :
  
    # initial variables
    win_name = 'Blizard Lizard Turntable Script'
    win_width = 400
    win_height = 150
    
    # check to see if window already exists
    if cmds.window( win_name, query=1, exists=1 ) == 1 :
        cmds.deleteUI( win_name )
        
    # Make a new window
    win_name = cmds.window( win_name, title="Blizard Lizard's Turntable Script", iconName='ObjectRandomizer', width=win_width, height=win_height )
    
    # create a column layout for our button
    cmds.formLayout( 'rgui_mainLayout', numberOfDivisions=100 )
    
                 
    # column layout
    cmds.columnLayout( rowSpacing=3, adjustableColumn=True )
    
    # column layout fields
    # column layout field: Description
    cmds.text( label='    Welcome to the Blizard Lizard Three Point Turntable Script ' )
    cmds.text( label=' ' )
    
    # column layout field: Light 1
    cmds.optionMenu( 'rgui_selectLighttypeField1', label='   Key Light:' )
    cmds.menuItem( label='Directional' )
    cmds.menuItem( label='Area' )
    cmds.menuItem( label='Arnold_Area' )
    cmds.text( label=' ' )
       
    # color selection
    color1 = cmds.colorSliderGrp( 'rgui_selectColorField1', label='Color:', rgb=(1, 1, 0.75) )
    
    # intensity
    intensity1 = cmds.floatSliderGrp( 'rgui_selectIntensityField1', field = True, label='Intensity:', minValue=0.00, maxValue=10.00,  value=10.00 )
  
    #cast shadows checkbox
    shadows1 = cmds.checkBox( label='Cast Shadows' )
       
    # column layout field: Light 2
    cmds.optionMenu( 'rgui_selectLighttypeField2', label='   Fill Light:' )
    cmds.menuItem( label='Directional' )
    cmds.menuItem( label='Area' )
    cmds.menuItem( label='Arnold_Area' )
    cmds.menuItem( label='None')
    cmds.text( label=' ' )
       
    # color selection
    cmds.colorSliderGrp( 'rgui_selectColorField2', label='Color:', rgb=(1, 1, 0.75) )

    # intensity
    intensity2 = cmds.floatSliderGrp( 'rgui_selectIntensityField2', field = True, label='Intensity:', minValue=0.00, maxValue=10.00,  value=10.00 )
        
    #cast shadows checkbox
    cmds.checkBox( label='Cast Shadows' )
    
    # column layout field: Light 3
    cmds.optionMenu( 'rgui_selectLighttypeField3', label='   Rim Light:' )
    cmds.menuItem( label='Directional' )
    cmds.menuItem( label='Area' )
    cmds.menuItem( label='Arnold_Area' )
    cmds.menuItem( label='None')
    cmds.text( label=' ' )
       
    # color selection
    cmds.colorSliderGrp( 'rgui_selectColorField3', label='Color:', rgb=(1, 1, 0.75) )

    # intensity
    intensity3 = cmds.floatSliderGrp( 'rgui_selectIntensityField3', field = True, label='Intensity:', minValue=0.00, maxValue=10.00,  value=10.00 )
        
    #cast shadows checkbox
    cmds.checkBox( label='Cast Shadows' )

    #cast shadows checkbox
    cmds.text( label=' ' )
    cmds.checkBox( label='Create Camera' )
    
    # escape the column layout
    cmds.setParent( '..' )
    
    # create button
    but = cmds.button( 'rgui_nameButt', label='Create', height=30, command='setup_button_press()' )
    
    # edit the formLayout
    cmds.formLayout( 'rgui_mainLayout', edit=True,
        attachForm=[ [but,'left',5], [but,'bottom',5], [but,'right',5] ],)
        
    # show the window
    cmds.showWindow( win_name )
    
    # set width and height again, to override maya's saved settings
    cmds.window( win_name, edit=1, width=win_width, height=win_height )
    
  
def setup_button_press() :
    #create stage
    stage = cmds.polyCylinder( n = 'Stage',r = 10, h = 2, sc = 1, sx = 35, sy = 5, sz = 6)

    #translate the stage
    cmds.xform(stage,translation=(0,1,0),objectSpace=1)
    
    #create the backdrop
    backdrop = cmds.polyPlane( n = 'Backdrop', w = 100, h = 100, sw = 25, sh = 25)
    
    #select the backdrop
    backdrop_sel = cmds.select(backdrop)
    
    #create bend deformer
    bend = cmds.nonLinear( type='bend', curvature = 0, lowBound = 0 )

    #select the backdrop
    backdrop_sel = cmds.select(backdrop)
    
    #curve the bend deformer
    cmds.nonLinear( 'bend1', e=True, curvature=90 )
    
    #select the bend deformer
    backdrop_sel = cmds.select('bend1Handle')
    
    #rotate the bend deformer
    cmds.rotate(0, 0, 90)
    
    # Create a camera and get the shape name.
    cameraName = cmds.camera( n = 'RenderCam')
    wcameraShape = cameraName[1]
    
    #select the camera
    camera_sel = cmds.select(cameraName)
    
    #translate and rotate the camera
    cmds.xform(camera_sel,translation=(50,10,0),objectSpace=1)
    cmds.rotate(-4, 90, 0)
    
    #Look through select camera
    cmds.lookThru( cameraName )
    
    
blizard_lizard_turntablescript()
