# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2022_09_28-21.41.55 183150
# Run by Amir on Sat Jun 21 15:12:03 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=114.44270324707, 
    height=122.148155212402)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(pathName="D:/sami's project/abaqus/first_try.cae")
#: The model database "D:\sami's project\abaqus\first_try.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['lower die']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['upper die']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['work-tube']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
Solidworks = mdb.openSolidworks(
    fileName="D:/sami's project/solid models/axial plunge.SLDPRT", topology=SOLID)
#* The file cannot be read. It may be corrupt or not a valid 
#* SolidWorks file.
parasolid = mdb.openParasolid(
    fileName="D:/sami's project/solid models/axial plunge.x_t", topology=SOLID)
mdb.models['Model-1'].PartFromGeometryFile(name='axial plunge', 
    geometryFile=parasolid, combine=False, dimensionality=THREE_D, 
    type=DEFORMABLE_BODY, scale=1.0)
p = mdb.models['Model-1'].parts['axial plunge']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
#: Warning: Parasolid file always contains units in mm. Hence, translated entities will be in mm.
parasolid = mdb.openParasolid(
    fileName="D:/sami's project/solid models/counter plunge.x_t", topology=SOLID)
mdb.models['Model-1'].PartFromGeometryFile(name='counter plunge', 
    geometryFile=parasolid, combine=False, dimensionality=THREE_D, 
    type=DEFORMABLE_BODY, scale=1.0)
p = mdb.models['Model-1'].parts['counter plunge']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
#: Warning: Parasolid file always contains units in mm. Hence, translated entities will be in mm.
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'lower die-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'work-tube-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'upper die-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'lower die-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=290.813, 
    farPlane=527.608, width=293.718, height=133.153, cameraPosition=(-151.757, 
    150.624, 337.321), cameraUpVector=(-0.321848, 0.529186, -0.785096), 
    cameraTarget=(-10.286, -7.49051, 5.54659))
session.viewports['Viewport: 1'].view.setValues(nearPlane=285.708, 
    farPlane=527.263, width=288.562, height=130.815, cameraPosition=(332.768, 
    141.85, 163.876), cameraUpVector=(-0.749983, 0.65584, 0.0860177), 
    cameraTarget=(7.94564, -7.82064, -0.979764))
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['axial plunge']
a.Instance(name='axial plunge-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=246.632, 
    farPlane=480.327, width=261.851, height=118.706, viewOffsetX=15.3253, 
    viewOffsetY=2.55097)
a = mdb.models['Model-1'].rootAssembly
a.translate(instanceList=('axial plunge-1', ), vector=(60.0, 0.0, 0.0))
#: The instance axial plunge-1 was translated by 60., 0., 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
a = mdb.models['Model-1'].rootAssembly
del a.features['axial plunge-1']
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['axial plunge']
a1.Instance(name='axial plunge-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.086, 
    farPlane=474.266, width=192.584, height=87.3049, viewOffsetX=0.73154, 
    viewOffsetY=4.3642)
a1 = mdb.models['Model-1'].rootAssembly
a1.rotate(instanceList=('axial plunge-1', ), axisPoint=(0.0, 0.0, 0.0), 
    axisDirection=(0.0, 1.0, 0.0), angle=90.0)
#: The instance axial plunge-1 was rotated by 90. degrees about the axis defined by the point 0., 0., 0. and the vector 0., 1., 0.
session.viewports['Viewport: 1'].view.setValues(nearPlane=265.367, 
    farPlane=461.985, width=108.762, height=49.3056, viewOffsetX=-1.73071, 
    viewOffsetY=16.0833)
session.viewports['Viewport: 1'].view.setValues(nearPlane=274.55, 
    farPlane=466.75, width=112.526, height=51.0119, cameraPosition=(-173.88, 
    195.441, 248.855), cameraUpVector=(-0.291003, 0.226518, -0.92952), 
    cameraTarget=(5.45405, -13.5887, 11.3553), viewOffsetX=-1.79061, 
    viewOffsetY=16.6398)
session.viewports['Viewport: 1'].view.setValues(nearPlane=269.227, 
    farPlane=465.141, width=110.344, height=50.0229, cameraPosition=(220.492, 
    183.137, 214.918), cameraUpVector=(-0.733351, 0.557353, -0.389299), 
    cameraTarget=(14.641, -22.5624, -3.19482), viewOffsetX=-1.75589, 
    viewOffsetY=16.3172)
session.viewports['Viewport: 1'].view.setValues(nearPlane=264.236, 
    farPlane=470.131, width=156.984, height=71.1664, viewOffsetX=-1.79444, 
    viewOffsetY=17.4444)
session.viewports['Viewport: 1'].view.setValues(nearPlane=265.902, 
    farPlane=475.786, width=157.974, height=71.6151, cameraPosition=(-226.961, 
    187.821, 210.005), cameraUpVector=(-0.185674, 0.132264, -0.973669), 
    cameraTarget=(6.80332, -10.1863, 14.0271), viewOffsetX=-1.80576, 
    viewOffsetY=17.5544)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=260.099, 
    farPlane=467.253, width=144.663, height=65.5806, viewOffsetX=1.11626, 
    viewOffsetY=5.50172)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('axial plunge-1', ), vector=(20.0, 0.0, 0.0))
#: The instance axial plunge-1 was translated by 20., 0., 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=264.51, 
    farPlane=459.16, width=147.116, height=66.6928, cameraPosition=(-133.209, 
    208.479, 249.327), cameraUpVector=(-0.412192, 0.17934, -0.893272), 
    cameraTarget=(4.99216, -21.366, 3.70046), viewOffsetX=1.13519, 
    viewOffsetY=5.59503)
session.viewports['Viewport: 1'].view.setValues(nearPlane=260.447, 
    farPlane=465.451, width=144.856, height=65.6685, cameraPosition=(309.465, 
    107.996, 142.328), cameraUpVector=(-0.613305, 0.756517, -0.227024), 
    cameraTarget=(1.5555, -23.8858, 0.696602), viewOffsetX=1.11775, 
    viewOffsetY=5.50909)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=278.119, 
    farPlane=530.887, width=244.469, height=110.826, cameraPosition=(251.189, 
    209.324, 235.108), cameraUpVector=(-0.548634, 0.576653, -0.60537))
session.viewports['Viewport: 1'].view.setValues(nearPlane=305.782, 
    farPlane=499.082, width=268.785, height=121.849, cameraPosition=(34.7503, 
    193.168, 342.265), cameraUpVector=(-0.27051, 0.591487, -0.759584), 
    cameraTarget=(17.6491, -24.2161, 1.5673))
session.viewports['Viewport: 1'].view.setValues(nearPlane=299.369, 
    farPlane=506.724, width=263.148, height=119.293, cameraPosition=(56.8125, 
    175.056, 351.389), cameraUpVector=(-0.157415, 0.653932, -0.739996), 
    cameraTarget=(17.5355, -24.1229, 1.52033))
session.viewports['Viewport: 1'].view.setValues(nearPlane=320.337, 
    farPlane=485.756, width=111.306, height=50.4588, viewOffsetX=23.1811, 
    viewOffsetY=6.79759)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('axial plunge-1', ), vector=(60.0, 0.0, 0.0))
#: The instance axial plunge-1 was translated by 60., 0., 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(width=104.934, height=47.5701, 
    viewOffsetX=24.6394, viewOffsetY=7.92832)
session.viewports['Viewport: 1'].view.setValues(nearPlane=299.495, 
    farPlane=483.579, width=97.8204, height=44.3454, cameraPosition=(-100.691, 
    240.146, 272.352), cameraUpVector=(-0.0639129, 0.402045, -0.913387), 
    cameraTarget=(19.9935, -30.5977, -2.88602), viewOffsetX=22.9691, 
    viewOffsetY=7.39088)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['axial plunge']
a1.Instance(name='axial plunge-2', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly
a1.rotate(instanceList=('axial plunge-2', ), axisPoint=(0.0, 0.0, 0.0), 
    axisDirection=(0.0, 1.0, 0.0), angle=-90.0)
#: The instance axial plunge-2 was rotated by -90. degrees about the axis defined by the point 0., 0., 0. and the vector 0., 1., 0.
session.viewports['Viewport: 1'].view.setValues(nearPlane=291.971, 
    farPlane=517.036, width=156.443, height=70.9209, viewOffsetX=-4.85832, 
    viewOffsetY=11.0519)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('axial plunge-2', ), vector=(-80.0, 0.0, 0.0))
#: The instance axial plunge-2 was translated by -80., 0., 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=287.429, 
    farPlane=536.011, width=209.849, height=95.1322, viewOffsetX=-4.82556, 
    viewOffsetY=17.1743)
mdb.save()
#: The model database has been saved to "D:\sami's project\abaqus\first_try.cae".
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['counter plunge']
a1.Instance(name='counter plunge-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=329.525, 
    farPlane=573.714, width=162.511, height=73.672, viewOffsetX=5.30665, 
    viewOffsetY=13.7277)
session.viewports['Viewport: 1'].view.setValues(nearPlane=340.467, 
    farPlane=588.985, width=167.908, height=76.1184, cameraPosition=(318.988, 
    138.954, -301.365), cameraUpVector=(-0.890407, -0.10776, -0.442225), 
    cameraTarget=(15.5909, 0.0306854, 2.95443), viewOffsetX=5.48288, 
    viewOffsetY=14.1836)
session.viewports['Viewport: 1'].view.setValues(nearPlane=342.66, 
    farPlane=582.487, width=168.99, height=76.609, cameraPosition=(317.848, 
    283.349, 155.353), cameraUpVector=(-0.775272, 0.482379, -0.407755), 
    cameraTarget=(11.5698, -16.7119, 13.5189), viewOffsetX=5.5182, 
    viewOffsetY=14.275)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('counter plunge-1', ), vector=(0.0, 0.0, 70.0))
#: The instance counter plunge-1 was translated by 0., 0., 70. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=328.811, 
    farPlane=588.485, width=221.859, height=100.577, viewOffsetX=8.62503, 
    viewOffsetY=17.2462)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=325.11, 
    farPlane=621.746, width=279.991, height=126.93, cameraPosition=(-436.368, 
    33.4556, 189.832), cameraUpVector=(0.0227061, 0.30224, -0.952961))
session.viewports['Viewport: 1'].view.setValues(nearPlane=339.103, 
    farPlane=590.635, width=292.042, height=132.393, cameraPosition=(-133.907, 
    341.991, -253.457), cameraUpVector=(-0.241577, -0.858076, -0.453152), 
    cameraTarget=(2.3513, -26.9126, 20.0744))
session.viewports['Viewport: 1'].view.setValues(nearPlane=312.423, 
    farPlane=613.386, width=269.065, height=121.977, cameraPosition=(388.345, 
    139.083, 211.819), cameraUpVector=(-0.659215, 0.748702, -0.0698585), 
    cameraTarget=(-13.5646, -20.7289, 5.89488))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'work-tube-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=312.823, 
    farPlane=612.987, width=304.901, height=138.222, viewOffsetX=8.80733, 
    viewOffsetY=0.916468)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=333.383, 
    farPlane=624.691, width=253.696, height=115.009, viewOffsetX=4.95976, 
    viewOffsetY=3.41094)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'upper die-1', ))
mdb.save()
#: The model database has been saved to "D:\sami's project\abaqus\first_try.cae".
mdb.save()
#: The model database has been saved to "D:\sami's project\abaqus\first_try.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].view.fitView()
p = mdb.models['Model-1'].parts['counter plunge']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['axial plunge']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['lower die']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['work-tube']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
import os
os.chdir(r"D:\sami's project\abaqus\Directory1")
mdb.save()
#: The model database has been saved to "D:\sami's project\abaqus\first_try.cae".
mdb.save()
#: The model database has been saved to "D:\sami's project\abaqus\first_try.cae".
mdb.save()
#: The model database has been saved to "D:\sami's project\abaqus\first_try.cae".
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
