def clothing_suggestion(season):
    if season.lower() == "spring":
        return "Light jacket or shirt, along with light jeans."
    elif season.lower() == "summer":
        return "Light dresses, shorts, and flip-flops."
    elif season.lower() == "autumn":
        return "Coat or light jacket, and dark jeans."
    elif season.lower() == "winter":
        return "Thick coat, scarf, and ear muffs."
    else:
        return "Invalid season entered."

season = input("Enter the season (spring, summer, autumn, winter): ")
suggestion = clothing_suggestion(season)
print(suggestion)
