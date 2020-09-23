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

import datetime

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1

    lottery_payout = ["$0,75", "$1,50", "$0,00"] # used in the html table template
    lottery_gamble_successrate = [(85 - i) for i in range(0,75, 5)] #[15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
    lottery_gamble_failurerate = [(15 + i) for i in range(0,75, 5)]

     #lottery payment
    lottery_success = 1.50
    lottery_failure = 0.00
    lottery_safe = 0.75

class Subsession(BaseSubsession):
    training = models.StringField() # VT/TT/UT
    accountability = models.StringField() # hoch/niedrig


    def creating_session(self): #automatically executed when session is generated (is executed for each new round)
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

class Group(BaseGroup):
    pass

def create_peq(labelinput):
    return models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label=labelinput)

def create_mc(mc,choiceslist):
    return models.IntegerField(verbose_name = mc,choices=choiceslist,widget=widgets.RadioSelect)

def create_neu(mc,choiceslist):
    return models.IntegerField(verbose_name = mc,choices=choiceslist,widget=widgets.RadioSelectHorizontal)



class Player(BasePlayer):

    qBiasknowledge2=create_mc("Do you have any prior experience with the topic ‘Cognitive Biases’?", [[1,"Yes, I have some experience with cognitive biases."],[2,"No, I do not have any experience with cognitive biases."]])

    qBiasknowledge3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Please evaluate to what extent the following statement applies to you. I am familiar with the topic of ‘Cognitive Biases’.")

    qsustaininvest2=create_mc("Do you have any prior experience with the topic ‘Sustainable Investing’?", [[1,"Yes, I have some experience with sustainable investing."],[2,"No, I do not have any experience with sustainable investing."]])
    
    qsustaininvest3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Please evaluate to what extent the following statement applies to you. I am familiar with the topic of ‘Sustainable Investing’.")

    sound_image_check=create_mc("Which of the statements about the video shown above is correct?", [[1,"I could see a cow and I heard a cat meow."],[2,"I could see a dog and I heard a cat meow."], [3, "I could see a cow and I heard a rooster crow."], [4, "I could see a dog and I heard a rooster crow."]])

    compensation=create_mc("What is the composition of your total compensation?", [[1,"Fixed component + variable component"], [2, "Fixed component + lottery payout"], [3, "Variable component + lottery payout"], [4, "Fixed component only"]])

    independency=create_mc("The three decision-making tasks are independent of each other.", [[1, "Yes"],[2, "No"]])

    procedure=create_mc("What is the order of the main part of the experiment?", [[1, "First you will be given three decision-making tasks, then you have to complete a training."], [2, "First you have to complete a training, then you will be given three decision-making tasks."]])

    NPV=create_neu("What is the formula to calculate the NPV in this example?", [[1, "A"], [2, "B"], [3, "C"], [4, "D"], [5, "E"], [6, "F"]])

    lottery_choice = models.PositiveIntegerField(choices=[[i, f"Scenario {i}"] for i in range(1,16)], widget=widgets.RadioSelect) #Lottery page; reuse in main experiment to determine payout

    Tsec2_quest1=create_mc("What is the cause of cognitive biases?", [[1, "System 1 can solve complex tasks, but is not activated enough."], [2, "System 1 generates erroneous suggestions and System 2 fails to correct them."], [3, "System 2 is constantly in a strained mode, whereas System 1 is mostly on stand-by."], [4, "System 2 is wrongly activated instead of using the reflective System 1."]])

    Tsec2_quest2=create_mc("Which of the statements about heuristics is incorrect?", [[1, "The use of heuristics can lead to cognitive biases."], [2, "Heuristics are effective in most cases."], [3, "Heuristics increase mental effort and reduce substantial amounts of time."], [4, "Knowledge and experience do not always prevent the erroneous use of heuristics."]])

    UVsec2_quest1=create_mc("What does the abbreviation ESG stand for?", [[1, "Economic, Sustainability, Governance"], [2, "Environmental, Sustainability, Global"], [3, "Environmental, Social, Governance"], [4, "Economic, Social, Global"]])

    UVsec2_quest2=create_mc("What was the result of the implementation of various ESG initiatives at state street?", [[1, "$23 mio. operational costs can be saved annually and 100k tons of carbon can be avoided."], [2, "$23 mio. operational costs must be paid annually but therefore, 100k tons of carbon can be avoided."], [3, "$23 mio. operational costs can be saved annually but therefore, 100k tons of carbon are additionally emitted."], [4, "$23 mio. operational costs must be paid annually and 100k tons of carbon are additionally emitted."]])

    Tsec3_quest1=create_mc("Which of the statements is correct?", [[1, "When making a decision, personal effort in the past should be considered in addition to monetary costs."], [2, "Sunk costs, e.g. past monetary costs or past personal effort, should not play a role in a decision-making process."], [3, "When making a decision, personal effort in the past should not be considered, but past monetary costs should."], [4, "A decision should take future and sunk costs into account."]])

    Tsec3_quest2=create_mc("Which of the statements is correct?", [[1, "The external environment has no influence on the decision-making process."], [2, "External influences and you yourself can cause cognitive biases."], [3, "There is nothing you can do yourself to make the decision-making process better."], [4, "To improve the efficiency of the decision-making process, System 2 should always be used."]])

    Tsec3_quest3=create_mc("In what situation is the use of System 1 not efficient? Please choose the second answer regardless of the question.", [[1, "Reading big words on billboards."], [2, "Driving over an empty road."], [3, "Preparing a cost benefit analysis."], [4, "Solving the equation 2 + 2."]])

    UVsec3_quest1=create_mc("The data show that stocks with better ESG performance…", [[1, "perform worse compared to other companies."], [2, "perform just as well as other companies."], [3, "always perform much better compared to other companies. "]])

    UVsec3_quest2=create_mc("Which of the statements is incorrect?", [[1, "The worth of the global stock and bond market exceeds the US GDP by eight and a half times."], [2, "Companies and investors are singularily responsible for the fate of the planet."], [3, "The global stock market is worth less than the global bond market."], [4, "CalPERS integrated ESG systematically across the entire fund."]])

    UVsec3_quest3=create_mc("According to CalPERS, long-term value creation requires the effective management of which forms of capital? Please choose the second answer regardless of the question.", [[1, "Spiritual, natural and philosophical"], [2, "Historical, social and cultural "], [3, "Fashionable, geographical and political "], [4, "Financial, human and physical"]])

    Intr_Mot1VT=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Watching the video was enjoyable.")

    Intr_Mot1TT=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Reading the text was enjoyable.")

    Intr_Mot2VT=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="The video was interesting.")
    
    Intr_Mot2TT=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="The text was interesting.")
    

    Mod1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="The presence of the moderator in the training enhanced my learning process.")

    Mod2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I have found the moderator useful in the training.")

    Pace=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is important to me to determine the learning pace myself.")

    Cogn_Lo1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It was easy for me to learn something from the presentation I just saw.")

    Cogn_Lo2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I would consider the training content as easy.")

    Cogn_Lo3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I consider the presentation format as bothersome.")

    Cogn_Lo4=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I did exert myself in order to learn the content.")

    Ment_Eff=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Please indicate the mental effort you perceived during the training.")

    Mood=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="How do you feel today?")

    Train_ManCheckVT=create_mc("The training was designed as:", [[1, " a video training on cognitive biases."], [2, "a text training on cognitive biases."], [3, "a video training on sustainable investing."], [4,  "a text training on sustainable investing."]])

    Train_ManCheckTT=create_mc("The training was designed as:", [[1, " a video training on cognitive biases."], [2, "a text training on cognitive biases."], [3, "a video training on sustainable investing."], [4,  "a text training on sustainable investing."]])

    Train_ManCheckUT=create_mc("The training was designed as:", [[1, " a video training on hedge funds."], [2, "a text training on hedge funds."], [3, "a video training on sustainable investing."], [4,  "a text training on sustainable investing."]])

    DuCha_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I can learn best when the content is presented...")

    Estima=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I think I perform well in estimation tasks.")

    Analy=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I think I perform well in analytical tasks.")



    timespent = models.StringField()
    time_start = models.StringField() #get time of participant when welcome page is loaded
    time_end = models.StringField() #get time of participant when last page is loaded
    time_Aussortieren2 = models.StringField() # time Aussortieren2
    time_wel_ins2 = models.StringField()
    time_Comprehension = models.StringField()
    time_Lottery_ins = models.StringField()
    time_Lottery = models.StringField()
    time_TT_sec_1 = models.StringField()
    time_TT_sec_2_1 = models.StringField()
    time_TT_sec_2_2 = models.StringField()
    time_TT_sec_3_1 = models.StringField()
    time_TT_sec_3_2 = models.StringField()
    time_TT_sec_4 = models.StringField()
    time_ACyes = models.StringField()

    timezone = models.IntegerField()
    tabNPV = models.IntegerField()
    tabVT1 = models.IntegerField()
    tabVT2 = models.IntegerField()
    tabVT3 = models.IntegerField()
    tabVT4 = models.IntegerField()
    tabUV1 = models.IntegerField()
    tabUV2 = models.IntegerField()
    tabUV3 = models.IntegerField()
    tabUV4 = models.IntegerField()

    tabTTsec21 = models.IntegerField()
    tabTTsec22 = models.IntegerField()
    tabTTsec31 = models.IntegerField()
    tabTTsec32 = models.IntegerField()
    tabTTsec4 = models.IntegerField()

    browser = models.StringField()

    lottery_choice = models.PositiveIntegerField() #to determine drafted scenario
    lottery_draft = models.PositiveIntegerField() #to determine drafted scenario
    lottery_outcome = models.PositiveIntegerField() #to determine outcome in case of lottery participation

    timespent = models.StringField()
    time_start = models.StringField() #get time of participant when welcome page is loaded
    time_end = models.StringField() #get time of participant when last page is loaded

    def get_time(self, start_or_end):
        if start_or_end == "start":
            self.time_start = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        else:
            self.time_end = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


    def time_spent(self):
        duration = datetime.datetime.strptime(self.time_end, "%d/%m/%Y %H:%M:%S") - datetime.datetime.strptime(self.time_start, "%d/%m/%Y %H:%M:%S")
        self.timespent = f"{duration.total_seconds():.0f}sec; {float(duration.total_seconds() / 60):.2f}min"
