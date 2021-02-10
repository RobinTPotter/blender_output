import bpy

for d in dir(bpy.context.scene.render):
    print(d,getattr(bpy.context.scene.render,d))

bpy.context.scene.render.resolution_percentage = 100

size_multiplier = {size_multiplier}

x = bpy.context.scene.render.resolution_x
y = bpy.context.scene.render.resolution_y
bpy.context.scene.render.resolution_x = x * size_multiplier
bpy.context.scene.render.resolution_y = y * size_multiplier

bpy.data.scenes["Scene"].render.use_border = {border_boolean}
bpy.data.scenes["Scene"].render.use_crop_to_border = True

if {place}=="bl":
    bpy.data.scenes["Scene"].render.border_min_x = 0
    bpy.data.scenes["Scene"].render.border_max_x = 0.5
    bpy.data.scenes["Scene"].render.border_min_y = 0
    bpy.data.scenes["Scene"].render.border_max_y = 0.5

if {place}=="br":
    bpy.data.scenes["Scene"].render.border_min_x = 0.5
    bpy.data.scenes["Scene"].render.border_max_x = 1
    bpy.data.scenes["Scene"].render.border_min_y = 0
    bpy.data.scenes["Scene"].render.border_max_y = 0.5

if {place}=="tl":
    bpy.data.scenes["Scene"].render.border_min_x = 0
    bpy.data.scenes["Scene"].render.border_max_x = 0.5
    bpy.data.scenes["Scene"].render.border_min_y = 0.5
    bpy.data.scenes["Scene"].render.border_max_y = 1

if {place}=="tr":
    bpy.data.scenes["Scene"].render.border_min_x = 0.5
    bpy.data.scenes["Scene"].render.border_max_x = 1
    bpy.data.scenes["Scene"].render.border_min_y = 0.5
    bpy.data.scenes["Scene"].render.border_max_y = 1


