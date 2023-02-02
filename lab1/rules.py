from production import IF, AND, THEN, OR, forward_chain, simplify


class SharedTokens:
    interested_in_jewellery = "(?x) interested in jewellery"
    is_jewellery_expert = "(?x) is a jewellery connoisseur"


class LeisureTokens:
    stress = "(?x) copes with a lot of stress during worktime"
    no_vacation = "(?x) didn't have vacation for a long time"
    hotel_recommended = "(?x) was recommended a good hotel in Lunaria"

    wants_fun = "(?x) Wants to have fun"
    wants_a_break = "(?x) wants to take a break from daily routine life"
    conclusion = "(?x) is a leisure tourist"


class BusinessTokens:
    wants_a_meet = "(?x) wants to join a meeting related to his job"
    company_allows = "(?x) Company can to offer a " \
                     "business trip to Lunaria on a particular conference"
    wants_know_more = \
        "(?x) isn't satisfied with current knowledge regarding job"
    is_outstanding = "(?x) is an outstanding member of the company"
    conclusion = "(?x) is a business tourist"


class GourmetTokens:
    wants_cooking_book = "(?x) wants to buy a cooking book of Lunaria pastries"
    wants_taste_food = "(?x) wants to try a lot of famous Lunaria food"
    wants_taste_wine = "(?x) wants to try famous Lunaria wines"

    interested_in_wine = "(?x) interested in wine"
    wine_expert = "(?x) is a wine expert"

    interested_in_cooking = "(?x) interested in cooking"
    chef_cook = "(?x) is a chef cook"
    conclusion = "(?x) is a gourmet tourist"


class CulturalTokens(SharedTokens):
    wants_visit_museums = "(?x) wants to visit some museums"
    wants_join_tour = "(?x) wants to join a historical tour"
    tour_ticket = "(?x) bought a ticket from a tour company"
    is_museum_guest = "(?x) is in invited guest list of a museum"
    wants_visit_jewellery_museum = "(?x) wants to visit a famous jewellery museum in Lunaria"
    conclusion = "(?x) is a cultural tourist"


class ShoppingTokens(SharedTokens):
    wants_buy_lunarithe_ring = "(?x) wants to buy a the ring with a Lunarithe gem"
    wants_shop_clothes = "(?x) wants to shop clothes with unique local design"

    interested_in_branded_clothes = "(?x) interested in branded clothes"
    interested_in_second_hand = "(?x) interested in second-hand clothes"
    has_necessary_money = "(?x) has necessary money"
    conclusion = "(?x) is a shopping tourist"


TOURIST_RULESET = (

    # first type
    IF(AND(LeisureTokens.stress,
           LeisureTokens.no_vacation),
       THEN(LeisureTokens.wants_a_break)),

    IF(AND(LeisureTokens.hotel_recommended,
           LeisureTokens.no_vacation),
       THEN(LeisureTokens.wants_fun)),

    IF(OR(LeisureTokens.wants_a_break,
          LeisureTokens.wants_fun),
       THEN(LeisureTokens.conclusion)),

    # second type
    IF(AND(BusinessTokens.wants_know_more),
       THEN(BusinessTokens.wants_a_meet)),

    IF(AND(BusinessTokens.is_outstanding),
       THEN(BusinessTokens.company_allows)),

    IF(AND(BusinessTokens.wants_a_meet,
           BusinessTokens.company_allows),
       THEN(BusinessTokens.conclusion)),

    # third type
    IF(AND(GourmetTokens.chef_cook),
       THEN(GourmetTokens.interested_in_cooking)),

    IF(AND(GourmetTokens.wine_expert),
       THEN(GourmetTokens.interested_in_wine)),

    IF(AND(GourmetTokens.interested_in_cooking),
       THEN(GourmetTokens.wants_cooking_book)),

    IF(AND(GourmetTokens.interested_in_cooking),
       THEN(GourmetTokens.wants_taste_food)),

    IF(AND(GourmetTokens.interested_in_wine),
       THEN(GourmetTokens.wants_taste_wine)),

    IF(OR(GourmetTokens.wants_taste_food,
          GourmetTokens.wants_taste_wine,
          GourmetTokens.wants_cooking_book),
       THEN(GourmetTokens.conclusion)),

    # fourth type

    # shared state
    IF(AND(CulturalTokens.is_jewellery_expert),
       THEN(CulturalTokens.interested_in_jewellery)),

    IF(AND(CulturalTokens.interested_in_jewellery,
           CulturalTokens.is_museum_guest),
       THEN(CulturalTokens.wants_visit_jewellery_museum)),

    IF(AND(CulturalTokens.tour_ticket),
       THEN(CulturalTokens.wants_join_tour)),

    IF(OR(CulturalTokens.wants_visit_jewellery_museum,
          CulturalTokens.wants_join_tour),
       THEN(CulturalTokens.conclusion)),

    # fifth type
    IF(OR(ShoppingTokens.interested_in_branded_clothes,
          ShoppingTokens.interested_in_jewellery),
       THEN(ShoppingTokens.wants_shop_clothes)),

    IF(AND(ShoppingTokens.interested_in_jewellery,
           ShoppingTokens.has_necessary_money),
       THEN(ShoppingTokens.wants_buy_lunarithe_ring)),

    IF(OR(ShoppingTokens.wants_buy_lunarithe_ring,
          ShoppingTokens.wants_shop_clothes),
       THEN(ShoppingTokens.conclusion)),
)

leisure_tourist_name = "Dmitriy"

TOURIST_DATA = (
    LeisureTokens.no_vacation.replace("(?x)", leisure_tourist_name),
    LeisureTokens.stress.replace("(?x)", leisure_tourist_name),
    LeisureTokens.wants_a_break.replace("(?x)", leisure_tourist_name),
)

inst = forward_chain(TOURIST_RULESET, TOURIST_DATA)
print(inst)
