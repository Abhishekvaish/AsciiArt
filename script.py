import numpy as np
import cv2


g_scale = '@%#*+=-:. '[::-1]
# g_scale = '##--...  '[::-1]





def ascii_art1(filename , base_width):
	vidcap = cv2.VideoCapture(filename)

	success,im = vidcap.read()
	# im = cv2.imread('fisherman.jpg')
	base_height = int( im.shape[0]/im.shape[1] * base_width )

	while success:

		im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
		im = cv2.resize(im, (base_width*2,base_height ),interpolation = cv2.INTER_NEAREST)

		im = np.asarray(im)


		a_art = ''
		for i in range(im.shape[0]):		
			for j in range(im.shape[1]):
				# print(g_scale [ int( ( im[i][j]/255) * (len(g_scale)-1) ) ] , end='')
				a_art+= g_scale [ int( ( im[i][j]/255) * (len(g_scale)-1) ) ]
			# print()
			a_art += '\n'
		print(a_art)

		success,im = vidcap.read()
		# os.system('cls')




def ascii_art2(filename , base_width):
	vidcap = cv2.VideoCapture(filename)

	success,im = vidcap.read()
	base_height = int( im.shape[0]/im.shape[1] * base_width )

	FRAMES = []

	while success:

		im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
		im = cv2.resize(im, (base_width*2,base_height ),interpolation = cv2.INTER_NEAREST)

		im = np.asarray(im)
		FRAMES.append(im)
		success,im = vidcap.read()

	for im in FRAMES:
		a_art = ''
		for i in range(im.shape[0]):		
			for j in range(im.shape[1]):
				# print(g_scale [ int( ( im[i][j]/255) * (len(g_scale)-1) ) ] , end='')
				a_art+= g_scale [ int( ( im[i][j]/255) * (len(g_scale)-1) ) ]
			# print()
			a_art += '\n'
		print(a_art)


ascii_art2('dlhsb.mp4' , 100)
# ascii_art2('dlhsb.mp4' , 80)
# ascii_art2('kvo.mp4' , 80)

