	
import random


years = {
    1801: [
    "Some events",
    "One more event"
    ],

    1802: [
        "Кого-то там убили",
        "Что-то ещё"
    ],

    1803: [
        "Абра кадабра какая-то",
        "Событие"
    ],

    1804: [
        "А здесь одно событие"
    ]
}

i = random.randint(0, len(years.keys())-1)

k = list(years)[i]

print ("Что произошло в", k, "году?")

for key in years.keys():   
    print(key, years[key])
