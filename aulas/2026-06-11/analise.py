arq = open('servidores.csv', 'r')
registros = arq.read().splitlines()
arq.close()

arq_html = open('cargos.html', 'w')

arq_html.write('<html>')
arq_html.write('<head>')
arq_html.write('<title>')
arq_html.write('Cargos')
arq_html.write('</title>')
arq_html.write('</head>')

arq_html.write('<body>')

# descobrir os cargos que tem no ifpb
cargos = []

for registro in registros:
    servidor = registro.split(',')
    if servidor[2] not in cargos:
        cargos.append(servidor[2])
        
        arq_html.write(servidor[2])
        arq_html.write('<br>')

arq_html.write('</body>')
arq_html.write('</html>')

arq_html.close()

#print(cargos)
