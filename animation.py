import bpy, math, os

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
FPS = 24
scene.render.fps = FPS
scene.frame_start, scene.frame_end = 1, FPS * 8

# أرضية
bpy.ops.mesh.primitive_plane_add(size=30)

# كرة تقفز
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.6, location=(0, 0, 0.6))
ball = bpy.context.object
for f, z in [(1, 0.6), (24, 4), (48, 0.6), (72, 4), (96, 0.6),
             (120, 4), (144, 0.6), (168, 4), (192, 0.6)]:
    ball.location.z = z
    ball.keyframe_insert("location", index=2, frame=f)

# مكعب يدور
bpy.ops.mesh.primitive_cube_add(size=2, location=(3, 0, 1))
cube = bpy.context.object
cube.rotation_euler = (0, 0, 0)
cube.keyframe_insert("rotation_euler", frame=1)
cube.rotation_euler = (0, 0, math.radians(720))
cube.keyframe_insert("rotation_euler", frame=192)

# كاميرا
bpy.ops.object.camera_add(location=(9, -9, 6),
                          rotation=(math.radians(65), 0, math.radians(45)))
scene.camera = bpy.context.object

# رندر سريع وبسيط، يحفظ صوراً
scene.render.engine = "BLENDER_WORKBENCH"
scene.display.shading.light = "STUDIO"
scene.render.resolution_x, scene.render.resolution_y = 1280, 720
scene.render.image_settings.file_format = "PNG"
os.makedirs("out/frames", exist_ok=True)
scene.render.filepath = os.path.join(os.getcwd(), "out", "frames", "f_")

bpy.ops.render.render(animation=True)
print("FRAMES:", len(os.listdir("out/frames")))
