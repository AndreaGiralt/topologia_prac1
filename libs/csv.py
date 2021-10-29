from libs.database import Database
import csv

def create_csv():
    db = Database ()
    real_states = db.getRealStates()

    for real_state in real_states:

        state.fromMongo(real_state)

        print(state)

        #exit(-1)

    """
    with open("data/royal_states.csv") as file:
        csv_file = csv.writer(file)
        #Ponemos las cabeceras:
        csv_file.writerow(['zone', 'total'])
    """
