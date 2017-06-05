def bq():
    from google.cloud import bigquery
    from pprint import pprint
    print("Program Running")

    google_client = bigquery.Client()
    
    dataset = google_client.dataset("Python")

    #dataset.create()

    print('Dataset {} Created'.format(dataset.name))

    tableName="gradClass"

    table = dataset.table(tableName)

    table.schema = (
        bigquery.SchemaField('couserId', 'INTEGER'),
        bigquery.SchemaField('capacity', 'INTEGER'),
        bigquery.SchemaField('Name', 'STRING'),
        bigquery.SchemaField('Instructor', 'STRING'),
        bigquery.SchemaField('University', 'STRING'),
    )
    table.create()

    print('Table {} Created in the Dataset {}'. format(tableName, dataset.name))

    Rows=(
        (541, 45, 'DBMS', 'YuniXia', 'IUPUI'),
        (537, 36, 'DCCN', 'Arjan Durresi', 'IUPUI'),
        (580, 45, 'Algos', 'Judith', 'IUPUI'),
        (501, 26, 'Informatics', 'Stuart', 'IUPUI'),
        (552, 27, 'Visualization', 'Fang', 'IUPUI'),
        (590, 60, 'Cloud Computing', 'Arjan Durresi', 'IUPUI'),

    )

    errors = table.insert_data(Rows)

    if not errors:
        print('Data loaded into the table {}'.format(tableName))
    else:
        print('Errors')
        pprint(errors)

if __name__ == '__main__':
    bq()
    

