import bpy
from mathutils import Vector 


# useful shortcut to reference the scene later
scene = bpy.context.scene
# clear all existing objects from scene
for obj in scene.objects:
 bpy.context.collection.objects.unlink(obj)
 
 #create sphere and make it smooth
bpy.ops.mesh.primitive_uv_sphere_add(location = (0,0,5), radius=0.1)
bpy.ops.object.shade_smooth()
# Store a reference to it while it is the active object (just created)
obj1 = bpy.context.active_object
# mat_r is defined be a new material with a red colour
mat_r = bpy.data.materials.new("mat_red")
mat_r.diffuse_color = (1, 0, 0, 1)
obj1.data.materials.append(mat_r) 

# Create a light source and configure it
light_data = bpy.data.lights.new(name="light_1", type='POINT')
light_data.energy = 30
# create new object with our light data block
light_object = bpy.data.objects.new(name="light_1", object_data=light_data)
# link light object
bpy.context.collection.objects.link(light_object)
# make it active
bpy.context.view_layer.objects.active = light_object
#change location
light_object.location = (-6, 0, 12) 

# Create a camera
cam_data = bpy.data.cameras.new(name="cam")
cam_object = bpy.data.objects.new(name="Camera", object_data=cam_data)
bpy.context.collection.objects.link(cam_object)
scene.camera = cam_object

# Configure the camera and face it towards the sphere
cam_object.location = (10.5, -4.0, 4.8)
direction = obj1.location - cam_object.location
rot_quat = direction.to_track_quat('-Z', 'Y')
cam_object.rotation_euler = rot_quat.to_euler()
cam = bpy.data.cameras[cam_data.name]
cam.lens = 30 

#INSERT OBJECT HERE
#This is the object that the two items fly around
bpy.ops.import_scene.obj(filepath="OBJECT FILEPATH",
filter_glob="*.obj;*.mtl", axis_forward='-Z', axis_up='Y', global_clight_size=0.0)
bpy.ops.transform.resize(value=(4, 4, 4))
bpy.ops.transform.translate(value=(0.0, 0.0, 2.5))

# Load the  model (and resize it)
bpy.ops.object.select_all(action='DESELECT')
#INSERT OBJECT HERE
bpy.ops.import_scene.obj(filepath="OBJECT FILEPATH",
filter_glob="*.obj;*.mtl", axis_forward='-Z', axis_up='Y')
#bpy.ops.transform.translate(value=(0.0, 0.0, 0.0))
bpy.ops.transform.resize(value=(0.1, 0.1, 0.1))
obj1=bpy.context.selected_objects[0]

# Load the model (and resize it)
bpy.ops.object.select_all(action='DESELECT')
#INSERT OBJECT HERE
bpy.ops.import_scene.obj(filepath="OBJECT FILEPATH",
filter_glob="*.obj;*.mtl", axis_forward='-Z', axis_up='Y')
#bpy.ops.transform.translate(value=(0.0, 0.0, 0.0))
bpy.ops.transform.resize(value=(0.1, 0.1, 0.1))
obj2=bpy.context.selected_objects[0]

# animation
positions = (-4,-4,7),(-4,4,7),(4,4,7),(4,-4,7),(-4,-4,7),(-4,4,7),(4,4,7),(4,-4,7),(-4,-4,7) 
positions1 = (-5.5,-5,7.5),(-5.5,5,7.5),(5.5,5,7.5),(5.5,-5,7.5),(-5.5,-5,7.5),(-5.5,5,7.5),(5.5,5,7.5),(5.5,-5,7.5),(-5.5,-5,7.5) 
# start on frame 0
number_of_frame = 0
for position in positions:
 # create a frame using number_of_frame
 scene.frame_set(number_of_frame)
 obj1.location = position
 obj1.keyframe_insert(data_path="location", index=-1)
 
 # move forward 10 frames, blender estimates positions between keyframes
 number_of_frame += 10 
 obj1.rotation_mode = 'XYZ'
 obj1.rotation_euler= [-3.1415/3, 3.1415/-1.2, (2*3.1415)*(-number_of_frame/50)]
 obj1.keyframe_insert(data_path="location", index=-1)
 obj1.keyframe_insert("rotation_euler", index=-1) 
 
 # Set start and end frames
scene.frame_start = 1
scene.frame_end = 40 

obj1.keyframe_insert(data_path="location", index=-1)
obj1.keyframe_insert("rotation_euler", index=-1) 

# start on frame 0
number_of_frame = 0
for position in positions1:
 # create a frame using number_of_frame
 scene.frame_set(number_of_frame)
 obj2.location = position
 obj2.keyframe_insert(data_path="location", index=-1)
 
 # move forward 10 frames, blender estimates positions between keyframes
 number_of_frame += 10 
 obj2.rotation_mode = 'XYZ'
 obj2.rotation_euler= [-3.1415/3, 3.1415/-1.2, (2*3.1415)*(-number_of_frame/50)]
 obj2.keyframe_insert(data_path="location", index=-1)
 obj2.keyframe_insert("rotation_euler", index=-1) 
 
 # Set start and end frames
scene.frame_start = 1
scene.frame_end = 40 

obj2.keyframe_insert(data_path="location", index=-1)
obj2.keyframe_insert("rotation_euler", index=-1) 
