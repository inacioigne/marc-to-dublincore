import csv

def escrever_csv(metadados):
    with open('dc.csv', 'w', newline='', encoding='utf-8') as a:

        n = ['id',
             'collection',
             'dc.contributor.advisor-co1',
             'dc.contributor.advisor1',
             'dc.creator',
             'dc.creator.Lattes[por]',
             'dc.date.issued',
             'dc.description.resumo[por]',
             'dc.language[por]',
             'dc.publisher.country[por]',
             'dc.publisher.department[por]',
             'dc.publisher.initials[por]',
             'dc.publisher.program[por]',
             'dc.publisher[por]',
             'dc.rights.uri',
             'dc.rights[por]',
             'dc.subject[por]',
             'dc.title[por]',
             'dc.type[por]']

        e = csv.DictWriter(a, fieldnames=n)
        e.writeheader()

        for i in metadados:
            e.writerow({'id' : i['id'],
                        'collection' : i['collection'],
                        'dc.contributor.advisor-co1' : i['dc.contributor.advisor-co1'],
                        'dc.contributor.advisor1' : i['dc.contributor.advisor1'],
                        'dc.creator' : i['dc.creator'],
                        'dc.creator.Lattes[por]' : i['dc.creator.Lattes[por]'],
                        'dc.date.issued' : i['dc.date.issued'],
                        'dc.description.resumo[por]' : i['dc.description.resumo[por]'],
                        'dc.language[por]' : i['dc.language[por]'],
                        'dc.publisher.country[por]' : i['dc.publisher.country[por]'],
                        'dc.publisher.department[por]' : i['dc.publisher.department[por]'],
                        'dc.publisher.initials[por]' : i['dc.publisher.initials[por]'],
                        'dc.publisher.program[por]' : i['dc.publisher.program[por]'],
                        'dc.publisher[por]':i['dc.publisher[por]'], 
                        'dc.rights.uri':i['dc.rights.uri'], 
                        'dc.rights[por]':i['dc.rights[por]'], 
                        'dc.subject[por]':i['dc.subject[por]'], 
                        'dc.title[por]' : i['dc.title[por]'],
                        'dc.type[por]' : i['dc.type[por]']})
            
                
                
    
