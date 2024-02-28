# Pandas não funciona muito bem no Pycharm, recomendo que use o Jupyter!

import pandas as pd

data = {
    'País': ['Bélgica', 'Índia', 'Brasil'],
    'Capital': ['Bruxelas', 'Nova Delhi', 'Brasília'],
    'População': [123456, 45678, 987655]
}

df = pd.DataFrame(data, columns=['País', 'Capital', 'População'])
print(df)

