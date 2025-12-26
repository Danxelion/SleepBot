// Generated from d:/School/PPL/Sleep-Schedule-Tracking-Chatbot-main/Sleep-Schedule-Tracking-Chatbot-main/SleepBot/parser/SleepCommands.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SleepCommandsParser}.
 */
public interface SleepCommandsListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SleepCommandsParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(SleepCommandsParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link SleepCommandsParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(SleepCommandsParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link SleepCommandsParser#sleepCmd}.
	 * @param ctx the parse tree
	 */
	void enterSleepCmd(SleepCommandsParser.SleepCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SleepCommandsParser#sleepCmd}.
	 * @param ctx the parse tree
	 */
	void exitSleepCmd(SleepCommandsParser.SleepCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SleepCommandsParser#wakeCmd}.
	 * @param ctx the parse tree
	 */
	void enterWakeCmd(SleepCommandsParser.WakeCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SleepCommandsParser#wakeCmd}.
	 * @param ctx the parse tree
	 */
	void exitWakeCmd(SleepCommandsParser.WakeCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SleepCommandsParser#setAlarmCmd}.
	 * @param ctx the parse tree
	 */
	void enterSetAlarmCmd(SleepCommandsParser.SetAlarmCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SleepCommandsParser#setAlarmCmd}.
	 * @param ctx the parse tree
	 */
	void exitSetAlarmCmd(SleepCommandsParser.SetAlarmCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SleepCommandsParser#setAlarmRelativeCmd}.
	 * @param ctx the parse tree
	 */
	void enterSetAlarmRelativeCmd(SleepCommandsParser.SetAlarmRelativeCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SleepCommandsParser#setAlarmRelativeCmd}.
	 * @param ctx the parse tree
	 */
	void exitSetAlarmRelativeCmd(SleepCommandsParser.SetAlarmRelativeCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SleepCommandsParser#cancelAlarmCmd}.
	 * @param ctx the parse tree
	 */
	void enterCancelAlarmCmd(SleepCommandsParser.CancelAlarmCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SleepCommandsParser#cancelAlarmCmd}.
	 * @param ctx the parse tree
	 */
	void exitCancelAlarmCmd(SleepCommandsParser.CancelAlarmCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SleepCommandsParser#snoozeAlarmCmd}.
	 * @param ctx the parse tree
	 */
	void enterSnoozeAlarmCmd(SleepCommandsParser.SnoozeAlarmCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SleepCommandsParser#snoozeAlarmCmd}.
	 * @param ctx the parse tree
	 */
	void exitSnoozeAlarmCmd(SleepCommandsParser.SnoozeAlarmCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SleepCommandsParser#lateAlertCmd}.
	 * @param ctx the parse tree
	 */
	void enterLateAlertCmd(SleepCommandsParser.LateAlertCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SleepCommandsParser#lateAlertCmd}.
	 * @param ctx the parse tree
	 */
	void exitLateAlertCmd(SleepCommandsParser.LateAlertCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SleepCommandsParser#queryCmd}.
	 * @param ctx the parse tree
	 */
	void enterQueryCmd(SleepCommandsParser.QueryCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SleepCommandsParser#queryCmd}.
	 * @param ctx the parse tree
	 */
	void exitQueryCmd(SleepCommandsParser.QueryCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SleepCommandsParser#consistencyCmd}.
	 * @param ctx the parse tree
	 */
	void enterConsistencyCmd(SleepCommandsParser.ConsistencyCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SleepCommandsParser#consistencyCmd}.
	 * @param ctx the parse tree
	 */
	void exitConsistencyCmd(SleepCommandsParser.ConsistencyCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SleepCommandsParser#helpCmd}.
	 * @param ctx the parse tree
	 */
	void enterHelpCmd(SleepCommandsParser.HelpCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SleepCommandsParser#helpCmd}.
	 * @param ctx the parse tree
	 */
	void exitHelpCmd(SleepCommandsParser.HelpCmdContext ctx);
}