import requests


def Lineconfig(command):
	url = 'https://notify-api.line.me/api/notify'
	token = 'ou3sVenvCnqH6ioTOD6LPpWpxUTRNl4LtGUlg2bm4oS' ## EDIT
	header = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
	return requests.post(url, headers=header, data = command)

def sendtext(message):
	# send plain text to line
	command = {'message':message}
	return Lineconfig(command)


def sticker(sticker_id,package_id):
	command = {'message':" ",'stickerPackageId':package_id,'stickerId':sticker_id}
	return Lineconfig(command)


def sendimage(url):
	command = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
	return Lineconfig(command)


sendtext("hello")
sticker(38,2)
sendimage('https://media.giphy.com/media/aQYR1p8saOQla/giphy.gif')
