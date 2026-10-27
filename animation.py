import bpy, math, os

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
FPS = 24
scene.render.fps = FPS
scene.frame_start, scene.frame_end = 1, FPS * 8

# عالم وخلفية
world = bpy.data.worlds.new("W")
scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.05, 0.08, 0.15, 1)

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

# إضاءة وكاميرا
bpy.ops.object.light_add(type="SUN", location=(5, -5, 10))
bpy.context.object.data.energy = 4
bpy.ops.object.camera_add(location=(9, -9, 6),
                          rotation=(math.radians(65), 0, math.radians(45)))
scene.camera = bpy.context.object

# إعدادات الرندر (Cycles على المعالج، يعمل بدون كرت شاشة)
scene.render.engine = "CYCLES"
scene.cycles.device = "CPU"
scene.cycles.samples = 16
scene.render.resolution_x, scene.render.resolution_y = 1280, 720
scene.render.image_settings.file_format = "FFMPEG"
scene.render.ffmpeg.format = "MPEG4"
scene.render.ffmpeg.codec = "H264"
os.makedirs("out", exist_ok=True)
scene.render.filepath = os.path.join(os.getcwd(), "out", "video.mp4")

bpy.ops.render.render(animation=True)
