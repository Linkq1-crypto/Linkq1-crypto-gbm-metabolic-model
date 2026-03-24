import cobra
import os
import pandas as pd

def load_gbm_model(path='model/gbm_model.xml'):
    """Carica il modello SBML. Se non esiste, crea un modello minimo di test."""
    if not os.path.exists(path):
        print(f"⚠️ Avviso: {path} non trovato. Creo un modello dummy per il test.")
        model = cobra.Model('GBM_Test_Model')
        v1 = cobra.Reaction('EX_glc__D_e') # Esempio Glucosio
        model.add_reactions([v1])
        return model
    return cobra.io.read_sbml_model(path)

def save_results(df, filename):
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv(f'data/processed/{filename}')