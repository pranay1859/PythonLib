from maya import cmds


def align(nodes=None, axis='x', mode='mid'):
	#  nodes to selection if nothings
	if not nodes:
		nodes = cmds.ls(sl=True)
	if not nodes:
		cmds.warning('nothing selected')

	#create list of already converted object
	_nodes = []

	for node in nodes:

		#.f[ is faceobj
		if '.f[' in node:
			node = cmds.polyListComponentConversion(node, fromFace=True, toVertex=True)
		#.e edge
		elif '.e[' in node:
			node = cmds.polyListComponentConversion(node, fromEdge=True, toVertex=True)

		cmds.select(node)

		node = cmds.ls(sl=True, fl=True)

		_nodes.extend(node)

	cmds.select(nodes)

	nodes = _nodes

	minMode = mode == 'min'
	maxMode = mode == 'max'
	midMode = mode == 'mid'

	# All our transform values give us back a list of x,y,z
	# Since we only care about one of these axes at a time,
	# the start variable tells us where to look
	# For x we look at the first item (0), y is second (1) and z is third (2)
	# Remember that lists start from 0

	if axis == 'x':
		start = 0
	elif axis == 'y':
		start = 1
	elif axis == 'z':
		start = 2
	else:

		cmds.warning('Unknown Axis')

	bboxes = {}
	values = []

	for node in nodes:
		if '.vtx[' in node:
			#vtx boundingbox to get worldspace value
			ws = cmds.xform(node, q=True, t=True, ws=True)

			minValue = midValue = maxValue = ws[start]
		else:

			bbox = cmds.exactWorldBoundingBox(node)
			#calculate value position
			minValue = bbox[start]
			maxValue = bbox[start + 3]
			midValue = (maxValue + minValue) / 2

		bboxes[node] = (minValue, midValue, maxValue)

		if minMode:
			values.append(minValue)
		elif maxMode:
			values.append(maxValue)
		else:
			values.append(midValue)

	if minMode:
		target = min(values)

	elif maxMode:
		target = max(values)

	else:
		target = sum(values) / len(values)

 # loop for our obj
	for node in nodes:

		bbox = bboxes[node]

		minValue, midValue, maxValue = bbox

		ws = cmds.xform(node, query=True,translation=True,ws=True)

		width = maxValue - minValue

		if minMode:
			distance = minValue - target
			ws[start] = (minValue - distance) + width / 2
		elif maxMode:
			distance = target - maxValue
			ws[start] = (maxValue + distance) - width / 2
		else:
			distance = target - midValue
			ws[start] = midValue + distance

		cmds.xform(node, translation=ws, ws=True)

class Aligner(object):

	def __init__(self):
		name = "Aligner"

		if cmds.window(name, query=True, exists=True):
			cmds.deleteUI(name)

		window = cmds.window(name)
		self.buildUI()
		cmds.showWindow()
		cmds.window(window, e=True, resizeToFitChildren=True)



	def buildUI(self):
		column = cmds.columnLayout()
		cmds.frameLayout(label="Choose an axis")

		cmds.rowLayout(numberOfColumns=3)
		cmds.radioCollection()

		self.xAxis = cmds.radioButton(label = "x",select=True)
		self.yAxis = cmds.radioButton(label="y")
		self.zAxis = cmds.radioButton(label="z")

		cmds.setParent(column)
		cmds.frameLayout(label = "Choose where to aligner")

		cmds.rowLayout(numberOfColumns=3)
		cmds.radioCollection()
		self.minMode = cmds.radioButton(label="min")
		self.midMode = cmds.radioButton(label="mid",select=True)
		self.maxMode = cmds.radioButton(label="max")

		cmds.setParent(column)

		cmds.button(label="Align",command = self.onApplyClick)


	def onApplyClick(self,*args):

		if cmds.radioButton(self.xAxis, q=True, select=True):
			axis = 'x'
		elif  cmds.radioButton(self.yAxis, q=True, select=True):
			axis = 'y'
		else :
			axis = 'z'

		#get mode
		if  cmds.radioButton(self.minMode, q=True, select=True):
			mode = 'min'
		elif  cmds.radioButton(self.midMode, q=True, select=True):
			mode = 'mid'
		else:
			mode = 'max'

		#call the align funtion
		align(axis=axis,mode=mode)
