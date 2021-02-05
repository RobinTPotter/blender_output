import bpy

for d in dir(bpy.context.scene.render):
    print(d,getattr(bpy.context.scene.render,d))

bpy.context.scene.render.resolution_percentage = 100
factor = 1 #4 * 1.25
x = bpy.context.scene.render.resolution_x
y = bpy.context.scene.render.resolution_y
bpy.context.scene.render.resolution_x = x * factor
bpy.context.scene.render.resolution_y = y * factor

print(bpy.context.scene.render.resolution_x,bpy.context.scene.render.resolution_y)

bpy.data.scenes["Scene"].render.use_border = True
bpy.data.scenes["Scene"].render.use_crop_to_border = True
bpy.data.scenes["Scene"].render.border_min_x = 0
bpy.data.scenes["Scene"].render.border_max_x = 0.5
bpy.data.scenes["Scene"].render.border_min_y = 0
bpy.data.scenes["Scene"].render.border_max_y = 0.5
