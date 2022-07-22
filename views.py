from tkinter import N
import db
import models
import json 

body_types = ['sedan', 'universal', 'coupe', 'hatchback', 'universal', 'minivan', 'SUV', 'pickup']

def create():
    brand = input('Укажите марку машины: ')
    model = input('Укажите модель машины: ')
    release_year = input('Укажите год выпуска: ')
    engine_volume = input('Укажите обьем двигателя: ')
    color = input('Укажите цвет машины: ')
    miliage = input('Укажите пробег машины: ')
    price = input('Укажите цену машины: ')


    print("Выберите тип кузова: ")

    selected_body_type = None

    for type in body_types:
        print(f"* {type}")
    while True:
        body_type = input("==================================\nВыберите тип кузова: ")
        if body_type in body_types:
            selected_body_type = body_type
            break
        else:
            raise print("Такого типа не существует")
    
    car = models.Car(
        brand=brand,
        model=model,
        release_year=int(release_year),
        engine_volume=float(engine_volume),
        color=color,
        body_type=selected_body_type,
        miliage=miliage,
        price=price
    )
    print(car)

    db1 = db.DBCar()
    db1.create(car)


def listing():
    db_car = db.DBCar()
    print(db_car.get_object_list())


def retrieve(id: int):
    db_car = db.DBCar()
    car = db_car.get_by_id(id=int(id))
    if car:
        print(car)
    else:
        print("Not found.")


def delete(id: int):
    db_car = db.DBCar()
    db_car.delete(int(id))
    print("Successfuly deleted")


def update(id: int):
    db_car = db.DBCar()
    car = db_car.get_by_id(id=int(id))

    
    brand = input(f'Укажите марку машины ({car.brand}): ')
    model = input(f'Укажите модель машины ({car.model}): ')
    release_year = input(f'Укажите год выпуска({car.release_year}): ')
    engine_volume = input(f'Укажите обьем двигателя ({car.engine_volume}): ')
    color = input(f'Укажите цвет машины ({car.color}): ')
    miliage = input(f'Укажите пробег машины ({car.miliage}): ')
    price = input(f'Укажите цену машины ({car.price}): ')


    print("Выберите тип кузова: ")

    selected_body_type = None

    for type in body_types:
        print(f"* {type}")
    while True:
        body_type = input(f"==================================\nВыберите тип кузова: ")
        if body_type in body_types:
            selected_body_type = body_type
            break
        else:
            raise print("Такого типа не существует")


    updated_car = models.Car(
        brand=brand,
        model=model,
        release_year=int(release_year),
        engine_volume=float(engine_volume),
        color=color,
        body_type=selected_body_type,
        miliage=miliage,
        price=price,
        id=car.id,
    )

    db_car.update(updated_car)


    


   

if __name__ == "__main__":
    create()

