# -*- coding: utf-8 -*-
# Generator prompt ảnh — Video07 "Why Do You Get Goosebumps?"
# Xuất: Script_Video07_narration.txt · SHOTLINES_FULL.txt · PROMPTS_FULL.txt
import os
HERE = os.path.dirname(os.path.abspath(__file__))

STYLE = ("Clean flat 2D cartoon explainer with smooth, even, confident medium-bold black outlines "
         "(single clean strokes, not scratchy, not wobbly, not heavy marker), a crisp minimalist educational look,")

CONSIST = ("The people are clean STICK-FIGURE doodles: a LARGE round white-filled head with a simple expressive face "
           "(two big round white eyes with small black pupils, thin expressive eyebrows, a tiny mouth, no nose) sitting on a THIN body "
           "made of clean black lines (a single medium-weight line for the torso plus thin noodle arms and legs) — NOT a filled or solid body shape, "
           "just clean stick lines, with simple rounded mitten hands and small oval feet, ALWAYS drawn as the SAME stickman, kept identical in every image. "
           "The modern man has a BALD round head with NO hair. Any animals are simple and cute in flat SOLID COLOUR (never black-and-white), "
           "each with a little face, drawn with more detail and body volume than the simple stick people. "
           "Clean smooth evenly-weighted medium-bold black outlines; flat colours, NO gradient shading, a clean flat digital-explainer look, evenly drawn (not 3D, not glossy).")

NEG = ("Family-friendly, wholesome, cute, gentle, non-violent, no blood, no gore, no injury. no gradients, no textures, no photorealism, no 3D, "
       "no glossy render, no sketchy scratchy lines, no extra limbs or fingers, no watermark, no logo, no frame borders, no duplicate characters, "
       "no collage, no picture-in-picture, 16:9, clean educational YouTube explainer doodle style.")

CHAR = {
 'you': ("the recurring modern guy, the same plain black-outline STICK FIGURE with a plain round BALD white head and NO hair (just a simple face), "
         "a bare thin bold black stick-line body, thin noodle arms and legs, simple rounded mitten hands and small oval feet, "),
 'ancestor': ("the recurring furry ancestor, the same stick figure but with a round white head topped with a messy tuft of short dark hair and light-brown fuzzy fur on the arms and body, "
              "a simple ragged brown animal-hide wrap on the torso, "),
 'none': "",
}

FRAME = {
 'm': "a medium shot, the subject drawn big and centered with clean breathing space around it.",
 'w': "a WIDE establishing shot, the subject fairly small inside a large scene.",
 'cu': "a tight CLOSE-UP filling most of the frame.",
}

SCENE = {
 'wh':   "ONE single scene on a plain WHITE background with lots of clean empty space and a soft light-grey shadow under the subject; RED accent for danger/warnings, GREEN for yes, a small YELLOW lightbulb for an idea,",
 'skin': "ONE single scene on a plain WHITE background: a large simple cross-section diagram of skin with a hair, a hair follicle pocket and a tiny muscle beside it, clean black outlines, small black labels and arrows, lots of empty space,",
 'cold': "ONE single scene: a flat pale icy-blue cold background with a few simple white snowflakes, a soft grey shadow, lots of clean empty space,",
 'warm': "ONE single scene: a soft warm glowing background, a gentle orange-to-purple concert/awe glow, a few tiny light dots, a calm moved mood, lots of clean space,",
 'home': "ONE single scene: a simple flat modern room, a plain muted wall, minimal furniture, a soft grey shadow, muted tone,",
 'sav':  "ONE single scene: a flat olive-brown savanna ground under a plain warm sky, a distant simple tree silhouette, lots of clean space,",
 'brain':"ONE single scene on a plain WHITE background: one big simple cartoon brain shape as the focus, clean flat pink-beige fill with black outline, small black labels/arrows, lots of empty space,",
}

# (shotline, char, bg, frame, action, text)
DATA = [
 # HOOK
 ("A song hits a certain note. Or you step out into the cold. Or something just feels... big.",'you','warm','m',"standing, a small music note, a snowflake and a sparkle floating around the head, a stirred look",""),
 ("And your skin does something strange.",'you','wh','cu',"looking at own forearm, curious, a small sparkle on the skin",""),
 ("Tiny bumps rise across your arms. The hair stands up on the back of your neck.",'you','wh','cu',"close on an arm covered in tiny bumps with a few faint hairs standing up",""),
 ("You didn't decide to do that. You couldn't stop it if you tried.",'you','wh','m',"shrugging with palms up, a small red 'no control' symbol",""),
 ("And here's the funny part. There's almost nothing up there to stand up.",'you','wh','m',"pointing at a nearly bare smooth arm, deadpan",""),
 ("You're a mostly hairless animal. A faint fuzz on your arms, and that's about it.",'you','wh','m',"gesturing at own smooth bald body, a tiny fuzz mark on the arm",""),
 ("So your body just carefully raised a coat of fur you don't have.",'you','wh','m',"a faint dotted-outline ghost fur coat hovering around the bald figure",""),
 ("It flexed a hundred tiny muscles to fluff up basically nothing.",'you','wh','m',"many tiny muscle icons flexing along a bare arm, a small puff of nothing",""),
 ("It's called goosebumps. And it's one of the clearest ghosts in your whole body.",'none','wh','m',"a big bold label card centered on white","GOOSEBUMPS"),
 ("A reflex built for an animal you stopped being a million years ago, still firing tonight, for no reason that helps you.",'ancestor','wh','m',"a faint furry ancestor ghost standing behind the modern bald figure",""),
 ("Because for your furry ancestors, this exact reflex did two life-or-death jobs.",'ancestor','cold','m',"a furry ancestor with fur standing up, two small icons floating: a snowflake and a fist",""),
 ("You kept the reflex. You just lost the fur that made it work.",'you','wh','m',"the bald figure holding an empty fur coat that has fallen off",""),
 ("Stick around, because the strangest trigger of all isn't cold. It isn't even fear.",'you','wh','m',"pointing forward, a snowflake icon and a scared-face icon each with a small grey X",""),
 ("It's a piece of music. And why THAT gives you goosebumps is the weirdest part. We saved it for the end.",'none','warm','m',"a single glowing music note radiating soft warmth","LATER"),
 # SETUP
 ("Let's get one thing clear first, because it reframes everything.",'you','wh','m',"flipping a big card over with both hands",""),
 ("Goosebumps aren't really about your skin. They're about your hair.",'none','wh','m',"a single upright hair with a small arrow, a patch of plain skin crossed out",""),
 ("Or more honestly, about the fur you were supposed to have.",'ancestor','wh','m',"a faint furry coat outline drawn over the bald figure",""),
 ("And like most things about your body, it isn't one story. It's built in layers.",'none','wh','m',"a neat stack of three labeled horizontal layers",""),
 ("One layer is the tiny machine under your skin that yanks each hair upright.",'none','skin','m',"a skin cross-section with a hair and a tiny muscle beside the follicle",""),
 ("One is the two jobs that machine was built to do, back when you were covered in fur.",'none','wh','m',"two icons side by side: a snowflake, and a bristling bigger silhouette",""),
 ("And the deepest layer is why a song, of all things, can still trip it, in a body with no fur left.",'none','warm','m',"a music note over a bare arm with a small spark",""),
 ("We saved that one for the end.",'none','wh','m',"a small closed box with a tag","LATER"),
 ("So let's rewind, past the razors and the sweaters, back to when you were warm because you were furry.",'ancestor','cold','w',"a furry ancestor standing content and warm in gentle snow",""),
 # CHUONG 1
 ("So let's go under the skin, to the machine itself.",'you','skin','w',"the modern figure pointing down into a big skin cross-section diagram",""),
 ("Every hair on your body grows out of a tiny pocket called a follicle.",'none','skin','m',"a single hair follicle pocket in the skin, labeled",""),
 ("And attached to the side of each one is a muscle. A microscopic one.",'none','skin','m',"a tiny muscle attached to the side of the follicle, an arrow pointing to it",""),
 ("It's called the arrector pili, which is Latin, roughly, for the thing that raises the hair.",'none','skin','m',"the tiny muscle highlighted with a little tag","ARRECTOR PILI"),
 ("You have millions of them, one for nearly every hair you own.",'you','wh','m',"the figure covered in many tiny dots, each marking a hair-muscle",""),
 ("When it fires, it contracts and yanks its hair upright.",'none','skin','m',"the muscle contracting and pulling the hair upright, a motion arrow",""),
 ("And as it pulls, it bunches the skin around the follicle into a tiny mound.",'none','skin','cu',"the skin bunching into a small mound around the follicle",""),
 ("A hundred thousand of those mounds at once, and that's a goosebump.",'you','wh','cu',"close on an arm covered in tiny goosebump mounds",""),
 ("The hair standing up is the whole point. The bump is just a side effect.",'none','wh','m',"a raised hair highlighted, the little bump greyed out beside it",""),
 ("Now here's the part that matters. You didn't tell those muscles to do that.",'you','wh','m',"the figure looking at own arm with hands held away, surprised",""),
 ("You can't, really. Try to give yourself goosebumps on command.",'you','wh','m',"the figure straining comically, trying to force goosebumps",""),
 ("For almost everyone, nothing happens.",'you','wh','m',"the figure deadpan, nothing happening, a small 'nope'",""),
 ("Because this machine isn't wired to your will. It's wired to your alarm.",'none','brain','m',"a brain with a wire skipping a 'WILL' icon and going to an 'ALARM' icon",""),
 ("Deep in your nervous system sits the fight-or-flight switch, the one that handles emergencies without asking you first.",'none','brain','m',"a brain with a glowing red fight-or-flight alarm switch",""),
 ("When it trips, it dumps a shot of adrenaline into your blood.",'none','wh','m',"a small burst labeled adrenaline spreading outward into the body",""),
 ("Your heart speeds up. Your pupils widen. And every tiny hair muscle pulls at once.",'you','wh','m',"the figure with a fast red heart, wide pupils, and all arm hairs standing up at once",""),
 ("Which means goosebumps were never really about the cold. Or about fear.",'none','wh','m',"a snowflake and a scared face, both with a grey X",""),
 ("They're about that ancient alarm firing. Cold and fear are just two things that trip it.",'none','wh','m',"one central alarm bell with cold and fear as two small triggers feeding into it",""),
 ("So step back and look at what your body actually built here.",'you','wh','w',"the figure standing small beside a big diagram of the whole reflex",""),
 ("Millions of dedicated muscles. A hair-trigger reflex. A slice of your emergency system.",'none','wh','m',"many tiny muscle icons, a trigger lever, and a small red emergency badge",""),
 ("All of it standing by, around the clock, to adjust the position of your fur.",'you','wh','m',"tiny muscles lined up like little guards along a bare arm",""),
 ("Fur that, on most of you, packed up and left about a million years ago.",'ancestor','wh','m',"a fur coat with a tiny suitcase walking away from the bald figure",""),
 ("It's a factory still running full shifts to make a product nobody orders anymore.",'none','wh','m',"a small factory running full shifts, producing fluff nobody collects",""),
 ("Which raises the obvious question. Why?",'you','wh','m',"the figure tilting its head under a big question mark","?"),
 ("Why would evolution wire up all this machinery just to lift a little hair?",'none','wh','m',"a tangle of machinery connected just to lift one small hair",""),
 ("Because for the animal you used to be, lifting that hair did two different jobs. And both could keep you alive.",'ancestor','cold','m',"a furry ancestor with two icons appearing: a warm snow-coat and a bristled-bigger shape",""),
 # CHUONG 2
 ("The first job was simple. Keep you warm.",'none','wh','m',"a job card number one with a warm sun and thermometer","WARMTH"),
 ("When a furry animal gets cold, those little muscles fire, and the fur stands up.",'none','cold','m',"a cute furry animal in the cold with its fur standing up",""),
 ("And a raised coat traps a layer of air right against the skin.",'none','cold','cu',"raised fur trapping a layer of little air dots against the skin",""),
 ("That trapped air is insulation. It's the whole reason a puffy coat keeps you warm.",'none','cold','m',"a puffy coat with a labeled trapped-air insulation layer",""),
 ("So the animal just... thickens. Same fur, more warmth, in about a second.",'none','cold','m',"an animal visibly puffing up thicker, same fur more volume",""),
 ("Watch a bird on a freezing morning. It puffs into a little round ball.",'none','cold','w',"a cute little bird puffed into a round ball on a branch in the cold",""),
 ("Same trick. Fluff the coat, trap the air, hold the heat.",'none','cold','m',"the puffed round bird with cozy air-trap arrows",""),
 ("For your ancestors, shivering through a cold night, this was an automatic thermostat.",'ancestor','cold','w',"a furry ancestor shivering at night, fur rising by itself",""),
 ("Cold hits, hair goes up, coat gets thicker, no thinking required.",'ancestor','cold','m',"a cold gust hitting the ancestor, fur going up automatically",""),
 ("And you still run that exact program. Every time you're cold, the muscles fire on schedule.",'you','home','m',"the modern bald figure feeling cold, arm hairs rising",""),
 ("There's just one problem. You're fluffing a coat that isn't there.",'you','home','m',"the figure with goosebumps but only a faint empty fur outline, no real coat",""),
 ("So you get the bumps, a faint prickle, and precisely zero extra warmth.",'you','home','cu',"close on a bumpy bare arm, shivering, a small blue cold mark, no warmth",""),
 ("A million years of engineering, and it ends with you reaching for a hoodie.",'you','home','m',"the figure reaching for a hoodie on a hook, defeated",""),
 ("The second job was stranger, and a lot more dramatic. Look bigger.",'none','wh','m',"a job card number two with a puffed-up bristling silhouette","LOOK BIGGER"),
 ("When a furry animal is threatened, the same muscles fire, everywhere, at once.",'none','sav','m',"a cute furry animal threatened, all its fur firing up at once",""),
 ("And suddenly the animal isn't its normal size. It's a puffed-up, bristling version of itself.",'none','sav','m',"the animal suddenly puffed into a bristling, bigger version of itself",""),
 ("You've seen a cat do it. The arched back, the bottle-brush tail, twice its size in an instant.",'none','wh','m',"a cute cat with an arched back and a huge bottle-brush puffed tail, twice its size",""),
 ("A dog raises its hackles. A bear looks even more enormous. The message is the same.",'none','sav','m',"a cute dog with raised hackles beside a big brown bear looking enormous",""),
 ("I am bigger than you thought. And this is going to be more trouble than it's worth.",'none','wh','m',"a big bold threat sign","BACK OFF"),
 ("It's a bluff, written in fur. And a good bluff can end a fight before it starts.",'none','sav','m',"two animals facing off, one bristled bigger, a tense bluff standoff",""),
 ("For your ancestors, squaring up to a rival or a predator, that bristle was a free threat.",'ancestor','sav','m',"a furry ancestor squaring up to a shadowy predator, fur bristled, looking bigger",""),
 ("Now picture you, doing the exact same thing.",'you','home','m',"cut to the modern bald figure attempting the same, starting to puff up",""),
 ("Something frightens you, and your body loyally tries to puff up to twice its size.",'you','home','m',"the figure scared, straining to look huge and threatening",""),
 ("And what it produces is a light tingle on two mostly bare arms. You have never intimidated anyone less.",'you','home','cu',"a faint tingle on two skinny bare arms, deadpan, intimidating no one",""),
 # CHUONG 3 / TWIST
 ("So that's the reflex. Warmth, and a bluff. Both built for fur. Both useless on you now.",'none','wh','m',"two job cards (warmth + bigger) both stamped 'for fur' and greyed out",""),
 ("Which should be the end of the story. A dead machine, twitching out of habit.",'none','wh','m',"a small dead machine twitching out of habit",""),
 ("Except there's a third trigger. And it fits none of this.",'none','warm','m',"a third glowing mysterious trigger card appearing",""),
 ("Because sometimes you get goosebumps when you're not cold, and nothing is threatening you at all.",'you','warm','m',"the figure calm, not cold, nothing threatening, yet goosebumps rising",""),
 ("A song swells at exactly the right moment. A choir hits a note that goes straight through you.",'you','warm','m',"the figure listening as a music note swells and passes straight through",""),
 ("You stand somewhere vast, or hear something true, and a wave of it rolls up your arms and neck.",'you','warm','w',"the figure standing before something vast, a wave rolling up the arms and neck",""),
 ("No cold. No danger. Just... a feeling too big for your body to hold quietly.",'you','warm','cu',"an awe-struck moved face, a feeling too big to hold, a gentle glow",""),
 ("Scientists have a name for it. They call it frisson.",'none','warm','m',"a soft glowing label card","FRISSON"),
 ("And it's the strangest thing your goosebumps do, because on paper it makes no sense.",'you','warm','m',"the figure puzzled, scratching head, a small question mark",""),
 ("Why would an alarm built for freezing nights and charging animals fire for a violin?",'none','warm','m',"an alarm bell beside a violin, an odd pairing with a question mark",""),
 ("The best answer we have is a little haunting.",'you','warm','m',"the figure leaning in with a slightly haunted, curious face",""),
 ("That surge of awe, of being deeply moved, runs through the same ancient wiring as fear.",'none','brain','m',"a brain with a wave of awe running through the same wiring as a fear signal",""),
 ("To your nervous system, a wave of overwhelming emotion looks a lot like a wave of alarm.",'none','brain','m',"the brain reading a big emotion wave as if it were an alarm, overlapping signals",""),
 ("Something huge is happening. Pay attention. All systems fire.",'none','wh','m',"a bold sign with systems lighting up","ALL SYSTEMS FIRE"),
 ("And one of the systems that fires is the oldest one. The one that raises the fur.",'none','skin','m',"among the firing systems, the oldest one lights up: the tiny hair-raiser muscle",""),
 ("So sit with what that actually means.",'you','warm','m',"the figure sitting quietly, taking it in",""),
 ("The exact reflex that once puffed your ancestors against the cold, and bristled them against a leopard,",'ancestor','sav','m',"a furry ancestor bristling against both cold and a faint leopard",""),
 ("is the one that lifts the hair on your arms when a piece of music breaks your heart.",'you','warm','m',"the modern figure moved to tears by music, arm hair rising, warm glow",""),
 ("A survival response, built for the worst nights of your life, quietly repurposed for the most beautiful ones.",'you','warm','w',"a dark cold night gently morphing into a glowing warm concert around the figure",""),
 ("The predator alarm, hijacked by a song.",'none','warm','m',"a predator-alarm bell with a small music note glowing inside it",""),
 # KET
 ("So. Why do you get goosebumps?",'you','wh','m',"the figure standing with the big title question above","?"),
 ("Not because your skin is cold. The skin is just where you see it happen.",'you','wh','m',"a cold skin patch with a grey X, labeled 'not the cause'",""),
 ("You get goosebumps because a reflex built to raise fur never got the message that the fur is gone.",'ancestor','wh','m',"the furry-ancestor reflex still firing on the bald modern figure",""),
 ("A machine for warmth and for looking dangerous, still fully staffed, on a body that traded its coat for sweat and bare skin a million years ago.",'you','wh','m',"a fur coat traded for sweat drops and bare skin, a million-year arrow",""),
 ("The cold still trips it. The fear still trips it.",'you','cold','m',"the figure cold with goosebumps and a faint fur ghost",""),
 ("And every so often, so does something beautiful.",'you','warm','m',"the figure moved by beauty, goosebumps, a warm glow",""),
 ("So the next time your skin prickles and the hair rises on your arms, over nothing you can point to,",'you','wh','cu',"close on an arm prickling, hairs rising, over nothing visible",""),
 ("don't brush it off as a shiver.",'you','wh','m',"the figure about to shrug it off, then pausing",""),
 ("That's the animal you used to be, reaching, one more time, for a coat that isn't there.",'ancestor','wh','m',"the faint animal-you-used-to-be reaching for a coat that isn't there",""),
 ("It's the same flinch as jerking awake, the same ghost as fearing the dark.",'you','wh','w',"three faint linked icons: a jerk-awake in bed, a fearful eye in the dark, and goosebumps",""),
 ("A body running ancient software, in a world that changed faster than your biology could.",'none','wh','m',"a body running an old floppy-disk 'ancient software' in a modern world",""),
 ("The fur is gone. The reflex stayed.",'ancestor','wh','m',"the fur faded away, the reflex still glowing on",""),
 ("And once in a while, when a song hits just right, that useless old reflex does the one thing it was never built for.",'you','warm','m',"the useless old reflex sparking into something new, a warm spark",""),
 ("It makes you feel something.",'you','warm','cu',"the figure feeling something, a single moved expression, gentle glow",""),
 ("That prickle on your arm isn't a glitch. It's a receipt from every ancestor who ever bristled in the dark and lived.",'you','wh','m',"a small receipt printed with tiny bristling-ancestor stamps",""),
 ("If you made it to the end, tell me one thing in the comments. What song, every single time, no matter what, gives you goosebumps?",'you','wh','m',"the figure beside a big comment box with a music note icon","COMMENT"),
]

def textpart(t):
    return ('a small "%s" in bold white ALL-CAPS letters on a little red tag.' % t) if t else "no text or letters."

def build(char, action, bg, frame, text):
    subj = action if char == 'none' else (CHAR[char] + action)
    return "%s %s. Framing: %s %s %s %s %s" % (STYLE, subj, FRAME[frame], CONSIST, SCENE[bg], textpart(text), NEG)

shot_lines, prompts = [], []
for i,(line,ch,bg,fr,act,txt) in enumerate(DATA,1):
    n="%03d"%i
    shot_lines.append("%s  %s"%(n,line))
    prompts.append("%s.\n%s"%(n,build(ch,act,bg,fr,txt)))

open(os.path.join(HERE,"Script_Video07_narration.txt"),"w").write("\n".join(l for (l,*_) in DATA))
open(os.path.join(HERE,"SHOTLINES_FULL.txt"),"w").write("\n".join(shot_lines))
open(os.path.join(HERE,"PROMPTS_FULL.txt"),"w").write("\n\n".join(prompts))
print("Shots:",len(DATA))
