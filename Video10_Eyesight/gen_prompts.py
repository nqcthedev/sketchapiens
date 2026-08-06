# -*- coding: utf-8 -*-
# GEN PROMPTS — Video10 "Why Are Your Eyes Worse Than a Caveman's?" (mat can / myopia, cum Co the Do Da)
# 1 dong narration = 1 shot = 1 anh. Nhat quan bang LAP CHU (STYLE/CONSIST/NEG y nguyen) — giong style video Rang.
# TRANG THAI: DOT 1 (shot 1-26: HOOK + Setup). DATA se noi tiep Ch3->KET o dot sau.

STYLE = ("Clean flat 2D cartoon explainer with smooth, even, confident medium-bold black "
         "outlines (single clean strokes, not scratchy, not wobbly, not heavy marker), a crisp "
         "minimalist educational look,")

CONSIST = ("The people are clean STICK-FIGURE doodles: a LARGE round white-filled head with a "
           "simple expressive face (two big round white eyes with small black pupils, thin "
           "expressive eyebrows, a tiny mouth, no nose) sitting on a THIN body made of clean black "
           "lines (a single medium-weight line for the torso plus thin noodle arms and legs), with "
           "simple rounded mitten hands and small oval feet, kept identical every time. The modern "
           "man has a BALD round head with NO hair; ONLY the caveman has hair. The body is "
           "bare line-art with no colour fill; a character only wears a garment if their own "
           "description names it. Any eyes, eyeballs, glasses, animals and props are simple and cute in flat "
           "SOLID COLOUR, drawn with a little more detail and volume than the plain stick people. "
           "Clean smooth evenly-weighted medium-bold black outlines, flat colours, NO gradient "
           "shading, a clean flat digital-explainer look (not 3D, not glossy).")

NEG = ("Family-friendly, wholesome, cute, gentle, non-violent, no blood, no gore. no gradients, no "
       "textures, no photorealism, no 3D, no glossy render, no sketchy scratchy lines, no extra "
       "limbs or fingers, no watermark, no logo, no frame borders, no collage, no picture-in-"
       "picture, no split-screen panels, 16:9, clean educational YouTube explainer doodle style.")

# ---- Nhan vat (lap y nguyen) ----
CHAR = {
 'you':   ("the recurring modern guy, the same plain black-outline STICK FIGURE with a plain round "
           "BALD white head and NO hair, a bare thin bold black stick-line body, thin noodle arms "
           "and legs, rounded mitten hands and small oval feet, "),
 'cave':  ("the recurring caveman, the same plain black-outline stickman with a messy scribbly tuft "
           "of short spiky dark doodle hair, wearing a simple ragged brown animal-hide smock as a "
           "flat brown shape over the torso, barefoot with small white oval feet, "),
 'optic': ("an optometrist stickman with a plain bald white head, wearing a flat pale-blue coat and "
           "small round glasses, "),
 'child': ("a small modern child stickman with a plain round bald white head, shorter than the adult, "),
 'none':  "",
}

# ---- Nen theo ngu canh (khai niem=trang; ke chuyen=canh phang-mau) ----
SCENE = {
 'wh':    ("Set on a plain solid WHITE background with lots of clean empty space and a soft "
           "light-grey shadow under the subject; a clear concept/diagram look."),
 'bed':   ("Set in a simple flat DIM bedroom, muted grey-blue walls low light, a plain bed and a small "
           "bedside table, low-detail, lots of clean space."),
 'ind':   ("Set in a simple flat DIM indoor room, muted grey walls in low light, a small window and a "
           "plain floor, low-detail, lots of clean space."),
 'out':   ("Set outdoors in bright daylight on flat open savanna, flat green-and-tan ground meeting a "
           "flat bright pale-blue sky with a big soft sun, lots of clean space."),
 'night': ("Set outdoors at night, a flat deep-navy sky with a small crescent moon and a few stars over "
           "a flat dark ground, lots of clean space."),
 'snow':  ("Set in a flat far-north snow landscape, plain white-and-pale-blue snow under a cold flat sky, "
           "low-detail, lots of clean space."),
 'school':("Set in a simple flat dim classroom, muted walls, a small desk and a chalkboard, low light, "
           "low-detail, clean space."),
 'play':  ("Set in a bright outdoor school playground in full daylight, flat green ground and a bright "
           "pale-blue sky with a big sun, low-detail, clean space."),
}

# ---- Khung hinh (doi lien tuc de de nhip don dieu) ----
FRAME = {
 'med':  "a medium shot, the subject drawn big and centered with clean breathing space around it.",
 'wide': "a WIDE establishing shot, the subject fairly small inside a large scene.",
 'close':"a tight CLOSE-UP, the expressive face or object filling most of the frame.",
 'high': "a HIGH-ANGLE shot looking DOWN, making the subject look small.",
 'low':  "a LOW-ANGLE shot looking UP, making the subject look powerful.",
}

def textpart(t):
    return ('a small "%s" in bold white ALL-CAPS letters on a little red tag.' % t) if t else "no text or letters."

def build(char, bg, frame, action, text):
    subj = action if char == 'none' else CHAR[char] + action
    return "%s %s. Framing: %s %s %s %s %s" % (STYLE, subj, FRAME[frame], CONSIST, SCENE[bg], textpart(text), NEG)

# DATA: (shotline, char, bg, frame, action, red-text)
DATA = [
 # ---- HOOK (1-18) ----
 ("The first thing you do every morning is reach for your glasses.", 'you','bed','med',"sitting up in bed just waking, groggy half-open eyes, reaching one hand toward a pair of glasses on a small bedside table",""),
 ("Before you find them, the world is a soft blur. A smear of light and shapes.", 'you','bed','med',"squinting hard with both hands feeling forward, everything around him drawn as soft fuzzy blurry shapes and smears",""),
 ("You can't read a clock across the room. You can't tell a friend from a stranger down the street.", 'you','wh','med',"squinting toward a blurry wall clock and a blurry vague person-shape, a small question mark over each",""),
 ("Without two thin curves of glass, you are, in one specific way, helpless.", 'you','wh','med',"standing lost and a little helpless, holding up a single pair of glasses, a small spotlight on the glasses",""),
 ("Now drop a caveman where you're standing.", 'cave','wh','med',"appearing standing in the same spot with a calm look, a small downward drop arrow above his head",""),
 ("He never read a word. Never saw a screen. Never sat in a classroom.", 'cave','wh','med',"standing beside a closed book, a glowing phone screen and a small school desk, each crossed out with a red X",""),
 ("And he could spot a single deer on a hillside, a mile off, at dusk.", 'cave','out','wide',"standing on the open savanna at dusk, pointing confidently at one tiny deer on a far distant ridge, thin sharp sight-lines going from his eyes to the deer",""),
 ("His eyes did, for free, what yours can't do with all of modern medicine behind you.", 'none','wh','med',"on the LEFT a bright cartoon caveman eyeball with a green check, on the RIGHT a modern eyeball wearing glasses next to a stack of medicine bottles with a red X",""),
 ("Right now, about one in three people on Earth is nearsighted.", 'none','wh','med',"a simple row of three little stick people, one of them clearly wearing glasses and highlighted","1 IN 3"),
 ("In parts of the world, it's nearly every young person.", 'none','wh','wide',"a group of young stick people almost all wearing glasses, only one without them",""),
 ("And the number keeps climbing. Fast. Everywhere.", 'none','wh','med',"a simple bold red line-graph arrow climbing steeply upward and off the top of the frame",""),
 ("Here's the strange part. This is new.", 'none','wh','med',"a bright tag stamped over a small calendar page with a little red now-mark","NEW"),
 ("Go back a few thousand years, and almost nobody's eyes worked like yours.", 'none','wh','med',"a left-pointing timeline arrow leading to a small group of ancient stick people, none of them wearing glasses",""),
 ("Your ancestors had sharp eyes. You have a prescription.", 'none','wh','med',"on the LEFT a caveman head with one bright sharp eye and a green check, on the RIGHT a modern bald guy holding a small prescription slip with a red mark",""),
 ("And the reason isn't what your optician probably told you.", 'optic','wh','med',"standing beside a big eye-test letter chart and shrugging, a small red X over a speech bubble by his head",""),
 ("It isn't just screens. It isn't just the genes you were born with.", 'none','wh','med',"a glowing phone screen and a blue DNA double-helix side by side, each with a small red 'not just' partial mark",""),
 ("It's a mismatch. Stone Age eyes, growing up in a world they were never built for.", 'none','wh','med',"two puzzle pieces that do NOT fit, one shaped like a stone-age eyeball and one like a modern city skyline, a small red gap between them","MISMATCH"),
 ("And the twist we saved for the end. It's still getting worse, and we're doing it to our own kids.", 'child','wh','med',"a small child stickman wearing thick round glasses, a saved-for-the-end star above and a red worsening down-arrow beside","THE TWIST"),
 # ---- SETUP (19-26) ----
 ("So start with the obvious suspect. The one everyone blames.", 'none','wh','med',"a police-lineup height wall with a single glowing phone standing alone in the suspect spotlight",""),
 ("Screens. Phones. Too much time staring at a glowing rectangle.", 'you','bed','close',"lying in the dark staring up close at a bright glowing phone rectangle that lights up his face",""),
 ("It feels right. It feels like the answer. It's mostly wrong.", 'none','wh','med',"the glowing phone suspect with a big red X stamped across it","WRONG"),
 ("Not because screens are innocent. But because they're only half of it, and not the half you think.", 'none','wh','med',"a glowing phone screen split down the middle, only one half shaded in, a small half label","HALF"),
 ("To see what's really warping your eyes, you need one strange fact about how an eye grows.", 'none','wh','close',"one big cute cartoon eyeball, a white sphere with a coloured iris and black pupil, a question mark hovering over it",""),
 ("It isn't born the right size. It builds itself, using the world around it as a blueprint.", 'none','wh','med',"a cartoon eyeball under construction with tiny scaffolding around it and a little blueprint scroll beside it","BLUEPRINT"),
 ("And if you hand it the wrong world, it builds itself wrong.", 'none','wh','med',"a cartoon eyeball built lopsided and stretched wrong out of a crumpled wrong blueprint, a small red warning mark",""),
 ("That's where this whole story starts. Not with a screen. With light.", 'none','wh','med',"a bright yellow sun sending light rays onto a cartoon eyeball on the right, a small phone screen set aside on the left with a red X","LIGHT"),
]

DATA += [
 # ---- Ch3: con mat tu dung bang anh sang + to tien nhin sac (27-44) ----
 ("The eye you were born with was too short.", 'none','wh','close',"a small stubby short cartoon eyeball with a short measuring bracket around it and a small red mark","TOO SHORT"),
 ("A newborn's eye is small and stubby, and the world comes in as a blur.", 'none','wh','med',"one tiny cute newborn cartoon eyeball, small and stubby, with soft blurry fuzzy smears all around it",""),
 ("Then it starts to grow.", 'none','wh','med',"the cartoon eyeball with small upward growth arrows around it, getting a little bigger",""),
 ("Not at random. It grows toward a target.", 'none','wh','med',"the cartoon eyeball stretching along a dotted line toward a small bullseye target",""),
 ("It stretches, front to back, until the image lands exactly on the retina. Then it stops.", 'none','wh','med',"a simple cross-section of a cartoon eyeball with a light ray focusing exactly onto the retina at the back, a small green check",""),
 ("But something has to tell it when to stop.", 'none','wh','med',"the cartoon eyeball with a big question mark and a small red stop sign beside it",""),
 ("That signal is light. Bright light.", 'none','wh','med',"a bright yellow sun beaming light rays straight onto the cartoon eyeball","LIGHT"),
 ("When enough light hits the back of the eye, the retina releases a little dopamine.", 'none','wh','med',"a cross-section eyeball with light hitting the retina at the back, releasing a few small coloured dopamine dots","DOPAMINE"),
 ("Dopamine is the brake. It tells the eye you're long enough now, stop.", 'none','wh','med',"a small cartoon brake pedal pressing down on the cartoon eyeball, a little red stop sign","BRAKE"),
 ("For your ancestors, that brake got slammed on every single day.", 'cave','out','med',"the caveman outdoors in bright daylight, a big brake symbol slamming down over his sunlit eyes",""),
 ("They lived outside. In the open. Under a sky.", 'cave','out','wide',"the caveman standing relaxed in a wide open bright savanna under a big open sky",""),
 ("Outdoor daylight is around a hundred thousand lux.", 'none','out','med',"a big bright sun with a small light-meter gauge maxed out high","100,000 LUX"),
 ("A bright room indoors is maybe three hundred.", 'none','ind','med',"a dim indoor room with a small light-meter gauge reading very low","300 LUX"),
 ("Their eyes were soaked, all day, in the exact signal that tells an eye when to stop.", 'cave','out','med',"the caveman outside with bright sun rays pouring into his wide eyes, a small green check",""),
 ("So the eye stopped at the right length. Almost every time.", 'none','wh','med',"a perfectly round correctly-sized cartoon eyeball with a small ruler showing the right length and a green check",""),
 ("And the payoff was vision you can barely imagine.", 'cave','out','med',"the caveman with wide bright sharp eyes and a small sparkle, gazing confidently into the distance",""),
 ("A hunter could pick out one animal on a far ridge, at dusk, and know what it was.", 'cave','out','wide',"the caveman as a hunter at dusk pointing at one tiny animal on a far distant ridge, thin sharp sight-lines from his eyes",""),
 ("Sharp, clean distance vision. Standard issue. For everyone.", 'none','wh','med',"a bright sharp cartoon eyeball with a green check and a small STANDARD stamp beside it",""),
 # ---- Ch4: ban thiet ke vo + de "tai gen" bang Inuit (45-66) ----
 ("Then we went inside.", 'you','ind','med',"the modern guy stepping through a doorway from bright daylight outside into a dim grey indoor room",""),
 ("We built walls, and roofs, and schools, and screens.", 'none','wh','med',"simple flat icons in a row, a brick wall, a house roof, a small school and a glowing screen, being stacked up",""),
 ("And we handed the growing eye a world it had never been shaped for.", 'none','wh','med',"a mitten hand offering a small growing cartoon eyeball a dark dim boxed-in little world",""),
 ("A dim one.", 'none','ind','med',"a single cartoon eyeball sitting alone in a dim dark low-light room","DIM"),
 ("Indoors, the light drops to a fraction of what the eye evolved to expect.", 'none','ind','med',"a dim indoor room with a light-meter gauge dropping low and a small red down arrow",""),
 ("The retina waits for the bright signal. The brake. And it never comes.", 'none','wh','med',"a cross-section eyeball, the retina waiting, a brake symbol with a big red X over it",""),
 ("So the eye keeps growing. Longer. And longer.", 'none','wh','med',"a cartoon eyeball stretching visibly longer and longer with repeated growth arrows, getting elongated",""),
 ("Past the point where the image lands cleanly on the retina.", 'none','wh','med',"a cross-section of a too-long eyeball, the light ray now focusing in front of the retina, a small red mark",""),
 ("Now the light focuses in front of the retina, and everything far away turns to blur.", 'none','wh','med',"a cross-section too-long eyeball with the focus point in front of the retina and a blurry distant object, red",""),
 ("The eyeball went from a round ball to a stretched one. From a basketball to a rugby ball.", 'none','wh','med',"on the LEFT a round orange basketball-shaped eyeball with a green check, on the RIGHT a stretched brown rugby-ball-shaped eyeball with a red mark, an arrow between them",""),
 ("That's myopia. Not a sickness you caught. A shape your eye grew into.", 'none','wh','med',"the stretched rugby-ball-shaped cartoon eyeball labeled as the problem","MYOPIA"),
 ("And here's the part that kills the easy answer.", 'none','wh','med',"a small speech bubble with a blue DNA icon inside it, a big red X stamped over the whole bubble",""),
 ("People love to say it's just genes. You got bad eyes from your parents.", 'none','wh','med',"two parent stick figures wearing glasses handing a pair of glasses down to a small child, a blue DNA strand nearby",""),
 ("Genes do matter. One nearsighted parent roughly doubles your odds. Two of them, about five times.", 'none','wh','med',"a simple chart, one glasses-parent icon with a x2 label and two glasses-parents with a x5 label","x2   x5"),
 ("But genes can't do this.", 'none','wh','med',"a blue DNA double-helix strand with a big red X over it",""),
 ("In a single century, nearsightedness went from rare to nearly half the planet.", 'none','wh','med',"a globe with nearly half of it shaded and covered in little glasses, a steep 100-year arrow","100 YEARS"),
 ("Genes don't change that fast. Nothing in your DNA rewrote itself in a hundred years.", 'none','wh','med',"a blue DNA strand beside a slow snail and a clock, a small red X over a fast-rewrite arrow",""),
 ("The clearest proof came from the far north.", 'none','snow','med',"a cold far-north snow landscape with a small compass pointing north",""),
 ("For generations, the Inuit had sharp eyes. Nearsightedness was almost unheard of.", 'none','snow','med',"a smiling Inuit person in a warm brown fur-hood parka with bright wide sharp eyes and a small green check",""),
 ("Then, in one generation, their children went to school.", 'none','school','med',"a small Inuit child in a fur parka walking into a simple little classroom with a chalkboard",""),
 ("And a quarter of them came out nearsighted.", 'none','wh','med',"a row of four small Inuit children, one of them clearly wearing glasses and highlighted","1 IN 4"),
 ("Same genes. Same families. One new thing. A childhood spent indoors.", 'none','wh','med',"a blue DNA strand and a family icon each with a green SAME check, and one red NEW arrow pointing to a small dim classroom",""),
 # ---- Ch5: can nang = benh, doa mu (67-80) ----
 ("So you wear glasses, and you think that's the end of it.", 'you','wh','med',"the modern guy putting on a pair of glasses with a relieved satisfied look and a small green check",""),
 ("For most people, it is. A prescription, a pair of lenses, done.", 'none','wh','med',"a prescription slip and a pair of lenses side by side with a small green DONE check",""),
 ("But here's the part almost nobody tells you.", 'you','wh','close',"the modern guy leaning in close with a serious lowered-voice look, one finger raised",""),
 ("The longer the eye grew, the more dangerous it gets.", 'none','wh','med',"a cartoon eyeball stretching longer beside a rising red danger warning meter",""),
 ("Remember what myopia really is. Stretch. The whole eyeball pulled long.", 'none','wh','med',"a cartoon eyeball being pulled long by two opposing arrows, a stretch feel, red",""),
 ("And the retina, the thin sheet of nerve at the back, gets pulled along with it.", 'none','wh','med',"a cross-section eyeball with the thin retina sheet at the back being stretched thin along with it",""),
 ("Stretch anything thin far enough, and it starts to tear.", 'none','wh','med',"a thin flat sheet being stretched by two arrows and starting to rip with a small red tear",""),
 ("Past a certain point, doctors stop calling it a prescription. They call it high myopia.", 'none','wh','med',"a prescription slip crossed out with a red X, replaced by a red HIGH MYOPIA label","HIGH MYOPIA"),
 ("And a badly stretched retina can begin to peel away, like old paint lifting off a wall.", 'none','wh','med',"a layer of retina peeling and curling away like old paint lifting off a wall, a small red mark",""),
 ("This is where it stops being about blurry road signs.", 'none','wh','med',"a blurry road sign with a big red X over it",""),
 ("A detaching retina. Glaucoma. Damage to the very center of your sight.", 'none','wh','med',"a cross-section eye with the retina peeling loose and a dark spot in the very center of the view, red warning marks",""),
 ("These are leading causes of blindness, and no lens can fix them.", 'none','wh','med',"an eye going dark and black beside a pair of glasses with a big red X","BLINDNESS"),
 ("The blur was never the real danger. The blur was the warning.", 'none','wh','med',"a blurry yellow warning triangle sign with a small exclamation, a warning feel",""),
 ("And an eye that grew too long as a child carries that risk for the rest of its life.", 'none','wh','med',"a stretched long cartoon eyeball with a small red risk tag chained to it and a lifelong clock",""),
 # ---- Ch6: beat hy vong, Dai Loan (81-92) ----
 ("So is this just our fate now. Half the world, going blurry, then worse.", 'none','wh','med',"a globe with half of it blurry, a gloomy downward arrow and a question mark",""),
 ("For a long time, that's how it looked. The numbers only ever climbed.", 'none','wh','med',"a red line graph arrow only ever climbing upward",""),
 ("Then a whole country ran the experiment for us.", 'none','wh','med',"a simple map outline of a country with a small science flask and clipboard on it",""),
 ("And what they found is the most hopeful part of this story.", 'none','wh','med',"a bright hopeful sunrise glow with a small green upward heart",""),
 ("Around 2010, Taiwan had one of the highest rates of childhood myopia on Earth.", 'none','wh','med',"a 2010 calendar page beside a group of children almost all wearing glasses, a tall red bar","2010"),
 ("Nearly nine in ten young people, nearsighted.", 'none','wh','med',"a row of ten young stick people, nine of them wearing glasses and highlighted","9 IN 10"),
 ("So they tried something almost stupidly simple.", 'none','wh','med',"a bright yellow lightbulb over a very simple obvious idea, a small shrug",""),
 ("They sent the kids back outside. Two hours a day. Recess in the open, under the real sky.", 'none','play','wide',"a few happy children playing outside in a bright sunny playground under a big open sky, a small two-hour clock","2 HOURS"),
 ("No new drug. No surgery. Just light. The old signal. The brake.", 'none','wh','med',"a pill bottle and a scalpel each with a red X, and a bright sun with a green check","JUST LIGHT"),
 ("And for the first time in forty years, the line stopped climbing. Then it started to fall.", 'none','wh','med',"a graph line climbing up then turning and falling back down, drawn green, a small 40-year mark",""),
 ("The thing that broke our eyes turned out to be the thing that could heal them.", 'none','wh','med',"a single bright sun with a red broke arrow on one side and a green heal arrow on the other",""),
 ("Not a screen you throw away. A sky you walk back under.", 'you','out','med',"the modern guy tossing a glowing phone into a bin and stepping outside under a big bright open sky",""),
 # ---- KET: tra loi + identity + cu lat + callback (93-113) ----
 ("So. Why are your eyes worse than a caveman's.", 'none','wh','med',"on the LEFT a bright caveman eyeball, on the RIGHT a modern eyeball wearing glasses, a big question mark between them","?"),
 ("Not because you did anything wrong. Not because your genes failed you.", 'none','wh','med',"a small your-fault note and a blue DNA strand, both crossed out with red X marks",""),
 ("Because your eyes did exactly what eyes are built to do. They grew to fit their world.", 'none','wh','med',"a cartoon eyeball fitting perfectly into a matching puzzle slot shaped like its world, a green check",""),
 ("The caveman's world was made of distance and daylight. So his eyes came out long and sharp.", 'cave','out','med',"the caveman under bright daylight gazing into the far distance with bright sharp eyes, a green check",""),
 ("Your world was made of walls, and dim light, and things held close to your face.", 'you','ind','med',"the modern guy in a dim room with close walls, holding a glowing phone right up against his face",""),
 ("So your eyes grew to match that instead.", 'none','wh','med',"a stretched rugby-ball-shaped eyeball matched to a small dim-room icon, a red mark",""),
 ("You're not broken. You're calibrated. Just to the wrong world.", 'you','wh','med',"the modern guy beside a calibration gauge, a green NOT BROKEN check and a small red wrong-world tag",""),
 ("That's you. A Stone Age eye, raised indoors.", 'none','wh','med',"a rough Stone Age style cartoon eyeball sitting inside a small modern dim living room",""),
 ("And here's the twist, the one saved for the end.", 'none','wh','med',"a saved-for-the-end star bookmark being opened up with a small reveal sparkle","THE TWIST"),
 ("It's not over. It's still happening. Right now.", 'none','wh','med',"a ticking clock with a red now arrow and a small still-happening loop symbol",""),
 ("The most nearsighted generation in human history is the one being born today.", 'child','wh','med',"a tiny newborn baby stick figure already being handed a pair of thick round glasses, a red today mark",""),
 ("We took our own children, the ones with those perfect newborn eyes, and we raised them inside.", 'none','ind','med',"a mitten hand gently placing a small bright-eyed child into a dim grey indoor room",""),
 ("We handed them screens, and rooms, and homework, and we took away the sky.", 'child','ind','med',"a small child indoors surrounded by a glowing screen, close walls and a stack of homework, a curtain closing over the sun behind",""),
 ("And their eyes are growing long, in the dark, exactly the way ours did. Only faster.", 'none','wh','med',"a small child's cartoon eyeball stretching long fast in the dark with quick red arrows, beside a slower adult one",""),
 ("The good news is the fix was never complicated.", 'none','wh','med',"a single bright simple lightbulb and sun with a green check","SIMPLE"),
 ("It's the same thing your ancestor's eyes drank in every day. For free.", 'cave','out','med',"the caveman outside with bright sunlight pouring into his eyes and a small FREE tag, a green check",""),
 ("So tomorrow morning, before you reach for your glasses, remember what they are.", 'you','bed','med',"the modern guy in the morning pausing thoughtfully as he reaches for the glasses on his bedside table",""),
 ("They are a patch. A small curved apology for a childhood spent indoors.", 'none','wh','close',"a single pair of glasses drawn like a small curved band-aid patch over an eye, a tiny apology note",""),
 ("And if there is a child near you, do the one thing evolution is quietly begging you to do.", 'none','wh','med',"a small child beside a gentle mitten hand pointing toward an open door with bright light beyond",""),
 ("Take them outside. Give them back the light.", 'you','out','wide',"the modern guy leading a small child outside by the hand into bright daylight under a big warm sun",""),
 ("Give them back the sky your ancestors could see a deer across.", 'child','out','wide',"a small child standing under a wide bright open sky, gazing at one tiny deer far away across a distant ridge",""),
]

if __name__ == "__main__":
    import io
    lines = [d[0] for d in DATA]
    prompts = [build(d[1], d[2], d[3], d[4], d[5]) for d in DATA]
    n = len(DATA)
    with io.open("SHOTLINES_FULL.txt","w",encoding="utf-8") as f:
        f.write("\n".join(lines))
    with io.open("PROMPTS_FULL.txt","w",encoding="utf-8") as f:
        for i,p in enumerate(prompts,1):
            f.write("%03d.\n%s\n\n" % (i,p))
    tag = "FULL 113" if n==113 else ("PARTIAL (%d/113 shots)"%n)
    print("Shots: %d  [%s]" % (n, tag))

    # --- Tu kiem: shotline PHAI khop file narration that (chong lech sync TTS) ---
    try:
        with io.open("Script_Video10_narration.txt","r",encoding="utf-8") as f:
            nar = [l.rstrip("\n") for l in f if l.strip()!=""]
        print("Narration that co %d dong; DATA hien co %d shot." % (len(nar), n))
        mism = 0
        for i in range(min(len(nar), n)):
            if nar[i].strip()!=lines[i].strip():
                mism += 1
                if mism<=3:
                    print("!! LECH dong %03d:\n   narration: %s\n   DATA     : %s" % (i+1, nar[i], lines[i]))
        print("Kiem khop %d dong dau: %s (%d dong lech)" % (min(len(nar),n), "OK 100%" if mism==0 else "CO LECH", mism))
    except FileNotFoundError:
        print("(khong thay Script_Video10_narration.txt de doi chieu)")

    print("\n=== SAMPLE 007 (caveman thay con nai xa) ===\n"+prompts[6])
    print("\n=== SAMPLE 023 (eyeball concept) ===\n"+prompts[22])
