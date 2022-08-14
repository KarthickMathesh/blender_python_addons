bl_info = {
    "name": "Plank Generator",
    "author": "Karthick",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar",
    "description": "Generate a Plank loop",
    "warning": "",
    "doc_url": "",
    "category": "Physics",
}

import bpy


def execute(context):
    class Plank(bpy.types.Operator):
        x = bpy.props.StringProperty(name="X", default="0")
        y = bpy.props.StringProperty(name="Y", default="0")
        z = bpy.props.StringProperty(name="Z", default="0")

        print(x, y, z)

    for x in range(0, 5):
        for z in range(0, 20):
            bpy.ops.mesh.primitive_cube_add(location=(x * 10, 4, z * 4), scale=(5, 1, 1))
            bpy.ops.mesh.primitive_cube_add(location=(x * 10, -4, z * 4), scale=(5, 1, 1))

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.transform.translate(value=(0, 0, 2), orient_axis_ortho='X', orient_type='GLOBAL',
                                orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL',
                                constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False,
                                proportional_edit_falloff='SMOOTH', proportional_size=1,
                                use_proportional_connected=False, use_proportional_projected=False)

    z_spacing = 4
    for z in range(20):
        bpy.ops.mesh.primitive_cube_add(location=(-4, 0, z * z_spacing),
                                        scale=(1, 5, 1))
        bpy.ops.mesh.primitive_cube_add(location=(4, 0, z * z_spacing),
                                        scale=(1, 5, 1))
        bpy.ops.mesh.primitive_cube_add(location=(6, 0, z * z_spacing),
                                        scale=(1, 5, 1))
        bpy.ops.mesh.primitive_cube_add(location=(14, 0, z * z_spacing),
                                        scale=(1, 5, 1))
        bpy.ops.mesh.primitive_cube_add(location=(16, 0, z * z_spacing),
                                        scale=(1, 5, 1))
        bpy.ops.mesh.primitive_cube_add(location=(24, 0, z * z_spacing),
                                        scale=(1, 5, 1))
        bpy.ops.mesh.primitive_cube_add(location=(26, 0, z * z_spacing),
                                        scale=(1, 5, 1))
        bpy.ops.mesh.primitive_cube_add(location=(34, 0, z * z_spacing),
                                        scale=(1, 5, 1))
        bpy.ops.mesh.primitive_cube_add(location=(36, 0, z * z_spacing),
                                        scale=(1, 5, 1))
        bpy.ops.mesh.primitive_cube_add(location=(44, 0, z * z_spacing),
                                        scale=(1, 5, 1))

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.transform.translate(value=(-20, 0, 1), orient_axis_ortho='X', orient_type='GLOBAL',
                                orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL',
                                constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False,
                                proportional_edit_falloff='SMOOTH', proportional_size=1,
                                use_proportional_connected=False, use_proportional_projected=False)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.rigidbody.object_add()
    bpy.context.object.rigid_body.collision_shape = 'BOX'
    bpy.context.object.rigid_body.friction = 1
    bpy.context.object.rigid_body.use_margin = True
    bpy.context.object.rigid_body.collision_margin = 0
    bpy.context.object.rigid_body.use_deactivation = True
    bpy.context.object.rigid_body.use_start_deactivated = True
    bpy.ops.rigidbody.object_settings_copy()

    return {'FINISHED'}


class ButtonOperator(bpy.types.Operator):
    bl_idname = "random.plank"
    bl_label = "Simple Random Plank Generator"


class CustomPanel(bpy.types.Panel):
    bl_label = "Plank Generator"
    bl_idname = "OBJECT_PT_Plank_Generator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Plank Generator"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        layout.scale_y = 2.0
        row.operator(ButtonOperator.bl_idname, text="Generate", icon='CUBE')


classes = [ButtonOperator, CustomPanel]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
