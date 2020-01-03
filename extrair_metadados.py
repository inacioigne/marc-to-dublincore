from pymarc import MARCReader

def extrair_metadados(marc):

    with open('marc/'+marc, 'rb') as m:
        ler = MARCReader(m)
        for j in ler:
            titulo = j.title()
            autor = j.author()
            coorientador = ''
            orientador = j['700']['a']
            data = j['260']['c']
            try:
                resumo = j['520']['a']
            except:
                resumo = ''
            pais = 'Brasil'
            departamento = 'Coordenação de Pós Graduação (COPG)::3806999977129213183::600'
            sigla = 'INPA'
            publisher = 'Instituto Nacional de Pesquisas da Amazônia'
            rights_uri = 'http://creativecommons.org/licenses/by-nc-nd/4.0/'
            rights = 'Acesso Aberto'
            print('Lendo o título: \n',j.title(),'\nde:\n',j['245']['c'])
            tipo = input('É Tese ou Dissertação: ')
            curso = input('Agora o nome do Curso: ')
            idioma = input('O idioma: ')
            print('Informe o Lattes do autor (',j['245']['c'],')')
            lattes = input(': ')
            
            assunto = ''
            for x in j.subjects():
                assunto = assunto+x.get_subfields('a')[0]+'||'
	    
            

            colecao = 0
            programa = 0

            collection_ms = {
                'tede/2775' : 'Agricultura no Trópico Úmido::-2011524928240164624::500',
                'tede/63' : 'Entomologia::-8690967648724457993::500',
                'tede/1508' : 'Biologia de Água Doce e Pesca Interior::6221427379504236215::500',
                'tede/54' : 'Ecologia::3587346049760125049::500',
                'tede/60' : 'Botânica::-6324248297523177975::500',
                'tede/66' : 'Ciências de Florestas Tropicais::-3476169710787017128::500',
                'tede/70' : 'Clima e Ambiente::-5609808621161116368::500',
                'tede/73' : 'Genética, Conservação e Biologia Evolutiva::7865240273087638359::500',
                'tede/76' : 'Gestão de Áreas Protegidas da Amazônia::-8487507448692226757::500'}

            collection_dr = {
                'tede/58' : 'Biologia de Água Doce e Pesca Interior::6221427379504236215::500',
                'tede/55' : 'Ecologia::3587346049760125049::500',
                'tede/61' : 'Botânica::-6324248297523177975::500',
                'tede/64' : 'Entomologia::-8690967648724457993::500',
                'tede/67' : 'Ciências de Florestas Tropicais::-3476169710787017128::500',
                'tede/71' : 'Clima e Ambiente::-5609808621161116368::500',
                'tede/74' : 'Genética, Conservação e Biologia Evolutiva::7865240273087638359::500'}

            if tipo == 'Dissertação':
                for i in collection_ms:
                    if curso in collection_ms[i]:
                        colecao = i
                        programa = collection_ms[i]
            elif tipo == 'Tese':
                for i in collection_dr:
                    if curso in collection_dr[i]:
                        colecao = i
                        programa = collection_dr[i]
                    

        
    dict_metadados = {
        'id' : '+',
        'collection' : colecao,
        'dc.contributor.advisor-co1' : coorientador.replace('.',''),
        'dc.contributor.advisor1' : orientador.replace('.',''),
        'dc.creator' : autor,
        'dc.creator.Lattes[por]' : lattes,
        'dc.date.issued' : data[0:4],
        'dc.description.resumo[por]' : resumo,
        'dc.language[por]' : idioma,
        'dc.publisher.country[por]' : pais,
        'dc.publisher.department[por]' : departamento,
        'dc.publisher.initials[por]' : sigla,
        'dc.publisher.program[por]': programa,
        'dc.publisher[por]' : publisher,
        'dc.rights.uri' : rights_uri,
        'dc.rights[por]' : rights,
        'dc.subject[por]' : assunto[0:len(assunto)-2],
        'dc.title[por]' : titulo.replace('/',''),
        'dc.type[por]' : tipo}

    return dict_metadados
        
