from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class CRT(Page):
    form_model = "player"
    form_fields = ["CRT_2", "time_CRT", "tabCRT"]

    def before_next_page(self):
        self.player.get_time("start")

class Bias_know_UV(Page):
    form_model = "player"
    form_fields = ["qBiasknowledge2b", "qBiasknowledge3b"]

    def is_displayed(self):
        return self.subsession.training == "UT"

class Bias_know(Page):
    form_model = "player"
    form_fields = ["BiasKnow1", "BiasKnow2", "BiasKnow3", "tabBiasknow", "time_Biasknow"]

class PEQ_ov(Page):
    form_model = "player"

class PEQ_1(Page):
    form_model = "player"
    form_fields = ["AccMan_1", "AccMan_3", "AccMan_4", "Sys_1", "Sys_2", "Sys_3", "Act_Pro_1", "Act_Pro_2"]

class PEQ_2(Page):
    form_model = "player"
    form_fields = ["EoC_Self1", "EoC_Self2", "EoC_Self3", "EoC_sunk1", "EoC_sunk2", "EoC_sunk3", "EoC_Opt1", "EoC_Opt2", "ATTChe"]

class PEQ_3(Page):
    form_model = "player"
    form_fields = ["Over_1", "Over_2", "Over_3", "OC_Mturk", "Doubt", "AtEx"]


class PEQ_person(Page):
    form_model = "player"
    form_fields = ["gender", "age", "language", "country", "degree", "workexperience", "industry", "mturk"]

class end_vorbereitung(Page):
    #determine lottery payment
    def before_next_page(self):
        self.player.lottery_draft = random.randint(1,15) # generate random number between 1 and 15 before session is generated
        self.player.lottery_outcome = random.randint(0,100) # generate random number between 0 and 100 before session is generated
        
        if self.participant.vars["global_lottery_choice"] > self.player.lottery_draft: # player chooses 14 and < 14 drafted --> lottery participation
            if self.player.lottery_outcome <= Constants.lottery_gamble_successrate[self.player.lottery_draft - 1]: #lottery participation succeeded
                self.player.payoff += c(Constants.lottery_success)
            else:
                self.player.payoff += c(Constants.lottery_failure) #failed
        else:
            self.player.payoff += c(Constants.lottery_safe) #safe payment

class PayoutLottery(Page):
    def vars_for_template(self):
        return dict(scsrate = Constants.lottery_gamble_successrate[self.player.lottery_draft - 1]) #successrate for drafted lotterys

    def before_next_page(self):
        self.player.get_time("end")
        self.player.time_spent()

class end(Page):
    form_model = "player"


page_sequence = [CRT, Bias_know_UV, Bias_know, PEQ_ov, PEQ_1, PEQ_2, PEQ_3, PEQ_person, end_vorbereitung, PayoutLottery, end]
