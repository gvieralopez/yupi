
"""
Data-related stuff
"""
data_folder = 'data' # Folder containing the videos
data_file = 'video2.mp4' # Video file being analized
skip_frames = 0 # Frames to skip before start processing


"""
Algorithm's parameters
"""
roi_width = 180 # Width of the region of image analized on each frame
roi_heigh = 180 # Heigh of the region of image analized on each frame
frame_diff_threshold = 15 # Min value-change of a pixel to be considered as altered
ant_pixels = 227 # approximate area of the ant in pixels


"""
Algorithm's constants
"""
ant_ratio = ant_pixels / (roi_width * roi_heigh) # approximate ratio of the ant compare to the roi


