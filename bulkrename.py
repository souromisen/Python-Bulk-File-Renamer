import os

def main():
	#to count the files
	i=0
	path="C:/Users/SOUROMI SEN/OneDrive/Documents/test/"
	#files stored in a list using os.listdir
	for filename in os.listdir(path):
		my_dest="img"+str(i)+".jpg"
		my_source=path+filename
		my_dest=path+my_dest
		os.rename(my_source,my_dest)
		i+=1

if __name__ == '__main__':
	main()		

