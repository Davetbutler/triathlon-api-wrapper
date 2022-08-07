from tri_api_wrapper import Athlete, AthleteListings

beth_athlete_id = 117212
athlete_info = Athlete.info(beth_athlete_id)

print(athlete_info)

athlete_listings = AthleteListings.listings(catagory_id="42", gender="female", elite="true")
print(athlete_listings)