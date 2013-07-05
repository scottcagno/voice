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

	"HASH-BANG"			:	[ snp("shebang") 	],
	"TAG"				:	[ snp("tag") 		],
	"FROM"				:	[ snp("from") 		],
	"IMPORT"			:	[ snp("import") 	],
	"CLASS"				:	[ snp("class") 		],
	"FUNCTION"			:	[ snp("def") 		],
	"METHOD"			:	[ snp("method") 	],
	"IN-IT"				:	[ snp("init") 		],
	"FOR-LOOP"			:	[ snp("for") 		],
	"FOR-K"				:	[ snp("fork") 		],
	"FOR-K-V"			:	[ snp("forkv") 		],
	"IF"				:	[ snp("if") 		],
	"ELSE-IF"			:	[ snp("elif") 		],
	"ELSE"				:	[ snp("else") 		],
	"RANGE"				:	[ snp("range") 		],
	"THREAD"			:	[ snp("thread") 	],
	"SWITCH"			:	[ snp("switch") 	],
	"OPEN"				:	[ snp("fwrite") 	],	
	"MAP"				:	[ snp("hashmap") 	],
	"LIST"				:	[ snp("list") 		],
	"COMMENT"			:	[ snp("comm") 		],
	"MULTI-COMMENT"		:	[ snp("mulcomm")	],
	"RETURN"			:	[ snp("return") 	],
	"PRINT"				:	[ snp("print") 		],
	"FILE-TYPE-PYTHON"	: [ key("ctrl+shift+p"), typ("syntax: python"), key("Return")]
}