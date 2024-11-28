import pandas as pd

def pull_data(URL_source, table):
    '''Returns a specific table from the web page where the first argument is the URL and the second is the web page table'''

    df = pd.read_html(URL_source)
    return df[table]
