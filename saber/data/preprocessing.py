import pandas as pd 
import pandas_flavor as pf 
from sklearn.preprocessing import LabelEncoder

@pf.register_dataframe_method
def _binary_label_encoder(df):

    label_encoder = LabelEncoder()

    categorical_cols = [column for column in df.columns if
                        df[column].nunique() == 2 and
                        df[column].dtype == 'object']

    
    for column in categorical_cols:

        encoder_column = label_encoder.fit_transform(df[column])
        encoder_column = pd.DataFrame(encoder_column, columns=[column])

        df.drop([column], axis=1, inplace=True)
        df = pd.concat([df, encoder_column], axis=1)

    return df