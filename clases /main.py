import parsear 
from razon import Razones
from report import GetHtml

data = parsear.paresearFile('../data/eventos_gold.json')
cliente = data.cliente
eventos = data.tranferencias
datosResporte = Razones(cliente, eventos)
html = GetHtml.create_HTML(datosResporte)



