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
				vr = str(data_element.VR)
				if vr != "OW":
					tag = str(data_element.tag)
					vm = str(data_element.VM)
					name = str(data_element.name)
					value = str(data_element.value)
					lenght = str(len(value))
					texto.append("\t\t<element vr=\"" + vr + "\" tag=\"" + tag + "\" vm=\"" + vm + "\" name=\"" + name + "\" len=\"" + lenght + "\">" + value + "</element>\n")
			texto.append("\t</data>\n")

arq.writelines(texto)
arq.close()