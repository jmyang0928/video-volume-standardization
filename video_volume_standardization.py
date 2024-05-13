#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Must install ffmpeg first


# In[2]:


# !pip install moviepy pandas


# In[7]:


import numpy as np
from moviepy.editor import VideoFileClip, concatenate
import sys
from os import listdir, path


# In[15]:


standard_volume = 0.1
volume_setting = ""


# In[13]:


dir = "queue"
old_file_name_list = []

if len(sys.argv) == 1:
    # If there is only one input parameter, the default is to read all video files in the dir folder.
    old_file_name_list = listdir(dir)
    old_file_name_list = [path.join(dir, file) for file in old_file_name_list]
    old_file_name_list = [file for file in old_file_name_list if path.isfile(file)]
elif len(sys.argv) == 2:
    # If there are two input parameters, it reads the video files of the second parameter.
    old_file_name_list = [sys.argv[1]]
elif len(sys.argv) == 3:
    # If there are three input parameters, it reads the video files of the second parameter and uses the third parameter as the volume adjustment factor.
    old_file_name_list = [sys.argv[1]]
    volume_setting = sys.argv[2]
    standard_volume *= (float)(sys.argv[2])


# In[14]:


for (old_file_name, cur_idx) in zip(old_file_name_list, list(range(len(old_file_name_list)))):
    extension_index = old_file_name.rfind(".")
    new_file_name = f"{old_file_name[:extension_index]}_{"standard" if volume_setting == "" else "x"+volume_setting}{old_file_name[extension_index:]}"

    # Check origin video volume
    clip = VideoFileClip(old_file_name)
    print(f"-> Origin video name: \t\t{clip.filename}")
    
    cut = lambda i: clip.audio.subclip(i,i+1).to_soundarray(fps=44100)
    volume = lambda array: np.sqrt(((1.0*array)**2).mean())
    volumes = [volume(cut(i)) for i in range(0,int(clip.audio.duration-2))] 
    print(f"-> Origin video volume: \t{sum(volumes)/len(volumes)/standard_volume*100:.2f}%")
    print()

    # Convert Video
    cut = lambda i: clip.audio.subclip(i,i+1).to_soundarray(fps=44100)
    volume = lambda array: np.sqrt(((1.0*array)**2).mean())
    volumes = [volume(cut(i)) for i in range(0,int(clip.audio.duration-2))] 
    cur_volume = sum(volumes)/len(volumes)

    new_audio = clip.audio.volumex(standard_volume/cur_volume)
    output = clip.set_audio(new_audio)
    output.write_videofile(new_file_name,temp_audiofile="temp-audio.m4a", remove_temp=True, codec="h264_nvenc", audio_codec="aac")
    print()

    # Check new video volume
    clip = VideoFileClip(new_file_name)
    print(f"-> New video name: \t\t{clip.filename}")
    cut = lambda i: clip.audio.subclip(i,i+1).to_soundarray(fps=44100)
    volume = lambda array: np.sqrt(((1.0*array)**2).mean())
    volumes = [volume(cut(i)) for i in range(0,int(clip.audio.duration-2))] 
    print(f"-> New video volume: \t\t{sum(volumes)/len(volumes)/standard_volume*100:.2f}%")

    print(f"{"="*50} [{cur_idx+1}/{len(old_file_name_list)}]\n")


# In[ ]:


# !jupyter nbconvert --to python video_volume_standardization.ipynb

