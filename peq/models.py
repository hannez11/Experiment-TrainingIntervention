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
    CRT_2 = models.IntegerField()
 
    qBiasknowledge2b=create_mc("Do you have any prior experience with the topic ‘Cognitive Biases’?", [[1,"Yes, I have some experience with cognitive biases."],[2,"No, I do not have any experience with cognitive biases."]])

    qBiasknowledge3b=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Please evaluate to what extent the following statement applies to you. I am familiar with the topic of ‘Cognitive Biases’.")

    gender = models.StringField(choices=["Male", "Female", "Divers"],widget=widgets.RadioSelectHorizontal, label="Please indicate your gender.")
    degree = models.StringField(choices=["High-school", "College", "Bachelor degree", "Master degree", "MBA", "PhD", "Others"], label="What is the highest degree you have already achieved?")
    age = models.IntegerField(choices=[i for i in range(14,99)], label="Please indicate your age.")
    language = models.StringField(label="What is your native language?")
    country = models.StringField(choices=["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "The Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Republic of the", "Congo, Democratic Republic of the", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor (Timor-Leste)", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "The Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein" , "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia, Federated States of", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates","United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City (Holy See)", "Venezuela","Vietnam", "Yemen", "Zambia", "Zimbabwe"], label="In which country do you live? ")
    workexperience = models.StringField(choices=["< 1 year", "1-2 years", "3-5 years", "6-10 years", "> 10 years"], label="How many years of work experience do you have?")
    industry = models.StringField(choices=["Accountant", "Advertising/Commercial/Public Relations", "Agriculture", "Airlines", "Automotive", "Banking, Finance, Insurance & Real Estate", "Business Services/Business Management", "Clothing Manufacturing", "Computer Software", "Doctors & Other Health Professionals", "Education", "Food Stores", "Government Employees", "Health", "IT", "Lawyers / Law Firms", "Manufacturing", "Pharmaceuticals / Health Products", "Restaurants & Drinking Establishments", "Retired", "Sports/Professional", "Student", "TV / Movies / Music", "Unemployed", "Others"], label="In which industry do you work? ")
    mturk = models.StringField(choices=["0", "1-3", "4-10", "> 10"], label="In how many experimental studies have you participated so far?")

    Train_ManCheck=create_mc("The training was designed as:", [[1, " a video training on cognitive biases."], [2, "a text training on cognitive biases."], [3, "a video training on sustainable investing."], [4,  "a text training on sustainable investing."]])

    time_CRT = models.StringField()
    time_Biasknow = models.StringField()

    tabCRT = models.IntegerField()
    tabBiasknow = models.IntegerField()

    # lottery_choice = models.PositiveIntegerField() #pass self.participant.vars["global_lottery_choice"] into here in one of the peq pages vars_for_template / before_next_page
    lottery_draft = models.PositiveIntegerField() #to determine drafted scenario
    lottery_outcome = models.PositiveIntegerField() #to determine outcome in case of lottery participation

    AccMan_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="During this experimental study I felt accountable for the procedure of my decisions.")

    AccMan_3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="When working on the experimental tasks, did you focus more on the outcome of your decision or more on the procedure of making your decision?")

    AccMan_4=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I had the feeling that I have to justify the decisions I made in the tasks to the experiment administrator.")

    Act_Pro_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is easy for me to differentiate the essential from the unessential.")

    Act_Pro_2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I have the feeling that too much information overwhelms me. ")

    Doubt=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I had doubts about the credibility of the experiment instructions.")

    Sys_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am a completely rational person. ")

    Sys_2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="When it comes to making important decisions I listen to my feelings. ")

    Sys_3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I jump into things without thinking.")

    ATTChe=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="While watching the television, have you ever had a fatal heart attack?")

    EoC_Self1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It was important for me to be perceived as a good decision maker.")

    EoC_Self2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I do not care to know what other people really think of me. ")

    EoC_Self3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am not concerned with making a good impression.")

    EoC_sunk1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I want to bring started projects to an end. ")

    EoC_sunk2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Once I have made up my mind, other people can seldom change my opinion. ")

    EoC_sunk3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is important to me to consider past costs and efforts in my decisions. ")

    EoC_Opt1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am optimistic that things will turn out in my favor. ")

    EoC_Opt2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="When it comes to new tasks, I prefer to expect less than too much at first. ")

    Over_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I have some doubts in my ability.")

    Over_2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am very confident of my judgements.")

    Over_3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am very sure about what I know.")

    AtEx=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I was attentive during the experiment.")

    BiasKnow1=create_mc("Which of the statements is correct?", [[1, "Frequently repeating decisions should be answered with the help of System 2."], [2, "Only if your System 1 approves, a decision can be made."], [3, "System 1 sometimes fails to overcome intuitive suggestions."], [4, "Only System 2 can follow rules and evaluate alternatives."]])

    BiasKnow2=create_mc("In what situation is the use of System 1 not efficient?", [[1, "Reading big words on billboards."], [2, "Driving over an empty road."], [3, "Preparing a cost benefit analysis."], [4, "Solving the equation 2 + 2."]])

    BiasKnow3=create_mc("Which of the statements is incorrect?", [[1, "The formulation of a decision problem has no influence on the decision."], [2, "People prefer positively presented alternatives to negatively presented alternatives with the same result."], [3, "Decisions are made based on the way the information is presented."], [4, "The opposite formulation of an information sometimes seems to change the meaning of the statement."]])

    OC_Mturk=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7,8,9,10], label="Indicate your estimated position in this experimental group depending on the quality of your mturk work. Please note that the higher the value you indicate, the better you estimate your position within the experimental group.")


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
