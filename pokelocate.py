
# ---imports
import requests

# ---setup and funcitons
pokeapiurl = "https://pokeapi.co/api/v2/"

# gets the data
def get_data(pokemon):
    url = f"{pokeapiurl}/pokemon/{pokemon}" # concatenate a url built on top of base url
    api_response = requests.get(url)

    if api_response.status_code == 200:
        pokemon_data = api_response.json() #gets it as a json file and then returns it
        return pokemon_data
    else: 
        print("Error in input or data unavailable")

def get_location_data(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}/encounters"
    api_response = requests.get(url)

    if api_response.status_code == 200:
        location_data = api_response.json() #gets it as a json file and then returns it
        return location_data
    else: 
        print("Error in the coder's logic, this guy bruh")

# ---main
state = True

while state:
    choice = input("Enter Pokemon name for which you want location data (or type exit to end the script): ")
    choice = choice.lower()
    
    if choice != "exit":
        info = get_data(choice)
    else:
        break

    if info:
        id = info["id"]
        location_info = get_location_data(id)

        if location_info:
            print ("It can be found in the following places:")
            for encounter in location_info:
            
                # location info
                location_dict = encounter["location_area"]
                name = location_dict["name"] 

                # game info
                other_info = encounter["version_details"]
                
                for version_detail in other_info:
                    version = version_detail["version"]
                    game_name = version["name"]
    
                    print(f"  - {name} in {game_name}") # final output


        else:
            print("This Pokemon cannot be obtained.")