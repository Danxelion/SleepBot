# Generated from SleepCommands.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u01a6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\5/\u016a\n/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\5/\u0173\n/\3/\3/\5/\u0177\n/\3/\3/\3/\3/\5")
        buf.write("/\u017d\n/\5/\u017f\n/\3\60\6\60\u0182\n\60\r\60\16\60")
        buf.write("\u0183\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\5\61\u019c\n\61\3\62\3\62\3\63\6\63\u01a1\n")
        buf.write("\63\r\63\16\63\u01a2\3\63\3\63\2\2\64\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\2e\63\3\2\4\3\2\62;\5\2\13\f\17\17\"\"\2\u01af")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2e\3\2\2\2\3g\3\2\2\2\5i\3")
        buf.write("\2\2\2\7l\3\2\2\2\to\3\2\2\2\13u\3\2\2\2\rx\3\2\2\2\17")
        buf.write("~\3\2\2\2\21\u0083\3\2\2\2\23\u0086\3\2\2\2\25\u008c\3")
        buf.write("\2\2\2\27\u0091\3\2\2\2\31\u0094\3\2\2\2\33\u0097\3\2")
        buf.write("\2\2\35\u009a\3\2\2\2\37\u009f\3\2\2\2!\u00a2\3\2\2\2")
        buf.write("#\u00a8\3\2\2\2%\u00ad\3\2\2\2\'\u00b2\3\2\2\2)\u00b6")
        buf.write("\3\2\2\2+\u00c0\3\2\2\2-\u00c5\3\2\2\2/\u00cb\3\2\2\2")
        buf.write("\61\u00ce\3\2\2\2\63\u00da\3\2\2\2\65\u00e5\3\2\2\2\67")
        buf.write("\u00e9\3\2\2\29\u00f4\3\2\2\2;\u00fc\3\2\2\2=\u0101\3")
        buf.write("\2\2\2?\u0108\3\2\2\2A\u010d\3\2\2\2C\u0113\3\2\2\2E\u011a")
        buf.write("\3\2\2\2G\u011e\3\2\2\2I\u0126\3\2\2\2K\u012b\3\2\2\2")
        buf.write("M\u0133\3\2\2\2O\u0138\3\2\2\2Q\u013c\3\2\2\2S\u0143\3")
        buf.write("\2\2\2U\u0148\3\2\2\2W\u0154\3\2\2\2Y\u015b\3\2\2\2[\u0163")
        buf.write("\3\2\2\2]\u017e\3\2\2\2_\u0181\3\2\2\2a\u019b\3\2\2\2")
        buf.write("c\u019d\3\2\2\2e\u01a0\3\2\2\2gh\7k\2\2h\4\3\2\2\2ij\7")
        buf.write("c\2\2jk\7o\2\2k\6\3\2\2\2lm\7k\2\2mn\7u\2\2n\b\3\2\2\2")
        buf.write("op\7i\2\2pq\7q\2\2qr\7k\2\2rs\7p\2\2st\7i\2\2t\n\3\2\2")
        buf.write("\2uv\7v\2\2vw\7q\2\2w\f\3\2\2\2xy\7u\2\2yz\7n\2\2z{\7")
        buf.write("g\2\2{|\7g\2\2|}\7r\2\2}\16\3\2\2\2~\177\7y\2\2\177\u0080")
        buf.write("\7q\2\2\u0080\u0081\7m\2\2\u0081\u0082\7g\2\2\u0082\20")
        buf.write("\3\2\2\2\u0083\u0084\7w\2\2\u0084\u0085\7r\2\2\u0085\22")
        buf.write("\3\2\2\2\u0086\u0087\7c\2\2\u0087\u0088\7y\2\2\u0088\u0089")
        buf.write("\7c\2\2\u0089\u008a\7m\2\2\u008a\u008b\7g\2\2\u008b\24")
        buf.write("\3\2\2\2\u008c\u008d\7y\2\2\u008d\u008e\7c\2\2\u008e\u008f")
        buf.write("\7m\2\2\u008f\u0090\7g\2\2\u0090\26\3\2\2\2\u0091\u0092")
        buf.write("\7o\2\2\u0092\u0093\7g\2\2\u0093\30\3\2\2\2\u0094\u0095")
        buf.write("\7c\2\2\u0095\u0096\7v\2\2\u0096\32\3\2\2\2\u0097\u0098")
        buf.write("\7k\2\2\u0098\u0099\7p\2\2\u0099\34\3\2\2\2\u009a\u009b")
        buf.write("\7y\2\2\u009b\u009c\7c\2\2\u009c\u009d\7t\2\2\u009d\u009e")
        buf.write("\7p\2\2\u009e\36\3\2\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1")
        buf.write("\7h\2\2\u00a1 \3\2\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4")
        buf.write("\7h\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7")
        buf.write("\7t\2\2\u00a7\"\3\2\2\2\u00a8\u00a9\7y\2\2\u00a9\u00aa")
        buf.write("\7j\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7v\2\2\u00ac$\3")
        buf.write("\2\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7k\2\2\u00af\u00b0")
        buf.write("\7o\2\2\u00b0\u00b1\7g\2\2\u00b1&\3\2\2\2\u00b2\u00b3")
        buf.write("\7f\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5\7f\2\2\u00b5(\3")
        buf.write("\2\2\2\u00b6\u00b7\7{\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9")
        buf.write("\7u\2\2\u00b9\u00ba\7v\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7f\2\2\u00bd\u00be\7c\2\2\u00be\u00bf")
        buf.write("\7{\2\2\u00bf*\3\2\2\2\u00c0\u00c1\7u\2\2\u00c1\u00c2")
        buf.write("\7j\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7y\2\2\u00c4,\3")
        buf.write("\2\2\2\u00c5\u00c6\7e\2\2\u00c6\u00c7\7j\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8\u00c9\7e\2\2\u00c9\u00ca\7m\2\2\u00ca.\3")
        buf.write("\2\2\2\u00cb\u00cc\7o\2\2\u00cc\u00cd\7{\2\2\u00cd\60")
        buf.write("\3\2\2\2\u00ce\u00cf\7e\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4")
        buf.write("\7u\2\2\u00d4\u00d5\7v\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7")
        buf.write("\7p\2\2\u00d7\u00d8\7e\2\2\u00d8\u00d9\7{\2\2\u00d9\62")
        buf.write("\3\2\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd")
        buf.write("\7i\2\2\u00dd\u00de\7w\2\2\u00de\u00df\7n\2\2\u00df\u00e0")
        buf.write("\7c\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3\u00e4\7{\2\2\u00e4\64\3\2\2\2\u00e5\u00e6")
        buf.write("\7j\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7y\2\2\u00e8\66")
        buf.write("\3\2\2\2\u00e9\u00ea\7e\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef")
        buf.write("\7u\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2")
        buf.write("\7p\2\2\u00f2\u00f3\7v\2\2\u00f38\3\2\2\2\u00f4\u00f5")
        buf.write("\7t\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7i\2\2\u00f7\u00f8")
        buf.write("\7w\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb")
        buf.write("\7t\2\2\u00fb:\3\2\2\2\u00fc\u00fd\7j\2\2\u00fd\u00fe")
        buf.write("\7g\2\2\u00fe\u00ff\7n\2\2\u00ff\u0100\7r\2\2\u0100<\3")
        buf.write("\2\2\2\u0101\u0102\7e\2\2\u0102\u0103\7c\2\2\u0103\u0104")
        buf.write("\7p\2\2\u0104\u0105\7e\2\2\u0105\u0106\7g\2\2\u0106\u0107")
        buf.write("\7n\2\2\u0107>\3\2\2\2\u0108\u0109\7u\2\2\u0109\u010a")
        buf.write("\7v\2\2\u010a\u010b\7q\2\2\u010b\u010c\7r\2\2\u010c@\3")
        buf.write("\2\2\2\u010d\u010e\7c\2\2\u010e\u010f\7n\2\2\u010f\u0110")
        buf.write("\7c\2\2\u0110\u0111\7t\2\2\u0111\u0112\7o\2\2\u0112B\3")
        buf.write("\2\2\2\u0113\u0114\7u\2\2\u0114\u0115\7p\2\2\u0115\u0116")
        buf.write("\7q\2\2\u0116\u0117\7q\2\2\u0117\u0118\7|\2\2\u0118\u0119")
        buf.write("\7g\2\2\u0119D\3\2\2\2\u011a\u011b\7h\2\2\u011b\u011c")
        buf.write("\7q\2\2\u011c\u011d\7t\2\2\u011dF\3\2\2\2\u011e\u011f")
        buf.write("\7s\2\2\u011f\u0120\7w\2\2\u0120\u0121\7c\2\2\u0121\u0122")
        buf.write("\7n\2\2\u0122\u0123\7k\2\2\u0123\u0124\7v\2\2\u0124\u0125")
        buf.write("\7{\2\2\u0125H\3\2\2\2\u0126\u0127\7t\2\2\u0127\u0128")
        buf.write("\7c\2\2\u0128\u0129\7v\2\2\u0129\u012a\7g\2\2\u012aJ\3")
        buf.write("\2\2\2\u012b\u012c\7c\2\2\u012c\u012d\7p\2\2\u012d\u012e")
        buf.write("\7c\2\2\u012e\u012f\7n\2\2\u012f\u0130\7{\2\2\u0130\u0131")
        buf.write("\7|\2\2\u0131\u0132\7g\2\2\u0132L\3\2\2\2\u0133\u0134")
        buf.write("\7i\2\2\u0134\u0135\7k\2\2\u0135\u0136\7x\2\2\u0136\u0137")
        buf.write("\7g\2\2\u0137N\3\2\2\2\u0138\u0139\7i\2\2\u0139\u013a")
        buf.write("\7g\2\2\u013a\u013b\7v\2\2\u013bP\3\2\2\2\u013c\u013d")
        buf.write("\7c\2\2\u013d\u013e\7f\2\2\u013e\u013f\7x\2\2\u013f\u0140")
        buf.write("\7k\2\2\u0140\u0141\7e\2\2\u0141\u0142\7g\2\2\u0142R\3")
        buf.write("\2\2\2\u0143\u0144\7v\2\2\u0144\u0145\7k\2\2\u0145\u0146")
        buf.write("\7r\2\2\u0146\u0147\7u\2\2\u0147T\3\2\2\2\u0148\u0149")
        buf.write("\7u\2\2\u0149\u014a\7w\2\2\u014a\u014b\7i\2\2\u014b\u014c")
        buf.write("\7i\2\2\u014c\u014d\7g\2\2\u014d\u014e\7u\2\2\u014e\u014f")
        buf.write("\7v\2\2\u014f\u0150\7k\2\2\u0150\u0151\7q\2\2\u0151\u0152")
        buf.write("\7p\2\2\u0152\u0153\7u\2\2\u0153V\3\2\2\2\u0154\u0155")
        buf.write("\7d\2\2\u0155\u0156\7g\2\2\u0156\u0157\7v\2\2\u0157\u0158")
        buf.write("\7v\2\2\u0158\u0159\7g\2\2\u0159\u015a\7t\2\2\u015aX\3")
        buf.write("\2\2\2\u015b\u015c\7k\2\2\u015c\u015d\7o\2\2\u015d\u015e")
        buf.write("\7r\2\2\u015e\u015f\7t\2\2\u015f\u0160\7q\2\2\u0160\u0161")
        buf.write("\7x\2\2\u0161\u0162\7g\2\2\u0162Z\3\2\2\2\u0163\u0164")
        buf.write("\7e\2\2\u0164\u0165\7c\2\2\u0165\u0166\7p\2\2\u0166\\")
        buf.write("\3\2\2\2\u0167\u0169\5c\62\2\u0168\u016a\5c\62\2\u0169")
        buf.write("\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016b\u016c\7<\2\2\u016c\u016d\5c\62\2\u016d\u0172\5")
        buf.write("c\62\2\u016e\u016f\7c\2\2\u016f\u0173\7o\2\2\u0170\u0171")
        buf.write("\7r\2\2\u0171\u0173\7o\2\2\u0172\u016e\3\2\2\2\u0172\u0170")
        buf.write("\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u017f\3\2\2\2\u0174")
        buf.write("\u0176\5c\62\2\u0175\u0177\5c\62\2\u0176\u0175\3\2\2\2")
        buf.write("\u0176\u0177\3\2\2\2\u0177\u017c\3\2\2\2\u0178\u0179\7")
        buf.write("c\2\2\u0179\u017d\7o\2\2\u017a\u017b\7r\2\2\u017b\u017d")
        buf.write("\7o\2\2\u017c\u0178\3\2\2\2\u017c\u017a\3\2\2\2\u017d")
        buf.write("\u017f\3\2\2\2\u017e\u0167\3\2\2\2\u017e\u0174\3\2\2\2")
        buf.write("\u017f^\3\2\2\2\u0180\u0182\5c\62\2\u0181\u0180\3\2\2")
        buf.write("\2\u0182\u0183\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184")
        buf.write("\3\2\2\2\u0184`\3\2\2\2\u0185\u0186\7o\2\2\u0186\u0187")
        buf.write("\7k\2\2\u0187\u0188\7p\2\2\u0188\u0189\7w\2\2\u0189\u018a")
        buf.write("\7v\2\2\u018a\u019c\7g\2\2\u018b\u018c\7o\2\2\u018c\u018d")
        buf.write("\7k\2\2\u018d\u018e\7p\2\2\u018e\u018f\7w\2\2\u018f\u0190")
        buf.write("\7v\2\2\u0190\u0191\7g\2\2\u0191\u019c\7u\2\2\u0192\u0193")
        buf.write("\7j\2\2\u0193\u0194\7q\2\2\u0194\u0195\7w\2\2\u0195\u019c")
        buf.write("\7t\2\2\u0196\u0197\7j\2\2\u0197\u0198\7q\2\2\u0198\u0199")
        buf.write("\7w\2\2\u0199\u019a\7t\2\2\u019a\u019c\7u\2\2\u019b\u0185")
        buf.write("\3\2\2\2\u019b\u018b\3\2\2\2\u019b\u0192\3\2\2\2\u019b")
        buf.write("\u0196\3\2\2\2\u019cb\3\2\2\2\u019d\u019e\t\2\2\2\u019e")
        buf.write("d\3\2\2\2\u019f\u01a1\t\3\2\2\u01a0\u019f\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4\u01a5\b\63\2\2\u01a5f\3\2\2")
        buf.write("\2\13\2\u0169\u0172\u0176\u017c\u017e\u0183\u019b\u01a2")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class SleepCommandsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    I = 1
    AM = 2
    IS = 3
    GOING = 4
    TO = 5
    SLEEP = 6
    WOKE = 7
    UP = 8
    AWAKE = 9
    WAKE = 10
    ME = 11
    AT = 12
    IN = 13
    WARN = 14
    IF = 15
    AFTER = 16
    WHAT = 17
    TIMEWORD = 18
    DID = 19
    YESTERDAY = 20
    SHOW = 21
    CHECK = 22
    MY = 23
    CONSISTENCY = 24
    REGULARITY = 25
    HOW = 26
    CONSISTENT = 27
    REGULAR = 28
    HELP = 29
    CANCEL = 30
    STOP = 31
    ALARM = 32
    SNOOZE = 33
    FOR = 34
    QUALITY = 35
    RATE = 36
    ANALYZE = 37
    GIVE = 38
    GET = 39
    ADVICE = 40
    TIPS = 41
    SUGGESTIONS = 42
    BETTER = 43
    IMPROVE = 44
    CAN = 45
    TIME = 46
    NUMBER = 47
    TIMEUNIT = 48
    WS = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'i'", "'am'", "'is'", "'going'", "'to'", "'sleep'", "'woke'", 
            "'up'", "'awake'", "'wake'", "'me'", "'at'", "'in'", "'warn'", 
            "'if'", "'after'", "'what'", "'time'", "'did'", "'yesterday'", 
            "'show'", "'check'", "'my'", "'consistency'", "'regularity'", 
            "'how'", "'consistent'", "'regular'", "'help'", "'cancel'", 
            "'stop'", "'alarm'", "'snooze'", "'for'", "'quality'", "'rate'", 
            "'analyze'", "'give'", "'get'", "'advice'", "'tips'", "'suggestions'", 
            "'better'", "'improve'", "'can'" ]

    symbolicNames = [ "<INVALID>",
            "I", "AM", "IS", "GOING", "TO", "SLEEP", "WOKE", "UP", "AWAKE", 
            "WAKE", "ME", "AT", "IN", "WARN", "IF", "AFTER", "WHAT", "TIMEWORD", 
            "DID", "YESTERDAY", "SHOW", "CHECK", "MY", "CONSISTENCY", "REGULARITY", 
            "HOW", "CONSISTENT", "REGULAR", "HELP", "CANCEL", "STOP", "ALARM", 
            "SNOOZE", "FOR", "QUALITY", "RATE", "ANALYZE", "GIVE", "GET", 
            "ADVICE", "TIPS", "SUGGESTIONS", "BETTER", "IMPROVE", "CAN", 
            "TIME", "NUMBER", "TIMEUNIT", "WS" ]

    ruleNames = [ "I", "AM", "IS", "GOING", "TO", "SLEEP", "WOKE", "UP", 
                  "AWAKE", "WAKE", "ME", "AT", "IN", "WARN", "IF", "AFTER", 
                  "WHAT", "TIMEWORD", "DID", "YESTERDAY", "SHOW", "CHECK", 
                  "MY", "CONSISTENCY", "REGULARITY", "HOW", "CONSISTENT", 
                  "REGULAR", "HELP", "CANCEL", "STOP", "ALARM", "SNOOZE", 
                  "FOR", "QUALITY", "RATE", "ANALYZE", "GIVE", "GET", "ADVICE", 
                  "TIPS", "SUGGESTIONS", "BETTER", "IMPROVE", "CAN", "TIME", 
                  "NUMBER", "TIMEUNIT", "DIGIT", "WS" ]

    grammarFileName = "SleepCommands.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


