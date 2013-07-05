#!/usr/bin/env python
# Copyright (c) 2013-Present, Scott Cagno
# All rights reserved. [BSD License]

# imports
from __init__ import typ, key, bsh, snp

live = False
togg = "TOGGLE-SUBLIME"
name = "SUBLIME-SCOPE"
kind = "EDITOR"
cmds = {
	
	"UP"				:	[ key("Up") 	],
	"DOWN"				:	[ key("Down") 	],
	"LEFT"				:	[ key("Left") 	],
	"RIGHT"				:	[ key("Right") 	],
	"LINE"				:	[ key("ctrl+g") ],

	"NEW"				:	[ key("ctrl+n") ],
	"OPEN"				:	[ key("ctrl+o") ],
	"SAVE"				:	[ key("ctrl+s") ],
	"CLOSE"				:	[ key("ctrl+w") ],
	"QUIT"				:	[ key("ctrl+q") ],

	"FULL-SCREEN"		:	[ key("shift+F11") ],
	
	"SPLIT-TWO"			:	[ key("shift+alt+2") 	],
	"SPLIT-THREE"		:	[ key("shift+alt+3") 	],
	"UN-SPLIT"			:	[ key("shift+alt+1") 	],
	"PAGE-ONE"			:	[ key("ctrl+1") 		],
	"PAGE-TWO"			:	[ key("ctrl+2") 		],
	"PAGE-THREE"		:	[ key("ctrl+3") 		],
	"NEXT-TAB"			:	[ key("ctrl+Pg_Down") 	],
	"PREVIOUS-TAB"		:	[ key("ctrl+Pg_Up") 	],

	"CUT"				:	[ key("ctrl+x") ],
	"COPY"				:	[ key("ctrl+c") ],
	"PASTE"				:	[ key("ctrl+v") ],
	"UNDO"				:	[ key("ctrl+z") ],
	"REDO"				:	[ key("ctrl+y") ],
	
	"SELECT-WORD"		:	[ key("ctrl+d") 		],
	"SELECT-LINE"		:	[ key("ctrl+l") 		],
	"SELECT-ELEMENT"	:	[ key("ctrl+shift+m") 	],
	"SELECT-BODY"		:	[ key("ctrl+shift+j") 	],
	"SELECT-ALL"		:	[ key("ctrl+a") 		],
	"SELECT-UP"			:	[ key("shift+Up") 		],
	"SELECT-DOWN"		:	[ key("shift+Down") 	],
	"SELECT-TILL-START"	:	[ key("shift+Home") 	],
	"SELECT-TILL-END"	:	[ key("shift+End") 		],
	"SELECT-MILTI"		:	[ key("alt+F3") 		],
	"MILTI-SELECT"		:	[ key("alt+F3")		 	],
	"DE-SELECT"			:	[ key("Escape") 		],

	"DELETE"			:	[ key("Delete") 				],
	"DELETE-WORD"		:	[ key("ctrl+d Delete") 			],
	"DELETE-LINE"		:	[ key("ctrl+shift+k") 			],
	"DELETE-BLOCK"		:	[ key("ctrl+shift+m Delete") 	],
	
	"RECORD-MACRO"		:	[ key("ctrl+alt+q") 		],
	"PLAY-MACRO"		:	[ key("shift+ctrl+alt+q") 	],
	"SAVE-MACRO"		:	[ key("alt+t"),  key("v") 	],
	"RUN-MACRO"			:	[ key("alt+m") 				],

	"ADD-SNIPPET"		:	[ key("alt+t"),  key("End"),  key("Return") ],
	"ADD-SNIPPET"		:	[ key("alt+t"),  key("End"),  key("Return") ],

	"CLICK-SAVE"		:	[ key("alt+s") 		],
	"CLICK-CANCEL"		:	[ key("alt+c") 		],
	"CHOOSE-FOLDER"		:	[ key("ctrl+Tab") 	],
	"CHOOSE"			:	[ key("Return") 	],
	"SELECT"			:	[ key("Return") 	],

	"LINE-UP"			:	[ key("ctrl+shift+Up") 		],
	"LINE-DOWN"			:	[ key("ctrl+shift+Down") 	],
	"DUPLICATE"			:	[ key("ctrl+shift+d") 		],
	"UN-WRAP"			:	[ key("ctrl+j") 			],
	"TOGGLE-BLOCK"		:	[ key("ctrl+m") 			],
	"AUTOCOMPLETE"		:	[ key("alt+/") 				],
	"USE"				:	[ key("ctrl+space") 		],
	"FIND"				:	[ key("ctrl+f") 			],
	"INDENT"			:	[ key("ctrl+]") 			],
	"UN-INDENT"			:	[ key("ctrl+[") 			],
	"UPPERCASE"			:	[ key("ctrl+k+u") 			],
	"LOWERCASE"			:	[ key("ctrl+k+l")			]
}