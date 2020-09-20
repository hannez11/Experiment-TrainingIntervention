from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

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
        list3 = [f"id_lottery_choice_{i}" for i in range(1,17)] #1 to 16, 16th in case someone always wants to gamble
        data = list(zip(list1,list2,list3))
        return {"data": data} # {% for a,b,c in data %} -> {{ a }} .. .. -> displays 85% .. 15% ..  form.lottery_choice.0

    def before_next_page(self):
        self.participant.vars["global_lottery_choice"] = self.player.lottery_choice #if payout is needed in another app
        print("global_lottery_choice" + str(self.participant.vars["global_lottery_choice"]))

class train_ov(Page):
    form_model = "player"

class VT_sec_1(Page):
    def is_displayed(self):
        return self.subsession.training == "VT" #page is only displayed on VT condition
    
    form_model = "player"
    form_fields = ["tabVT1"]


class TT_sec_1(Page):
    form_model = "player"
    form_fields = ["time_TT_sec_1"]

    def is_displayed(self):
        return self.subsession.training == "TT" #page is only displayed on VT condition

class UV_sec_1(Page):
    form_model = "player"
    form_fields = ["tabUV1"]
   
    def is_displayed(self):
        return self.subsession.training == "UT" #page is only displayed on UT condition
    
class T_sec_1_ques1(Page):
    def is_displayed(self):
        return self.subsession.training != "UT"

    form_model = "player"
    form_fields = ["qBiasknowledge2", "qBiasknowledge3"]

class T_sec_1_ques1_fn(Page):
    def is_displayed(self):
        return self.player.qBiasknowledge2!=1 and self.subsession.training != "UT"

class T_sec_1_ques1_fp(Page):
    def is_displayed(self):
        return self.player.qBiasknowledge2!=2 and self.subsession.training != "UT"

class UV_sec_1_ques1(Page):
    form_model = "player"
    form_fields = ["qsustaininvest2", "qsustaininvest3"]

    def is_displayed(self):
        return self.subsession.training == "UT"

class UV_sec_1_ques1_fn(Page):
    def is_displayed(self):
        return self.player.qsustaininvest2!=1 and (self.subsession.training == "UT")

class UV_sec_1_ques1_fp(Page):
    def is_displayed(self):
        return self.player.qsustaininvest2!=2 and (self.subsession.training == "UT")

class VT_sec_2(Page):
    form_model = "player"
    form_fields = ["tabVT2"]

    def is_displayed(self):
        return self.subsession.training == "VT"

class TT_sec_2_1(Page):
    form_model = "player"
    form_fields = ["time_TT_sec_2_1", "tabTTsec21"]

    def is_displayed(self):
        return self.subsession.training == "TT"

class TT_sec_2_2(Page):
    form_model = "player"
    form_fields = ["time_TT_sec_2_2", "tabTTsec22"]

    def is_displayed(self):
        return self.subsession.training == "TT"

class UV_sec_2(Page):
    form_model = "player"
    form_fields = ["tabUV2"]

    def is_displayed(self):
        return self.subsession.training == "UT"

class T_sec_2_ques1(Page):
    form_model = "player"
    form_fields = ["Tsec2_quest1"]

    def is_displayed(self):
        return self.subsession.training != "UT"

class T_sec_2_ques1_fp(Page):
    def is_displayed(self):
        return self.player.Tsec2_quest1==2 and self.subsession.training != "UT"

class T_sec_2_ques1_fn(Page):
    def is_displayed(self):
        return self.player.Tsec2_quest1!=2 and self.subsession.training != "UT"

class T_sec_2_ques2(Page):
    form_model = "player"
    form_fields = ["Tsec2_quest2"]

    def is_displayed(self):
        return self.subsession.training != "UT"

class T_sec_2_ques2_fp(Page):
    def is_displayed(self):
        return self.player.Tsec2_quest2==3 and self.subsession.training != "UT"

class T_sec_2_ques2_fn(Page):
    def is_displayed(self):
        return self.player.Tsec2_quest2!=3 and self.subsession.training != "UT"

class UV_sec_2_ques1(Page):
    form_model = "player"
    form_fields = ["UVsec2_quest1"]

    def is_displayed(self):
        return self.subsession.training == "UT"

class UV_sec_2_ques1_fn(Page):
    def is_displayed(self):
        return self.player.UVsec2_quest1!=3 and (self.subsession.training == "UT")

class UV_sec_2_ques1_fp(Page):
    def is_displayed(self):
        return self.player.UVsec2_quest1==3 and (self.subsession.training == "UT")

class UV_sec_2_ques2(Page):
    form_model = "player"
    form_fields = ["UVsec2_quest2"]

    def is_displayed(self):
        return self.subsession.training == "UT"

class UV_sec_2_ques2_fn(Page):
    def is_displayed(self):
        return self.player.UVsec2_quest2!=1 and (self.subsession.training == "UT")

class UV_sec_2_ques2_fp(Page):
    def is_displayed(self):
        return self.player.UVsec2_quest2==1 and (self.subsession.training == "UT")

class VT_sec_3(Page):
    form_model = "player"
    form_fields = ["tabVT3"]

    def is_displayed(self):
        return self.subsession.training == "VT"

class TT_sec_3_1(Page):
    form_model = "player"
    form_fields = ["time_TT_sec_3_1", "tabTTsec31"]

    def is_displayed(self):
        return self.subsession.training == "TT"

class TT_sec_3_2(Page):
    form_model = "player"
    form_fields = ["time_TT_sec_3_2", "tabTTsec32"]

    def is_displayed(self):
        return self.subsession.training == "TT"

class UV_sec_3(Page):
    # def is_displayed(self):
    #     return self.player.treatment == 3 or 6
    form_model = "player"
    form_fields = ["tabUV3"]

    def is_displayed(self):
        return self.subsession.training == "UT"

class T_sec_3_ques1(Page):
    form_model = "player"
    form_fields = ["Tsec3_quest1"]

    def is_displayed(self):
        return self.subsession.training != "UT"

class T_sec_3_ques1_fn(Page):
    def is_displayed(self):
        return self.player.Tsec3_quest1!=4 and self.subsession.training != "UT"

class T_sec_3_ques1_fp(Page):
    def is_displayed(self):
        return self.player.Tsec3_quest1==4 and self.subsession.training != "UT"

class T_sec_3_ques2(Page):
    form_model = "player"
    form_fields = ["Tsec3_quest2"] 

    def is_displayed(self):
        return self.subsession.training != "UT"

class T_sec_3_ques2_fn(Page):
    def is_displayed(self):
        return self.player.Tsec3_quest2!=2 and self.subsession.training != "UT"

class T_sec_3_ques2_fp(Page):
    def is_displayed(self):
        return self.player.Tsec3_quest2==2 and self.subsession.training != "UT"

class T_sec_3_ques3(Page):
    form_model = "player"
    form_fields = ["Tsec3_quest3"]

    def is_displayed(self):
        return self.subsession.training != "UT"

class T_sec_3_ques3_fn(Page):
    def is_displayed(self):
        return self.player.Tsec3_quest3!=2 and self.subsession.training != "UT"

class T_sec_3_ques3_fp(Page):
    def is_displayed(self):
        return self.player.Tsec3_quest3==2 and self.subsession.training != "UT"

class UV_sec_3_ques1(Page):
    form_model = "player"
    form_fields = ["UVsec3_quest1"]

    def is_displayed(self):
        return self.subsession.training == "UT"

class UV_sec_3_ques1_fn(Page):
    def is_displayed(self):
        return self.player.UVsec3_quest1!=2 and (self.subsession.training == "UT")

class UV_sec_3_ques1_fp(Page):
    def is_displayed(self):
        return self.player.UVsec3_quest1==2 and (self.subsession.training == "UT")

class UV_sec_3_ques2(Page):
    form_model = "player"
    form_fields = ["UVsec3_quest2"]

    def is_displayed(self):
        return self.subsession.training == "UT"

class UV_sec_3_ques2_fn(Page):
    def is_displayed(self):
        return self.player.UVsec3_quest2!=2 and (self.subsession.training == "UT")

class UV_sec_3_ques2_fp(Page):
    def is_displayed(self):
        return self.player.UVsec3_quest2==2 and (self.subsession.training == "UT")

class UV_sec_3_ques3(Page):
    form_model = "player"
    form_fields = ["UVsec3_quest3"]

    def is_displayed(self):
        return self.subsession.training == "UT"

class UV_sec_3_ques3_fn(Page):
    def is_displayed(self):
        return self.player.UVsec3_quest3!=2 and (self.subsession.training == "UT")

class UV_sec_3_ques3_fp(Page):
    def is_displayed(self):
        return self.player.UVsec3_quest3==2 and (self.subsession.training == "UT")

class VT_sec_4(Page):
    form_model = "player"
    form_fields = ["tabVT4"]

    def is_displayed(self):
        return self.subsession.training == "VT"

class TT_sec_4(Page):
    form_model = "player"
    form_fields = ["time_TT_sec_4", "tabTTsec4"]

    def is_displayed(self):
        return self.subsession.training == "TT"

class UV_sec_4(Page):
    form_model = "player"
    form_fields = ["tabUV4"]

    def is_displayed(self):
        return self.subsession.training == "UT"

class PEQ_trainVT(Page):
    form_model = "player"
    form_fields = ["Intr_Mot1VT", "Intr_Mot2VT", "Intr_Mot3", "Mod1", "Mod2", "Cogn_Lo1", "Cogn_Lo2", "Cogn_Lo3", "Cogn_Lo4", "Ment_Eff", "Train_ManCheckVT"]

    def is_displayed(self):
        return self.subsession.training == "VT"

class PEQ_trainTT(Page):
    form_model = "player"
    form_fields = ["Intr_Mot1TT", "Intr_Mot2TT", "Intr_Mot3", "Mod1", "Mod2", "Cogn_Lo1", "Cogn_Lo2", "Cogn_Lo3", "Cogn_Lo4", "Ment_Eff", "Train_ManCheckTT"]

    def is_displayed(self):
        return self.subsession.training == "TT"

class PEQ_trainUT(Page):
    form_model = "player"
    form_fields = ["Intr_Mot1VT", "Intr_Mot2VT", "Intr_Mot3", "Mod1", "Mod2", "Cogn_Lo1", "Cogn_Lo2", "Cogn_Lo3", "Cogn_Lo4", "Ment_Eff", "Train_ManCheckUT"]

    def is_displayed(self):
        return self.subsession.training == "UT"

class AC_no(Page):
    form_model = "player"

    def is_displayed(self):
        return self.subsession.accountability == "niedrig"

    def before_next_page(self):
        self.player.get_time("end")
        self.player.time_spent()

class AC_yes(Page):
    form_model = "player"
    form_fields = ["time_ACyes"]

    def before_next_page(self):
        self.player.get_time("end")
        self.player.time_spent()

    def is_displayed(self):
        return self.subsession.accountability == "hoch"

page_sequence = [Lottery]

#page_sequence = [wel_ins1, Aussortieren_1, fail, Aussortieren_2, fail2, wel_ins2, Comprehension, Lottery_ins, Lottery, train_ov, VT_sec_1, TT_sec_1, UV_sec_1, T_sec_1_ques1, T_sec_1_ques1_fp, T_sec_1_ques1_fn, UV_sec_1_ques1, UV_sec_1_ques1_fp, UV_sec_1_ques1_fn, VT_sec_2, TT_sec_2_1, TT_sec_2_2, UV_sec_2, T_sec_2_ques1, T_sec_2_ques1_fp, T_sec_2_ques1_fn, T_sec_2_ques2, T_sec_2_ques2_fp, T_sec_2_ques2_fn, UV_sec_2_ques1, UV_sec_2_ques1_fp, UV_sec_2_ques1_fn, UV_sec_2_ques2, UV_sec_2_ques2_fp, UV_sec_2_ques2_fn, VT_sec_3, TT_sec_3_1, TT_sec_3_2, UV_sec_3, T_sec_3_ques1, T_sec_3_ques1_fp, T_sec_3_ques1_fn, T_sec_3_ques2, T_sec_3_ques2_fp, T_sec_3_ques2_fn,T_sec_3_ques3, T_sec_3_ques3_fp, T_sec_3_ques3_fn, UV_sec_3_ques1, UV_sec_3_ques1_fp, UV_sec_3_ques1_fn, UV_sec_3_ques2, UV_sec_3_ques2_fp, UV_sec_3_ques2_fn, UV_sec_3_ques3, UV_sec_3_ques3_fp, UV_sec_3_ques3_fn, VT_sec_4, TT_sec_4, UV_sec_4, PEQ_trainTT, PEQ_trainUT, PEQ_trainVT, AC_no, AC_yes]