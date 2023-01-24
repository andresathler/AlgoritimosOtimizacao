import pytube

url = input("URL: ")

path = "C:/Users/andre.sathler_evolua/Downloads"

pytube.YouTube(url).streams.get_highest_resolution().download(path)
