import requests


def get_all_cities():
    response = requests.get("https://my-json-server.typicode.com/leisurepassgroup/SDET-interview/citys")
    response_body = response.json()
    print("All cities Includes")
    for d in response_body:
        city = d['title']
        print(city)


def get_all_attractions_for_a_city_New_York():
    response = requests.get("https://my-json-server.typicode.com/leisurepassgroup/SDET-interview/attractions")
    response_body = response.json()
    print("New York Attractions are:")
    for d in response_body:
        attraction = d['cityId' and 'title' ]
        print(attraction)



def get_all_attractions_for_a_city_New_York_type_Museum_ordered_by_desc(cityid,type):
    response = requests.get(f"https://my-json-server.typicode.com/leisurepassgroup/SDET-interview/attractions?cityId={cityid}&type={type}&_sort=type&_order=desc")
    response_body = response.json()
    print("New York Attractions for type Museum  are:")
    for d in response_body:
        attraction = d['type' and 'cityId'and 'title']

        print(attraction)




