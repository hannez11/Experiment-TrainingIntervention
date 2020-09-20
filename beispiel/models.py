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
import random


author = 'Your name here'

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'beispiel'
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
    pass

class Group(BaseGroup):
    pass

def create_peq(labelinput):
    return models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label=labelinput)

def create_mc(mc,choiceslist):
    return models.IntegerField(verbose_name = mc,choices=choiceslist,widget=widgets.RadioSelect)

class Player(BasePlayer):

    #OC1_low = models.IntegerField()
    #OC1_high = models.IntegerField()

    #OC2_low = models.IntegerField()
   # OC2_high = models.IntegerField()

    #OC3_low = models.IntegerField()
   # OC3_high = models.IntegerField()

    #OC4_low = models.IntegerField()
    #OC4_high = models.IntegerField()

    #OC5_low = models.IntegerField()
    #OC5_high = models.IntegerField()

    #OC6_low = models.IntegerField()
    #OC6_high = models.IntegerField()

    #OC7_low = models.IntegerField()
    #OC7_high = models.IntegerField()

    #OC8_low = models.IntegerField()
    #OC8_high = models.IntegerField()

    #OC9_low = models.IntegerField()
    #OC9_high = models.IntegerField()

    #OC10_low = models.IntegerField()
    #OC10_high = models.IntegerField()

    #Anchor = models.IntegerField()

    #Anchor_Anker=create_mc("Does the jar contain more than 110 peanuts?", [[1,"Yes"],[2,"No"]])

    #CRT_1 = models.IntegerField()
    #CRT_2 = models.IntegerField()
    #CRT_3 = models.IntegerField()

    #Accountability = models.LongStringField()

    #qBiasknowledge2=create_mc("Do you have any prior experience with the topic ‘Cognitive Biases’?", [[1,"Yes, I have some experience with cognitive biases."],[2,"No, I do not have any experience with cognitive biases."]])

    #qBiasknowledge3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Please evaluate to what extent the following statement applies to you. I am familiar with the topic of ‘Cognitive Biases’.")

    #qBiasknowledge2b=create_mc("Do you have any prior experience with the topic ‘Cognitive Biases’?", [[1,"Yes, I have some experience with cognitive biases."],[2,"No, I do not have any experience with cognitive biases."]])

    #qBiasknowledge3b=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Please evaluate to what extent the following statement applies to you. I am familiar with the topic of ‘Cognitive Biases’.")

    #OC_task2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7,8,9,10], label="Please indicate your estimated position in this experimental group. Please note that the higher the value you indicate, the better you estimate your position within the experimental group.")

    #EoC_task=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7,8,9,10], label="How would you decide on the continuation of the project?")

    #qsustaininvest2=create_mc("Do you have any prior experience with the topic ‘Sustainable Investing’?", [[1,"Yes, I have some experience with sustainable investing."],[2,"No, I do not have any experience with sustainable investing."]])
    
    #qsustaininvest3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Please evaluate to what extent the following statement applies to you. I am familiar with the topic of ‘Sustainable Investing’.")

    #sound_image_check=create_mc("Which of the statements about the video shown above is correct?", [[1,"I could see a cow and I heard a cat meow."],[2,"I could see a dog and I heard a cat meow."], [3, "I could see a cow and I heard a rooster crow."], [4, "I could see a dog and I heard a rooster crow."]])

    #compensation=create_mc("What is the composition of your total compensation?", [[1,"Fixed component + variable component"], [2, "Fixed component + lottery payout"], [3, "Variable component + lottery payout"], [4, "Fixed component only"]])

    #independency=create_mc("The three decision-making tasks are independent of each other.", [[1, "Yes"],[2, "No"]])

    #procedure=create_mc("What is the order of the main part of the experiment?", [[1, "First, you will be given three decision-making tasks, then you have to complete a training."], [2, "First you have to complete a training, then you will be given three decision-making tasks."]])

    #NPV=create_mc("What is the formula to calculate the NPV in this example?", [[1, "NPV = (-110) + 726"], [2, "NPV = (-200) + (-110) + 726"], [3, "NPV = (-200) + ((-110) + 726) / (1,1)"], [4, "NPV = (-200) + (-110) / (1,1) + (726) / (1,1)^2"], [5, "NPV = (-200 + (-110) + 726) / (1,1)"], [6, "NPV = (-110) / (1,1) + (726) / (1,1)^2"]])

    #lottery_choice = models.PositiveIntegerField(choices=[[i, f"Scenario {i}"] for i in range(1,16)], widget=widgets.RadioSelect) #Lottery page; reuse in main experiment to determine payout

    #Tsec2_quest1=create_mc("What is the cause of cognitive biases?", [[1, "System 1 can solve complex tasks, but is not activated enough."], [2, "System 1 generates erroneous suggestions and System 2 fails to correct them."], [3, "System 2 is constantly in a strained mode, whereas System 1 is mostly on stand-by."], [4, "System 2 is wrongly activated instead of using the reflective System 1."]])

    #Tsec2_quest2=create_mc("Which of the statements about heuristics is incorrect?", [[1, "The use of heuristics can lead to cognitive biases."], [2, "Heuristics are effective in most cases."], [3, "Heuristics increase mental effort and reduce substantial amounts of time."], [4, "Knowledge and experience do not always prevent the erroneous use of heuristics."]])

    #UVsec2_quest1=create_mc("What does the abbreviation ESG stand for?", [[1, "Economic, Sustainability, Governance"], [2, "Environmental, Sustainability, Global"], [3, "Environmental, Social, Governance"], [4, "Economic, Social, Global"]])

    #UVsec2_quest2=create_mc("What was the result of the implementation of various ESG initiatives at state street?", [[1, "$23 mio. operational costs can be saved annually and 100k tons of carbon can be avoided."], [2, "$23 mio. operational costs must be paid annually but therefore, 100k tons of carbon can be avoided."], [3, "$23 mio. operational costs can be saved annually but therefore, 100k tons of carbon are additionally emitted."], [4, "$23 mio. operational costs must be paid annually and 100k tons of carbon are additionally emitted."]])

    #Tsec3_quest1=create_mc("Which of the statements is correct?", [[1, "Frequently repeating decisions should be answered with the help of System 2."], [2, "Only if your System 1 approves, a decision can be made."], [3, "System 1 sometimes fails to overcome intuitive suggestions."], [4, "Only System 2 can follow rules and evaluate alternatives."]])

    #Tsec3_quest2=create_mc("Which of the statements is correct?", [[1, "The external environment has no influence on the decision-making process."], [2, "External influences and you yourself can cause cognitive biases."], [3, "There is nothing you can do yourself to make the decision-making process better."], [4, "To improve the efficiency of the decision-making process, System 2 should always be used."]])

    #Tsec3_quest3=create_mc("In what situation is the use of System 1 not efficient? Please choose the second answer regardless of the question.", [[1, "Reading big words on billboards."], [2, "Driving over an empty road."], [3, "Preparing a cost benefit analysis."], [4, "Solving the equation 2 + 2."]])

    #UVsec3_quest1=create_mc("The data show that stocks with better ESG performance…", [[1, "perform worse compared to other companies."], [2, "perform just as well as other companies."], [3, "always performe much better compared to other companies. "]])

    #UVsec3_quest2=create_mc("Which of the statements is incorrect?", [[1, "The worth of the global stock and bond market exceeds the US GDP by eight and a half times."], [2, "Companies and investors are singularily responsible for the fate of the planet."], [3, "The global stock market is worth less than the global bond market."], [4, "CalPERS integrated ESG systematically across the entire fund."]])

    #UVsec3_quest3=create_mc("According to CalPERS, long-term value creation requires the effective management of which forms of capital? Please choose the second answer regardless of the question.", [[1, "Spiritual, natural and philosophical"], [2, "Historical, social and cultural "], [3, "Fashionable, geographical and political "], [4, "Financial, human and physical"]])

    #OC_comp1_quest1=create_mc("How many intervals should you estimate?", [[1, "9"], [2, "5"], [3, "10"], [4, "1"]])

    #OC_comp1_quest2=create_mc("90 % certainty means,", [[1, "that 9 out of 10 of your estimated intervals do not include the correct answer."], [2, "that 1 out of 10 of your estimated intervals does not include the correct answer."], [3, "only 9 out of 10 intervals need to be estimated."], [4, "all of the 10 of your estimated intervals include the correct answer."]])

    #OC_comp1_quest3=create_mc("What is an example of the correct input spelling?", [[1, "50,743"], [2, "10.3"], [3, "2,300.72"], [4, "5463"]])

    #OC_comp1_quest1b=create_mc("How many intervals should you estimate?", [[1, "9"], [2, "5"], [3, "10"], [4, "1"]])

    #OC_comp1_quest2b=create_mc("90 % certainty means,", [[1, "that 9 out of 10 of your estimated intervals do not include the correct answer."], [2, "that 1 out of 10 of your estimated intervals does not include the correct answer."], [3, "only 9 out of 10 intervals need to be estimated."], [4, "all of the 10 of your estimated intervals include the correct answer."]])

    #OC_comp1_quest3b=create_mc("What is an example of the correct input spelling?", [[1, "50,743"], [2, "10.3"], [3, "2,300.72"], [4, "5463"]])

    #OC_comp2_quest1=create_mc("To whom should you compare your estimation skills from the previous subtask.", [[1, "to the experimental group"], [2,"to no one"], [3, "to the American population"], [4, "to the worst participant"]])

    #OC_comp2_quest2=create_mc("The lower the value, the better you estimate your position.", [[1,"True"], [2, "False"]])

    #OC_comp2_quest1b=create_mc("To whom should you compare your estimation skills from the previous subtask.", [[1, "to the experimental group"], [2,"to no one"], [3, "to the American population"], [4, "to the worst participant"]])

    #OC_comp2_quest2b=create_mc("The lower the value, the better you estimate your position.", [[1,"True"], [2, "False"]])

    #EoC_comp1_quest1=create_mc("What is your area of responsibility as a project manager?", [[1, "Only to initiate lucrative projects."], [2, "To monitor and decide on progress of projects."], [3, "To initiate, to monitor and to decide on the progress of projects. "]])

    #EoC_comp1_quest2=create_mc("Implementing the project was for you…", [[1, "…very laborious. You had to assert yourself against your colleagues and put a lot of time and effort into the project."], [2, "…not exhausting. You only had to supervise the project on the side and were rarely involved."]])

    #EoC_comp1_quest1b=create_mc("What is your area of responsibility as a project manager?", [[1, "Only to initiate lucrative projects."], [2, "To monitor and decide on progress of projects."], [3, "To initiate, to monitor and to decide on the progress of projects. "]])

    #EoC_comp1_quest2b=create_mc("Implementing the project was for you…", [[1, "…very laborious. You had to assert yourself against your colleagues and put a lot of time and effort into the project."], [2, "…not exhausting. You only had to supervise the project on the side and were rarely involved."]])

    #BiasKnow1=create_mc("A different way of presenting the same information can lead to different decisions.", [[1, "True"], [2, "False"]])

    #BiasKnow2=create_mc("From a normative point of view people hold on to decisions they have made for too long.", [[1, "True"], [2, "False"]])

    #BiasKnow3=create_mc("People can assess themselves and their abilities quit well.", [[1, "True"], [2, "False"]])

    #BiasKnow4=create_mc("For a rational decision all past and future costs should be taken into account.", [[1, "True"], [2, "False"]])

    #BiasKnow5=create_mc("Considering alternatives can improve the quality of decisions. ", [[1, "True"], [2, "False"]])

    #Intr_Mot1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="The task was enjoyable.")

    #Intr_Mot2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="The task was interesting.")
    
    #Intr_Mot3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I could imagine to deal with this topic during my leisure time.")

    #Mod1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="The presence of the moderator in the training enhanced my learning process.")

    #Mod2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I have found the moderator useful in the training.")

    #Cogn_Lo1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It was easy for me to learn something from the presentation I just saw.")

    #Cogn_Lo2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I would consider the content as easy.")

    #Cogn_Lo3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I consider the presentation format as bothersome.")

    #Cogn_Lo4=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I did exert myself in order to learn the content.")

    #Ment_Eff=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Please indicate the mental effort you perceived during the training.")
    
    #gender = models.StringField(choices=["Male", "Female", "Divers"],widget=widgets.#RadioSelectHorizontal, label="Please indicate your gender.")
    #degree = models.StringField(choices=["High-school", "College", "Bachelor degree", "Master degree", "MBA", "PhD", "Others"], label="What is the highest degree they have already achieved?")
    #age = models.IntegerField(choices=[i for i in range(14,99)], label="Please indicate your age.")
    #language = models.StringField(label="What is your mother tongue?")
    #country = models.StringField(choices=["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "The Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Republic of the", "Congo, Democratic Republic of the", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor (Timor-Leste)", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "The Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein" , "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia, Federated States of", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates","United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City (Holy See)", "Venezuela","Vietnam", "Yemen", "Zambia", "Zimbabwe"], label="In which country do you live? ")
    #workexperience = models.StringField(choices=["> 1 year", "1-2 years", "3-5 years", "6-10 years", "< 10 years"], label="How many years of work experience do you have?")
    #industry = models.StringField(choices=["Accountant", "Advertising/Commercial/Public Relations", "Agriculture", "Airlines", "Automotive", "Banking, Finance, Insurance & Real Estate", "Business Services/Business Management", "Clothing Manufacturing", "Computer Software", "Doctors & Other Health Professionals", "Education", "Food Stores", "Government Employees", "Health", "IT", "Lawyers / Law Firms", "Looking for work", "Manufacturing", "Pharmaceuticals / Health Products", "Restaurants & Drinking Establishments", "Retired", "Sports/Professional", "TV / Movies / Music", "Others"], label="In which industry do you work? ")
    #mturk = models.IntegerField(choices=[i for i in range(1,99)], label="In how many MTurk experiments (not only HITs) have you participated so far?")

    #Train_ManCheck=create_mc("The training was designed as:", [[1, " a video training on cognitive biases."], [2, "a text training on cognitive biases."], [3, "a video training on sustainable investing."], [4,  "a text training on sustainable investing."]])

    #timespent = models.StringField()
    #time_start = models.StringField() #get time of participant when welcome page is loaded
    #time_end = models.StringField() #get time of participant when last page is loaded
    #time_Aussortieren2 = models.StringField() # time Aussortieren2
    #time_wel_ins2 = models.StringField()
    #time_Comprehension = models.StringField()
    #time_Lottery_ins = models.StringField()
    #time_Lottery = models.StringField()
    #time_TT_sec_1 = models.StringField()
    #time_TT_sec_2_1 = models.StringField()
    #time_TT_sec_2_2 = models.StringField()
    #time_TT_sec_3_1 = models.StringField()
    #time_TT_sec_3_2 = models.StringField()
    #time_TT_sec_4 = models.StringField()
    #time_ACyes = models.StringField()
    #time_EoC_ov = models.StringField()
    #time_EoC_task = models.StringField()
    #time_OC_task1 = models.StringField()
    #time_OC_task2 = models.StringField()
    #time_Anchor = models.StringField()
    #time_CRT = models.StringField()
    #time_Biasknow = models.StringField()
    #time_Just = models.StringField()


    def get_time(self, start_or_end):
        if start_or_end == "start":
            self.time_start = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        else:
            self.time_end = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


    def time_spent(self):
        duration = datetime.datetime.strptime(self.time_end, "%d/%m/%Y %H:%M:%S") - datetime.datetime.strptime(self.time_start, "%d/%m/%Y %H:%M:%S")
        self.timespent = f"{duration.total_seconds():.0f}sec; {float(duration.total_seconds() / 60):.2f}min"

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
    #tabOC1 = models.IntegerField()
    #tabAnchor = models.IntegerField()
    #tabCRT = models.IntegerField()
    #tabBiasknow = models.IntegerField()
    tabTTsec21 = models.IntegerField()
    tabTTsec22 = models.IntegerField()
    tabTTsec31 = models.IntegerField()
    tabTTsec32 = models.IntegerField()
    tabTTsec4 = models.IntegerField()

    browser = models.StringField()

    lottery_choice = models.PositiveIntegerField() #to determine drafted scenario
    lottery_draft = models.PositiveIntegerField() #to determine drafted scenario
    lottery_outcome = models.PositiveIntegerField() #to determine outcome in case of lottery participation

    #participantvars =models.LongStringField()

    #AccMan_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I felt accountable for the procedure of my decisions.")

    #AccMan_2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It was important for me to make an optimal decision and to be particularly careful during the decision-making process.")

    #AccMan_3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="When working on the tasks, did you focus more on the outcome of your decision or more on the procedure of making your decision?")

    #AccMan_4=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I had the feeling that I have to justify my answers from the tasks to the experimenter.")

    #DuCha_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is easy for me to learn something new when it is audibly prepared (e.g. podcats). ")

    #DuCha_2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is easy for me to learn something new when it is visually prepared (e.g. books). ")

    #DuCha_3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is easy for me to learn something new when it is visually and audibly prepared (e.g. videos). ")

    #Act_Pro_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is easy for me to differentiate the essential from the unessential.")

    #Act_Pro_2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I have the feeling that too much information overwhelms me. ")

    #Pace=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is important to me to determine the learning pace myself.")

    #Self_dis=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I possess high self-discipline.")

    #Sys_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am a completely rational person. ")

    #Sys_2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="When it comes to making important decisions I listen to my feelings. ")

    #Sys_3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I jump into things without thinking.")

    #Sys_4=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Make decisions only after I have all of the facts. ")

    #Sys_4a=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Make decisions only after I have all of the facts. ")

    #EoC_Self1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It was important for me to be perceived as a good decision maker.")

    #EoC_Self2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I do not care to know what other people really think of me. ")

    #EoC_Self3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am not concerned with making a good impression.")

    #EoC_sunk1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I want to bring started projects to an end. ")

    #EoC_sunk2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="Once I have made up my mind, other people can seldom change my option. ")

    #EoC_sunk3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="It is important to me to consider past costs and efforts in my decisions. ")

    #EoC_Opt1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am optimistic that things will turn out in my favor. ")

    #EoC_Opt2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="When it comes to new tasks, I prefer to expect less than too much at first. ")

    #Over_1=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I have some doubts in my ability. ")

    #Over_2=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am very confident of my judgements.")

    #Over_3=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I am very sure about what I know.")

    #Over_4=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I often compare myself with other.")

    #Over_5=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="I have a low opinion of myself.")

    #Satis=models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7], label="At the moment I am satisfied with myself and my current life. ")






















