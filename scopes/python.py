#!/usr/bin/env python
# Copyright (c) 2013-Present, Scott Cagno
# All rights reserved. [BSD License]

# imports
from __init__ import typ, key, bsh, snp

live = False
togg = "TOGGLE-PYTHON"
name = "PYTHON-SCOPE"
kind = "LANGUAGE"
cmds = {

	"CLASS"				:	[ snp("class") 		],
	"COMMENT"			:	[ snp("comment") 	],
	"ELSE-IF"			:	[ snp("elif") 		],
	"ELSE"				:	[ snp("else") 		],
	"FOR-KEY"			:	[ snp("forkey") 	],
	"FOR-LOOP"			:	[ snp("for") 		],
	"FUNCTION"			:	[ snp("function") 	],
	"IF"				:	[ snp("if") 		],
	"IMPORT-FROM"		:	[ snp("importfrom") ],
	"IMPORT"			:	[ snp("import") 	],
	"MAIN"				:	[ snp("main") 		],
	"METHOD"			:	[ snp("method") 	],
	"OPEN-FILE"			:	[ snp("openfile")	],
	"PRINT-F"			:	[ snp("printf") 	],
	"PRINT"				:	[ snp("print") 		],
	"SELF"				:	[ snp("self")		],
	"SHA-BANG"			:	[ snp("shabang") 	],
	"TRY"				:	[ snp("try")		],
	"WHILE"				:	[ snp("while")		],
	"RANGE"				:	[ snp("range") 		],
	"RETURN"			:	[ snp("return") 	],
	"FILE-TYPE-PYTHON"	: 	[ key("ctrl+shift+p"), typ("syntax: python"), key("Return")]
}