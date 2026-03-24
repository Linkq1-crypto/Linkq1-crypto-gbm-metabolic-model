def run_fba_pipeline(model):
    """Esegue FBA e valida lo stato della soluzione."""
    solution = model.optimize()
    if solution.status != 'optimal':
        print(f"⚠️ Soluzione non ottimale: {solution.status}")
    return solution