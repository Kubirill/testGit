from moviepy.editor import VideoFileClip
import moviepy.editor as mp

# Define the input video file path
input_video_path = r'C:\Users\Student\Downloads\Мусор\video_2023-09-13_06-38-50.mp4'  # Use 'r' to specify a raw string


# Define the output video file name and rotation angle (in degrees)
output_video_path = 'output_rot_video.mp4'
rotation_angle = 90  # Change this angle as needed

# Load the video clip
clip = VideoFileClip(input_video_path)

# Rotate the video clip
rotated_clip = clip.rotate(rotation_angle)

# Set the audio of the rotated clip to be the same as the original
rotated_clip = rotated_clip.set_audio(clip.audio)

# Write the rotated video to an output file
rotated_clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac')

print("Video rotation complete. Check the output video:", output_video_path)
