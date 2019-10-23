import os
import pydicom

print("Executando... Por favor aguarde.")
arq = open('dicom.xml', 'w')
texto = []


texto.append("<?xml version=\"1.0\"?>\n")
		
path = os.getcwd() + '\\Exames de imagem\\'
for r, d, f in os.walk(path):
	for file in f:
		if '.dcm' in file:
			path = str(r) + "\\" + str(file)
			texto.append("\t<data src=\"" + path + "\">\n")
			ds = pydicom.filereader.dcmread(path)
			for key in ds.dir():
				data_element = ds.data_element(key)
				vr = str(data_element.VR) # ok
				tag = str(data_element.tag) # ok
				vm = str(data_element.VM) # ok
				name = str(data_element.name) # ok
				value = str(data_element.value) # ok
				lenght = str(len(value)) # ok
				texto.append("\t\t<element vr=\"" + vr + "\" tag=\"" + tag + "\" vm=\"" + vm + "\" name=\"" + name + "\" len=\"" + lenght + "\">" + value + "</element>\n")

arq.writelines(texto)
arq.close()