try:
    import flask
    import pandas
    import sklearn
    print("Toutes les dépendances sont correctement installées.")
except ImportError as e:
    print(f"Une dépendance est manquante : {e}")