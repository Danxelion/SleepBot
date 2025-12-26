// Generated from d:/School/PPL/Sleep-Schedule-Tracking-Chatbot-main/Sleep-Schedule-Tracking-Chatbot-main/SleepBot/parser/SleepCommands.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class SleepCommandsParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		I=1, AM=2, IS=3, GOING=4, TO=5, SLEEP=6, WOKE=7, UP=8, AWAKE=9, WAKE=10, 
		ME=11, AT=12, IN=13, WARN=14, IF=15, AFTER=16, WHAT=17, TIMEWORD=18, DID=19, 
		YESTERDAY=20, SHOW=21, CHECK=22, MY=23, CONSISTENCY=24, REGULARITY=25, 
		HOW=26, CONSISTENT=27, REGULAR=28, HELP=29, CANCEL=30, STOP=31, ALARM=32, 
		SNOOZE=33, FOR=34, QUALITY=35, RATE=36, ANALYZE=37, GIVE=38, GET=39, ADVICE=40, 
		TIPS=41, SUGGESTIONS=42, BETTER=43, IMPROVE=44, CAN=45, TIME=46, NUMBER=47, 
		TIMEUNIT=48, WS=49;
	public static final int
		RULE_command = 0, RULE_sleepCmd = 1, RULE_wakeCmd = 2, RULE_setAlarmCmd = 3, 
		RULE_setAlarmRelativeCmd = 4, RULE_cancelAlarmCmd = 5, RULE_snoozeAlarmCmd = 6, 
		RULE_lateAlertCmd = 7, RULE_queryCmd = 8, RULE_consistencyCmd = 9, RULE_qualityCmd = 10, 
		RULE_adviceCmd = 11, RULE_helpCmd = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"command", "sleepCmd", "wakeCmd", "setAlarmCmd", "setAlarmRelativeCmd", 
			"cancelAlarmCmd", "snoozeAlarmCmd", "lateAlertCmd", "queryCmd", "consistencyCmd", 
			"qualityCmd", "adviceCmd", "helpCmd"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'i'", "'am'", "'is'", "'going'", "'to'", "'sleep'", "'woke'", 
			"'up'", "'awake'", "'wake'", "'me'", "'at'", "'in'", "'warn'", "'if'", 
			"'after'", "'what'", "'time'", "'did'", "'yesterday'", "'show'", "'check'", 
			"'my'", "'consistency'", "'regularity'", "'how'", "'consistent'", "'regular'", 
			"'help'", "'cancel'", "'stop'", "'alarm'", "'snooze'", "'for'", "'quality'", 
			"'rate'", "'analyze'", "'give'", "'get'", "'advice'", "'tips'", "'suggestions'", 
			"'better'", "'improve'", "'can'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "I", "AM", "IS", "GOING", "TO", "SLEEP", "WOKE", "UP", "AWAKE", 
			"WAKE", "ME", "AT", "IN", "WARN", "IF", "AFTER", "WHAT", "TIMEWORD", 
			"DID", "YESTERDAY", "SHOW", "CHECK", "MY", "CONSISTENCY", "REGULARITY", 
			"HOW", "CONSISTENT", "REGULAR", "HELP", "CANCEL", "STOP", "ALARM", "SNOOZE", 
			"FOR", "QUALITY", "RATE", "ANALYZE", "GIVE", "GET", "ADVICE", "TIPS", 
			"SUGGESTIONS", "BETTER", "IMPROVE", "CAN", "TIME", "NUMBER", "TIMEUNIT", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "SleepCommands.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SleepCommandsParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandContext extends ParserRuleContext {
		public SleepCmdContext sleepCmd() {
			return getRuleContext(SleepCmdContext.class,0);
		}
		public WakeCmdContext wakeCmd() {
			return getRuleContext(WakeCmdContext.class,0);
		}
		public SetAlarmCmdContext setAlarmCmd() {
			return getRuleContext(SetAlarmCmdContext.class,0);
		}
		public SetAlarmRelativeCmdContext setAlarmRelativeCmd() {
			return getRuleContext(SetAlarmRelativeCmdContext.class,0);
		}
		public CancelAlarmCmdContext cancelAlarmCmd() {
			return getRuleContext(CancelAlarmCmdContext.class,0);
		}
		public SnoozeAlarmCmdContext snoozeAlarmCmd() {
			return getRuleContext(SnoozeAlarmCmdContext.class,0);
		}
		public LateAlertCmdContext lateAlertCmd() {
			return getRuleContext(LateAlertCmdContext.class,0);
		}
		public QueryCmdContext queryCmd() {
			return getRuleContext(QueryCmdContext.class,0);
		}
		public ConsistencyCmdContext consistencyCmd() {
			return getRuleContext(ConsistencyCmdContext.class,0);
		}
		public QualityCmdContext qualityCmd() {
			return getRuleContext(QualityCmdContext.class,0);
		}
		public AdviceCmdContext adviceCmd() {
			return getRuleContext(AdviceCmdContext.class,0);
		}
		public HelpCmdContext helpCmd() {
			return getRuleContext(HelpCmdContext.class,0);
		}
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_command);
		try {
			setState(38);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(26);
				sleepCmd();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(27);
				wakeCmd();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(28);
				setAlarmCmd();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(29);
				setAlarmRelativeCmd();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(30);
				cancelAlarmCmd();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(31);
				snoozeAlarmCmd();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(32);
				lateAlertCmd();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(33);
				queryCmd();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(34);
				consistencyCmd();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(35);
				qualityCmd();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(36);
				adviceCmd();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(37);
				helpCmd();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SleepCmdContext extends ParserRuleContext {
		public TerminalNode GOING() { return getToken(SleepCommandsParser.GOING, 0); }
		public TerminalNode TO() { return getToken(SleepCommandsParser.TO, 0); }
		public TerminalNode SLEEP() { return getToken(SleepCommandsParser.SLEEP, 0); }
		public TerminalNode I() { return getToken(SleepCommandsParser.I, 0); }
		public TerminalNode AM() { return getToken(SleepCommandsParser.AM, 0); }
		public SleepCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sleepCmd; }
	}

	public final SleepCmdContext sleepCmd() throws RecognitionException {
		SleepCmdContext _localctx = new SleepCmdContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_sleepCmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==I) {
				{
				setState(40);
				match(I);
				}
			}

			setState(44);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AM) {
				{
				setState(43);
				match(AM);
				}
			}

			setState(46);
			match(GOING);
			setState(47);
			match(TO);
			setState(48);
			match(SLEEP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WakeCmdContext extends ParserRuleContext {
		public TerminalNode WOKE() { return getToken(SleepCommandsParser.WOKE, 0); }
		public TerminalNode UP() { return getToken(SleepCommandsParser.UP, 0); }
		public TerminalNode AM() { return getToken(SleepCommandsParser.AM, 0); }
		public TerminalNode AWAKE() { return getToken(SleepCommandsParser.AWAKE, 0); }
		public TerminalNode I() { return getToken(SleepCommandsParser.I, 0); }
		public WakeCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wakeCmd; }
	}

	public final WakeCmdContext wakeCmd() throws RecognitionException {
		WakeCmdContext _localctx = new WakeCmdContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_wakeCmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==I) {
				{
				setState(50);
				match(I);
				}
			}

			setState(57);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case WOKE:
				{
				setState(53);
				match(WOKE);
				setState(54);
				match(UP);
				}
				break;
			case AM:
				{
				setState(55);
				match(AM);
				setState(56);
				match(AWAKE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SetAlarmCmdContext extends ParserRuleContext {
		public TerminalNode WAKE() { return getToken(SleepCommandsParser.WAKE, 0); }
		public TerminalNode ME() { return getToken(SleepCommandsParser.ME, 0); }
		public TerminalNode UP() { return getToken(SleepCommandsParser.UP, 0); }
		public TerminalNode AT() { return getToken(SleepCommandsParser.AT, 0); }
		public TerminalNode TIME() { return getToken(SleepCommandsParser.TIME, 0); }
		public SetAlarmCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setAlarmCmd; }
	}

	public final SetAlarmCmdContext setAlarmCmd() throws RecognitionException {
		SetAlarmCmdContext _localctx = new SetAlarmCmdContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_setAlarmCmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(WAKE);
			setState(60);
			match(ME);
			setState(61);
			match(UP);
			setState(62);
			match(AT);
			setState(63);
			match(TIME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SetAlarmRelativeCmdContext extends ParserRuleContext {
		public TerminalNode WAKE() { return getToken(SleepCommandsParser.WAKE, 0); }
		public TerminalNode ME() { return getToken(SleepCommandsParser.ME, 0); }
		public TerminalNode UP() { return getToken(SleepCommandsParser.UP, 0); }
		public TerminalNode IN() { return getToken(SleepCommandsParser.IN, 0); }
		public TerminalNode NUMBER() { return getToken(SleepCommandsParser.NUMBER, 0); }
		public TerminalNode TIMEUNIT() { return getToken(SleepCommandsParser.TIMEUNIT, 0); }
		public SetAlarmRelativeCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setAlarmRelativeCmd; }
	}

	public final SetAlarmRelativeCmdContext setAlarmRelativeCmd() throws RecognitionException {
		SetAlarmRelativeCmdContext _localctx = new SetAlarmRelativeCmdContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_setAlarmRelativeCmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			match(WAKE);
			setState(66);
			match(ME);
			setState(67);
			match(UP);
			setState(68);
			match(IN);
			setState(69);
			match(NUMBER);
			setState(70);
			match(TIMEUNIT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CancelAlarmCmdContext extends ParserRuleContext {
		public TerminalNode ALARM() { return getToken(SleepCommandsParser.ALARM, 0); }
		public TerminalNode CANCEL() { return getToken(SleepCommandsParser.CANCEL, 0); }
		public TerminalNode STOP() { return getToken(SleepCommandsParser.STOP, 0); }
		public TerminalNode MY() { return getToken(SleepCommandsParser.MY, 0); }
		public CancelAlarmCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cancelAlarmCmd; }
	}

	public final CancelAlarmCmdContext cancelAlarmCmd() throws RecognitionException {
		CancelAlarmCmdContext _localctx = new CancelAlarmCmdContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_cancelAlarmCmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			_la = _input.LA(1);
			if ( !(_la==CANCEL || _la==STOP) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==MY) {
				{
				setState(73);
				match(MY);
				}
			}

			setState(76);
			match(ALARM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SnoozeAlarmCmdContext extends ParserRuleContext {
		public TerminalNode SNOOZE() { return getToken(SleepCommandsParser.SNOOZE, 0); }
		public TerminalNode NUMBER() { return getToken(SleepCommandsParser.NUMBER, 0); }
		public TerminalNode TIMEUNIT() { return getToken(SleepCommandsParser.TIMEUNIT, 0); }
		public TerminalNode FOR() { return getToken(SleepCommandsParser.FOR, 0); }
		public SnoozeAlarmCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_snoozeAlarmCmd; }
	}

	public final SnoozeAlarmCmdContext snoozeAlarmCmd() throws RecognitionException {
		SnoozeAlarmCmdContext _localctx = new SnoozeAlarmCmdContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_snoozeAlarmCmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(SNOOZE);
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==FOR) {
				{
				setState(79);
				match(FOR);
				}
			}

			setState(82);
			match(NUMBER);
			setState(83);
			match(TIMEUNIT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LateAlertCmdContext extends ParserRuleContext {
		public TerminalNode WARN() { return getToken(SleepCommandsParser.WARN, 0); }
		public TerminalNode ME() { return getToken(SleepCommandsParser.ME, 0); }
		public TerminalNode IF() { return getToken(SleepCommandsParser.IF, 0); }
		public TerminalNode I() { return getToken(SleepCommandsParser.I, 0); }
		public TerminalNode AM() { return getToken(SleepCommandsParser.AM, 0); }
		public TerminalNode AWAKE() { return getToken(SleepCommandsParser.AWAKE, 0); }
		public TerminalNode AFTER() { return getToken(SleepCommandsParser.AFTER, 0); }
		public TerminalNode TIME() { return getToken(SleepCommandsParser.TIME, 0); }
		public LateAlertCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lateAlertCmd; }
	}

	public final LateAlertCmdContext lateAlertCmd() throws RecognitionException {
		LateAlertCmdContext _localctx = new LateAlertCmdContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_lateAlertCmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(WARN);
			setState(86);
			match(ME);
			setState(87);
			match(IF);
			setState(88);
			match(I);
			setState(89);
			match(AM);
			setState(90);
			match(AWAKE);
			setState(91);
			match(AFTER);
			setState(92);
			match(TIME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QueryCmdContext extends ParserRuleContext {
		public TerminalNode WHAT() { return getToken(SleepCommandsParser.WHAT, 0); }
		public TerminalNode TIMEWORD() { return getToken(SleepCommandsParser.TIMEWORD, 0); }
		public TerminalNode DID() { return getToken(SleepCommandsParser.DID, 0); }
		public TerminalNode I() { return getToken(SleepCommandsParser.I, 0); }
		public TerminalNode SLEEP() { return getToken(SleepCommandsParser.SLEEP, 0); }
		public TerminalNode YESTERDAY() { return getToken(SleepCommandsParser.YESTERDAY, 0); }
		public QueryCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_queryCmd; }
	}

	public final QueryCmdContext queryCmd() throws RecognitionException {
		QueryCmdContext _localctx = new QueryCmdContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_queryCmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(WHAT);
			setState(95);
			match(TIMEWORD);
			setState(96);
			match(DID);
			setState(97);
			match(I);
			setState(98);
			match(SLEEP);
			setState(99);
			match(YESTERDAY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConsistencyCmdContext extends ParserRuleContext {
		public TerminalNode MY() { return getToken(SleepCommandsParser.MY, 0); }
		public TerminalNode SLEEP() { return getToken(SleepCommandsParser.SLEEP, 0); }
		public TerminalNode SHOW() { return getToken(SleepCommandsParser.SHOW, 0); }
		public TerminalNode CHECK() { return getToken(SleepCommandsParser.CHECK, 0); }
		public TerminalNode CONSISTENCY() { return getToken(SleepCommandsParser.CONSISTENCY, 0); }
		public TerminalNode REGULARITY() { return getToken(SleepCommandsParser.REGULARITY, 0); }
		public TerminalNode HOW() { return getToken(SleepCommandsParser.HOW, 0); }
		public TerminalNode IS() { return getToken(SleepCommandsParser.IS, 0); }
		public TerminalNode CONSISTENT() { return getToken(SleepCommandsParser.CONSISTENT, 0); }
		public TerminalNode REGULAR() { return getToken(SleepCommandsParser.REGULAR, 0); }
		public ConsistencyCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_consistencyCmd; }
	}

	public final ConsistencyCmdContext consistencyCmd() throws RecognitionException {
		ConsistencyCmdContext _localctx = new ConsistencyCmdContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_consistencyCmd);
		int _la;
		try {
			setState(110);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SHOW:
			case CHECK:
				enterOuterAlt(_localctx, 1);
				{
				setState(101);
				_la = _input.LA(1);
				if ( !(_la==SHOW || _la==CHECK) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(102);
				match(MY);
				setState(103);
				match(SLEEP);
				setState(104);
				_la = _input.LA(1);
				if ( !(_la==CONSISTENCY || _la==REGULARITY) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case HOW:
				enterOuterAlt(_localctx, 2);
				{
				setState(105);
				match(HOW);
				setState(106);
				_la = _input.LA(1);
				if ( !(_la==CONSISTENT || _la==REGULAR) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(107);
				match(IS);
				setState(108);
				match(MY);
				setState(109);
				match(SLEEP);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QualityCmdContext extends ParserRuleContext {
		public TerminalNode MY() { return getToken(SleepCommandsParser.MY, 0); }
		public TerminalNode SLEEP() { return getToken(SleepCommandsParser.SLEEP, 0); }
		public TerminalNode QUALITY() { return getToken(SleepCommandsParser.QUALITY, 0); }
		public TerminalNode SHOW() { return getToken(SleepCommandsParser.SHOW, 0); }
		public TerminalNode CHECK() { return getToken(SleepCommandsParser.CHECK, 0); }
		public TerminalNode HOW() { return getToken(SleepCommandsParser.HOW, 0); }
		public TerminalNode IS() { return getToken(SleepCommandsParser.IS, 0); }
		public TerminalNode RATE() { return getToken(SleepCommandsParser.RATE, 0); }
		public TerminalNode ANALYZE() { return getToken(SleepCommandsParser.ANALYZE, 0); }
		public QualityCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qualityCmd; }
	}

	public final QualityCmdContext qualityCmd() throws RecognitionException {
		QualityCmdContext _localctx = new QualityCmdContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_qualityCmd);
		int _la;
		try {
			setState(124);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SHOW:
			case CHECK:
				enterOuterAlt(_localctx, 1);
				{
				setState(112);
				_la = _input.LA(1);
				if ( !(_la==SHOW || _la==CHECK) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(113);
				match(MY);
				setState(114);
				match(SLEEP);
				setState(115);
				match(QUALITY);
				}
				break;
			case HOW:
				enterOuterAlt(_localctx, 2);
				{
				setState(116);
				match(HOW);
				setState(117);
				match(IS);
				setState(118);
				match(MY);
				setState(119);
				match(SLEEP);
				setState(120);
				match(QUALITY);
				}
				break;
			case RATE:
			case ANALYZE:
				enterOuterAlt(_localctx, 3);
				{
				setState(121);
				_la = _input.LA(1);
				if ( !(_la==RATE || _la==ANALYZE) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(122);
				match(MY);
				setState(123);
				match(SLEEP);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AdviceCmdContext extends ParserRuleContext {
		public TerminalNode GIVE() { return getToken(SleepCommandsParser.GIVE, 0); }
		public TerminalNode ME() { return getToken(SleepCommandsParser.ME, 0); }
		public TerminalNode ADVICE() { return getToken(SleepCommandsParser.ADVICE, 0); }
		public TerminalNode TIPS() { return getToken(SleepCommandsParser.TIPS, 0); }
		public TerminalNode SUGGESTIONS() { return getToken(SleepCommandsParser.SUGGESTIONS, 0); }
		public TerminalNode SLEEP() { return getToken(SleepCommandsParser.SLEEP, 0); }
		public TerminalNode SHOW() { return getToken(SleepCommandsParser.SHOW, 0); }
		public TerminalNode GET() { return getToken(SleepCommandsParser.GET, 0); }
		public TerminalNode HOW() { return getToken(SleepCommandsParser.HOW, 0); }
		public TerminalNode CAN() { return getToken(SleepCommandsParser.CAN, 0); }
		public TerminalNode I() { return getToken(SleepCommandsParser.I, 0); }
		public TerminalNode BETTER() { return getToken(SleepCommandsParser.BETTER, 0); }
		public TerminalNode TO() { return getToken(SleepCommandsParser.TO, 0); }
		public TerminalNode IMPROVE() { return getToken(SleepCommandsParser.IMPROVE, 0); }
		public TerminalNode MY() { return getToken(SleepCommandsParser.MY, 0); }
		public AdviceCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_adviceCmd; }
	}

	public final AdviceCmdContext adviceCmd() throws RecognitionException {
		AdviceCmdContext _localctx = new AdviceCmdContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_adviceCmd);
		int _la;
		try {
			setState(147);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				match(GIVE);
				setState(127);
				match(ME);
				setState(129);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==SLEEP) {
					{
					setState(128);
					match(SLEEP);
					}
				}

				setState(131);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7696581394432L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(132);
				_la = _input.LA(1);
				if ( !(_la==SHOW || _la==GET) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(134);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==SLEEP) {
					{
					setState(133);
					match(SLEEP);
					}
				}

				setState(136);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7696581394432L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(137);
				match(HOW);
				setState(138);
				match(CAN);
				setState(139);
				match(I);
				setState(140);
				match(SLEEP);
				setState(141);
				match(BETTER);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(142);
				match(HOW);
				setState(143);
				match(TO);
				setState(144);
				match(IMPROVE);
				setState(145);
				match(MY);
				setState(146);
				match(SLEEP);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class HelpCmdContext extends ParserRuleContext {
		public TerminalNode HELP() { return getToken(SleepCommandsParser.HELP, 0); }
		public HelpCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_helpCmd; }
	}

	public final HelpCmdContext helpCmd() throws RecognitionException {
		HelpCmdContext _localctx = new HelpCmdContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_helpCmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			match(HELP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u00011\u0098\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0003\u0000\'\b\u0000\u0001\u0001\u0003\u0001*\b\u0001\u0001"+
		"\u0001\u0003\u0001-\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0003\u00024\b\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0003\u0002:\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0003\u0005K\b\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0003\u0006Q\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0003\to\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n}\b"+
		"\n\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u0082\b\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u0087\b\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u0094\b\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0000\u0000\r\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u0000\u0007\u0001\u0000\u001e\u001f\u0001\u0000"+
		"\u0015\u0016\u0001\u0000\u0018\u0019\u0001\u0000\u001b\u001c\u0001\u0000"+
		"$%\u0001\u0000(*\u0002\u0000\u0015\u0015\'\'\u00a3\u0000&\u0001\u0000"+
		"\u0000\u0000\u0002)\u0001\u0000\u0000\u0000\u00043\u0001\u0000\u0000\u0000"+
		"\u0006;\u0001\u0000\u0000\u0000\bA\u0001\u0000\u0000\u0000\nH\u0001\u0000"+
		"\u0000\u0000\fN\u0001\u0000\u0000\u0000\u000eU\u0001\u0000\u0000\u0000"+
		"\u0010^\u0001\u0000\u0000\u0000\u0012n\u0001\u0000\u0000\u0000\u0014|"+
		"\u0001\u0000\u0000\u0000\u0016\u0093\u0001\u0000\u0000\u0000\u0018\u0095"+
		"\u0001\u0000\u0000\u0000\u001a\'\u0003\u0002\u0001\u0000\u001b\'\u0003"+
		"\u0004\u0002\u0000\u001c\'\u0003\u0006\u0003\u0000\u001d\'\u0003\b\u0004"+
		"\u0000\u001e\'\u0003\n\u0005\u0000\u001f\'\u0003\f\u0006\u0000 \'\u0003"+
		"\u000e\u0007\u0000!\'\u0003\u0010\b\u0000\"\'\u0003\u0012\t\u0000#\'\u0003"+
		"\u0014\n\u0000$\'\u0003\u0016\u000b\u0000%\'\u0003\u0018\f\u0000&\u001a"+
		"\u0001\u0000\u0000\u0000&\u001b\u0001\u0000\u0000\u0000&\u001c\u0001\u0000"+
		"\u0000\u0000&\u001d\u0001\u0000\u0000\u0000&\u001e\u0001\u0000\u0000\u0000"+
		"&\u001f\u0001\u0000\u0000\u0000& \u0001\u0000\u0000\u0000&!\u0001\u0000"+
		"\u0000\u0000&\"\u0001\u0000\u0000\u0000&#\u0001\u0000\u0000\u0000&$\u0001"+
		"\u0000\u0000\u0000&%\u0001\u0000\u0000\u0000\'\u0001\u0001\u0000\u0000"+
		"\u0000(*\u0005\u0001\u0000\u0000)(\u0001\u0000\u0000\u0000)*\u0001\u0000"+
		"\u0000\u0000*,\u0001\u0000\u0000\u0000+-\u0005\u0002\u0000\u0000,+\u0001"+
		"\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000\u0000"+
		"./\u0005\u0004\u0000\u0000/0\u0005\u0005\u0000\u000001\u0005\u0006\u0000"+
		"\u00001\u0003\u0001\u0000\u0000\u000024\u0005\u0001\u0000\u000032\u0001"+
		"\u0000\u0000\u000034\u0001\u0000\u0000\u000049\u0001\u0000\u0000\u0000"+
		"56\u0005\u0007\u0000\u00006:\u0005\b\u0000\u000078\u0005\u0002\u0000\u0000"+
		"8:\u0005\t\u0000\u000095\u0001\u0000\u0000\u000097\u0001\u0000\u0000\u0000"+
		":\u0005\u0001\u0000\u0000\u0000;<\u0005\n\u0000\u0000<=\u0005\u000b\u0000"+
		"\u0000=>\u0005\b\u0000\u0000>?\u0005\f\u0000\u0000?@\u0005.\u0000\u0000"+
		"@\u0007\u0001\u0000\u0000\u0000AB\u0005\n\u0000\u0000BC\u0005\u000b\u0000"+
		"\u0000CD\u0005\b\u0000\u0000DE\u0005\r\u0000\u0000EF\u0005/\u0000\u0000"+
		"FG\u00050\u0000\u0000G\t\u0001\u0000\u0000\u0000HJ\u0007\u0000\u0000\u0000"+
		"IK\u0005\u0017\u0000\u0000JI\u0001\u0000\u0000\u0000JK\u0001\u0000\u0000"+
		"\u0000KL\u0001\u0000\u0000\u0000LM\u0005 \u0000\u0000M\u000b\u0001\u0000"+
		"\u0000\u0000NP\u0005!\u0000\u0000OQ\u0005\"\u0000\u0000PO\u0001\u0000"+
		"\u0000\u0000PQ\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000RS\u0005"+
		"/\u0000\u0000ST\u00050\u0000\u0000T\r\u0001\u0000\u0000\u0000UV\u0005"+
		"\u000e\u0000\u0000VW\u0005\u000b\u0000\u0000WX\u0005\u000f\u0000\u0000"+
		"XY\u0005\u0001\u0000\u0000YZ\u0005\u0002\u0000\u0000Z[\u0005\t\u0000\u0000"+
		"[\\\u0005\u0010\u0000\u0000\\]\u0005.\u0000\u0000]\u000f\u0001\u0000\u0000"+
		"\u0000^_\u0005\u0011\u0000\u0000_`\u0005\u0012\u0000\u0000`a\u0005\u0013"+
		"\u0000\u0000ab\u0005\u0001\u0000\u0000bc\u0005\u0006\u0000\u0000cd\u0005"+
		"\u0014\u0000\u0000d\u0011\u0001\u0000\u0000\u0000ef\u0007\u0001\u0000"+
		"\u0000fg\u0005\u0017\u0000\u0000gh\u0005\u0006\u0000\u0000ho\u0007\u0002"+
		"\u0000\u0000ij\u0005\u001a\u0000\u0000jk\u0007\u0003\u0000\u0000kl\u0005"+
		"\u0003\u0000\u0000lm\u0005\u0017\u0000\u0000mo\u0005\u0006\u0000\u0000"+
		"ne\u0001\u0000\u0000\u0000ni\u0001\u0000\u0000\u0000o\u0013\u0001\u0000"+
		"\u0000\u0000pq\u0007\u0001\u0000\u0000qr\u0005\u0017\u0000\u0000rs\u0005"+
		"\u0006\u0000\u0000s}\u0005#\u0000\u0000tu\u0005\u001a\u0000\u0000uv\u0005"+
		"\u0003\u0000\u0000vw\u0005\u0017\u0000\u0000wx\u0005\u0006\u0000\u0000"+
		"x}\u0005#\u0000\u0000yz\u0007\u0004\u0000\u0000z{\u0005\u0017\u0000\u0000"+
		"{}\u0005\u0006\u0000\u0000|p\u0001\u0000\u0000\u0000|t\u0001\u0000\u0000"+
		"\u0000|y\u0001\u0000\u0000\u0000}\u0015\u0001\u0000\u0000\u0000~\u007f"+
		"\u0005&\u0000\u0000\u007f\u0081\u0005\u000b\u0000\u0000\u0080\u0082\u0005"+
		"\u0006\u0000\u0000\u0081\u0080\u0001\u0000\u0000\u0000\u0081\u0082\u0001"+
		"\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0094\u0007"+
		"\u0005\u0000\u0000\u0084\u0086\u0007\u0006\u0000\u0000\u0085\u0087\u0005"+
		"\u0006\u0000\u0000\u0086\u0085\u0001\u0000\u0000\u0000\u0086\u0087\u0001"+
		"\u0000\u0000\u0000\u0087\u0088\u0001\u0000\u0000\u0000\u0088\u0094\u0007"+
		"\u0005\u0000\u0000\u0089\u008a\u0005\u001a\u0000\u0000\u008a\u008b\u0005"+
		"-\u0000\u0000\u008b\u008c\u0005\u0001\u0000\u0000\u008c\u008d\u0005\u0006"+
		"\u0000\u0000\u008d\u0094\u0005+\u0000\u0000\u008e\u008f\u0005\u001a\u0000"+
		"\u0000\u008f\u0090\u0005\u0005\u0000\u0000\u0090\u0091\u0005,\u0000\u0000"+
		"\u0091\u0092\u0005\u0017\u0000\u0000\u0092\u0094\u0005\u0006\u0000\u0000"+
		"\u0093~\u0001\u0000\u0000\u0000\u0093\u0084\u0001\u0000\u0000\u0000\u0093"+
		"\u0089\u0001\u0000\u0000\u0000\u0093\u008e\u0001\u0000\u0000\u0000\u0094"+
		"\u0017\u0001\u0000\u0000\u0000\u0095\u0096\u0005\u001d\u0000\u0000\u0096"+
		"\u0019\u0001\u0000\u0000\u0000\f&),39JPn|\u0081\u0086\u0093";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}