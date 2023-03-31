__author__='Christian Marius Lillelund'
__author_email__='chr1000@gmail.com'

import numpy as np
import pandas as pd
import shap
from sksurv import datasets

import pkg_resources

resource_package = __name__

def convert_to_structured(T, E):
    default_dtypes = {"names": ("event", "time"), "formats": ("bool", "f8")}
    concat = list(zip(E, T))
    return np.array(concat, dtype=default_dtypes)

def load_seer_dataset():
    resource = pkg_resources.resource_stream(resource_package, 'seer.csv')    
    data = pd.read_csv(resource)

    outcomes = data.copy()
    outcomes['event'] =  data['Status']
    outcomes['time'] = data['Survival Months']
    outcomes = outcomes[['event', 'time']]
    outcomes.loc[outcomes['event'] == 'Alive', ['event']] = 0
    outcomes.loc[outcomes['event'] == 'Dead', ['event']] = 1
    
    data = data.drop(['Status', "Survival Months"], axis=1)
    
    X = pd.DataFrame(data)
    y = convert_to_structured(outcomes['time'], outcomes['event'])
    return (X, y)

def load_nhanes_dataset():    
    nhanes_X, nhanes_y = shap.datasets.nhanesi()
    X = pd.DataFrame(nhanes_X)
    event = np.array([True if x > 0 else False for x in nhanes_y])
    time = np.array(abs(nhanes_y))
    y = convert_to_structured(time, event)
    return (X, y)

def load_support_dataset():
    resource = pkg_resources.resource_stream(resource_package, 'support.feather')    
    data = pd.read_feather(resource)

    outcomes = data.copy()
    outcomes['event'] =  data['event']
    outcomes['time'] = data['duration']
    outcomes = outcomes[['event', 'time']]
    
    feats =  ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6',
              'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13']
    
    X = pd.DataFrame(data[feats])
    y = convert_to_structured(outcomes['time'], outcomes['event'])
    return (X, y)

def load_aids_dataset():
    X, y = datasets.load_aids()
    X = pd.DataFrame(X) 
    y = convert_to_structured(y['time'], y['censor'])
    return (X, y)

def load_veterans_dataset():
    X, y = datasets.load_veterans_lung_cancer()
    X = pd.DataFrame(X) 
    y = convert_to_structured(y['Survival_in_days'], y['Status'])
    return (X, y)

def load_whas500_dataset():
    X, y = datasets.load_whas500()
    X = pd.DataFrame(X) 
    y = convert_to_structured(y['lenfol'], y['fstat'])
    return (X, y)

def load_flchain_dataset():
    X, y = datasets.load_flchain()
    X = pd.DataFrame(X) 
    y = convert_to_structured(y['futime'], y['death'])
    return (X, y)

def load_gbsg2_dataset():
    X, y = datasets.load_gbsg2()
    X = pd.DataFrame(X) 
    y = convert_to_structured(y['time'], y['cens'])
    return (X, y)

def load_metabric_dataset():
    resource = pkg_resources.resource_stream(resource_package, 'metabric.feather')
    data = pd.read_feather(resource)

    outcomes = data.copy()
    outcomes['event'] =  data['event']
    outcomes['time'] = data['duration']
    outcomes = outcomes[['event', 'time']]

    num_feats =  ['x0', 'x1', 'x2', 'x3', 'x8'] \
                    + ['x4', 'x5', 'x6', 'x7']

    X = pd.DataFrame(data[num_feats])
    y = convert_to_structured(outcomes['time'], outcomes['event'])
    return (X, y)