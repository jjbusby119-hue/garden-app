def get_season_advice(season):

    # Set advice for season
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):

    # Set advice for plant
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def gen_advice(season, plant_type):

    # Generate advice
    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type)

    return advice


def main():

    # Get user input
    season = input("Enter the season:")
    plant_type = input("Enter the plant type:")

    advice = gen_advice(season, plant_type)
    print(advice)

if __name__ == "__main__":
    main()
