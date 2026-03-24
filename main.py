<<<<<<< HEAD
# Codice ARES v3.0 Omnia Integrato
import pandas as pd
import numpy as np
# ... (copia qui il codice completo che ti ho dato prima o usa quello che hai)
=======

import ares_engine as engine
import ares_falsification_check as check
import ares_fuzzer as fuzzer
import ares_anti_bias as antibias

def start_ares():
    print("--- [ARES SYSTEM START: V1.0 SAFE MODE] ---")
    
    # 1. Security Scan
    fuzzer.run_security_fuzzing()
    
    # 2. Integrità Dati
    check.verify_integrity("TCGA-DATA")
    
    # 3. Audit Etico
    # Simuliamo un dataset per l'audit
    import pandas as pd
    sample_data = pd.DataFrame({'Age': [45, 32, 67], 'VQE_Eigenscore_eV': [0.12, 0.15, 0.11]})
    print(antibias.check_demographic_parity(sample_data))
    
    # 4. Esecuzione Core
    results = engine.run_quantum_metabolic_protocol(n_patients=10)
    print("✅ ARES: Esecuzione completata con successo.")

if __name__ == "__main__":
    start_ares()
>>>>>>> 3c61d4e (fix: sincronizzazione repository e aggiunta 30 record clinici XML)
