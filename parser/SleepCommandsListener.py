# Generated from SleepCommands.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SleepCommandsParser import SleepCommandsParser
else:
    from SleepCommandsParser import SleepCommandsParser

# This class defines a complete listener for a parse tree produced by SleepCommandsParser.
class SleepCommandsListener(ParseTreeListener):

    # Enter a parse tree produced by SleepCommandsParser#command.
    def enterCommand(self, ctx:SleepCommandsParser.CommandContext):
        pass

    # Exit a parse tree produced by SleepCommandsParser#command.
    def exitCommand(self, ctx:SleepCommandsParser.CommandContext):
        pass


    # Enter a parse tree produced by SleepCommandsParser#sleepCmd.
    def enterSleepCmd(self, ctx:SleepCommandsParser.SleepCmdContext):
        pass

    # Exit a parse tree produced by SleepCommandsParser#sleepCmd.
    def exitSleepCmd(self, ctx:SleepCommandsParser.SleepCmdContext):
        pass


    # Enter a parse tree produced by SleepCommandsParser#wakeCmd.
    def enterWakeCmd(self, ctx:SleepCommandsParser.WakeCmdContext):
        pass

    # Exit a parse tree produced by SleepCommandsParser#wakeCmd.
    def exitWakeCmd(self, ctx:SleepCommandsParser.WakeCmdContext):
        pass


    # Enter a parse tree produced by SleepCommandsParser#setAlarmCmd.
    def enterSetAlarmCmd(self, ctx:SleepCommandsParser.SetAlarmCmdContext):
        pass

    # Exit a parse tree produced by SleepCommandsParser#setAlarmCmd.
    def exitSetAlarmCmd(self, ctx:SleepCommandsParser.SetAlarmCmdContext):
        pass


    # Enter a parse tree produced by SleepCommandsParser#setAlarmRelativeCmd.
    def enterSetAlarmRelativeCmd(self, ctx:SleepCommandsParser.SetAlarmRelativeCmdContext):
        pass

    # Exit a parse tree produced by SleepCommandsParser#setAlarmRelativeCmd.
    def exitSetAlarmRelativeCmd(self, ctx:SleepCommandsParser.SetAlarmRelativeCmdContext):
        pass


    # Enter a parse tree produced by SleepCommandsParser#cancelAlarmCmd.
    def enterCancelAlarmCmd(self, ctx:SleepCommandsParser.CancelAlarmCmdContext):
        pass

    # Exit a parse tree produced by SleepCommandsParser#cancelAlarmCmd.
    def exitCancelAlarmCmd(self, ctx:SleepCommandsParser.CancelAlarmCmdContext):
        pass


    # Enter a parse tree produced by SleepCommandsParser#snoozeAlarmCmd.
    def enterSnoozeAlarmCmd(self, ctx:SleepCommandsParser.SnoozeAlarmCmdContext):
        pass

    # Exit a parse tree produced by SleepCommandsParser#snoozeAlarmCmd.
    def exitSnoozeAlarmCmd(self, ctx:SleepCommandsParser.SnoozeAlarmCmdContext):
        pass


    # Enter a parse tree produced by SleepCommandsParser#lateAlertCmd.
    def enterLateAlertCmd(self, ctx:SleepCommandsParser.LateAlertCmdContext):
        pass

    # Exit a parse tree produced by SleepCommandsParser#lateAlertCmd.
    def exitLateAlertCmd(self, ctx:SleepCommandsParser.LateAlertCmdContext):
        pass


    # Enter a parse tree produced by SleepCommandsParser#queryCmd.
    def enterQueryCmd(self, ctx:SleepCommandsParser.QueryCmdContext):
        pass

    # Exit a parse tree produced by SleepCommandsParser#queryCmd.
    def exitQueryCmd(self, ctx:SleepCommandsParser.QueryCmdContext):
        pass


    # Enter a parse tree produced by SleepCommandsParser#consistencyCmd.
    def enterConsistencyCmd(self, ctx:SleepCommandsParser.ConsistencyCmdContext):
        pass

    # Exit a parse tree produced by SleepCommandsParser#consistencyCmd.
    def exitConsistencyCmd(self, ctx:SleepCommandsParser.ConsistencyCmdContext):
        pass


    # Enter a parse tree produced by SleepCommandsParser#qualityCmd.
    def enterQualityCmd(self, ctx:SleepCommandsParser.QualityCmdContext):
        pass

    # Exit a parse tree produced by SleepCommandsParser#qualityCmd.
    def exitQualityCmd(self, ctx:SleepCommandsParser.QualityCmdContext):
        pass


    # Enter a parse tree produced by SleepCommandsParser#adviceCmd.
    def enterAdviceCmd(self, ctx:SleepCommandsParser.AdviceCmdContext):
        pass

    # Exit a parse tree produced by SleepCommandsParser#adviceCmd.
    def exitAdviceCmd(self, ctx:SleepCommandsParser.AdviceCmdContext):
        pass


    # Enter a parse tree produced by SleepCommandsParser#helpCmd.
    def enterHelpCmd(self, ctx:SleepCommandsParser.HelpCmdContext):
        pass

    # Exit a parse tree produced by SleepCommandsParser#helpCmd.
    def exitHelpCmd(self, ctx:SleepCommandsParser.HelpCmdContext):
        pass



del SleepCommandsParser