from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'tasks'
    players_per_group = None
    tasks = ["anchoring", "overconfidence", "escalation"]
    num_rounds = len(tasks) #3 rounds


class Subsession(BaseSubsession):
    training = models.StringField() # VT/TT/UT
    accountability = models.StringField() # hoch/niedrig
    
    def creating_session(self):
        if self.session.config["name"] == "VT_hoch": #see dict in settings.py
            self.training = "VT"
            self.accountability = "hoch"
        elif self.session.config["name"] == "TT_hoch":
            self.training = "TT"
            self.accountability = "hoch"
        elif self.session.config["name"] == "UT_hoch":
            self.training = "UT"
            self.accountability = "hoch"
        elif self.session.config["name"] == "VT_niedrig":
            self.training = "VT"
            self.accountability = "niedrig"
        elif self.session.config["name"] == "TT_niedrig":
            self.training = "TT"
            self.accountability = "niedrig"
        elif self.session.config["name"] == "UT_niedrig":
            self.training = "UT"
            self.accountability = "niedrig"
        else:
            print("treatment not found")

        if self.round_number == 1: #shuffle tasks in the beginning of the app session
            for p in self.get_players(): #access each player
                round_numbers = list(range(1, Constants.num_rounds+1)) #round_numbers = [1,2,3]
                random.shuffle(round_numbers) #eg round_numbers = [2,1,3]
                # print(round_numbers)
                p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers)) #{"anchoring":2, "overconfidence":1, "escalation":3}

        for player in self.get_players(): #generate random number for every player at the start of the session 
            player.participant.vars['accountability_draft'] = random.randint(1,4) #assign one random number in the range 1-4 to every participant. 1 = EoC, 2 = OC1, 3 = OC2, 4 = Anchor 
            # print(player.participant.vars.get('accountability_draft')) #debug


class Group(BaseGroup):
    pass


def create_peq(labelinput):
    return models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label=labelinput)

def create_mc(mc,choiceslist):
    return models.IntegerField(verbose_name = mc,choices=choiceslist,widget=widgets.RadioSelect)

class Player(BasePlayer):
    OC1_low = models.IntegerField()
    OC1_high = models.IntegerField()

    OC2_low = models.IntegerField()
    OC2_high = models.IntegerField()

    OC3_low = models.IntegerField()
    OC3_high = models.IntegerField()

    OC4_low = models.IntegerField()
    OC4_high = models.IntegerField()

    OC5_low = models.IntegerField()
    OC5_high = models.IntegerField()

    OC6_low = models.IntegerField()
    OC6_high = models.IntegerField()

    OC7_low = models.IntegerField()
    OC7_high = models.IntegerField()

    OC8_low = models.IntegerField()
    OC8_high = models.IntegerField()

    OC9_low = models.IntegerField()
    OC9_high = models.IntegerField()

    OC10_low = models.IntegerField()
    OC10_high = models.IntegerField()

    Anchor = models.IntegerField()

    Anchor_Anker=create_mc("Does the jar contain more than 95 peanuts?", [[1,"Yes"],[2,"No"]])

    Accountability = models.LongStringField()

    OC_task2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7,8,9,10], label="Please indicate your estimated position in this experimental group. Please note that the higher the value you indicate, the better you estimate your position within the experimental group.")

    EoC_task=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7,8,9,10], label="How would you decide on the continuation of the project?")

    Initial=create_mc("Which of the two projects will you present at the meeting?", [[1, "Project A"], [2, "Project B"]])

    OC_comp1_quest1=create_mc("How many intervals should you estimate?", [[1, "9"], [2, "5"], [3, "10"], [4, "1"]])

    OC_comp1_quest2=create_mc("90 % certainty means,", [[1, "that 9 out of 10 of your estimated intervals do not include the correct answer."], [2, "that 1 out of 10 of your estimated intervals does not include the correct answer."], [3, "only 9 out of 10 intervals need to be estimated."], [4, "all of the 10 of your estimated intervals include the correct answer."]])

    OC_comp1_quest3=create_mc("What is an example of the correct input spelling?", [[1, "50,743"], [2, "10.3"], [3, "2,300.72"], [4, "5463"]])

    OC_comp1_quest1b=create_mc("How many intervals should you estimate?", [[1, "9"], [2, "5"], [3, "10"], [4, "1"]])

    OC_comp1_quest2b=create_mc("90 % certainty means,", [[1, "that 9 out of 10 of your estimated intervals do not include the correct answer."], [2, "that 1 out of 10 of your estimated intervals does not include the correct answer."], [3, "only 9 out of 10 intervals need to be estimated."], [4, "all of the 10 of your estimated intervals include the correct answer."]])

    OC_comp1_quest3b=create_mc("What is an example of the correct input spelling?", [[1, "50,743"], [2, "10.3"], [3, "2,300.72"], [4, "5463"]])

    OC_comp2_quest1=create_mc("To whom should you compare your estimation performance from the previous subtask.", [[1, "to other experiment participants"], [2,"to no one"], [3, "to the American population"], [4, "to the worst participant"]])

    OC_comp2_quest2=create_mc("The lower the value, the better you estimate your position.", [[1,"True"], [2, "False"]])

    OC_comp2_quest1b=create_mc("To whom should you compare your estimation performance from the previous subtask.", [[1, "to other experiment participants"], [2,"to no one"], [3, "to the American population"], [4, "to the worst participant"]])

    OC_comp2_quest2b=create_mc("The lower the value, the better you estimate your position.", [[1,"True"], [2, "False"]])

    EoC_comp1_quest1=create_mc("Which of the following statements is correct?", [[1, "The life span of your project is over and you are looking for a new lucrative project."], [2, "Your project is going better than expected and still has fantastic predictions."], [3, "The further development of your project is uncertain and you have to decide on the further course."]])

    EoC_comp1_quest2=create_mc("Initiating your project was…", [[1, "…very laborious. You had to assert yourself against your colleagues and put a lot of time and effort into the project."], [2, "…not exhausting. You only had to supervise the project on the side and were rarely involved."]])

    EoC_comp1_quest1b=create_mc("Which of the following statements is correct?", [[1, "The life span of your project is over and you are looking for a new lucrative project."], [2, "Your project is going better than expected and still has fantastic predictions."], [3, "The further development of your project is uncertain and you have to decide on the further course."]])

    EoC_comp1_quest2b=create_mc("Initiating your project was…", [[1, "…very laborious. You had to assert yourself against your colleagues and put a lot of time and effort into the project."], [2, "…not exhausting. You only had to supervise the project on the side and were rarely involved."]])


    time_EoC_ov = models.StringField() 
    time_EoC_ovCheck = models.StringField()
    time_EoC_ov2 = models.StringField()
    time_EoC_task = models.StringField()
    time_OC_task1 = models.StringField()
    time_OC_task2 = models.StringField()
    time_Anchor = models.StringField()
    time_Just = models.StringField()


    tabOC1 = models.IntegerField()
    tabAnchor = models.IntegerField()

    participantvars =models.LongStringField()
