# -*- coding: utf-8 -*-
import maya.cmds as cmds
import random

cmds.polySphere(r=10, sx=40, sy=40)

cmds.select(r=True)
list = cmds.ls(sl=True)

node = cmds.createNode('spliceMayaNode', n="FE_MultiChannelWeightMap")
cmds.select(node, r=True)
FENodeName = cmds.ls(sl=True)

cmds.fabricSplice('addOutputPort', node, '{"portName":"multiChannelWeightMap", "dataType":"MultiChWeightmap", "extension":"TKCM"}')
cmds.fabricSplice('setPortPersistence', node, '{"portName": "multiChannelWeightMap", "persistence": true}')
cmds.fabricSplice('addIOPort', node, '{"portName":"mesh", "dataType":"PolygonMesh", "addMayaAttr":true}')
cmds.fabricSplice('addInputPort', node, '{"portName":"matrix44", "dataType":"Mat44", "addMayaAttr":true}')
cmds.fabricSplice('addInputPort', node, '{"portName":"activeChnnel", "dataType":"Integer"}')
cmds.fabricSplice('addInputPort', node, '{"portName":"chnnelCount", "dataType":"Integer", "addMayaAttr":true}')
cmds.fabricSplice('addInputPort', node, '{"portName":"saveEnable", "dataType":"Boolean", "addMayaAttr":true}')
cmds.fabricSplice('addInputPort', node, '{"portName":"saveExternalFile", "dataType":"Boolean", "addMayaAttr":true}')
cmds.fabricSplice('addInputPort', node, '{"portName":"saveFolderPath", "dataType":"String", "addMayaAttr":true}')
cmds.fabricSplice('addInputPort', node, '{"portName":"saveFileName", "dataType":"String", "addMayaAttr":true}')
cmds.fabricSplice('addOutputPort', node, '{"portName":"run", "dataType":"Vec3", "addMayaAttr":true}')

cmds.addAttr(node, ln='activeChnnel', at="long", min=0)
cmds.connectAttr(list[0]+'.worldMesh[0]', FENodeName[0]+'.mesh')
cmds.connectAttr(list[0]+'.worldMatrix[0]', FENodeName[0]+'.matrix44')
cmds.setAttr( FENodeName[0]+'.chnnelCount', 10 )
loc = cmds.spaceLocator( p=(0, 0, 0), n="run")
cmds.select(loc, r=True)
locName = cmds.ls(sl=True)
print locName
cmds.connectAttr(FENodeName[0]+'.run', locName[0]+'.translate')

cmds.fabricSplice('addKLOperator', node, '{"opName": "MultiChWeightMapOP"}', '''
require Math;
require TKCM;
require Geometry;
operator MultiChWeightMapOP(
  io MultiChWeightmap multiChannelWeightMap, 
  in Mat44 matrix44, 
  io PolygonMesh mesh, 
  io Vec3 run,
  
  in Integer activeChnnel,
  in Integer chnnelCount,
  
  in Boolean saveEnable, 
  in Boolean saveExternalFile,
  in String saveFolderPath,
  in String saveFileName,
) {
  multiChannelWeightMap.connect(mesh, Xfo(matrix44), chnnelCount);
  multiChannelWeightMap.changeActiveCh(activeChnnel);
  multiChannelWeightMap.activateManipulator();
  multiChannelWeightMap.setLimit(0.3,1.0);
  
  multiChannelWeightMap.save(saveEnable, saveExternalFile, FilePath(saveFolderPath), saveFileName);

}
''')





