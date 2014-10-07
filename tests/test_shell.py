# -*- coding: utf-8 -*-
"""
    Basic Shell Tests
    ~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2006-2014 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import unittest

from pygments.token import Token
from pygments.lexers import BashLexer


class BashTest(unittest.TestCase):

    def setUp(self):
        self.lexer = BashLexer()
        self.maxDiff = None

    def testCurlyNoEscapeAndQuotes(self):
        fragment = u'echo "${a//["b"]/}"\n'
        tokens = [
            (Token.Name.Builtin, u'echo'),
            (Token.Text, u' '),
            (Token.Literal.String.Double, u'"'),
            (Token.Keyword, u'${'),
            (Token.Name.Variable, u'a'),
            (Token.Punctuation, u'//['),
            (Token.Literal.String.Double, u'"b"'),
            (Token.Punctuation, u']/'),
            (Token.Keyword, u'}'),
            (Token.Literal.String.Double, u'"'),
            (Token.Text, u'\n'),
        ]
        self.assertEqual(tokens, list(self.lexer.get_tokens(fragment)))

    def testCurlyWithEscape(self):
        fragment = u'echo ${a//[\\"]/}\n'
        tokens = [
            (Token.Name.Builtin, u'echo'),
            (Token.Text, u' '),
            (Token.Keyword, u'${'),
            (Token.Name.Variable, u'a'),
            (Token.Punctuation, u'//['),
            (Token.Literal.String.Escape, u'\\"'),
            (Token.Punctuation, u']/'),
            (Token.Keyword, u'}'),
            (Token.Text, u'\n'),
        ]
        self.assertEqual(tokens, list(self.lexer.get_tokens(fragment)))
