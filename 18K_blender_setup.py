
import bpy

# Set resolution to 18K (18000x8000 pixels)
bpy.context.scene.render.resolution_x = 18000
bpy.context.scene.render.resolution_y = 8000
bpy.context.scene.render.resolution_percentage = 100

# Set up a basic scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Add a camera
bpy.ops.object.camera_add(location=(0, -10, 5))
camera = bpy.context.object
camera.data.lens = 35
bpy.context.scene.camera = camera

# Add a light source
bpy.ops.object.light_add(type='SUN', location=(10, -10, 10))

# Add a basic ground plane
bpy.ops.mesh.primitive_plane_add(size=50, location=(0, 0, 0))
ground = bpy.context.object
ground.name = "Ground"

# Create an animated object (e.g., a sphere moving through a portal)
bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 1))
sphere = bpy.context.object
sphere.name = "Portal_Sphere"

# Animate sphere movement (frame 1 to 100)
sphere.keyframe_insert(data_path="location", frame=1)
sphere.location.z = 5
sphere.keyframe_insert(data_path="location", frame=100)

# Set render engine to Cycles for high-quality output
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.samples = 256

# Save the scene file
bpy.ops.wm.save_as_mainfile(filepath="18K_animation.blend")

print("Blender scene setup complete. Ready for rendering at 18K resolution.")
