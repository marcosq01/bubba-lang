// Generated from d:\1000220000\8vo semestre\RepoCompis\bubbaGrammar.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class bubbaGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROG=1, MAIN=2, FLOAT=3, INT=4, STRING=5, PRINT=6, VARS=7, IF=8, ELSE=9, 
		DOT=10, COMMA=11, LPARENTHESIS=12, RPARENTHESIS=13, LBRACE=14, RBRACE=15, 
		LBRACKET=16, RBRACKET=17, SEMICOLON=18, ADD=19, MINUS=20, STAR=21, SLASH=22, 
		GREATER=23, GREATEREQ=24, LESS=25, LESSEQ=26, EQUAL=27, COLON=28, QUOTE=29, 
		AND=30, OR=31, NOT=32, EQEQUAL=33, NOTEQUAL=34, WHILE=35, FOR=36, STEP=37, 
		RETURN=38, CLASS=39, EXTENDS=40, FUNC=41, VOID=42, INPUT=43, TO=44, V_STRING=45, 
		ID=46, V_INT=47, V_FLOAT=48, WS=49;
	public static final int
		RULE_program = 0, RULE_paux = 1, RULE_paux2 = 2, RULE_paux3 = 3, RULE_main = 4, 
		RULE_whiler = 5, RULE_whileaux = 6, RULE_whileaux2 = 7, RULE_forr = 8, 
		RULE_foraux = 9, RULE_foraux2 = 10, RULE_foraux3 = 11, RULE_foraux4 = 12, 
		RULE_statement = 13, RULE_lid = 14, RULE_lidaux = 15, RULE_laux = 16, 
		RULE_laux2 = 17, RULE_maux = 18, RULE_cond = 19, RULE_condaux = 20, RULE_condaux2 = 21, 
		RULE_condaux3 = 22, RULE_assign = 23, RULE_assignaux = 24, RULE_factor = 25, 
		RULE_faux = 26, RULE_faux2 = 27, RULE_faux3 = 28, RULE_faux4 = 29, RULE_term = 30, 
		RULE_termaux = 31, RULE_exp = 32, RULE_expaux = 33, RULE_aexp = 34, RULE_aexpaux = 35, 
		RULE_aexps = 36, RULE_bexp = 37, RULE_bexpaux = 38, RULE_expression = 39, 
		RULE_expressionaux = 40, RULE_func = 41, RULE_funcaux = 42, RULE_classr = 43, 
		RULE_class_a = 44, RULE_class_b = 45, RULE_output = 46, RULE_output_a = 47, 
		RULE_inputr = 48, RULE_input_a = 49, RULE_body = 50, RULE_body_a = 51, 
		RULE_body_b = 52, RULE_varsr = 53, RULE_vars_a = 54, RULE_vars_b = 55, 
		RULE_args = 56, RULE_args_a = 57, RULE_type_simple = 58, RULE_call = 59, 
		RULE_call_a = 60, RULE_call_b = 61, RULE_params = 62, RULE_params_a = 63, 
		RULE_var_cte = 64, RULE_void = 65, RULE_void_a = 66, RULE_methods = 67;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "paux", "paux2", "paux3", "main", "whiler", "whileaux", "whileaux2", 
			"forr", "foraux", "foraux2", "foraux3", "foraux4", "statement", "lid", 
			"lidaux", "laux", "laux2", "maux", "cond", "condaux", "condaux2", "condaux3", 
			"assign", "assignaux", "factor", "faux", "faux2", "faux3", "faux4", "term", 
			"termaux", "exp", "expaux", "aexp", "aexpaux", "aexps", "bexp", "bexpaux", 
			"expression", "expressionaux", "func", "funcaux", "classr", "class_a", 
			"class_b", "output", "output_a", "inputr", "input_a", "body", "body_a", 
			"body_b", "varsr", "vars_a", "vars_b", "args", "args_a", "type_simple", 
			"call", "call_a", "call_b", "params", "params_a", "var_cte", "void", 
			"void_a", "methods"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'prog'", "'main'", "'float'", "'int'", "'string'", "'print'", 
			"'vars'", "'if'", "'else'", "'.'", "','", "'('", "')'", "'{'", "'}'", 
			"'['", "']'", "';'", "'+'", "'-'", "'*'", "'/'", "'>'", "'>='", "'<'", 
			"'<='", "'='", "':'", "'\"'", "'&&'", "'||'", "'!'", "'=='", "'!='", 
			"'while'", "'for'", "'step'", "'return'", "'class'", "'extends'", "'func'", 
			"'void'", "'input'", "'to'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROG", "MAIN", "FLOAT", "INT", "STRING", "PRINT", "VARS", "IF", 
			"ELSE", "DOT", "COMMA", "LPARENTHESIS", "RPARENTHESIS", "LBRACE", "RBRACE", 
			"LBRACKET", "RBRACKET", "SEMICOLON", "ADD", "MINUS", "STAR", "SLASH", 
			"GREATER", "GREATEREQ", "LESS", "LESSEQ", "EQUAL", "COLON", "QUOTE", 
			"AND", "OR", "NOT", "EQEQUAL", "NOTEQUAL", "WHILE", "FOR", "STEP", "RETURN", 
			"CLASS", "EXTENDS", "FUNC", "VOID", "INPUT", "TO", "V_STRING", "ID", 
			"V_INT", "V_FLOAT", "WS"
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
	public String getGrammarFileName() { return "bubbaGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public bubbaGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode PROG() { return getToken(bubbaGrammarParser.PROG, 0); }
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public TerminalNode COLON() { return getToken(bubbaGrammarParser.COLON, 0); }
		public PauxContext paux() {
			return getRuleContext(PauxContext.class,0);
		}
		public Paux2Context paux2() {
			return getRuleContext(Paux2Context.class,0);
		}
		public Paux3Context paux3() {
			return getRuleContext(Paux3Context.class,0);
		}
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			match(PROG);
			setState(137);
			match(ID);
			setState(138);
			match(COLON);
			setState(139);
			paux();
			setState(140);
			paux2();
			setState(141);
			paux3();
			setState(142);
			main();
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

	public static class PauxContext extends ParserRuleContext {
		public ClassrContext classr() {
			return getRuleContext(ClassrContext.class,0);
		}
		public PauxContext paux() {
			return getRuleContext(PauxContext.class,0);
		}
		public PauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paux; }
	}

	public final PauxContext paux() throws RecognitionException {
		PauxContext _localctx = new PauxContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_paux);
		try {
			setState(148);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CLASS:
				enterOuterAlt(_localctx, 1);
				{
				setState(144);
				classr();
				setState(145);
				paux();
				}
				break;
			case MAIN:
			case VARS:
			case FUNC:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class Paux2Context extends ParserRuleContext {
		public VarsrContext varsr() {
			return getRuleContext(VarsrContext.class,0);
		}
		public Paux2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paux2; }
	}

	public final Paux2Context paux2() throws RecognitionException {
		Paux2Context _localctx = new Paux2Context(_ctx, getState());
		enterRule(_localctx, 4, RULE_paux2);
		try {
			setState(152);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VARS:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				varsr();
				}
				break;
			case MAIN:
			case FUNC:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class Paux3Context extends ParserRuleContext {
		public MethodsContext methods() {
			return getRuleContext(MethodsContext.class,0);
		}
		public Paux3Context paux3() {
			return getRuleContext(Paux3Context.class,0);
		}
		public Paux3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paux3; }
	}

	public final Paux3Context paux3() throws RecognitionException {
		Paux3Context _localctx = new Paux3Context(_ctx, getState());
		enterRule(_localctx, 6, RULE_paux3);
		try {
			setState(158);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FUNC:
				enterOuterAlt(_localctx, 1);
				{
				setState(154);
				methods();
				setState(155);
				paux3();
				}
				break;
			case MAIN:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class MainContext extends ParserRuleContext {
		public TerminalNode MAIN() { return getToken(bubbaGrammarParser.MAIN, 0); }
		public TerminalNode LPARENTHESIS() { return getToken(bubbaGrammarParser.LPARENTHESIS, 0); }
		public TerminalNode RPARENTHESIS() { return getToken(bubbaGrammarParser.RPARENTHESIS, 0); }
		public TerminalNode LBRACE() { return getToken(bubbaGrammarParser.LBRACE, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(bubbaGrammarParser.RBRACE, 0); }
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_main);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			match(MAIN);
			setState(161);
			match(LPARENTHESIS);
			setState(162);
			match(RPARENTHESIS);
			setState(163);
			match(LBRACE);
			setState(164);
			body();
			setState(165);
			match(RBRACE);
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

	public static class WhilerContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(bubbaGrammarParser.WHILE, 0); }
		public TerminalNode LPARENTHESIS() { return getToken(bubbaGrammarParser.LPARENTHESIS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPARENTHESIS() { return getToken(bubbaGrammarParser.RPARENTHESIS, 0); }
		public TerminalNode LBRACE() { return getToken(bubbaGrammarParser.LBRACE, 0); }
		public WhileauxContext whileaux() {
			return getRuleContext(WhileauxContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(bubbaGrammarParser.RBRACE, 0); }
		public WhilerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whiler; }
	}

	public final WhilerContext whiler() throws RecognitionException {
		WhilerContext _localctx = new WhilerContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_whiler);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(WHILE);
			setState(168);
			match(LPARENTHESIS);
			setState(169);
			expression();
			setState(170);
			match(RPARENTHESIS);
			setState(171);
			match(LBRACE);
			setState(172);
			whileaux();
			setState(173);
			match(RBRACE);
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

	public static class WhileauxContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public Whileaux2Context whileaux2() {
			return getRuleContext(Whileaux2Context.class,0);
		}
		public WhileauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileaux; }
	}

	public final WhileauxContext whileaux() throws RecognitionException {
		WhileauxContext _localctx = new WhileauxContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_whileaux);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			statement();
			setState(176);
			whileaux2();
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

	public static class Whileaux2Context extends ParserRuleContext {
		public WhileauxContext whileaux() {
			return getRuleContext(WhileauxContext.class,0);
		}
		public Whileaux2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileaux2; }
	}

	public final Whileaux2Context whileaux2() throws RecognitionException {
		Whileaux2Context _localctx = new Whileaux2Context(_ctx, getState());
		enterRule(_localctx, 14, RULE_whileaux2);
		try {
			setState(180);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINT:
			case IF:
			case WHILE:
			case FOR:
			case INPUT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(178);
				whileaux();
				}
				break;
			case RBRACE:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class ForrContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(bubbaGrammarParser.FOR, 0); }
		public List<ForauxContext> foraux() {
			return getRuleContexts(ForauxContext.class);
		}
		public ForauxContext foraux(int i) {
			return getRuleContext(ForauxContext.class,i);
		}
		public TerminalNode TO() { return getToken(bubbaGrammarParser.TO, 0); }
		public Foraux2Context foraux2() {
			return getRuleContext(Foraux2Context.class,0);
		}
		public TerminalNode LBRACE() { return getToken(bubbaGrammarParser.LBRACE, 0); }
		public Foraux3Context foraux3() {
			return getRuleContext(Foraux3Context.class,0);
		}
		public TerminalNode RBRACE() { return getToken(bubbaGrammarParser.RBRACE, 0); }
		public ForrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forr; }
	}

	public final ForrContext forr() throws RecognitionException {
		ForrContext _localctx = new ForrContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_forr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(FOR);
			setState(183);
			foraux();
			setState(184);
			match(TO);
			setState(185);
			foraux();
			setState(186);
			foraux2();
			setState(187);
			match(LBRACE);
			setState(188);
			foraux3();
			setState(189);
			match(RBRACE);
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

	public static class ForauxContext extends ParserRuleContext {
		public TerminalNode V_INT() { return getToken(bubbaGrammarParser.V_INT, 0); }
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public ForauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_foraux; }
	}

	public final ForauxContext foraux() throws RecognitionException {
		ForauxContext _localctx = new ForauxContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_foraux);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==V_INT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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

	public static class Foraux2Context extends ParserRuleContext {
		public TerminalNode STEP() { return getToken(bubbaGrammarParser.STEP, 0); }
		public ForauxContext foraux() {
			return getRuleContext(ForauxContext.class,0);
		}
		public Foraux2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_foraux2; }
	}

	public final Foraux2Context foraux2() throws RecognitionException {
		Foraux2Context _localctx = new Foraux2Context(_ctx, getState());
		enterRule(_localctx, 20, RULE_foraux2);
		try {
			setState(196);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STEP:
				enterOuterAlt(_localctx, 1);
				{
				setState(193);
				match(STEP);
				setState(194);
				foraux();
				}
				break;
			case LBRACE:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class Foraux3Context extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public Foraux4Context foraux4() {
			return getRuleContext(Foraux4Context.class,0);
		}
		public Foraux3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_foraux3; }
	}

	public final Foraux3Context foraux3() throws RecognitionException {
		Foraux3Context _localctx = new Foraux3Context(_ctx, getState());
		enterRule(_localctx, 22, RULE_foraux3);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			statement();
			setState(199);
			foraux4();
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

	public static class Foraux4Context extends ParserRuleContext {
		public Foraux3Context foraux3() {
			return getRuleContext(Foraux3Context.class,0);
		}
		public Foraux4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_foraux4; }
	}

	public final Foraux4Context foraux4() throws RecognitionException {
		Foraux4Context _localctx = new Foraux4Context(_ctx, getState());
		enterRule(_localctx, 24, RULE_foraux4);
		try {
			setState(203);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINT:
			case IF:
			case WHILE:
			case FOR:
			case INPUT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(201);
				foraux3();
				}
				break;
			case RBRACE:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class StatementContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public ForrContext forr() {
			return getRuleContext(ForrContext.class,0);
		}
		public WhilerContext whiler() {
			return getRuleContext(WhilerContext.class,0);
		}
		public OutputContext output() {
			return getRuleContext(OutputContext.class,0);
		}
		public InputrContext inputr() {
			return getRuleContext(InputrContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_statement);
		try {
			setState(212);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(205);
				assign();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(206);
				call();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(207);
				cond();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(208);
				forr();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(209);
				whiler();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(210);
				output();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(211);
				inputr();
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

	public static class LidContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public LidauxContext lidaux() {
			return getRuleContext(LidauxContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(bubbaGrammarParser.SEMICOLON, 0); }
		public LidContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lid; }
	}

	public final LidContext lid() throws RecognitionException {
		LidContext _localctx = new LidContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_lid);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			match(ID);
			setState(215);
			lidaux();
			setState(216);
			match(SEMICOLON);
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

	public static class LidauxContext extends ParserRuleContext {
		public LauxContext laux() {
			return getRuleContext(LauxContext.class,0);
		}
		public Laux2Context laux2() {
			return getRuleContext(Laux2Context.class,0);
		}
		public LidauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lidaux; }
	}

	public final LidauxContext lidaux() throws RecognitionException {
		LidauxContext _localctx = new LidauxContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_lidaux);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			laux();
			setState(219);
			laux2();
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

	public static class LauxContext extends ParserRuleContext {
		public TerminalNode COMMA() { return getToken(bubbaGrammarParser.COMMA, 0); }
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public LauxContext laux() {
			return getRuleContext(LauxContext.class,0);
		}
		public LauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_laux; }
	}

	public final LauxContext laux() throws RecognitionException {
		LauxContext _localctx = new LauxContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_laux);
		try {
			setState(225);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(221);
				match(COMMA);
				setState(222);
				match(ID);
				setState(223);
				laux();
				}
				break;
			case LBRACKET:
			case SEMICOLON:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class Laux2Context extends ParserRuleContext {
		public TerminalNode LBRACKET() { return getToken(bubbaGrammarParser.LBRACKET, 0); }
		public TerminalNode V_INT() { return getToken(bubbaGrammarParser.V_INT, 0); }
		public MauxContext maux() {
			return getRuleContext(MauxContext.class,0);
		}
		public TerminalNode RBRACKET() { return getToken(bubbaGrammarParser.RBRACKET, 0); }
		public LauxContext laux() {
			return getRuleContext(LauxContext.class,0);
		}
		public Laux2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_laux2; }
	}

	public final Laux2Context laux2() throws RecognitionException {
		Laux2Context _localctx = new Laux2Context(_ctx, getState());
		enterRule(_localctx, 34, RULE_laux2);
		try {
			setState(234);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LBRACKET:
				enterOuterAlt(_localctx, 1);
				{
				setState(227);
				match(LBRACKET);
				setState(228);
				match(V_INT);
				setState(229);
				maux();
				setState(230);
				match(RBRACKET);
				setState(231);
				laux();
				}
				break;
			case SEMICOLON:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class MauxContext extends ParserRuleContext {
		public TerminalNode COMMA() { return getToken(bubbaGrammarParser.COMMA, 0); }
		public TerminalNode V_INT() { return getToken(bubbaGrammarParser.V_INT, 0); }
		public MauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_maux; }
	}

	public final MauxContext maux() throws RecognitionException {
		MauxContext _localctx = new MauxContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_maux);
		try {
			setState(239);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(236);
				match(COMMA);
				setState(237);
				match(V_INT);
				}
				break;
			case RBRACKET:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class CondContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(bubbaGrammarParser.IF, 0); }
		public TerminalNode LPARENTHESIS() { return getToken(bubbaGrammarParser.LPARENTHESIS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPARENTHESIS() { return getToken(bubbaGrammarParser.RPARENTHESIS, 0); }
		public TerminalNode LBRACE() { return getToken(bubbaGrammarParser.LBRACE, 0); }
		public CondauxContext condaux() {
			return getRuleContext(CondauxContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(bubbaGrammarParser.RBRACE, 0); }
		public Condaux3Context condaux3() {
			return getRuleContext(Condaux3Context.class,0);
		}
		public CondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond; }
	}

	public final CondContext cond() throws RecognitionException {
		CondContext _localctx = new CondContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_cond);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			match(IF);
			setState(242);
			match(LPARENTHESIS);
			setState(243);
			expression();
			setState(244);
			match(RPARENTHESIS);
			setState(245);
			match(LBRACE);
			setState(246);
			condaux();
			setState(247);
			match(RBRACE);
			setState(248);
			condaux3();
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

	public static class CondauxContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public Condaux2Context condaux2() {
			return getRuleContext(Condaux2Context.class,0);
		}
		public CondauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condaux; }
	}

	public final CondauxContext condaux() throws RecognitionException {
		CondauxContext _localctx = new CondauxContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_condaux);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			statement();
			setState(251);
			condaux2();
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

	public static class Condaux2Context extends ParserRuleContext {
		public CondauxContext condaux() {
			return getRuleContext(CondauxContext.class,0);
		}
		public Condaux2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condaux2; }
	}

	public final Condaux2Context condaux2() throws RecognitionException {
		Condaux2Context _localctx = new Condaux2Context(_ctx, getState());
		enterRule(_localctx, 42, RULE_condaux2);
		try {
			setState(255);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINT:
			case IF:
			case WHILE:
			case FOR:
			case INPUT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(253);
				condaux();
				}
				break;
			case RBRACE:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class Condaux3Context extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(bubbaGrammarParser.ELSE, 0); }
		public TerminalNode LBRACE() { return getToken(bubbaGrammarParser.LBRACE, 0); }
		public CondauxContext condaux() {
			return getRuleContext(CondauxContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(bubbaGrammarParser.RBRACE, 0); }
		public Condaux3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condaux3; }
	}

	public final Condaux3Context condaux3() throws RecognitionException {
		Condaux3Context _localctx = new Condaux3Context(_ctx, getState());
		enterRule(_localctx, 44, RULE_condaux3);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(ELSE);
			setState(258);
			match(LBRACE);
			setState(259);
			condaux();
			setState(260);
			match(RBRACE);
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

	public static class AssignContext extends ParserRuleContext {
		public AssignauxContext assignaux() {
			return getRuleContext(AssignauxContext.class,0);
		}
		public TerminalNode EQUAL() { return getToken(bubbaGrammarParser.EQUAL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(262);
			assignaux();
			setState(263);
			match(EQUAL);
			setState(264);
			expression();
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

	public static class AssignauxContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(bubbaGrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(bubbaGrammarParser.ID, i);
		}
		public TerminalNode DOT() { return getToken(bubbaGrammarParser.DOT, 0); }
		public AssignauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignaux; }
	}

	public final AssignauxContext assignaux() throws RecognitionException {
		AssignauxContext _localctx = new AssignauxContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_assignaux);
		try {
			setState(270);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(266);
				match(ID);
				setState(267);
				match(DOT);
				setState(268);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(269);
				match(ID);
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

	public static class FactorContext extends ParserRuleContext {
		public FauxContext faux() {
			return getRuleContext(FauxContext.class,0);
		}
		public Faux2Context faux2() {
			return getRuleContext(Faux2Context.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_factor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			faux();
			setState(273);
			faux2();
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

	public static class FauxContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(bubbaGrammarParser.ADD, 0); }
		public TerminalNode MINUS() { return getToken(bubbaGrammarParser.MINUS, 0); }
		public FauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_faux; }
	}

	public final FauxContext faux() throws RecognitionException {
		FauxContext _localctx = new FauxContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_faux);
		try {
			setState(278);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADD:
				enterOuterAlt(_localctx, 1);
				{
				setState(275);
				match(ADD);
				}
				break;
			case MINUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(276);
				match(MINUS);
				}
				break;
			case LPARENTHESIS:
			case V_STRING:
			case ID:
			case V_INT:
			case V_FLOAT:
				enterOuterAlt(_localctx, 3);
				{
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

	public static class Faux2Context extends ParserRuleContext {
		public Var_cteContext var_cte() {
			return getRuleContext(Var_cteContext.class,0);
		}
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public TerminalNode LPARENTHESIS() { return getToken(bubbaGrammarParser.LPARENTHESIS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPARENTHESIS() { return getToken(bubbaGrammarParser.RPARENTHESIS, 0); }
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public Faux3Context faux3() {
			return getRuleContext(Faux3Context.class,0);
		}
		public Faux2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_faux2; }
	}

	public final Faux2Context faux2() throws RecognitionException {
		Faux2Context _localctx = new Faux2Context(_ctx, getState());
		enterRule(_localctx, 54, RULE_faux2);
		try {
			setState(288);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(280);
				var_cte();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(281);
				call();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(282);
				match(LPARENTHESIS);
				setState(283);
				expression();
				setState(284);
				match(RPARENTHESIS);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(286);
				match(ID);
				setState(287);
				faux3();
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

	public static class Faux3Context extends ParserRuleContext {
		public TerminalNode LBRACKET() { return getToken(bubbaGrammarParser.LBRACKET, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Faux4Context faux4() {
			return getRuleContext(Faux4Context.class,0);
		}
		public TerminalNode RBRACKET() { return getToken(bubbaGrammarParser.RBRACKET, 0); }
		public TerminalNode DOT() { return getToken(bubbaGrammarParser.DOT, 0); }
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public Faux3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_faux3; }
	}

	public final Faux3Context faux3() throws RecognitionException {
		Faux3Context _localctx = new Faux3Context(_ctx, getState());
		enterRule(_localctx, 56, RULE_faux3);
		try {
			setState(298);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LBRACKET:
				enterOuterAlt(_localctx, 1);
				{
				setState(290);
				match(LBRACKET);
				setState(291);
				expression();
				setState(292);
				faux4();
				setState(293);
				match(RBRACKET);
				}
				break;
			case DOT:
				enterOuterAlt(_localctx, 2);
				{
				setState(295);
				match(DOT);
				setState(296);
				match(ID);
				}
				break;
			case PRINT:
			case IF:
			case COMMA:
			case RPARENTHESIS:
			case RBRACE:
			case RBRACKET:
			case SEMICOLON:
			case ADD:
			case MINUS:
			case STAR:
			case SLASH:
			case GREATER:
			case GREATEREQ:
			case LESS:
			case LESSEQ:
			case AND:
			case OR:
			case EQEQUAL:
			case NOTEQUAL:
			case WHILE:
			case FOR:
			case RETURN:
			case INPUT:
			case ID:
				enterOuterAlt(_localctx, 3);
				{
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

	public static class Faux4Context extends ParserRuleContext {
		public TerminalNode COMMA() { return getToken(bubbaGrammarParser.COMMA, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Faux4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_faux4; }
	}

	public final Faux4Context faux4() throws RecognitionException {
		Faux4Context _localctx = new Faux4Context(_ctx, getState());
		enterRule(_localctx, 58, RULE_faux4);
		try {
			setState(303);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(300);
				match(COMMA);
				setState(301);
				expression();
				}
				break;
			case RBRACKET:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class TermContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TermauxContext termaux() {
			return getRuleContext(TermauxContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_term);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(305);
			factor();
			setState(306);
			termaux();
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

	public static class TermauxContext extends ParserRuleContext {
		public TerminalNode STAR() { return getToken(bubbaGrammarParser.STAR, 0); }
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TerminalNode SLASH() { return getToken(bubbaGrammarParser.SLASH, 0); }
		public TermauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termaux; }
	}

	public final TermauxContext termaux() throws RecognitionException {
		TermauxContext _localctx = new TermauxContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_termaux);
		try {
			setState(313);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(308);
				match(STAR);
				setState(309);
				term();
				}
				break;
			case SLASH:
				enterOuterAlt(_localctx, 2);
				{
				setState(310);
				match(SLASH);
				setState(311);
				term();
				}
				break;
			case PRINT:
			case IF:
			case COMMA:
			case RPARENTHESIS:
			case RBRACE:
			case RBRACKET:
			case SEMICOLON:
			case ADD:
			case MINUS:
			case GREATER:
			case GREATEREQ:
			case LESS:
			case LESSEQ:
			case AND:
			case OR:
			case EQEQUAL:
			case NOTEQUAL:
			case WHILE:
			case FOR:
			case RETURN:
			case INPUT:
			case ID:
				enterOuterAlt(_localctx, 3);
				{
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

	public static class ExpContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public ExpauxContext expaux() {
			return getRuleContext(ExpauxContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(315);
			term();
			setState(316);
			expaux();
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

	public static class ExpauxContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(bubbaGrammarParser.ADD, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(bubbaGrammarParser.MINUS, 0); }
		public ExpauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expaux; }
	}

	public final ExpauxContext expaux() throws RecognitionException {
		ExpauxContext _localctx = new ExpauxContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_expaux);
		try {
			setState(323);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADD:
				enterOuterAlt(_localctx, 1);
				{
				setState(318);
				match(ADD);
				setState(319);
				exp();
				}
				break;
			case MINUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(320);
				match(MINUS);
				setState(321);
				exp();
				}
				break;
			case PRINT:
			case IF:
			case COMMA:
			case RPARENTHESIS:
			case RBRACE:
			case RBRACKET:
			case SEMICOLON:
			case GREATER:
			case GREATEREQ:
			case LESS:
			case LESSEQ:
			case AND:
			case OR:
			case EQEQUAL:
			case NOTEQUAL:
			case WHILE:
			case FOR:
			case RETURN:
			case INPUT:
			case ID:
				enterOuterAlt(_localctx, 3);
				{
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

	public static class AexpContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public AexpauxContext aexpaux() {
			return getRuleContext(AexpauxContext.class,0);
		}
		public AexpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aexp; }
	}

	public final AexpContext aexp() throws RecognitionException {
		AexpContext _localctx = new AexpContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_aexp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(325);
			exp();
			setState(326);
			aexpaux();
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

	public static class AexpauxContext extends ParserRuleContext {
		public AexpsContext aexps() {
			return getRuleContext(AexpsContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public AexpauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aexpaux; }
	}

	public final AexpauxContext aexpaux() throws RecognitionException {
		AexpauxContext _localctx = new AexpauxContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_aexpaux);
		try {
			setState(332);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GREATER:
			case GREATEREQ:
			case LESS:
			case LESSEQ:
			case EQEQUAL:
			case NOTEQUAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(328);
				aexps();
				setState(329);
				exp();
				}
				break;
			case PRINT:
			case IF:
			case COMMA:
			case RPARENTHESIS:
			case RBRACE:
			case RBRACKET:
			case SEMICOLON:
			case AND:
			case OR:
			case WHILE:
			case FOR:
			case RETURN:
			case INPUT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class AexpsContext extends ParserRuleContext {
		public TerminalNode GREATER() { return getToken(bubbaGrammarParser.GREATER, 0); }
		public TerminalNode LESS() { return getToken(bubbaGrammarParser.LESS, 0); }
		public TerminalNode EQEQUAL() { return getToken(bubbaGrammarParser.EQEQUAL, 0); }
		public TerminalNode NOTEQUAL() { return getToken(bubbaGrammarParser.NOTEQUAL, 0); }
		public TerminalNode GREATEREQ() { return getToken(bubbaGrammarParser.GREATEREQ, 0); }
		public TerminalNode LESSEQ() { return getToken(bubbaGrammarParser.LESSEQ, 0); }
		public AexpsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aexps; }
	}

	public final AexpsContext aexps() throws RecognitionException {
		AexpsContext _localctx = new AexpsContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_aexps);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(334);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GREATER) | (1L << GREATEREQ) | (1L << LESS) | (1L << LESSEQ) | (1L << EQEQUAL) | (1L << NOTEQUAL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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

	public static class BexpContext extends ParserRuleContext {
		public AexpContext aexp() {
			return getRuleContext(AexpContext.class,0);
		}
		public BexpauxContext bexpaux() {
			return getRuleContext(BexpauxContext.class,0);
		}
		public BexpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bexp; }
	}

	public final BexpContext bexp() throws RecognitionException {
		BexpContext _localctx = new BexpContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_bexp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(336);
			aexp();
			setState(337);
			bexpaux();
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

	public static class BexpauxContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(bubbaGrammarParser.AND, 0); }
		public BexpContext bexp() {
			return getRuleContext(BexpContext.class,0);
		}
		public BexpauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bexpaux; }
	}

	public final BexpauxContext bexpaux() throws RecognitionException {
		BexpauxContext _localctx = new BexpauxContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_bexpaux);
		try {
			setState(342);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AND:
				enterOuterAlt(_localctx, 1);
				{
				setState(339);
				match(AND);
				setState(340);
				bexp();
				}
				break;
			case PRINT:
			case IF:
			case COMMA:
			case RPARENTHESIS:
			case RBRACE:
			case RBRACKET:
			case SEMICOLON:
			case OR:
			case WHILE:
			case FOR:
			case RETURN:
			case INPUT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class ExpressionContext extends ParserRuleContext {
		public BexpContext bexp() {
			return getRuleContext(BexpContext.class,0);
		}
		public ExpressionauxContext expressionaux() {
			return getRuleContext(ExpressionauxContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(344);
			bexp();
			setState(345);
			expressionaux();
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

	public static class ExpressionauxContext extends ParserRuleContext {
		public TerminalNode OR() { return getToken(bubbaGrammarParser.OR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpressionauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionaux; }
	}

	public final ExpressionauxContext expressionaux() throws RecognitionException {
		ExpressionauxContext _localctx = new ExpressionauxContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_expressionaux);
		try {
			setState(350);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OR:
				enterOuterAlt(_localctx, 1);
				{
				setState(347);
				match(OR);
				setState(348);
				expression();
				}
				break;
			case PRINT:
			case IF:
			case COMMA:
			case RPARENTHESIS:
			case RBRACE:
			case RBRACKET:
			case SEMICOLON:
			case WHILE:
			case FOR:
			case RETURN:
			case INPUT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class FuncContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(bubbaGrammarParser.FUNC, 0); }
		public Type_simpleContext type_simple() {
			return getRuleContext(Type_simpleContext.class,0);
		}
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public TerminalNode LPARENTHESIS() { return getToken(bubbaGrammarParser.LPARENTHESIS, 0); }
		public FuncauxContext funcaux() {
			return getRuleContext(FuncauxContext.class,0);
		}
		public TerminalNode RPARENTHESIS() { return getToken(bubbaGrammarParser.RPARENTHESIS, 0); }
		public TerminalNode LBRACE() { return getToken(bubbaGrammarParser.LBRACE, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode RETURN() { return getToken(bubbaGrammarParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(bubbaGrammarParser.SEMICOLON, 0); }
		public TerminalNode RBRACE() { return getToken(bubbaGrammarParser.RBRACE, 0); }
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_func);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(352);
			match(FUNC);
			setState(353);
			type_simple();
			setState(354);
			match(ID);
			setState(355);
			match(LPARENTHESIS);
			setState(356);
			funcaux();
			setState(357);
			match(RPARENTHESIS);
			setState(358);
			match(LBRACE);
			setState(359);
			body();
			setState(360);
			match(RETURN);
			setState(361);
			expression();
			setState(362);
			match(SEMICOLON);
			setState(363);
			match(RBRACE);
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

	public static class FuncauxContext extends ParserRuleContext {
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public FuncauxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcaux; }
	}

	public final FuncauxContext funcaux() throws RecognitionException {
		FuncauxContext _localctx = new FuncauxContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_funcaux);
		try {
			setState(367);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FLOAT:
			case INT:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(365);
				args();
				}
				break;
			case RPARENTHESIS:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class ClassrContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(bubbaGrammarParser.CLASS, 0); }
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public Class_aContext class_a() {
			return getRuleContext(Class_aContext.class,0);
		}
		public TerminalNode LBRACKET() { return getToken(bubbaGrammarParser.LBRACKET, 0); }
		public VarsrContext varsr() {
			return getRuleContext(VarsrContext.class,0);
		}
		public Class_bContext class_b() {
			return getRuleContext(Class_bContext.class,0);
		}
		public TerminalNode RBRACKET() { return getToken(bubbaGrammarParser.RBRACKET, 0); }
		public TerminalNode SEMICOLON() { return getToken(bubbaGrammarParser.SEMICOLON, 0); }
		public ClassrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classr; }
	}

	public final ClassrContext classr() throws RecognitionException {
		ClassrContext _localctx = new ClassrContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_classr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(369);
			match(CLASS);
			setState(370);
			match(ID);
			setState(371);
			class_a();
			setState(372);
			match(LBRACKET);
			setState(373);
			varsr();
			setState(374);
			class_b();
			setState(375);
			match(RBRACKET);
			setState(376);
			match(SEMICOLON);
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

	public static class Class_aContext extends ParserRuleContext {
		public TerminalNode EXTENDS() { return getToken(bubbaGrammarParser.EXTENDS, 0); }
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public Class_aContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_a; }
	}

	public final Class_aContext class_a() throws RecognitionException {
		Class_aContext _localctx = new Class_aContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_class_a);
		try {
			setState(381);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EXTENDS:
				enterOuterAlt(_localctx, 1);
				{
				setState(378);
				match(EXTENDS);
				setState(379);
				match(ID);
				}
				break;
			case LBRACKET:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class Class_bContext extends ParserRuleContext {
		public MethodsContext methods() {
			return getRuleContext(MethodsContext.class,0);
		}
		public Class_bContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_b; }
	}

	public final Class_bContext class_b() throws RecognitionException {
		Class_bContext _localctx = new Class_bContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_class_b);
		try {
			setState(385);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FUNC:
				enterOuterAlt(_localctx, 1);
				{
				setState(383);
				methods();
				}
				break;
			case RBRACKET:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class OutputContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(bubbaGrammarParser.PRINT, 0); }
		public TerminalNode LPARENTHESIS() { return getToken(bubbaGrammarParser.LPARENTHESIS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Output_aContext output_a() {
			return getRuleContext(Output_aContext.class,0);
		}
		public TerminalNode RPARENTHESIS() { return getToken(bubbaGrammarParser.RPARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(bubbaGrammarParser.SEMICOLON, 0); }
		public OutputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_output; }
	}

	public final OutputContext output() throws RecognitionException {
		OutputContext _localctx = new OutputContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_output);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(387);
			match(PRINT);
			setState(388);
			match(LPARENTHESIS);
			setState(389);
			expression();
			setState(390);
			output_a();
			setState(391);
			match(RPARENTHESIS);
			setState(392);
			match(SEMICOLON);
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

	public static class Output_aContext extends ParserRuleContext {
		public TerminalNode COMMA() { return getToken(bubbaGrammarParser.COMMA, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Output_aContext output_a() {
			return getRuleContext(Output_aContext.class,0);
		}
		public Output_aContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_output_a; }
	}

	public final Output_aContext output_a() throws RecognitionException {
		Output_aContext _localctx = new Output_aContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_output_a);
		try {
			setState(399);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(394);
				match(COMMA);
				setState(395);
				expression();
				setState(396);
				output_a();
				}
				break;
			case RPARENTHESIS:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class InputrContext extends ParserRuleContext {
		public TerminalNode INPUT() { return getToken(bubbaGrammarParser.INPUT, 0); }
		public TerminalNode LPARENTHESIS() { return getToken(bubbaGrammarParser.LPARENTHESIS, 0); }
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public Input_aContext input_a() {
			return getRuleContext(Input_aContext.class,0);
		}
		public TerminalNode RPARENTHESIS() { return getToken(bubbaGrammarParser.RPARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(bubbaGrammarParser.SEMICOLON, 0); }
		public InputrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inputr; }
	}

	public final InputrContext inputr() throws RecognitionException {
		InputrContext _localctx = new InputrContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_inputr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(401);
			match(INPUT);
			setState(402);
			match(LPARENTHESIS);
			setState(403);
			match(ID);
			setState(404);
			input_a();
			setState(405);
			match(RPARENTHESIS);
			setState(406);
			match(SEMICOLON);
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

	public static class Input_aContext extends ParserRuleContext {
		public TerminalNode COMMA() { return getToken(bubbaGrammarParser.COMMA, 0); }
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public Input_aContext input_a() {
			return getRuleContext(Input_aContext.class,0);
		}
		public Input_aContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_input_a; }
	}

	public final Input_aContext input_a() throws RecognitionException {
		Input_aContext _localctx = new Input_aContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_input_a);
		try {
			setState(412);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(408);
				match(COMMA);
				setState(409);
				match(ID);
				setState(410);
				input_a();
				}
				break;
			case RPARENTHESIS:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class BodyContext extends ParserRuleContext {
		public Body_aContext body_a() {
			return getRuleContext(Body_aContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public Body_bContext body_b() {
			return getRuleContext(Body_bContext.class,0);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(414);
			body_a();
			setState(415);
			statement();
			setState(416);
			body_b();
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

	public static class Body_aContext extends ParserRuleContext {
		public VarsrContext varsr() {
			return getRuleContext(VarsrContext.class,0);
		}
		public Body_aContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body_a; }
	}

	public final Body_aContext body_a() throws RecognitionException {
		Body_aContext _localctx = new Body_aContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_body_a);
		try {
			setState(420);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VARS:
				enterOuterAlt(_localctx, 1);
				{
				setState(418);
				varsr();
				}
				break;
			case PRINT:
			case IF:
			case WHILE:
			case FOR:
			case INPUT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class Body_bContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public Body_bContext body_b() {
			return getRuleContext(Body_bContext.class,0);
		}
		public Body_bContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body_b; }
	}

	public final Body_bContext body_b() throws RecognitionException {
		Body_bContext _localctx = new Body_bContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_body_b);
		try {
			setState(426);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINT:
			case IF:
			case WHILE:
			case FOR:
			case INPUT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(422);
				statement();
				setState(423);
				body_b();
				}
				break;
			case RBRACE:
			case RETURN:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class VarsrContext extends ParserRuleContext {
		public TerminalNode VARS() { return getToken(bubbaGrammarParser.VARS, 0); }
		public Vars_aContext vars_a() {
			return getRuleContext(Vars_aContext.class,0);
		}
		public TerminalNode COLON() { return getToken(bubbaGrammarParser.COLON, 0); }
		public LidContext lid() {
			return getRuleContext(LidContext.class,0);
		}
		public Vars_bContext vars_b() {
			return getRuleContext(Vars_bContext.class,0);
		}
		public VarsrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varsr; }
	}

	public final VarsrContext varsr() throws RecognitionException {
		VarsrContext _localctx = new VarsrContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_varsr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(428);
			match(VARS);
			setState(429);
			vars_a();
			setState(430);
			match(COLON);
			setState(431);
			lid();
			setState(432);
			vars_b();
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

	public static class Vars_aContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public Type_simpleContext type_simple() {
			return getRuleContext(Type_simpleContext.class,0);
		}
		public Vars_aContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars_a; }
	}

	public final Vars_aContext vars_a() throws RecognitionException {
		Vars_aContext _localctx = new Vars_aContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_vars_a);
		try {
			setState(436);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(434);
				match(ID);
				}
				break;
			case FLOAT:
			case INT:
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(435);
				type_simple();
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

	public static class Vars_bContext extends ParserRuleContext {
		public VarsrContext varsr() {
			return getRuleContext(VarsrContext.class,0);
		}
		public Vars_bContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars_b; }
	}

	public final Vars_bContext vars_b() throws RecognitionException {
		Vars_bContext _localctx = new Vars_bContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_vars_b);
		try {
			setState(440);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VARS:
				enterOuterAlt(_localctx, 1);
				{
				setState(438);
				varsr();
				}
				break;
			case MAIN:
			case PRINT:
			case IF:
			case RBRACKET:
			case WHILE:
			case FOR:
			case FUNC:
			case INPUT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class ArgsContext extends ParserRuleContext {
		public Type_simpleContext type_simple() {
			return getRuleContext(Type_simpleContext.class,0);
		}
		public TerminalNode COLON() { return getToken(bubbaGrammarParser.COLON, 0); }
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public Args_aContext args_a() {
			return getRuleContext(Args_aContext.class,0);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_args);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(442);
			type_simple();
			setState(443);
			match(COLON);
			setState(444);
			match(ID);
			setState(445);
			args_a();
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

	public static class Args_aContext extends ParserRuleContext {
		public TerminalNode COMMA() { return getToken(bubbaGrammarParser.COMMA, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public Args_aContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args_a; }
	}

	public final Args_aContext args_a() throws RecognitionException {
		Args_aContext _localctx = new Args_aContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_args_a);
		try {
			setState(450);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(447);
				match(COMMA);
				setState(448);
				args();
				}
				break;
			case RPARENTHESIS:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class Type_simpleContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(bubbaGrammarParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(bubbaGrammarParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(bubbaGrammarParser.STRING, 0); }
		public Type_simpleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_simple; }
	}

	public final Type_simpleContext type_simple() throws RecognitionException {
		Type_simpleContext _localctx = new Type_simpleContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_type_simple);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(452);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FLOAT) | (1L << INT) | (1L << STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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

	public static class CallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public Call_aContext call_a() {
			return getRuleContext(Call_aContext.class,0);
		}
		public TerminalNode LPARENTHESIS() { return getToken(bubbaGrammarParser.LPARENTHESIS, 0); }
		public Call_bContext call_b() {
			return getRuleContext(Call_bContext.class,0);
		}
		public TerminalNode RPARENTHESIS() { return getToken(bubbaGrammarParser.RPARENTHESIS, 0); }
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(454);
			match(ID);
			setState(455);
			call_a();
			setState(456);
			match(LPARENTHESIS);
			setState(457);
			call_b();
			setState(458);
			match(RPARENTHESIS);
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

	public static class Call_aContext extends ParserRuleContext {
		public TerminalNode DOT() { return getToken(bubbaGrammarParser.DOT, 0); }
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public Call_aContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_a; }
	}

	public final Call_aContext call_a() throws RecognitionException {
		Call_aContext _localctx = new Call_aContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_call_a);
		try {
			setState(463);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(460);
				match(DOT);
				setState(461);
				match(ID);
				}
				break;
			case LPARENTHESIS:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class Call_bContext extends ParserRuleContext {
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public Call_bContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_b; }
	}

	public final Call_bContext call_b() throws RecognitionException {
		Call_bContext _localctx = new Call_bContext(_ctx, getState());
		enterRule(_localctx, 122, RULE_call_b);
		try {
			setState(467);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPARENTHESIS:
			case ADD:
			case MINUS:
			case V_STRING:
			case ID:
			case V_INT:
			case V_FLOAT:
				enterOuterAlt(_localctx, 1);
				{
				setState(465);
				params();
				}
				break;
			case RPARENTHESIS:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class ParamsContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Params_aContext params_a() {
			return getRuleContext(Params_aContext.class,0);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 124, RULE_params);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(469);
			expression();
			setState(470);
			params_a();
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

	public static class Params_aContext extends ParserRuleContext {
		public TerminalNode COMMA() { return getToken(bubbaGrammarParser.COMMA, 0); }
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public Params_aContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params_a; }
	}

	public final Params_aContext params_a() throws RecognitionException {
		Params_aContext _localctx = new Params_aContext(_ctx, getState());
		enterRule(_localctx, 126, RULE_params_a);
		try {
			setState(475);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(472);
				match(COMMA);
				setState(473);
				params();
				}
				break;
			case RPARENTHESIS:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class Var_cteContext extends ParserRuleContext {
		public TerminalNode V_INT() { return getToken(bubbaGrammarParser.V_INT, 0); }
		public TerminalNode V_FLOAT() { return getToken(bubbaGrammarParser.V_FLOAT, 0); }
		public TerminalNode V_STRING() { return getToken(bubbaGrammarParser.V_STRING, 0); }
		public Var_cteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_cte; }
	}

	public final Var_cteContext var_cte() throws RecognitionException {
		Var_cteContext _localctx = new Var_cteContext(_ctx, getState());
		enterRule(_localctx, 128, RULE_var_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(477);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << V_STRING) | (1L << V_INT) | (1L << V_FLOAT))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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

	public static class VoidContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(bubbaGrammarParser.FUNC, 0); }
		public TerminalNode VOID() { return getToken(bubbaGrammarParser.VOID, 0); }
		public TerminalNode ID() { return getToken(bubbaGrammarParser.ID, 0); }
		public TerminalNode LPARENTHESIS() { return getToken(bubbaGrammarParser.LPARENTHESIS, 0); }
		public Void_aContext void_a() {
			return getRuleContext(Void_aContext.class,0);
		}
		public TerminalNode RPARENTHESIS() { return getToken(bubbaGrammarParser.RPARENTHESIS, 0); }
		public TerminalNode LBRACE() { return getToken(bubbaGrammarParser.LBRACE, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(bubbaGrammarParser.RBRACE, 0); }
		public VoidContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_void; }
	}

	public final VoidContext void() throws RecognitionException {
		VoidContext _localctx = new VoidContext(_ctx, getState());
		enterRule(_localctx, 130, RULE_void);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(479);
			match(FUNC);
			setState(480);
			match(VOID);
			setState(481);
			match(ID);
			setState(482);
			match(LPARENTHESIS);
			setState(483);
			void_a();
			setState(484);
			match(RPARENTHESIS);
			setState(485);
			match(LBRACE);
			setState(486);
			body();
			setState(487);
			match(RBRACE);
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

	public static class Void_aContext extends ParserRuleContext {
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public Void_aContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_void_a; }
	}

	public final Void_aContext void_a() throws RecognitionException {
		Void_aContext _localctx = new Void_aContext(_ctx, getState());
		enterRule(_localctx, 132, RULE_void_a);
		try {
			setState(491);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FLOAT:
			case INT:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(489);
				args();
				}
				break;
			case RPARENTHESIS:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class MethodsContext extends ParserRuleContext {
		public VoidContext void() {
			return getRuleContext(VoidContext.class,0);
		}
		public MethodsContext methods() {
			return getRuleContext(MethodsContext.class,0);
		}
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public MethodsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methods; }
	}

	public final MethodsContext methods() throws RecognitionException {
		MethodsContext _localctx = new MethodsContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_methods);
		try {
			setState(499);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(493);
				void();
				setState(494);
				methods();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(496);
				func();
				setState(497);
				methods();
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63\u01f8\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0097\n\3\3\4\3\4\5\4\u009b\n\4\3\5\3\5"+
		"\3\5\3\5\5\5\u00a1\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\5\t\u00b7\n\t\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\5\f\u00c7\n\f\3\r\3\r\3\r\3\16\3\16"+
		"\5\16\u00ce\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00d7\n\17\3"+
		"\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00e4\n\22"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00ed\n\23\3\24\3\24\3\24\5\24"+
		"\u00f2\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26"+
		"\3\27\3\27\5\27\u0102\n\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31"+
		"\3\32\3\32\3\32\3\32\5\32\u0111\n\32\3\33\3\33\3\33\3\34\3\34\3\34\5\34"+
		"\u0119\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0123\n\35\3"+
		"\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u012d\n\36\3\37\3\37\3\37"+
		"\5\37\u0132\n\37\3 \3 \3 \3!\3!\3!\3!\3!\5!\u013c\n!\3\"\3\"\3\"\3#\3"+
		"#\3#\3#\3#\5#\u0146\n#\3$\3$\3$\3%\3%\3%\3%\5%\u014f\n%\3&\3&\3\'\3\'"+
		"\3\'\3(\3(\3(\5(\u0159\n(\3)\3)\3)\3*\3*\3*\5*\u0161\n*\3+\3+\3+\3+\3"+
		"+\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\5,\u0172\n,\3-\3-\3-\3-\3-\3-\3-\3-\3"+
		"-\3.\3.\3.\5.\u0180\n.\3/\3/\5/\u0184\n/\3\60\3\60\3\60\3\60\3\60\3\60"+
		"\3\60\3\61\3\61\3\61\3\61\3\61\5\61\u0192\n\61\3\62\3\62\3\62\3\62\3\62"+
		"\3\62\3\62\3\63\3\63\3\63\3\63\5\63\u019f\n\63\3\64\3\64\3\64\3\64\3\65"+
		"\3\65\5\65\u01a7\n\65\3\66\3\66\3\66\3\66\5\66\u01ad\n\66\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\38\38\58\u01b7\n8\39\39\59\u01bb\n9\3:\3:\3:\3:\3:"+
		"\3;\3;\3;\5;\u01c5\n;\3<\3<\3=\3=\3=\3=\3=\3=\3>\3>\3>\5>\u01d2\n>\3?"+
		"\3?\5?\u01d6\n?\3@\3@\3@\3A\3A\3A\5A\u01de\nA\3B\3B\3C\3C\3C\3C\3C\3C"+
		"\3C\3C\3C\3C\3D\3D\5D\u01ee\nD\3E\3E\3E\3E\3E\3E\5E\u01f6\nE\3E\2\2F\2"+
		"\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL"+
		"NPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\2\6\3\2\60\61"+
		"\4\2\31\34#$\3\2\5\7\4\2//\61\62\2\u01e2\2\u008a\3\2\2\2\4\u0096\3\2\2"+
		"\2\6\u009a\3\2\2\2\b\u00a0\3\2\2\2\n\u00a2\3\2\2\2\f\u00a9\3\2\2\2\16"+
		"\u00b1\3\2\2\2\20\u00b6\3\2\2\2\22\u00b8\3\2\2\2\24\u00c1\3\2\2\2\26\u00c6"+
		"\3\2\2\2\30\u00c8\3\2\2\2\32\u00cd\3\2\2\2\34\u00d6\3\2\2\2\36\u00d8\3"+
		"\2\2\2 \u00dc\3\2\2\2\"\u00e3\3\2\2\2$\u00ec\3\2\2\2&\u00f1\3\2\2\2(\u00f3"+
		"\3\2\2\2*\u00fc\3\2\2\2,\u0101\3\2\2\2.\u0103\3\2\2\2\60\u0108\3\2\2\2"+
		"\62\u0110\3\2\2\2\64\u0112\3\2\2\2\66\u0118\3\2\2\28\u0122\3\2\2\2:\u012c"+
		"\3\2\2\2<\u0131\3\2\2\2>\u0133\3\2\2\2@\u013b\3\2\2\2B\u013d\3\2\2\2D"+
		"\u0145\3\2\2\2F\u0147\3\2\2\2H\u014e\3\2\2\2J\u0150\3\2\2\2L\u0152\3\2"+
		"\2\2N\u0158\3\2\2\2P\u015a\3\2\2\2R\u0160\3\2\2\2T\u0162\3\2\2\2V\u0171"+
		"\3\2\2\2X\u0173\3\2\2\2Z\u017f\3\2\2\2\\\u0183\3\2\2\2^\u0185\3\2\2\2"+
		"`\u0191\3\2\2\2b\u0193\3\2\2\2d\u019e\3\2\2\2f\u01a0\3\2\2\2h\u01a6\3"+
		"\2\2\2j\u01ac\3\2\2\2l\u01ae\3\2\2\2n\u01b6\3\2\2\2p\u01ba\3\2\2\2r\u01bc"+
		"\3\2\2\2t\u01c4\3\2\2\2v\u01c6\3\2\2\2x\u01c8\3\2\2\2z\u01d1\3\2\2\2|"+
		"\u01d5\3\2\2\2~\u01d7\3\2\2\2\u0080\u01dd\3\2\2\2\u0082\u01df\3\2\2\2"+
		"\u0084\u01e1\3\2\2\2\u0086\u01ed\3\2\2\2\u0088\u01f5\3\2\2\2\u008a\u008b"+
		"\7\3\2\2\u008b\u008c\7\60\2\2\u008c\u008d\7\36\2\2\u008d\u008e\5\4\3\2"+
		"\u008e\u008f\5\6\4\2\u008f\u0090\5\b\5\2\u0090\u0091\5\n\6\2\u0091\3\3"+
		"\2\2\2\u0092\u0093\5X-\2\u0093\u0094\5\4\3\2\u0094\u0097\3\2\2\2\u0095"+
		"\u0097\3\2\2\2\u0096\u0092\3\2\2\2\u0096\u0095\3\2\2\2\u0097\5\3\2\2\2"+
		"\u0098\u009b\5l\67\2\u0099\u009b\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u0099"+
		"\3\2\2\2\u009b\7\3\2\2\2\u009c\u009d\5\u0088E\2\u009d\u009e\5\b\5\2\u009e"+
		"\u00a1\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009c\3\2\2\2\u00a0\u009f\3\2"+
		"\2\2\u00a1\t\3\2\2\2\u00a2\u00a3\7\4\2\2\u00a3\u00a4\7\16\2\2\u00a4\u00a5"+
		"\7\17\2\2\u00a5\u00a6\7\20\2\2\u00a6\u00a7\5f\64\2\u00a7\u00a8\7\21\2"+
		"\2\u00a8\13\3\2\2\2\u00a9\u00aa\7%\2\2\u00aa\u00ab\7\16\2\2\u00ab\u00ac"+
		"\5P)\2\u00ac\u00ad\7\17\2\2\u00ad\u00ae\7\20\2\2\u00ae\u00af\5\16\b\2"+
		"\u00af\u00b0\7\21\2\2\u00b0\r\3\2\2\2\u00b1\u00b2\5\34\17\2\u00b2\u00b3"+
		"\5\20\t\2\u00b3\17\3\2\2\2\u00b4\u00b7\5\16\b\2\u00b5\u00b7\3\2\2\2\u00b6"+
		"\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\21\3\2\2\2\u00b8\u00b9\7&\2\2"+
		"\u00b9\u00ba\5\24\13\2\u00ba\u00bb\7.\2\2\u00bb\u00bc\5\24\13\2\u00bc"+
		"\u00bd\5\26\f\2\u00bd\u00be\7\20\2\2\u00be\u00bf\5\30\r\2\u00bf\u00c0"+
		"\7\21\2\2\u00c0\23\3\2\2\2\u00c1\u00c2\t\2\2\2\u00c2\25\3\2\2\2\u00c3"+
		"\u00c4\7\'\2\2\u00c4\u00c7\5\24\13\2\u00c5\u00c7\3\2\2\2\u00c6\u00c3\3"+
		"\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\27\3\2\2\2\u00c8\u00c9\5\34\17\2\u00c9"+
		"\u00ca\5\32\16\2\u00ca\31\3\2\2\2\u00cb\u00ce\5\30\r\2\u00cc\u00ce\3\2"+
		"\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\33\3\2\2\2\u00cf\u00d7"+
		"\5\60\31\2\u00d0\u00d7\5x=\2\u00d1\u00d7\5(\25\2\u00d2\u00d7\5\22\n\2"+
		"\u00d3\u00d7\5\f\7\2\u00d4\u00d7\5^\60\2\u00d5\u00d7\5b\62\2\u00d6\u00cf"+
		"\3\2\2\2\u00d6\u00d0\3\2\2\2\u00d6\u00d1\3\2\2\2\u00d6\u00d2\3\2\2\2\u00d6"+
		"\u00d3\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\35\3\2\2"+
		"\2\u00d8\u00d9\7\60\2\2\u00d9\u00da\5 \21\2\u00da\u00db\7\24\2\2\u00db"+
		"\37\3\2\2\2\u00dc\u00dd\5\"\22\2\u00dd\u00de\5$\23\2\u00de!\3\2\2\2\u00df"+
		"\u00e0\7\r\2\2\u00e0\u00e1\7\60\2\2\u00e1\u00e4\5\"\22\2\u00e2\u00e4\3"+
		"\2\2\2\u00e3\u00df\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4#\3\2\2\2\u00e5\u00e6"+
		"\7\22\2\2\u00e6\u00e7\7\61\2\2\u00e7\u00e8\5&\24\2\u00e8\u00e9\7\23\2"+
		"\2\u00e9\u00ea\5\"\22\2\u00ea\u00ed\3\2\2\2\u00eb\u00ed\3\2\2\2\u00ec"+
		"\u00e5\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed%\3\2\2\2\u00ee\u00ef\7\r\2\2"+
		"\u00ef\u00f2\7\61\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00ee\3\2\2\2\u00f1\u00f0"+
		"\3\2\2\2\u00f2\'\3\2\2\2\u00f3\u00f4\7\n\2\2\u00f4\u00f5\7\16\2\2\u00f5"+
		"\u00f6\5P)\2\u00f6\u00f7\7\17\2\2\u00f7\u00f8\7\20\2\2\u00f8\u00f9\5*"+
		"\26\2\u00f9\u00fa\7\21\2\2\u00fa\u00fb\5.\30\2\u00fb)\3\2\2\2\u00fc\u00fd"+
		"\5\34\17\2\u00fd\u00fe\5,\27\2\u00fe+\3\2\2\2\u00ff\u0102\5*\26\2\u0100"+
		"\u0102\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102-\3\2\2\2"+
		"\u0103\u0104\7\13\2\2\u0104\u0105\7\20\2\2\u0105\u0106\5*\26\2\u0106\u0107"+
		"\7\21\2\2\u0107/\3\2\2\2\u0108\u0109\5\62\32\2\u0109\u010a\7\35\2\2\u010a"+
		"\u010b\5P)\2\u010b\61\3\2\2\2\u010c\u010d\7\60\2\2\u010d\u010e\7\f\2\2"+
		"\u010e\u0111\7\60\2\2\u010f\u0111\7\60\2\2\u0110\u010c\3\2\2\2\u0110\u010f"+
		"\3\2\2\2\u0111\63\3\2\2\2\u0112\u0113\5\66\34\2\u0113\u0114\58\35\2\u0114"+
		"\65\3\2\2\2\u0115\u0119\7\25\2\2\u0116\u0119\7\26\2\2\u0117\u0119\3\2"+
		"\2\2\u0118\u0115\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0117\3\2\2\2\u0119"+
		"\67\3\2\2\2\u011a\u0123\5\u0082B\2\u011b\u0123\5x=\2\u011c\u011d\7\16"+
		"\2\2\u011d\u011e\5P)\2\u011e\u011f\7\17\2\2\u011f\u0123\3\2\2\2\u0120"+
		"\u0121\7\60\2\2\u0121\u0123\5:\36\2\u0122\u011a\3\2\2\2\u0122\u011b\3"+
		"\2\2\2\u0122\u011c\3\2\2\2\u0122\u0120\3\2\2\2\u01239\3\2\2\2\u0124\u0125"+
		"\7\22\2\2\u0125\u0126\5P)\2\u0126\u0127\5<\37\2\u0127\u0128\7\23\2\2\u0128"+
		"\u012d\3\2\2\2\u0129\u012a\7\f\2\2\u012a\u012d\7\60\2\2\u012b\u012d\3"+
		"\2\2\2\u012c\u0124\3\2\2\2\u012c\u0129\3\2\2\2\u012c\u012b\3\2\2\2\u012d"+
		";\3\2\2\2\u012e\u012f\7\r\2\2\u012f\u0132\5P)\2\u0130\u0132\3\2\2\2\u0131"+
		"\u012e\3\2\2\2\u0131\u0130\3\2\2\2\u0132=\3\2\2\2\u0133\u0134\5\64\33"+
		"\2\u0134\u0135\5@!\2\u0135?\3\2\2\2\u0136\u0137\7\27\2\2\u0137\u013c\5"+
		"> \2\u0138\u0139\7\30\2\2\u0139\u013c\5> \2\u013a\u013c\3\2\2\2\u013b"+
		"\u0136\3\2\2\2\u013b\u0138\3\2\2\2\u013b\u013a\3\2\2\2\u013cA\3\2\2\2"+
		"\u013d\u013e\5> \2\u013e\u013f\5D#\2\u013fC\3\2\2\2\u0140\u0141\7\25\2"+
		"\2\u0141\u0146\5B\"\2\u0142\u0143\7\26\2\2\u0143\u0146\5B\"\2\u0144\u0146"+
		"\3\2\2\2\u0145\u0140\3\2\2\2\u0145\u0142\3\2\2\2\u0145\u0144\3\2\2\2\u0146"+
		"E\3\2\2\2\u0147\u0148\5B\"\2\u0148\u0149\5H%\2\u0149G\3\2\2\2\u014a\u014b"+
		"\5J&\2\u014b\u014c\5B\"\2\u014c\u014f\3\2\2\2\u014d\u014f\3\2\2\2\u014e"+
		"\u014a\3\2\2\2\u014e\u014d\3\2\2\2\u014fI\3\2\2\2\u0150\u0151\t\3\2\2"+
		"\u0151K\3\2\2\2\u0152\u0153\5F$\2\u0153\u0154\5N(\2\u0154M\3\2\2\2\u0155"+
		"\u0156\7 \2\2\u0156\u0159\5L\'\2\u0157\u0159\3\2\2\2\u0158\u0155\3\2\2"+
		"\2\u0158\u0157\3\2\2\2\u0159O\3\2\2\2\u015a\u015b\5L\'\2\u015b\u015c\5"+
		"R*\2\u015cQ\3\2\2\2\u015d\u015e\7!\2\2\u015e\u0161\5P)\2\u015f\u0161\3"+
		"\2\2\2\u0160\u015d\3\2\2\2\u0160\u015f\3\2\2\2\u0161S\3\2\2\2\u0162\u0163"+
		"\7+\2\2\u0163\u0164\5v<\2\u0164\u0165\7\60\2\2\u0165\u0166\7\16\2\2\u0166"+
		"\u0167\5V,\2\u0167\u0168\7\17\2\2\u0168\u0169\7\20\2\2\u0169\u016a\5f"+
		"\64\2\u016a\u016b\7(\2\2\u016b\u016c\5P)\2\u016c\u016d\7\24\2\2\u016d"+
		"\u016e\7\21\2\2\u016eU\3\2\2\2\u016f\u0172\5r:\2\u0170\u0172\3\2\2\2\u0171"+
		"\u016f\3\2\2\2\u0171\u0170\3\2\2\2\u0172W\3\2\2\2\u0173\u0174\7)\2\2\u0174"+
		"\u0175\7\60\2\2\u0175\u0176\5Z.\2\u0176\u0177\7\22\2\2\u0177\u0178\5l"+
		"\67\2\u0178\u0179\5\\/\2\u0179\u017a\7\23\2\2\u017a\u017b\7\24\2\2\u017b"+
		"Y\3\2\2\2\u017c\u017d\7*\2\2\u017d\u0180\7\60\2\2\u017e\u0180\3\2\2\2"+
		"\u017f\u017c\3\2\2\2\u017f\u017e\3\2\2\2\u0180[\3\2\2\2\u0181\u0184\5"+
		"\u0088E\2\u0182\u0184\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0182\3\2\2\2"+
		"\u0184]\3\2\2\2\u0185\u0186\7\b\2\2\u0186\u0187\7\16\2\2\u0187\u0188\5"+
		"P)\2\u0188\u0189\5`\61\2\u0189\u018a\7\17\2\2\u018a\u018b\7\24\2\2\u018b"+
		"_\3\2\2\2\u018c\u018d\7\r\2\2\u018d\u018e\5P)\2\u018e\u018f\5`\61\2\u018f"+
		"\u0192\3\2\2\2\u0190\u0192\3\2\2\2\u0191\u018c\3\2\2\2\u0191\u0190\3\2"+
		"\2\2\u0192a\3\2\2\2\u0193\u0194\7-\2\2\u0194\u0195\7\16\2\2\u0195\u0196"+
		"\7\60\2\2\u0196\u0197\5d\63\2\u0197\u0198\7\17\2\2\u0198\u0199\7\24\2"+
		"\2\u0199c\3\2\2\2\u019a\u019b\7\r\2\2\u019b\u019c\7\60\2\2\u019c\u019f"+
		"\5d\63\2\u019d\u019f\3\2\2\2\u019e\u019a\3\2\2\2\u019e\u019d\3\2\2\2\u019f"+
		"e\3\2\2\2\u01a0\u01a1\5h\65\2\u01a1\u01a2\5\34\17\2\u01a2\u01a3\5j\66"+
		"\2\u01a3g\3\2\2\2\u01a4\u01a7\5l\67\2\u01a5\u01a7\3\2\2\2\u01a6\u01a4"+
		"\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7i\3\2\2\2\u01a8\u01a9\5\34\17\2\u01a9"+
		"\u01aa\5j\66\2\u01aa\u01ad\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac\u01a8\3\2"+
		"\2\2\u01ac\u01ab\3\2\2\2\u01adk\3\2\2\2\u01ae\u01af\7\t\2\2\u01af\u01b0"+
		"\5n8\2\u01b0\u01b1\7\36\2\2\u01b1\u01b2\5\36\20\2\u01b2\u01b3\5p9\2\u01b3"+
		"m\3\2\2\2\u01b4\u01b7\7\60\2\2\u01b5\u01b7\5v<\2\u01b6\u01b4\3\2\2\2\u01b6"+
		"\u01b5\3\2\2\2\u01b7o\3\2\2\2\u01b8\u01bb\5l\67\2\u01b9\u01bb\3\2\2\2"+
		"\u01ba\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bbq\3\2\2\2\u01bc\u01bd\5"+
		"v<\2\u01bd\u01be\7\36\2\2\u01be\u01bf\7\60\2\2\u01bf\u01c0\5t;\2\u01c0"+
		"s\3\2\2\2\u01c1\u01c2\7\r\2\2\u01c2\u01c5\5r:\2\u01c3\u01c5\3\2\2\2\u01c4"+
		"\u01c1\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5u\3\2\2\2\u01c6\u01c7\t\4\2\2"+
		"\u01c7w\3\2\2\2\u01c8\u01c9\7\60\2\2\u01c9\u01ca\5z>\2\u01ca\u01cb\7\16"+
		"\2\2\u01cb\u01cc\5|?\2\u01cc\u01cd\7\17\2\2\u01cdy\3\2\2\2\u01ce\u01cf"+
		"\7\f\2\2\u01cf\u01d2\7\60\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01ce\3\2\2\2"+
		"\u01d1\u01d0\3\2\2\2\u01d2{\3\2\2\2\u01d3\u01d6\5~@\2\u01d4\u01d6\3\2"+
		"\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d4\3\2\2\2\u01d6}\3\2\2\2\u01d7\u01d8"+
		"\5P)\2\u01d8\u01d9\5\u0080A\2\u01d9\177\3\2\2\2\u01da\u01db\7\r\2\2\u01db"+
		"\u01de\5~@\2\u01dc\u01de\3\2\2\2\u01dd\u01da\3\2\2\2\u01dd\u01dc\3\2\2"+
		"\2\u01de\u0081\3\2\2\2\u01df\u01e0\t\5\2\2\u01e0\u0083\3\2\2\2\u01e1\u01e2"+
		"\7+\2\2\u01e2\u01e3\7,\2\2\u01e3\u01e4\7\60\2\2\u01e4\u01e5\7\16\2\2\u01e5"+
		"\u01e6\5\u0086D\2\u01e6\u01e7\7\17\2\2\u01e7\u01e8\7\20\2\2\u01e8\u01e9"+
		"\5f\64\2\u01e9\u01ea\7\21\2\2\u01ea\u0085\3\2\2\2\u01eb\u01ee\5r:\2\u01ec"+
		"\u01ee\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ec\3\2\2\2\u01ee\u0087\3\2"+
		"\2\2\u01ef\u01f0\5\u0084C\2\u01f0\u01f1\5\u0088E\2\u01f1\u01f6\3\2\2\2"+
		"\u01f2\u01f3\5T+\2\u01f3\u01f4\5\u0088E\2\u01f4\u01f6\3\2\2\2\u01f5\u01ef"+
		"\3\2\2\2\u01f5\u01f2\3\2\2\2\u01f6\u0089\3\2\2\2&\u0096\u009a\u00a0\u00b6"+
		"\u00c6\u00cd\u00d6\u00e3\u00ec\u00f1\u0101\u0110\u0118\u0122\u012c\u0131"+
		"\u013b\u0145\u014e\u0158\u0160\u0171\u017f\u0183\u0191\u019e\u01a6\u01ac"+
		"\u01b6\u01ba\u01c4\u01d1\u01d5\u01dd\u01ed\u01f5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}