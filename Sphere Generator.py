# import bpy
# import random
# from math import radians

# bpy.ops.object.select_all(action='SELECT')
# bpy.ops.object.delete(use_global=False, confirm=False)

# for i in range(1, 6):
#   if i == 1:
#     bpy.ops.mesh.primitive_cube_add()
#     plank = bpy.context.active_object
#     plank.name = "Plank_" + str(i)
#     plank.scale = [12, 3, 1]
#     plank.rotation_euler[0] = radians(90)
#     plank.location[0] = 24 * i
#     plank.location[2] = 3


#   elif i == 10:
#     plank = bpy.context.active_object
#     plank.name = "Plank_" + str(i)
#     plank.location[0] = 24 * i
#     plank.location[2] = 3

#   else:
#     bpy.ops.object.duplicate_move()
#     plank = bpy.context.active_object
#     plank.name = "Plank_" + str(i)
#     plank.location[0] = 24 * i
#     plank.location[2] = 3

bl_info = {
    "name": "Random Sphere Regerator",
    "author": "Karthick",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sibebar",
    "description": "Adds a random sphere",
    "warning": "",
    "doc_url": "",
    "category": "",
}


import bpy
from random import randint
from bpy.types import (Panel, Operator)

class ButtonOperator(bpy.types.Operator):
    bl_idname = "random.sphere"
    bl_label = "Simple Random Operator"

    def execute(self, context):
        # bpy.ops.object.select_all(action='SELECT')
        # bpy.ops.object.delete(use_global=False, confirm=False)
        for x in range(5):
            for y in range(5):
                for z in range(15):

                  bpy.ops.mesh.primitive_uv_sphere_add(radius=2, enter_editmode=False, align='WORLD', location=(x * 5, y * 5, z * 5), scale=(1, 1, 1))
                  bpy.ops.object.shade_smooth()

        return {'FINISHED'}
    
class CustomPanel(bpy.types.Panel):
    bl_label = "Random Panel"
    bl_idname = "OBJECT_PT_random"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Random Sphere"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Generate", icon='SPHERE')

classes = [ButtonOperator, CustomPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
