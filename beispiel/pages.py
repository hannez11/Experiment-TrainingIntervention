from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class wel_ins1(Page):
    form_model = "player"
    form_fields = ["timezone"]

    def before_next_page(self):
        self.player.get_time("start")
        self.player.browser = self.request.META['HTTP_USER_AGENT']

class Aussortieren_1(Page):
    form_model = "player"
    form_fields = ["sound_image_check"]

class fail(Page):
    def is_displayed(self):
        return self.player.sound_image_check!=3 

class Aussortieren_2(Page):
    form_model = "player"
    form_fields = ["NPV", "tabNPV", "time_Aussortieren2"]

class fail2(Page):
    def is_displayed(self):
        return self.player.NPV!=4 

class wel_ins2(Page):
    form_model = "player"
    form_fields = ["time_wel_ins2"]
    
class Comprehension(Page):
    form_model = "player"
    form_fields = ["compensation","independency","procedure", "time_Comprehension"]

    def compensation_error_message(self,value):
         if value!=2:
             return "Your answer is not correct. Please read the experiment instructions again."
    def independency_error_message(self,value):
         if value!=1:
             return "Your answer is not correct. Please read the experiment instructions again."
    def procedure_error_message(self,value):
         if value!=2:
             return "Your answer is not correct. Please read the experiment instructions again."

class Lottery_ins(Page):
    form_model = "player"
    form_fields = ["time_Lottery_ins"]

class Lottery(Page):
    form_model = "player"
    form_fields = ["lottery_choice", "time_Lottery"]

    def vars_for_template(self): #to create risk lottery bootstrap table
        list1 = Constants.lottery_gamble_successrate
        list2 = Constants.lottery_gamble_failurerate
        list3 = [f"id_lottery_choice_{i}" for i in range(1,16)]
        data = list(zip(list1,list2,list3))
        return {"data": data} # {% for a,b,c in data %} -> {{ a }} .. .. -> displays 85% .. 15% ..  form.lottery_choice.0

    # def before_next_page(self):
    #     self.participant.vars["lottery_choice"] = self.player.lottery_choice #if payout is needed in another app
    #     print("global_lottery_choice" + str(self.participant.vars["global_lottery_choice"]))

class train_ov(Page):
    form_model = "player"

class VT_sec_1(Page):
    form_model = "player"
    form_fields = ["tabVT1"]

class TT_sec_1(Page):
    form_model = "player"
    form_fields = ["time_TT_sec_1"]

class UV_sec_1(Page):
    form_model = "player"
    form_fields = ["tabUV1"]

class T_sec_1_ques1(Page):
    form_model = "player"
    form_fields = ["qBiasknowledge2", "qBiasknowledge3"]

class T_sec_1_ques1_fn(Page):
    def is_displayed(self):
        return self.player.qBiasknowledge2!=1 

class T_sec_1_ques1_fp(Page):
    def is_displayed(self):
        return self.player.qBiasknowledge2!=2

class UV_sec_1_ques1(Page):
    form_model = "player"
    form_fields = ["qsustaininvest2", "qsustaininvest3"]

class UV_sec_1_ques1_fn(Page):
    def is_displayed(self):
        return self.player.qsustaininvest2!=1 

class UV_sec_1_ques1_fp(Page):
    def is_displayed(self):
        return self.player.qsustaininvest2!=2

class VT_sec_2(Page):
    form_model = "player"
    form_fields = ["tabVT2"]

class TT_sec_2_1(Page):
    form_model = "player"
    form_fields = ["time_TT_sec_2_1", "tabTTsec21"]

class TT_sec_2_2(Page):
    form_model = "player"
    form_fields = ["time_TT_sec_2_2", "tabTTsec22"]

class UV_sec_2(Page):
    form_model = "player"
    form_fields = ["tabUV2"]

class T_sec_2_ques1(Page):
    form_model = "player"
    form_fields = ["Tsec2_quest1"]

class T_sec_2_ques1_fp(Page):
    def is_displayed(self):
        return self.player.Tsec2_quest1==2

class T_sec_2_ques1_fn(Page):
    def is_displayed(self):
        return self.player.Tsec2_quest1!=2

class T_sec_2_ques2(Page):
    form_model = "player"
    form_fields = ["Tsec2_quest2"]

class T_sec_2_ques2_fp(Page):
    def is_displayed(self):
        return self.player.Tsec2_quest2==3

class T_sec_2_ques2_fn(Page):
    def is_displayed(self):
        return self.player.Tsec2_quest2!=3

class UV_sec_2_ques1(Page):
    form_model = "player"
    form_fields = ["UVsec2_quest1"]

class UV_sec_2_ques1_fn(Page):
    def is_displayed(self):
        return self.player.UVsec2_quest1!=3

class UV_sec_2_ques1_fp(Page):
    def is_displayed(self):
        return self.player.UVsec2_quest1==3

class UV_sec_2_ques2(Page):
    form_model = "player"
    form_fields = ["UVsec2_quest2"]

class UV_sec_2_ques2_fn(Page):
    def is_displayed(self):
        return self.player.UVsec2_quest2!=1

class UV_sec_2_ques2_fp(Page):
    def is_displayed(self):
        return self.player.UVsec2_quest2==1

class VT_sec_3(Page):
    form_model = "player"
    form_fields = ["tabVT3"]

class TT_sec_3_1(Page):
    form_model = "player"
    form_fields = ["time_TT_sec_3_1", "tabTTsec31"]

class TT_sec_3_2(Page):
    form_model = "player"
    form_fields = ["time_TT_sec_3_2", "tabTTsec32"]

class UV_sec_3(Page):
    # def is_displayed(self):
    #     return self.player.treatment == 3 or 6
    form_model = "player"
    form_fields = ["tabUV3"]

class T_sec_3_ques1(Page):
    form_model = "player"
    form_fields = ["Tsec3_quest1"]

class T_sec_3_ques1_fn(Page):
    def is_displayed(self):
        return self.player.Tsec3_quest1!=4

class T_sec_3_ques1_fp(Page):
    def is_displayed(self):
        return self.player.Tsec3_quest1==4

class T_sec_3_ques2(Page):
    form_model = "player"
    form_fields = ["Tsec3_quest2"]

class T_sec_3_ques2_fn(Page):
    def is_displayed(self):
        return self.player.Tsec3_quest2!=2

class T_sec_3_ques2_fp(Page):
    def is_displayed(self):
        return self.player.Tsec3_quest2==2

class T_sec_3_ques3(Page):
    form_model = "player"
    form_fields = ["Tsec3_quest3"]

class T_sec_3_ques3_fn(Page):
    def is_displayed(self):
        return self.player.Tsec3_quest3!=2

class T_sec_3_ques3_fp(Page):
    def is_displayed(self):
        return self.player.Tsec3_quest3==2

class UV_sec_3_ques1(Page):
    form_model = "player"
    form_fields = ["UVsec3_quest1"]

class UV_sec_3_ques1_fn(Page):
    def is_displayed(self):
        return self.player.UVsec3_quest1!=2

class UV_sec_3_ques1_fp(Page):
    def is_displayed(self):
        return self.player.UVsec3_quest1==2

class UV_sec_3_ques2(Page):
    form_model = "player"
    form_fields = ["UVsec3_quest2"]

class UV_sec_3_ques2_fn(Page):
    def is_displayed(self):
        return self.player.UVsec3_quest2!=2

class UV_sec_3_ques2_fp(Page):
    def is_displayed(self):
        return self.player.UVsec3_quest2==2

class UV_sec_3_ques3(Page):
    form_model = "player"
    form_fields = ["UVsec3_quest3"]

class UV_sec_3_ques3_fn(Page):
    def is_displayed(self):
        return self.player.UVsec3_quest3!=2

class UV_sec_3_ques3_fp(Page):
    def is_displayed(self):
        return self.player.UVsec3_quest3==2

class VT_sec_4(Page):
    form_model = "player"
    form_fields = ["tabVT4"]

class TT_sec_4(Page):
    form_model = "player"
    form_fields = ["time_TT_sec_4", "tabTTsec4"]

class UV_sec_4(Page):
    form_model = "player"
    form_fields = ["tabUV4"]

class PEQ_train(Page):
    form_model = "player"
    form_fields = ["Intr_Mot1", "Intr_Mot2", "Intr_Mot3", "Mod1", "Mod2", "Cogn_Lo1", "Cogn_Lo2", "Cogn_Lo3", "Cogn_Lo4", "Ment_Eff", "Train_ManCheck"]

class AC_no(Page):
    form_model = "player"

class AC_yes(Page):
    form_model = "player"
    form_fields = ["time_ACyes"]


class EoC_ov(Page):
    form_model = "player"
    form_fields = ["EoC_comp1_quest1", "EoC_comp1_quest2", "time_EoC_ov"]

class EoC_instructions(Page):
    form_model = "player"
    def is_displayed(self):
        return self.player.EoC_comp1_quest1!=3 or self.player.EoC_comp1_quest2!=1

class EoC_comp1(Page):
    form_model = "player"
    form_fields = ["EoC_comp1_quest1b", "EoC_comp1_quest2b"]
    def is_displayed(self):
        return self.player.EoC_comp1_quest1!=3 or self.player.EoC_comp1_quest2!=1

    def EoC_comp1_quest1b_error_message(self,value):
         if value!=3:
             return "Your answer is not correct."
    def EoC_comp1_quest2b_error_message(self,value):
         if value!=1:
             return "Your answer is not correct."

class EoC_task(Page):
    form_model = "player"
    form_fields = ["EoC_task", "time_EoC_task"]
    def is_displayed(self):
        return self.player.EoC_comp1_quest1 ==3 and self.player.EoC_comp1_quest2 ==1 or self.player.EoC_comp1_quest1b ==3 and self.player.EoC_comp1_quest2b ==1

class OC_ov(Page):
    form_model = "player"

class OC_comp1(Page):
    form_model = "player"
    form_fields = ["OC_comp1_quest1", "OC_comp1_quest2", "OC_comp1_quest3"]

class OC_instruction1(Page):
    form_model = "player"
    def is_displayed(self):
        return self.player.OC_comp1_quest1!=3 or self.player.OC_comp1_quest2!=2 or self.player.OC_comp1_quest3!=4

class OC_comp1_2(Page):
    form_model = "player"
    form_fields = ["OC_comp1_quest1b", "OC_comp1_quest2b", "OC_comp1_quest3b"]
    def is_displayed(self):
        return self.player.OC_comp1_quest1!=3 or self.player.OC_comp1_quest2!=2 or self.player.OC_comp1_quest3!=4

    def OC_comp1_quest1b_error_message(self,value):
         if value!=3:
             return "Your answer is not correct."
    def OC_comp1_quest2b_error_message(self,value):
         if value!=2:
             return "Your answer is not correct."
    def OC_comp1_quest3b_error_message(self,value):
         if value!=4:
             return "Your answer is not correct."
   
class OC_task1(Page):
    form_model = "player"
    form_fields = ["OC1_low", "OC1_high", "OC2_low", "OC2_high", "OC3_low", "OC3_high", "OC4_low", "OC4_high", "OC5_low", "OC5_high", "OC6_low", "OC6_high", "OC7_low", "OC7_high", "OC8_low", "OC8_high", "OC9_low", "OC9_high", "OC10_low", "OC10_high", "tabOC1", "time_OC_task1"]
    def is_displayed(self):
        return self.player.OC_comp1_quest1==3 and self.player.OC_comp1_quest2 ==2 and self.player.OC_comp1_quest3 ==4 or self.player.OC_comp1_quest1b ==3 and self.player.OC_comp1_quest2b ==2 and self.player.OC_comp1_quest3b ==4

class OC_comp2(Page):
    form_model = "player"
    form_fields = ["OC_comp2_quest1", "OC_comp2_quest2"]

class OC_instruction2(Page):
    form_model = "player"
    def is_displayed(self):
        return self.player.OC_comp2_quest1!=1 or self.player.OC_comp2_quest2!=2

class OC_comp2_2(Page):
    form_model = "player"
    form_fields = ["OC_comp2_quest1b", "OC_comp2_quest2b"]
    def is_displayed(self):
        return self.player.OC_comp2_quest1!=1 or self.player.OC_comp2_quest2!=2

    def OC_comp2_quest1b_error_message(self,value):
         if value!=1:
             return "Your answer is not correct."
    def OC_comp2_quest2b_error_message(self,value):
         if value!=2:
             return "Your answer is not correct."

class OC_task2(Page):
    form_model = "player"
    form_fields = ["OC_task2", "time_OC_task2"]
    def is_displayed(self):
        return self.player.OC_comp2_quest1 ==1 and self.player.OC_comp2_quest2 ==2 or self.player.OC_comp2_quest1b ==1 and self.player.OC_comp2_quest2b==2


class Anchor_ov(Page):
    form_model = "player"

class Anchor_task(Page):
    form_model = "player"
    form_fields = ["Anchor", "Anchor_Anker", "tabAnchor", "time_Anchor"]

class AC_rand_EoC(Page):
    def is_displayed(self):
        return self.participant.vars["accountability_draft"] == 1

    def vars_for_template(self):
        self.player.participantvars = str(self.participant.vars)

class AC_rand_OC1(Page):
    def is_displayed(self):
        return self.participant.vars["accountability_draft"] == 2 

    def vars_for_template(self):
        self.player.participantvars = str(self.participant.vars)

class AC_rand_OC2(Page):
    def is_displayed(self):
        return self.participant.vars["accountability_draft"] == 3 

    def vars_for_template(self):
        self.player.participantvars = str(self.participant.vars)

class AC_rand_Anchor(Page):
    def is_displayed(self):
        return self.participant.vars["accountability_draft"] == 4

    def vars_for_template(self):
        self.player.participantvars = str(self.participant.vars)

class AC_just(Page):
    form_model = "player"
    form_fields = ["Accountability", "time_Just"]

class CRT(Page):
    form_model = "player"
    form_fields = ["CRT_1", "CRT_2", "CRT_3", "time_CRT", "tabCRT"]

class Bias_know_UV(Page):
    form_model = "player"
    form_fields = ["qBiasknowledge2b", "qBiasknowledge3b"]

class Bias_know(Page):
    form_model = "player"
    form_fields = ["BiasKnow1", "BiasKnow2", "BiasKnow3", "BiasKnow4", "BiasKnow5", "tabBiasknow", "time_Biasknow"]

class PEQ_ov(Page):
    form_model = "player"

class PEQ_1(Page):
    form_model = "player"
    form_fields = ["DuCha_1", "DuCha_2", "DuCha_3", "Act_Pro_1", "Act_Pro_2", "Pace", "Self_dis", "Satis"]

class PEQ_2(Page):
    form_model = "player"
    form_fields = ["Sys_4a", "Sys_1", "Sys_2", "Sys_3", "Sys_4", "AccMan_1", "AccMan_2", "AccMan_3", "AccMan_4"]

class PEQ_3(Page):
    form_model = "player"
    form_fields = ["EoC_Self1", "EoC_Self2", "EoC_Self3", "EoC_sunk1", "EoC_sunk2", "EoC_sunk3", "EoC_Opt1", "EoC_Opt2"]

class PEQ_4(Page):
    form_model = "player"
    form_fields = ["Over_1", "Over_2", "Over_3", "Over_4", "Over_5"]

class PEQ_person(Page):
    form_model = "player"
    form_fields = ["gender", "age", "language", "country", "degree", "workexperience", "industry", "mturk"]

class end_vorbereitung(Page):
    #determine lottery payment
    def before_next_page(self):
        self.player.lottery_draft = random.randint(1,15) # generate random number between 1 and 15 before session is generated
        self.player.lottery_outcome = random.randint(0,100) # generate random number between 0 and 100 before session is generated

        if self.player.lottery_choice > self.player.lottery_draft: # player chooses 14 and < 14 drafted --> lottery participation
            if self.player.lottery_outcome <= Constants.lottery_gamble_successrate[self.player.lottery_draft - 1]: #lottery participation succeeded
                self.player.payoff += c(Constants.lottery_success)
            else:
                self.player.payoff += c(Constants.lottery_failure) #failed
        else:
            self.player.payoff += c(Constants.lottery_safe) #safe payment

class PayoutLottery(Page):
    def vars_for_template(self):
        return dict(scsrate = Constants.lottery_gamble_successrate[self.player.lottery_draft - 1]) #successrate for drafted lotterys

class end(Page):
    def before_next_page(self):
        self.player.get_time("end")
        self.player.time_spent()

    

page_sequence = [wel_ins1]

## Alle Seiten: wel_ins1, Aussortieren_1, fail, Aussortieren_2, fail2, wel_ins2, Comprehension, Lottery_ins, Lottery, train_ov, VT_sec_1, TT_sec_1, UV_sec_1, T_sec_1_ques1, T_sec_1_ques1_fp,T_sec_1_ques1_fn, UV_sec_1_ques1, UV_sec_1_ques1_fp, UV_sec_1_ques1_fn, VT_sec_2, TT_sec_2_1, TT_sec_2_2, UV_sec_2, T_sec_2_ques1, T_sec_2_ques1_fp, T_sec_2_ques1_fn, T_sec_2_ques2, T_sec_2_ques2_fp, T_sec_2_ques2_fn, UV_sec_2_ques1, UV_sec_2_ques1_fp, UV_sec_2_ques1_fn, UV_sec_2_ques2, UV_sec_2_ques2_fp, UV_sec_2_ques2_fn, VT_sec_3, TT_sec_3_1, TT_sec_3_2, UV_sec_3, T_sec_3_ques1, T_sec_3_ques1_fp, T_sec_3_ques1_fn, T_sec_3_ques2, T_sec_3_ques2_fp, T_sec_3_ques2_fn, T_sec_3_ques3, T_sec_3_ques3_fp, T_sec_3_ques3_fn, UV_sec_3_ques1, UV_sec_3_ques1_fp, UV_sec_3_ques1_fn, UV_sec_3_ques2, UV_sec_3_ques2_fp, UV_sec_3_ques2_fn, UV_sec_3_ques3, UV_sec_3_ques3_fp, UV_sec_3_ques3_fn, VT_sec_4, TT_sec_4, UV_sec_4, PEQ_train, AC_no, AC_yes, EoC_ov, EoC_instructions, EoC_comp1, EoC_task, OC_ov, OC_comp1, OC_instruction1, OC_comp1_2, OC_task1, OC_comp2, OC_instruction2, OC_comp2_2, OC_task2, Anchor_ov, Anchor_task, AC_rand_EoC, AC_rand_Anchor, AC_rand_OC1, AC_rand_OC2, AC_just, CRT, Bias_know_UV, Bias_know, PEQ_ov, PEQ_1, PEQ_2, PEQ_3, PEQ_4, PEQ_person, end_vorbereitung, PayoutLottery, end



