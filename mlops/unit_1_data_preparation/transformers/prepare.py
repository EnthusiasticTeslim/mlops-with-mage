from typing import Tuple

import pandas as pd

from mlops.dependency.data_preparation.cleaning import clean
from mlops.dependency.data_preparation.feature_engineering import combine_features
from mlops.dependency.data_preparation.feature_selector import select_features
from mlops.dependency.data_preparation.splitters import split_on_value

if 'transformer' not in globals():
    f141001
181287
x

⌘
+

.




























































rom mage_ai.data_preparation.decorators import transformer


@transformer
def transform(
    df: pd.DataFrame, **kwargs
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    split_on_feature = kwargs.get('split_on_feature') # new global variable (x= icon) added to allow easy control from outside, lprep_pickup_datetime
    split_on_feature_value = kwargs.get('split_on_feature_value') # new global variable added to allow easy control from outside, 2024-02-01
    target = kwargs.get('target') # set as duration

    df = clean(df)
    df = combine_features(df)
    df = select_features(df, features=[split_on_feature, target])

    df_train, df_val = split_on_value(
        df,
        split_on_feature,
        split_on_feature_value,
    )

    return df, df_train, df_val