
    scene.render.engine = "BLENDER_EEVEE_NEXT"
except TypeError:
    scene.render.engine = "BLENDER_EEVEE"
scene.render.resolution_x, scene.render.resolution_y = 1280, 720
scene.render.image_settings.file_format = "FFMPEG"
scene.render.ffmpeg.format = "MPEG4"
scene.render.ffmpeg.codec = "H264"
os.makedirs("out", exist_ok=True)
scene.render.filepath = os.path.join(os.getcwd(), "out", "video.mp4")

bpy.ops.render.render(animation=True)
