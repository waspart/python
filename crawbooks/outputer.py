class Outputer(object):

	def saveImg(self, img_cont, img_path):
		# print("saving......" + img_path, end=" ")
		try:
			with open(img_path, 'wb') as fin:
				fin.write(img_cont)
				# print("Done!!!!")
			return True
		except:
			# print("Failed")
			return False

		