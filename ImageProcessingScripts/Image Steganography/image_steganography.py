

# PIL module is used to extract pixels of image and modify it
from PIL import Image

# Convert the secret data into 8-bit binary value by using the ASCII value
def genData(data):

		binLst = []  #list to store binary data

		for i in data:
			binLst.append(format(ord(i), '08b'))   #Converting and appending binary data
		return binLst

# Pixels are modified according to the 8-bit binary data and finally returned
def modPixel(pix, data):

	datalist = genData(data)
	lendata = len(datalist)
	igdata = iter(pix)

	for i in range(lendata):

		# Extracting 3 pixels at a time
		pix = [value for value in igdata.__next__()[:3] + igdata.__next__()[:3] + igdata.__next__()[:3]]

		# Pixel value should be made odd for 1 and even for 0
		for j in range(0, 8):
			if (datalist[i][j] == '0' and pix[j]% 2 != 0):
				pix[j] -= 1

			elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
				if(pix[j] != 0):
					pix[j] -= 1
				else:
					pix[j] += 1

		# Eighth pixel of every set tells us whether to stop or read further.
		# 0 means keep reading; 1 means the message is over.
		if (i == lendata - 1):
			if (pix[-1] % 2 == 0):
				if(pix[-1] != 0):
					pix[-1] -= 1
				else:
					pix[-1] += 1

		else:
			if (pix[-1] % 2 != 0):
				pix[-1] -= 1

		pix = tuple(pix)
		yield pix[0:3]
		yield pix[3:6]
		yield pix[6:9]

def encode_enc(newimg, data):
	w = newimg.size[0]
	(x, y) = (0, 0)

	for pixel in modPixel(newimg.getdata(), data):

		# Putting modified pixels with encoded data in the new image
		newimg.putpixel((x, y), pixel)
		if (x == w - 1):
			x = 0
			y += 1
		else:
			x += 1


# Method to encode data into image
def encode():
	img = input("Enter image name(with extension) in which data is to be encoded : ")
	image = Image.open("Images/"+img, 'r')

	data = input("Enter the data to be encoded : ")
	if (len(data) == 0):
		raise ValueError('Data is empty')

	newimg = image.copy()
	encode_enc(newimg, data)

	en_img = input("Enter the name of new encoded image(with extension) : ")
	newimg.save("Images/"+en_img, str(en_img.split(".")[1].upper()))


# Method to decode the data present in the image
def decode():
	img = input("Enter image name(with extension) from which data is to be dencoded : ")
	image = Image.open("Images/"+img, 'r')

	data = ''
	imgdata = iter(image.getdata())

	while (True):
		pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]]

		# string to store converted binary data
		binstr = ''

		#converting the binary data into ASCII value
		for i in pixels[:8]:
			if (i % 2 == 0):
				binstr += '0'
			else:
				binstr += '1'

		#Converting ASCII value to form a string i.e secret data
		data += chr(int(binstr, 2))
		if (pixels[-1] % 2 != 0):
			image.show()     #shows the image which contains the secret data
			return data

# Main Function
def main():
	ch = int(input("\n:: Welcome to Image Steganography ::\n"
						"   1. Encode the data\n   2. Decode the data\n"
						"\nSelect your choice : "))
	if (ch == 1):
		encode()
		print("\n*** Encoding secret data into image Successful ***\n")

	elif (ch == 2):
		print("Decoded Message : " + decode())
		print("\n*** Decoding secret data from image Successful ***\n")
	else:
		raise Exception("Invalid input")

# Driver Code
if __name__ == '__main__' :
	
	# Calling main function
	main()


