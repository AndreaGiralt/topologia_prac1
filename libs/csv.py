from libs.database import Database
import csv

def return_value(real_state,key):
    if key in real_state:
        return real_state[key]
    return ""

def create_csv():
    db = Database ()
    real_states = db.getRealStates()

    with open("data/real_states.csv","w",encoding='UTF8') as file:
        csv_file = csv.writer(file,delimiter=";")
        #Writing headers
        csv_file.writerow(['id', 'type','title'
                              ,'description','town','zone','price','surface'
                              ,'rooms','bathrooms','floor','longitude'
                              ,'latitude','url','exact_position','recently_date'
                              ,'is_promo','image_url','owner_name','old_price'])

        for real_state in real_states:
            csv_file.writerow([return_value(real_state,'id')
                                  , return_value(real_state,'type')
                                  , return_value(real_state,'title')
                                  , return_value(real_state,'description')
                                  , return_value(real_state,'town')
                                  , return_value(real_state,'zone')
                                  , return_value(real_state,'price')
                                  , return_value(real_state,'surface')
                                  , return_value(real_state,'rooms')
                                  , return_value(real_state,'bathrooms')
                                  , return_value(real_state,'floor')
                                  , return_value(real_state,'longitude')
                                  , return_value(real_state,'latitude')
                                  , return_value(real_state,'url')
                                  , return_value(real_state,'exact_position')
                                  , return_value(real_state,'recently_date')
                                  , return_value(real_state,'is_promo')
                                  , return_value(real_state,'image_url')
                                  , return_value(real_state,'owner_name')
                                  , return_value(real_state,'old_price')
                               ])
