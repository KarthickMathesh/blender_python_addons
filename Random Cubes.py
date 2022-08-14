import bpy
from random import randint, uniform
import math

for mesh in bpy.data.meshes:
    if mesh is not bpy.data.meshes['Plane']:
        bpy.data.meshes.remove(mesh)

RND_VAL = 1.5

for i in range(50):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(uniform(-RND_VAL, RND_VAL), uniform(-RND_VAL, RND_VAL), uniform(-RND_VAL, RND_VAL)), scale=(uniform(0.5, 1), uniform(0.5, 1), uniform(0.5, 1)))
    
    obj = bpy.context.active_object
    
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='EDGE')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.bevel(offset=0.05, segments=4)
    bpy.ops.object.mode_set(mode='OBJECT')
    
    bpy.ops.object.shade_smooth()
    
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    
    obj.rotation_euler = [math.radians(-8.77), math.radians(-1.97), math.radians(45.5)]
    obj.keyframe_insert(data_path='rotation_euler', frame=1)
    
    obj.rotation_euler = [math.radians(-8.77), math.radians(-1.97), math.radians(45.5) + math.pi*2]
    obj.keyframe_insert(data_path='rotation_euler', frame=120)
    
    fcurves = obj.animation_data.action.fcurves
    for fcurve in fcurves:
        for kf in fcurve.keyframe_points:
            kf.interpolation = 'LINEAR'
            
       
    mat = bpy.data.materials[randint(2, len(bpy.data.materials)-1)]
    
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)