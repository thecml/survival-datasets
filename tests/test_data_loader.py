from survdata import datasets
import sklearn.utils as skut

def test_seer_dataset():
    X, y = datasets.load_seer_dataset()
    skut.check_X_y(X, y, dtype=None)
    
def test_load_nhanes_dataset():
    X, y = datasets.load_nhanes_dataset()
    skut.check_X_y(X, y, dtype=None, force_all_finite='allow-nan')
    
def test_load_support_dataset():
    X, y = datasets.load_support_dataset()
    skut.check_X_y(X, y, dtype=None)
    
def test_load_aids_dataset():
    X, y = datasets.load_aids_dataset()
    skut.check_X_y(X, y, dtype=None)

def test_load_veterans_dataset():
    X, y = datasets.load_veterans_dataset()
    skut.check_X_y(X, y, dtype=None)
    
def test_load_whas500_dataset():
    X, y = datasets.load_whas500_dataset()
    skut.check_X_y(X, y, dtype=None)

def test_load_flchain_dataset():
    X, y = datasets.load_flchain_dataset()
    skut.check_X_y(X, y, dtype=None, force_all_finite='allow-nan')
    
def test_load_gbsg2_dataset():
    X, y = datasets.load_gbsg2_dataset()
    skut.check_X_y(X, y, dtype=None)

def test_load_metabric_dataset():
    X, y = datasets.load_metabric_dataset()
    skut.check_X_y(X, y, dtype=None)