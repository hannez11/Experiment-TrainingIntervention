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
    name_in_url = 'peq'
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

class Player(BasePlayer):
    CRT_1 = models.IntegerField()
    CRT_2 = models.IntegerField()
    CRT_3 = models.IntegerField()

    BiasKnow1=create_mc("A different way of presenting the same information can lead to different decisions.", [[1, "True"], [2, "False"]])

    BiasKnow2=create_mc("From a normative point of view, most people stick to their decisions for too long, even though the decisions do not promise the greatest benefits.", [[1, "True"], [2, "False"]])

    BiasKnow3=create_mc("Most people can assess themselves and their abilities quit well.", [[1, "True"], [2, "False"]])

    BiasKnow4=create_mc("For a rational decision all past and future costs should be taken into account.", [[1, "True"], [2, "False"]])

    BiasKnow5=create_mc("Considering alternatives can improve the quality of decisions. ", [[1, "True"], [2, "False"]])

    qBiasknowledge2b=create_mc("Do you have any prior experience with the topic ‘Cognitive Biases’?", [[1,"Yes, I have some experience with cognitive biases."],[2,"No, I do not have any experience with cognitive biases."]])

    qBiasknowledge3b=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Please evaluate to what extent the following statement applies to you. I am familiar with the topic of ‘Cognitive Biases’.")

    gender = models.StringField(choices=["Male", "Female", "Divers"],widget=widgets.RadioSelectHorizontal, label="Please indicate your gender.")
    degree = models.StringField(choices=["High-school", "College", "Bachelor degree", "Master degree", "MBA", "PhD", "Others"], label="What is the highest degree they have already achieved?")
    age = models.IntegerField(choices=[i for i in range(14,99)], label="Please indicate your age.")
    language = models.StringField(label="What is your mother tongue?")
    country = models.StringField(choices=["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "The Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Republic of the", "Congo, Democratic Republic of the", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor (Timor-Leste)", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "The Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein" , "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia, Federated States of", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates","United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City (Holy See)", "Venezuela","Vietnam", "Yemen", "Zambia", "Zimbabwe"], label="In which country do you live? ")
    workexperience = models.StringField(choices=["> 1 year", "1-2 years", "3-5 years", "6-10 years", "< 10 years"], label="How many years of work experience do you have?")
    industry = models.StringField(choices=["Accountant", "Advertising/Commercial/Public Relations", "Agriculture", "Airlines", "Automotive", "Banking, Finance, Insurance & Real Estate", "Business Services/Business Management", "Clothing Manufacturing", "Computer Software", "Doctors & Other Health Professionals", "Education", "Food Stores", "Government Employees", "Health", "IT", "Lawyers / Law Firms", "Looking for work", "Manufacturing", "Pharmaceuticals / Health Products", "Restaurants & Drinking Establishments", "Retired", "Sports/Professional", "TV / Movies / Music", "Others"], label="In which industry do you work? ")
    mturk = models.IntegerField(choices=[i for i in range(1,99)], label="In how many experimental studies have you participated so far?")

    Train_ManCheck=create_mc("The training was designed as:", [[1, " a video training on cognitive biases."], [2, "a text training on cognitive biases."], [3, "a video training on sustainable investing."], [4,  "a text training on sustainable investing."]])

    time_CRT = models.StringField()
    time_Biasknow = models.StringField()

    tabCRT = models.IntegerField()
    tabBiasknow = models.IntegerField()

    # lottery_choice = models.PositiveIntegerField() #pass self.participant.vars["global_lottery_choice"] into here in one of the peq pages vars_for_template / before_next_page
    lottery_draft = models.PositiveIntegerField() #to determine drafted scenario
    lottery_outcome = models.PositiveIntegerField() #to determine outcome in case of lottery participation

    AccMan_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="During this experimental study I felt accountable for the procedure of my decisions.")

    AccMan_2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="During the experiment it was important for me to make an optimal decision and to be particularly careful in the  decision-making process.")

    AccMan_3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="When working on the experimental tasks, did you focus more on the outcome of your decision or more on the procedure of making your decision?")

    AccMan_4=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I had the feeling that I have to justify the decisions I made in the tasks to the experimenter.")

    DuCha_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is easy for me to learn something new when it is audibly prepared (e.g. podcats). ")

    DuCha_2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is easy for me to learn something new when it is visually prepared (e.g. books). ")

    DuCha_3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is easy for me to learn something new when it is visually and audibly prepared (e.g. videos). ")

    Act_Pro_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is easy for me to differentiate the essential from the unessential.")

    Act_Pro_2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I have the feeling that too much information overwhelms me. ")

    Pace=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is important to me to determine the learning pace myself.")

    Self_dis=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I possess high self-discipline.")

    Sys_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am a completely rational person. ")

    Sys_2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="When it comes to making important decisions I listen to my feelings. ")

    Sys_3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I jump into things without thinking.")

    Sys_4=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I make decisions only after I have all of the facts. ")

    Sys_4a=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I make decisions only after I have all of the facts. ")

    EoC_Self1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It was important for me to be perceived as a good decision maker.")

    EoC_Self2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I do not care to know what other people really think of me. ")

    EoC_Self3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am not concerned with making a good impression.")

    EoC_sunk1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I want to bring started projects to an end. ")

    EoC_sunk2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Once I have made up my mind, other people can seldom change my option. ")

    EoC_sunk3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is important to me to consider past costs and efforts in my decisions. ")

    EoC_Opt1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am optimistic that things will turn out in my favor. ")

    EoC_Opt2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="When it comes to new tasks, I prefer to expect less than too much at first. ")

    Over_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I have some doubts in my ability. ")

    Over_2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am very confident of my judgements.")

    Over_3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am very sure about what I know.")

    Over_4=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I often compare myself with others.")

    Over_5=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I have a low opinion of myself.")

    Satis=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="At the moment I am satisfied with myself and my current life. ")

    lottery_choice = models.PositiveIntegerField(choices=[[i, f"Scenario {i}"] for i in range(1,16)], widget=widgets.RadioSelect) #Lottery page; reuse in main experiment to determine payout

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
