from rules import TOURIST_RULESET, \
    LeisureTokens, CulturalTokens, BusinessTokens, ShoppingTokens, GourmetTokens
from production import forward_chain, backward_chain


class Selector:
    def __init__(self):
        self.var = "(?x)"
        self.leisure_list = LeisureTokens().to_choice_list()
        self.cultural_list = CulturalTokens().to_choice_list()
        self.business_list = BusinessTokens().to_choice_list()
        self.shopping_list = ShoppingTokens().to_choice_list()
        self.gourmet_list = GourmetTokens().to_choice_list()
        self.conclusion_list = [LeisureTokens.conclusion,
                                CulturalTokens.conclusion,
                                BusinessTokens.conclusion,
                                ShoppingTokens.conclusion,
                                GourmetTokens.conclusion]
        self.selector = ""

    def selection_input(self, name):
        choice_list = self._choice_list()
        print(
            f"Pick from the list of facts about {name} (ex:1 2 10 4).\n"
            f"Your choices are:")

        for index, fact in choice_list:
            print(f"\t{index}: {fact}")

        self.selector = input("\nChoose: ")

        to_chain = []
        for index in self.selector.split(" "):
            if int(index) == choice_list[int(index)][0]:
                to_chain.append(
                    choice_list[int(index)][1].replace(self.var, name))
        forward = forward_chain(TOURIST_RULESET, to_chain)

        return self._suggestion(forward, name)

    def _combine_lists(self):
        return list(
            set(self.leisure_list +
                self.cultural_list +
                self.gourmet_list +
                self.shopping_list +
                self.business_list
                )
        )

    def _suggestion(self, chained_data, name):
        suggestion_list = []
        for conclusion in self.conclusion_list:
            named_conclusion = conclusion.replace(self.var, name)
            if named_conclusion in chained_data:
                suggestion_list.append(named_conclusion)

        if len(suggestion_list) == 0:
            return f"{name} doesn't belong to any of the tourist groups. " \
                   f"(write yes/no to proceed)"
        return f"Does tourist belong to the" \
               f" next group of tourist {suggestion_list}? " \
               f"(write yes/no to proceed)"

    def _choice_list(self):
        return list(enumerate(self._combine_lists()))


if __name__ == '__main__':
    print("Welcome to Expert System! Lets do a quiz to find a tourist type!\n")
    selector = Selector()
    while True:
        name = input("Write new tourist name: ")
        suggestion = selector.selection_input(name)
        print(suggestion)
        suggestion_confirm = input("Write Here: ")
        while True:
            if suggestion_confirm == "yes":
                print("We are glad to help you!")
                break
            elif suggestion_confirm == "no":
                print(
                    "Sorry for inconveniences, "
                    "The Expert System still needs more data and rulesets "
                    "to become more accurate")
                break
            else:
                print(
                    f"System doesn't now what {suggestion_confirm}. "
                    f"Please write 'yes' or 'no'")
                suggestion_confirm = input("Write Here: ")

        exit_command = input(
            "\nDo you want to continue? "
            "(write yes/any other input to proceed)\n"
            "Write Here: ")

        if exit_command != "yes":
            print("Thanks for using expert system!")
            break
