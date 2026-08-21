# -*- coding: utf-8 -*-
"""V20 COLD — "What Kept Ancient Humans Alive Through Freezing Nights?"

(line, kind, subj, text, bg, face)

kind : SCENE_A ancient | SCENE_W woman | GROUP nhom | SCENE_N khong nguoi | CARD
bg   : cold_night night_dark night_open fire_ring fire_edge dusk_grey dry_plain
       cave_warm dark_card white
face : flat shock tired worry scared happy asleep dumb curious sad

⚠️ DUNG LAI TU DAU 19/08/2026. Bo shot cu (282) dung cho KICH BAN DAU TIEN
   (2.132 tu). Kich ban da viet lai toan bo -> chi 12% cau con dung lai duoc.
   Ban cu giu o _cu_shot_data_ban1.py

3.228 tu / 269 cau -> 426 shot (trung vi 7 tu/shot).
Dong-shot sinh boi tools/chia_shot.py, co cong kiem ghep-lai-khop-tung-ky-tu.

LUAT HINH RIENG CUA V20
───────────────────────
1. KHONG CO NHAN VAT HIEN DAI. Lane "ve BAN" da bo 10/08.
2. Khoi nhan vat ep MOI nguoi trong MOI kind deu la nguoi co dai mac ao da.
   -> Doan KHOA HOC HIEN DAI (Krauchi 2000, buong nhiet Haskell 1981) ve DO VAT,
      khong ve nguoi: giuong, num chinh nhiet, nhiet ke, bieu do.
      Ngu phap: qua khu co NGUOI, khoa hoc co VAT.
3. Co che sinh ly ve TREN THAN NGUOI CO DAI (tay am, tay lanh, hoi nong bay len),
   KHONG ve thanh so do. V19 hong vi 62% khung la the; doi thu 36-41%.
4. KET BAI moi (phong ngu 21 do, cai chan) van VE DO VAT, khong ve nguoi hien dai.
"""

SHOTS = [

# ═════════════════ HOOK — 34 shot ═════════════════
("There is a point in freezing to death where the shivering stops.","SCENE_A","he lies curled on his side on frozen ground, whole body drawn tight, small motion lines shaking off his shoulders and knees","no text","cold_night","scared"),
("It feels like the worst of it has passed.","SCENE_A","the same man lying on frozen ground, now completely still, the shaking lines gone, his face gone slack","no text","cold_night","tired"),
("It is the body giving up.","SCENE_A","close on him lying still on the frost, one hand fallen open on the ground beside his face","no text","cold_night","tired"),
("Shivering is us burning fuel to make heat,","SCENE_A","he sits hunched and shaking on frozen ground with small wavy orange heat lines rising off his shoulders","a label \"HEAT\" beside the rising lines","cold_night","scared"),
("and it stops when there is no fuel left to burn.","SCENE_N","a small pile of glowing embers on frozen ground going grey and dark, one last thin wisp lifting off it","no text","cold_night","flat"),
("Doctors put that moment at a core temperature of about thirty two degrees.","SCENE_N","one plain upright thermometer standing on frost, the column low, a heavy black arrow pointing at one mark on the glass","a label \"32\" at the mark the arrow points to","cold_night","flat"),
("Below it the thinking goes,","SCENE_A","close on his face on the frozen ground, eyes half open and unfocused, looking at nothing","no text","night_dark","dumb"),
("and some people start pulling their clothes off.","SCENE_A","he kneels on the frost with both hands pulling his hide tunic up off one shoulder, the hide half slipped down his arm","no text","cold_night","dumb"),
("It is called paradoxical undressing,","CARD","one ragged animal hide lying discarded flat on white ground, alone","large bold headline text \"PARADOXICAL UNDRESSING\"","white","flat"),
("and it is how a certain number of people are","SCENE_N","a hide tunic lying crumpled on open frost, empty, with a light dusting of snow across it","no text","cold_night","flat"),
("found dead every winter.","SCENE_N","the same crumpled empty hide on frost, now with a thin drift of snow half burying it","no text","cold_night","flat"),
("Your body has that same shutdown in it,","SCENE_A","he stands upright facing the front, both hands held open at his sides, small orange heat lines drawn rising off his chest","no text","cold_night","flat"),
("and it will not warn you before it starts.","SCENE_A","the same man standing, the heat lines now gone from his chest and his hands drawn pale, nothing else changed","no text","cold_night","flat"),
("Now take that body,","SCENE_A","the man standing alone in an empty white frame, nothing around him at all","no text","white","flat"),
("put it on frozen ground,","SCENE_A","the same man now lying flat on his back on a wide sheet of frost, seen from the side","no text","cold_night","flat"),
("and take the roof away.","SCENE_N","a wide black sky filling most of the frame over one thin strip of frost, with a small scatter of white stars","no text","night_open","flat"),
("That is where our ancestors slept.","GROUP","four of them lying close together in a row on open frozen ground under a black sky, no shelter of any kind above them","no text","night_open","asleep"),
("Not for one bad night.","CARD","one small square drawn alone on white, with a thin black frame around it","a label \"ONE NIGHT\" under the square","white","flat"),
("Every night, for months, for hundreds of generations.","CARD","a dense grid of many small identical squares filling the whole frame","no text","white","flat"),
("And the strange part is not","SCENE_N","a wide frozen plain at night with one small dark shape lying motionless in the middle distance","no text","cold_night","flat"),
("that some of them died out there.","SCENE_N","the same frozen plain, the small dark shape now half covered by snow, no fire anywhere in the frame","no text","cold_night","flat"),
("It is that most of them woke up.","GROUP","three of them sitting up on the frost at first light, stretching, a low pale sun just clearing the horizon behind them","no text","dusk_grey","tired"),
("And that is not luck, it is arithmetic.","CARD","one plain black equals sign drawn large and alone","no text","white","flat"),
("Every person watching this sits at the end of a line","CARD","a long horizontal row of many tiny plain figures standing shoulder to shoulder, running off both edges of the frame","no text","white","flat"),
("where not one ancestor froze before they had children.","CARD","the same long row of tiny figures, unbroken, with one thin black line drawn linking each figure to the next","no text","white","flat"),
("Hundreds of thousands of nights,","SCENE_N","a vast field of small white stars filling a black frame, far more than can be counted","no text","night_dark","flat"),
("and the line never broke once.","CARD","the same unbroken row of linked tiny figures, with one small green check mark at the far right end","no text","white","flat"),
("This has three parts,","CARD","three plain empty circles drawn in a row, evenly spaced, nothing inside them","a label \"1\" \"2\" \"3\" under the three circles","white","flat"),
("and only the first one is about how cold it got.","CARD","the same three circles with only the first one filled solid pale blue and small frost marks around it","a label \"COLD\" under the first circle","white","flat"),
("The second is a trap the body sets for itself.","CARD","the same three circles with the second one now filled, a small closed loop drawn inside it","a label \"THE TRAP\" under the second circle","white","flat"),
("The third is within arm's reach of you tonight,","CARD","the same three circles with the third one filled warm orange","a label \"TONIGHT\" under the third circle","white","flat"),
("and it is doing the fire's job right now.","SCENE_N","one small fire burning alone on dark ground, and beside it a folded blanket lying on plain pale ground, the two objects side by side","no text","fire_ring","flat"),
("I have left that one until the end,","CARD","the third circle alone, filled orange, with a thin black arrow curving from it away to the right edge of the frame","no text","white","flat"),
("because it changes what the other two were for.","CARD","all three circles again with two thin black arrows curving back from the third one to the first and second","no text","white","flat"),

# ═════════════════ CH1 — DEM DAI BAO LAU — 18 shot ═════════════════
("Start with how long the night was,","SCENE_N","a wide frozen plain under a black sky, with one thin pale band of light along the very bottom of the horizon","no text","cold_night","flat"),
("because it is longer than people think.","SCENE_N","the same plain, the pale band along the horizon now much thinner and the black sky much taller","no text","cold_night","flat"),
("Fifty degrees north is the line through Kyiv and Krakow and Prague.","SCENE_N","a plain outline map of Europe with one straight horizontal line drawn across it and three small dots sitting on that line","a label \"KYIV\" \"KRAKOW\" \"PRAGUE\" at the three dots","white","flat"),
("On the shortest day of the year","SCENE_N","a very low pale sun sitting just above a flat frozen horizon, throwing one long thin shadow across the frost","no text","cold_night","flat"),
("that line gets under eight hours of light.","SCENE_N","the low pale sun with a short dotted arc drawn across the sky showing the whole path it will travel","a label \"8 HOURS\" along the dotted arc","cold_night","flat"),
("Sixteen hours of dark.","CARD","the words filling the frame, nothing else drawn","large bold headline text \"SIXTEEN HOURS OF DARK\"","dark_card","flat"),
("Go up to sixty degrees,","SCENE_N","the same outline map of Europe with a second straight line drawn higher up, above the first one","no text","white","flat"),
("through Oslo and Helsinki and Saint Petersburg,","SCENE_N","the outline map with three small dots sitting on the upper line","a label \"OSLO\" \"HELSINKI\" \"ST PETERSBURG\" at the three dots","white","flat"),
("and it is eighteen and a half.","CARD","one plain circle with a very thin pale slice and the rest filled solid black","a label \"18.5 HOURS DARK\"","white","flat"),
("None of that is a guess.","SCENE_N","a simple tilted globe with one straight axis line drawn through it and a small sun off to one side","no text","white","flat"),
("The tilt of the planet has not moved,","SCENE_N","the same tilted globe with a small padlock drawn beside the axis line","no text","white","flat"),
("and it is the one thing in this story that is simply settled.","CARD","one small green check mark drawn large and alone","no text","white","flat"),
("And the months with the longest nights are the months","SCENE_N","a bare tree with no leaves standing on frozen ground under a black sky","no text","cold_night","flat"),
("with the least to eat.","SCENE_N","an empty woven basket lying tipped over on frozen ground, nothing inside it","no text","cold_night","flat"),
("That matters,","SCENE_N","the same empty basket alone on the frost, seen closer","no text","cold_night","flat"),
("because everything a body does to survive a cold night","SCENE_A","he sits hunched on frozen ground with heat lines rising off him and both hands over his stomach","no text","cold_night","tired"),
("is paid for in food.","SCENE_N","one small piece of dried meat lying on a flat stone, and beside it a small pile of glowing embers, drawn the same size","no text","cold_night","flat"),
("The night gets longer exactly as the account it draws on runs dry.","SCENE_N","a black sky growing taller on the left of the frame while an empty basket sits on the frost at the right, nothing between them","no text","cold_night","flat"),
]
