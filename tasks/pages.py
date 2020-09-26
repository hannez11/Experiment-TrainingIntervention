from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class EoC_ov1(Page):
    form_model = "player"
    form_fields = ["Initial", "time_EoC_ov", "time_EoC_ovCheck"]

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']["escalation"]

    def vars_for_template(self):
        return {"roundnumber": self.round_number}

class EoC_ov(Page):
    form_model = "player"
    form_fields = ["EoC_comp1_quest2","EoC_comp1_quest1", "time_EoC_ov2"]

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']["escalation"] and self.player.Initial==1 

class EoC_ovB(Page):
    form_model = "player"
    form_fields = ["EoC_comp1_quest2","EoC_comp1_quest1","time_EoC_ov2"]

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']["escalation"] and self.player.Initial==2 

class EoC_instructions(Page):
    def is_displayed(self):
        return (self.player.EoC_comp1_quest1!=3 or self.player.EoC_comp1_quest2!=1) and self.round_number == self.participant.vars['task_rounds']["escalation"]

class EoC_comp1(Page):
    form_model = "player"
    form_fields = ["EoC_comp1_quest2b", "EoC_comp1_quest1b"]
    def is_displayed(self):
        return (self.player.EoC_comp1_quest1!=3 or self.player.EoC_comp1_quest2!=1) and self.round_number == self.participant.vars['task_rounds']["escalation"]

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
        return (self.player.EoC_comp1_quest1 ==3 and self.player.EoC_comp1_quest2 ==1) or (self.player.EoC_comp1_quest1b ==3 and self.player.EoC_comp1_quest2b ==1) and (self.round_number == self.participant.vars['task_rounds']["escalation"])

    def before_next_page(self):
        self.participant.vars["global_EoC_task"] = self.player.EoC_task


#########################################

class OC_ov(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']["overconfidence"]

    def vars_for_template(self):
        return {"roundnumber": self.round_number}

class OC_comp1(Page):
    form_model = "player"
    form_fields = ["OC_comp1_quest1", "OC_comp1_quest2", "OC_comp1_quest3"]

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']["overconfidence"]

class OC_instruction1(Page):
    form_model = "player"
    def is_displayed(self):
        return (self.player.OC_comp1_quest1!=3 or self.player.OC_comp1_quest2!=2 or self.player.OC_comp1_quest3!=4) and (self.round_number == self.participant.vars['task_rounds']["overconfidence"])

class OC_comp1_2(Page):
    form_model = "player"
    form_fields = ["OC_comp1_quest1b", "OC_comp1_quest2b", "OC_comp1_quest3b"]
    def is_displayed(self):
        return (self.player.OC_comp1_quest1!=3 or self.player.OC_comp1_quest2!=2 or self.player.OC_comp1_quest3!=4) and (self.round_number == self.participant.vars['task_rounds']["overconfidence"])

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
        return (self.player.OC_comp1_quest1==3 and self.player.OC_comp1_quest2 ==2 and self.player.OC_comp1_quest3 ==4) or (self.player.OC_comp1_quest1b ==3 and self.player.OC_comp1_quest2b ==2 and self.player.OC_comp1_quest3b ==4) and (self.round_number == self.participant.vars['task_rounds']["overconfidence"])

    def before_next_page(self):
        self.participant.vars["global_OC1_low"] = self.player.OC1_low
        self.participant.vars["global_OC1_high"] = self.player.OC1_high
        

class OC_comp2(Page):
    form_model = "player"
    form_fields = ["OC_comp2_quest1", "OC_comp2_quest2"]

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']["overconfidence"]

class OC_instruction2(Page):
    form_model = "player"
    def is_displayed(self):
        return (self.player.OC_comp2_quest1!=1 or self.player.OC_comp2_quest2!=2) and (self.round_number == self.participant.vars['task_rounds']["overconfidence"])

class OC_comp2_2(Page):
    form_model = "player"
    form_fields = ["OC_comp2_quest1b", "OC_comp2_quest2b"]
    def is_displayed(self):
        return (self.player.OC_comp2_quest1!=1 or self.player.OC_comp2_quest2!=2) and (self.round_number == self.participant.vars['task_rounds']["overconfidence"])

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
        return (self.player.OC_comp2_quest1 ==1 and self.player.OC_comp2_quest2 ==2 or self.player.OC_comp2_quest1b ==1 and self.player.OC_comp2_quest2b==2) and (self.round_number == self.participant.vars['task_rounds']["overconfidence"])

    def before_next_page(self):
        self.participant.vars["global_OC_task2"] = self.player.OC_task2


##########################

class Anchor_ov(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']["anchoring"]

    def vars_for_template(self):
        return {"roundnumber": self.round_number}

class Anchor_task(Page):
    form_model = "player"
    form_fields = ["Anchor", "Anchor_Anker", "tabAnchor", "time_Anchor"]

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']["anchoring"]

    def before_next_page(self):
        self.participant.vars["global_Anchor"] = self.player.Anchor

###########################

class AC_rand_EoC(Page):
    def is_displayed(self):
        return self.participant.vars["accountability_draft"] == 1 and (self.subsession.accountability == "hoch") and (self.round_number == 3)

    def vars_for_template(self):
        self.player.participantvars = str(self.participant.vars)

class AC_rand_OC1(Page):
    def is_displayed(self):
        return self.participant.vars["accountability_draft"] == 2 and (self.subsession.accountability == "hoch") and (self.round_number == 3)

    def vars_for_template(self):
        self.player.participantvars = str(self.participant.vars)

class AC_rand_OC2(Page):
    def is_displayed(self):
        return self.participant.vars["accountability_draft"] == 3 and (self.subsession.accountability == "hoch") and (self.round_number == 3)

    def vars_for_template(self):
        self.player.participantvars = str(self.participant.vars)

class AC_rand_Anchor(Page):
    def is_displayed(self):
        return self.participant.vars["accountability_draft"] == 4 and (self.subsession.accountability == "hoch") and (self.round_number == 3)

    def vars_for_template(self):
        self.player.participantvars = str(self.participant.vars)

class AC_just(Page):
    form_model = "player"
    form_fields = ["Accountability", "time_Just"]

    def is_displayed(self):
        return self.subsession.accountability == "hoch" and (self.round_number == 3)





page_sequence = [EoC_ov1, EoC_ov, EoC_ovB, EoC_instructions, EoC_comp1, EoC_task, OC_ov, OC_comp1, OC_instruction1, OC_comp1_2, OC_task1, OC_comp2, OC_instruction2, OC_comp2_2, OC_task2, Anchor_ov, Anchor_task, AC_rand_EoC, AC_rand_Anchor, AC_rand_OC1, AC_rand_OC2, AC_just]


