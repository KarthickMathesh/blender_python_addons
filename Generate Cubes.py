import bpy
import random

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)

spacing = 2
for x in range(15):
    for y in range(15):
        location = (x * spacing, y * spacing, random.random() * 2)
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=location, scale=(1, 1, 1))
        
        item = bpy.context.object
        if random.random() < 0.1:
            item.data.materials.append(bpy.data.materials["Material 1"])
        else:
            item.data.materials.append(bpy.data.materials["Material 2"])
            
        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.collision_shape = 'BOX'
        bpy.context.object.rigid_body.friction = 1
        bpy.context.object.rigid_body.use_margin = True
        bpy.context.object.rigid_body.collision_margin = 0.01
        
bpy.ops.object.select_all(action='SELECT')
bpy.ops.transform.translate(value=(-9, -9, 2), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)