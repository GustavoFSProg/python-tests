import xml.etree.ElementTree as et

arquivo = et.parse('livros.xml')
print(arquivo)
# <xml.etree.ElementTree.ElementTree object at 0x7fb4985b0050>

raiz = arquivo.getroot()
print(raiz) # <Element 'catalog' at 0x7fb4984ab530>
print(raiz.tag) # 'catalog'

for filhas in raiz:
    print(filhas.tag, filhas.attrib)

    print(raiz[0][0].text) # Orwell, George
print(raiz[1][1].text)

for filhas in raiz.findall('book'):
    autor = filhas.find('author').text 
    titulo = filhas.find('title').text 
    print(f'Autor: {autor} | Título: {titulo}')

    descricoes = [d.text for d in raiz.iter('description')]
print(descricoes[0])

for genre in raiz.findall('book'):
    genero = genre.find('genre')
    if genero.text == 'Cyberpunk':
        genero.text = 'Science Fiction'
        genero.set('atualizado','sim')
    print(genero.text)
arquivo.write('novo_livros.xml')