import cobra
import os

def load_all_raw_models(raw_path='data/raw'):
    files = [os.path.join(raw_path, f) for f in os.listdir(raw_path) if f.endswith('.xml')]
    return files

def load_sbml(path):
    return cobra.io.read_sbml_model(path)
