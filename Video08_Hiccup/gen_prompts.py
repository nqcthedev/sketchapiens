# -*- coding: utf-8 -*-
# Generator prompt anh — Video08 "Why Do You Hiccup?"
# Xuat: Script_Video08_narration.txt · SHOTLINES_FULL.txt · PROMPTS_FULL.txt
import os
HERE = os.path.dirname(os.path.abspath(__file__))

STYLE = ("Clean flat 2D cartoon explainer with smooth, even, confident medium-bold black outlines "
         "(single clean strokes, not scratchy, not wobbly, not heavy marker), a crisp minimalist educational look,")

CONSIST = ("The people are clean STICK-FIGURE doodles: a LARGE round white-filled head with a simple expressive face "
           "(two big round white eyes with small black pupils, thin expressive eyebrows, a tiny mouth, no nose) sitting on a THIN body "
           "made of clean black lines (a single medium-weight line for the torso plus thin noodle arms and legs), NOT a filled or solid body shape, "
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
 'baby': ("a tiny cute stick-figure baby, a small round white bald head slightly big for its little curled stick body, a simple sweet face, "),
 'farmer': ("the recurring old farmer stickman, the same plain black-outline stick figure with a round BALD white head wearing a simple flat straw hat "
            "and a plain bib-overalls shape on the torso, thin noodle arms and legs, "),
 'none': "",
}

FRAME = {
 'm': "a medium shot, the subject drawn big and centered with clean breathing space around it.",
 'w': "a WIDE establishing shot, the subject fairly small inside a large scene.",
 'cu': "a tight CLOSE-UP filling most of the frame.",
}

SCENE = {
 'wh':   "ONE single scene on a plain WHITE background with lots of clean empty space and a soft light-grey shadow under the subject; RED accent for danger/warnings, GREEN for a yes/check, a small YELLOW lightbulb for an idea,",
 'water':"ONE single scene: a flat blue underwater background with a few tiny round bubble dots and soft wavy lines, a calm aquatic feel, lots of clean empty space,",
 'edge': "ONE single scene: a shallow prehistoric riverbank, flat tan mud meeting flat shallow blue water under a plain pale sky, a few simple reeds, lots of clean space,",
 'body': "ONE single scene on a plain WHITE background: a large simple cross-section diagram of a human torso showing two lungs and the dome-shaped diaphragm muscle just below them, clean black outlines, small black labels and arrows, lots of empty space,",
 'nerve':"ONE single scene on a plain WHITE background: a large simple front-view outline of a human body showing the spine, the dome diaphragm low in the torso, and a single highlighted nerve line, clean black outlines, small labels and arrows, lots of empty space,",
 'brain':"ONE single scene on a plain WHITE background: one big simple cartoon brain shape as the focus, clean flat pink-beige fill with black outline, small black labels and arrows, lots of empty space,",
 'gilld':"ONE single scene on a plain WHITE background: a simple side diagram of a tadpole head, water entering the mouth, passing across the gills, and a small flap valve, clean black outlines, blue arrows and small labels, lots of empty space,",
 'home': "ONE single scene: a simple flat modern room, a plain muted wall, minimal furniture, a soft grey shadow, muted tone,",
 'womb': "ONE single scene: a soft warm rounded pinkish womb space, a gentle curved outline, a calm muted glow, lots of clean empty space,",
 'farm': "ONE single scene: a simple flat old farmyard, a plain warm-tan ground, a small barn silhouette in the distance, a plain pale sky, muted tone,",
 'night':"ONE single scene: a flat dark-navy night background with a few tiny white star dots, a soft shadow, a quiet nighttime mood, lots of clean empty space,",
}

# (shotline, char, bg, frame, action, text)
DATA = [
 # HOOK
 ("You're talking. Mid sentence. Nothing unusual.",'you','home','m',"standing casually mid-conversation, mouth open talking, a small speech bubble with a wavy line",""),
 ("And then, without asking you, your body cuts you off.",'you','home','m',"jolting slightly, a small red spark bursting at the chest, the speech bubble cut short",""),
 ("Hic.",'none','wh','cu',"a big bold text card centered on white with a tiny snap mark","HIC"),
 ("You didn't do that. Something in your chest did.",'you','wh','m',"looking down at own chest with surprise, hands held away, a small red spark glowing inside the chest",""),
 ("You can't start it. You can't stop it. And while it lasts, you are not the one in charge of you.",'you','wh','m',"hands up helpless, a small control panel with a red no-entry slash over its buttons",""),
 ("A grown adult, quietly overruled by their own ribcage.",'you','wh','m',"standing deadpan as a simple rib-cage outline on its own chest glows, overruled, a flat unimpressed face",""),
 ("We call it a glitch. A hiccup. A small thing that went slightly wrong.",'none','wh','m',"a small label card with a tiny glitch/error icon","GLITCH?"),
 ("It didn't.",'none','wh','cu',"a short bold text card on white","IT DIDN'T"),
 ("That stupid little spasm is one of the oldest, best preserved things your body still knows how to do.",'you','wh','cu',"close on the chest with a small glowing spasm mark carrying a tiny ancient fossil stamp",""),
 ("It's older than every word you've ever spoken. Older than your species. Older than the first creature that ever crawled out of the water onto dry land.",'none','edge','w',"a small fishapod crawling from shallow blue water onto tan mud, a long faded timeline arrow stretching across",""),
 ("Because that is exactly where it comes from.",'none','water','m',"a single cute fish in blue water with an arrow pointing to it labeling it the origin",""),
 ("A hiccup is a ghost. The ghost of a fish. Still moving, right now, inside your chest.",'you','wh','cu',"close on the modern figure's chest, a faint pale ghost-fish glowing and moving inside it",""),
 ("And the reason evolution let you keep it, for three hundred and seventy million years, is stranger than almost anything else your body does.",'none','wh','m',"a mysterious closed box with a question mark and a small clock beside it","370 MYA"),
 # SETUP
 ("So let's actually answer this.",'you','wh','m',"rolling up sleeves, ready to explain, a small forward answer arrow",""),
 ("Why do you hiccup?",'you','wh','m',"standing under a big bold title question mark","WHY?"),
 ("Not the useless version your doctor gives you. The real one.",'you','wh','m',"pushing aside a dull grey clipboard toward a bright glowing door labeled the real one",""),
 ("Because here's the problem with a hiccup. It does nothing.",'none','wh','m',"a single hiccup icon sitting on a card doing nothing, a flat grey zero",""),
 ("It doesn't help you digest food. It doesn't clear your throat. It doesn't warn you about anything.",'none','wh','m',"three greyed icons each with a small red X: a stomach, a throat, a warning triangle",""),
 ("Sneezing protects you. Coughing protects you. Even a yawn does something.",'none','wh','m',"three working icons each with a green check: a sneeze burst, a cough, a yawn",""),
 ("A hiccup just interrupts you and leaves.",'you','wh','m',"a tiny hiccup icon popping up then walking away, the figure shrugging",""),
 ("So if it's useless, evolution should have deleted it a hundred million years ago.",'none','wh','m',"a trash bin with a hiccup icon over it and a big red delete arrow, an old calendar",""),
 ("It didn't. It kept it. In you. In every baby. In almost every mammal alive.",'you','wh','m',"the hiccup icon kept, shown over three figures in a row: an adult, a tiny baby, and a cute cat, each with a tiny hiccup mark",""),
 ("And things that survive that long usually survive for a reason.",'none','wh','m',"a small survival badge glowing over a long horizontal timeline",""),
 ("The reason isn't in your lungs. It's in your history.",'none','wh','m',"a lung icon with a grey X beside a glowing history scroll timeline, an arrow pointing to the scroll",""),
 # CHUONG 1 — nac la gi
 ("Start with what a hiccup actually is, physically.",'you','body','w',"the modern figure pointing into a big torso cross-section diagram of lungs and the diaphragm",""),
 ("Just under your lungs sits a dome of muscle called the diaphragm.",'none','body','m',"the dome-shaped diaphragm muscle just below the two lungs, highlighted and labeled","DIAPHRAGM"),
 ("It's the muscle you breathe with. It's pulling down right now, filling your lungs, and you never once told it to.",'none','body','m',"the diaphragm pulling downward with motion arrows, the lungs filling with air, a small auto gear icon",""),
 ("A hiccup begins when that muscle suddenly jerks. Sharp. Hard. Out of nowhere.",'none','body','cu',"close on the diaphragm suddenly jerking down sharply, a red jolt burst",""),
 ("Your lungs yank in a fast gulp of air you never asked for.",'none','body','m',"the lungs yanking in a fast gulp of air, big inward arrows",""),
 ("And then, about thirty five thousandths of a second later, a flap at the top of your windpipe slams shut on top of it.",'none','body','m',"at the top of the windpipe a little flap valve slamming shut on the incoming air, a tiny clock, a snap mark",""),
 ("That slam has a name. It's the sound. Hic.",'none','wh','cu',"a bold text card with a small snap/clap mark","HIC"),
 ("Air rushing in, a trapdoor snapping shut to stop it.",'none','body','m',"a simple trapdoor snapping shut over an inward air arrow, a clean diagram",""),
 ("That's the whole event.",'none','wh','m',"a small summary card showing the two-step icon: a gulp arrow and a snapping flap",""),
 ("Now look at what your brain just did there.",'you','brain','m',"the modern figure pointing at a big brain with a spotlight on it",""),
 ("It ran that entire sequence without asking you, and it locked you out of stopping it.",'none','brain','m',"the brain running a sequence arrow that skips a greyed WILL icon and clamps a small padlock on a stop button",""),
 ("Same as goosebumps rising on your arm. Same as your leg kicking you awake as you fall asleep.",'you','wh','w',"two faint linked side icons: goosebumps rising on a forearm, and a figure kicking awake in bed",""),
 ("This is a reflex. And a reflex is just a program your body kept because, once, it mattered.",'none','wh','m',"a small old program disk labeled reflex with a note that it once mattered","REFLEX"),
 # CHUONG 2 — con ca
 ("So when did this reflex matter? What was it for?",'you','wh','m',"the figure tilting its head under a big question mark","?"),
 ("To find that, you have to go back further than you have ever been asked to imagine.",'none','wh','m',"a long timeline arrow sweeping far back to the left past small faded icons",""),
 ("Not to cavemen. Not to the first apes.",'none','wh','m',"a caveman icon and an ape icon side by side, each with a small grey X",""),
 ("Three hundred and seventy million years. To water.",'none','water','w',"a big bold label floating over wide flat blue water","370 MYA"),
 ("Picture a tadpole. You've seen one. A little body, a tail, living underwater.",'none','water','m',"a single cute dark-green tadpole with a round body, a little face and a curvy tail swimming in blue water",""),
 ("A tadpole breathes with gills. And breathing with gills is not simple.",'none','gilld','m',"the tadpole head diagram with the gills clearly marked and labeled","GILLS"),
 ("It has to gulp a mouthful of water, push that water back across its gills to pull the oxygen out, and then close a flap so the water doesn't flood its lungs.",'none','gilld','m',"water entering the tadpole's mouth, pushed across the gills with blue arrows, and a little flap closing before the lungs",""),
 ("Gulp the water in. Push it across. Snap the flap shut.",'none','gilld','m',"three little labeled steps: gulp an in-arrow, push an across-arrow, snap a closing flap",""),
 ("Read that one more time. A sharp gulp, then a flap slamming shut to guard the airway.",'none','gilld','m',"a highlighted close on a sharp gulp then the flap slamming shut with a small shield guard icon",""),
 ("You already know that rhythm. Your chest just did it.",'you','wh','m',"the modern figure with a tadpole-gulp icon and a chest hiccup icon linked by an equals sign",""),
 ("In 2003, a physiologist named Christian Straus put this side by side.",'none','wh','m',"a scientist stick figure with small round glasses placing two cards side by side on white","STRAUS 2003"),
 ("He compared the exact nerves and muscles that fire during a human hiccup to the ones a tadpole uses to breathe.",'none','wh','m',"two side-by-side diagrams being compared: a human hiccup's nerves and muscles, and a tadpole breathing",""),
 ("They were the same pattern.",'none','wh','m',"the two diagrams overlapping perfectly with a big green equals sign","MATCH"),
 ("Same wiring. Same motion. The same ancient breathing program, still running in a body that hasn't had a gill in over three hundred million years.",'you','wh','m',"the modern figure with a faint tadpole breathing pattern glowing over its chest",""),
 ("And if that sounds like a coincidence, the next part is where it stops being one.",'none','wh','m',"a card reading coincidence being flipped over to reveal more evidence behind it",""),
 ("A hiccup doesn't behave like anything a human lung should.",'none','body','m',"a lung diagram with a puzzled expression and a small question mark, not behaving normally",""),
 ("When the carbon dioxide in your blood goes down, hiccups get worse. When it goes up, they fade.",'none','wh','m',"a gauge labeled CO2: an arrow down enlarges a hiccup icon, an arrow up shrinks it","CO2"),
 ("Your lungs don't work like that. But a gill does. That is exactly how water breathing is controlled.",'none','gilld','m',"a lung icon with a grey X beside a gill diagram with a green check",""),
 ("There's even a drug, baclofen, that can switch hiccups off.",'none','wh','m',"a small medicine bottle flicking a hiccup icon toggle to off","BACLOFEN"),
 ("And it switches off the same water breathing reflex in amphibians.",'none','water','m',"the same medicine bottle switching off a cute green frog's breathing in blue water",""),
 ("Your hiccup isn't a lung malfunctioning. It's a gill, still firing for water that isn't there anymore.",'you','wh','m',"the modern figure's chest showing a tiny gill still flapping over a small patch of dry cracked ground",""),
 # CHUONG 3 — Tiktaalik
 ("So how did a fish reflex end up in your chest?",'you','wh','m',"the figure with a fish icon and an arrow pointing to its chest, a question mark","?"),
 ("Something had to carry it out of the water. And we know roughly what that something looked like.",'none','edge','w',"a shallow prehistoric riverbank, something small stirring at the water's edge, a curious spotlight",""),
 ("About three hundred and seventy five million years ago, there was a creature we now call Tiktaalik.",'none','edge','m',"a cute olive-green Tiktaalik fishapod with a flat wide head, little eyes on top, green scales and stubby bony front fins, in shallow water","TIKTAALIK"),
 ("It was found in the Arctic, in rock that was once a shallow riverbed, by a team led by a scientist named Neil Shubin.",'none','wh','m',"a scientist stick figure with a small pickaxe kneeling by a slab of rock holding a Tiktaalik fossil, a hint of ice","NEIL SHUBIN"),
 ("Tiktaalik was a fish. Mostly. It had scales and gills and lived in water.",'none','water','m',"the cute olive-green Tiktaalik fishapod in blue water showing its scales and gills, mostly a fish",""),
 ("But it also had something new. Flat, strong fins with bones inside them that bent like a wrist.",'none','edge','cu',"close on the Tiktaalik's flat front fin with small bones inside that bend like a wrist, labeled",""),
 ("It could prop itself up. It could push its head out of the water and breathe air.",'none','edge','m',"the Tiktaalik propping itself up on its fins, pushing its head out of the water to breathe, a small air puff",""),
 ("It was a fish learning to do push ups at the edge of the world.",'none','edge','m',"the cute Tiktaalik comically doing a little push up at the water's edge, deadpan",""),
 ("Creatures like this crawled out of the shallows and never fully went back.",'none','edge','w',"several small fishapods crawling from the shallows onto land, a one-way arrow forward",""),
 ("Their fins became legs. Their gulping, water clearing reflex came along for free.",'none','edge','m',"fins morphing into legs with an arrow, and a small gulp-and-flap reflex icon riding along with a zero price tag",""),
 ("Every amphibian, every reptile, every mammal, every person, is descended from an animal that made that move.",'none','wh','m',"a family tree fanning out to a frog, a lizard, a cat and a person, all from a single fish at the root",""),
 ("You are the great, great, unthinkably great grandchild of a fish that decided to breathe air.",'you','wh','m',"the modern figure shaking hands with a tiny cute fish wearing a small label reading grandparent",""),
 ("And it packed light. It brought its skeleton, its spine, its jaws.",'none','edge','m',"the fishapod carrying a tiny suitcase packed with a small skeleton, a spine and a jaw icon",""),
 ("And, tucked deep in the wiring, it brought the hiccup.",'none','wh','m',"deep inside the suitcase wiring, a small glowing hiccup icon","HIC"),
 # CHUONG 4 — day than kinh di vong
 ("Here's the fingerprint it left behind. The proof is still inside you.",'you','nerve','m',"the modern figure pointing at a body outline, a small fingerprint mark glowing on it",""),
 ("Your diaphragm, the muscle that hiccups, is controlled by a nerve called the phrenic nerve.",'none','nerve','m',"the body outline with the low diaphragm and a single highlighted nerve line labeled","PHRENIC NERVE"),
 ("You'd expect that nerve to be short. The diaphragm sits low in your body, so the wire should run straight to it.",'none','nerve','m',"a dotted short straight expected path from the mid-spine to the diaphragm, an expected note",""),
 ("It doesn't.",'none','wh','cu',"a short bold text card on white","IT DOESN'T"),
 ("The phrenic nerve starts up in your neck. Near the top of your spine.",'none','nerve','m',"the real nerve starting way up at the neck near the top of the spine, a bright start dot",""),
 ("And then it travels all the way down, past your heart, to reach the diaphragm far below.",'none','nerve','m',"the highlighted nerve line traveling all the way down past a small heart to the diaphragm far below",""),
 ("It's a long, absurd, looping detour. If you were designing a body from scratch, you would never do this.",'none','nerve','m',"the long looping nerve detour highlighted in red, a small facepalm bad-design note",""),
 ("But evolution wasn't designing from scratch. It was renovating a fish.",'none','wh','m',"evolution as a builder in a hard hat renovating an old fish blueprint rather than drawing a new one",""),
 ("In our fish ancestors, the muscles that became the diaphragm sat up near the gills, in the neck.",'none','nerve','m',"a simple fish outline where the future-diaphragm muscles sit up near the gills in the neck, highlighted",""),
 ("As the body changed and the diaphragm slid down into the chest, it dragged its nerve along behind it.",'none','nerve','m',"the diaphragm sliding downward into the chest and dragging its nerve line behind it, a stretch arrow",""),
 ("The wire never got rerouted. It just stretched.",'none','nerve','m',"the nerve wire simply stretched long like an elastic band, never rerouted",""),
 ("So the next time you hiccup, that spasm is being ordered by a nerve still running the route it ran in a fish.",'you','wh','m',"the modern figure hiccuping while the long neck-to-diaphragm nerve glows as the one giving the order","HIC"),
 ("Neil Shubin, the same man who dug up Tiktaalik, calls this one of the clearest leftovers of our life in water.",'none','wh','m',"the scientist stick figure with glasses standing beside a small Tiktaalik, pointing at the glowing nerve",""),
 ("You are not just descended from a fish. You are still, quietly, wired like one.",'you','wh','m',"the modern figure with a faint fish nervous system glowing softly inside the human body",""),
 # CHUONG 5 — vi sao khong bi xoa
 ("Which brings us back to the question that should still be bothering you.",'you','wh','m',"the figure back at a nagging question mark hovering over its head","?"),
 ("Evolution deletes what you don't use. So why keep a dead fish reflex for three hundred and seventy million years?",'none','wh','m',"a delete key hovering over a dead fish reflex card that refuses to delete, a long timeline",""),
 ("Because somewhere along the way, it got a second job.",'none','wh','m',"the reflex icon receiving a small badge","2ND JOB"),
 ("The circuit that fires a hiccup, that sharp gulp and snap, turned out to be perfect for one of the most important things a mammal ever does.",'none','wh','m',"the glowing gulp-and-snap circuit icon pointed toward a very important mammal task ahead",""),
 ("Feeding as a newborn.",'baby','wh','m',"a tiny stick baby feeding happily, a bold label","FEEDING"),
 ("When a baby drinks milk, it has to pull the milk in and keep it out of its lungs at the same time.",'baby','wh','m',"a tiny stick baby drinking milk, one arrow pulling milk in and a little flap keeping it out of the lungs",""),
 ("Gulp, and snap the airway shut. The exact same move as a hiccup. The exact same move as a gill.",'none','wh','m',"a baby gulp-and-snap icon linked by equals signs to a hiccup icon and a tadpole gulp icon",""),
 ("So the old program was never deleted. It was quietly promoted.",'none','wh','m',"the old program disk getting a small promoted badge and an up arrow","PROMOTED"),
 ("And that's why hiccups show up earliest, in the smallest, most unfinished humans there are.",'baby','womb','m',"a tiny curled stick baby, the smallest most unfinished human, with a small hiccup mark",""),
 ("A baby hiccups in the womb, curled in fluid, before it has taken a single breath of air.",'baby','womb','m',"a tiny stick baby curled in the soft womb space, a little hiccup mark, before any breath",""),
 ("Ultrasounds catch it constantly. A tiny body, hiccuping, with lungs that have never once been used.",'none','wh','m',"a simple ultrasound screen showing a tiny curled baby with a little hiccup mark","ULTRASOUND"),
 ("Some scientists think those hiccups are rehearsal, teaching the breathing muscles to fire before they're ever needed.",'baby','womb','m',"the tiny baby hiccuping as a rehearsal, small breathing muscles practicing with a little note",""),
 ("So before you could think, before you could breathe, before you were even finished, you were already running the oldest program in your body.",'baby','womb','m',"the unfinished tiny baby already running an ancient glowing program icon","OLDEST PROGRAM"),
 # CHUONG 6 — ban khong don doc
 ("And here is how you know, for certain, that this is inherited and not just some human quirk.",'you','wh','m',"the modern figure holding up a small proof tag, confident",""),
 ("You are not the only one who does it.",'you','wh','m',"the figure pointing sideways toward a group of animals",""),
 ("Cats hiccup. Dogs hiccup. Puppies and kittens hiccup constantly, especially as babies.",'none','wh','m',"a cute grey cat and a cute light-brown dog, plus a tiny kitten and puppy, each with a small hiccup mark",""),
 ("Rats hiccup. Horses do a version of it. Nearly every mammal carries the same reflex.",'none','wh','m',"a cute grey rat and a cute brown horse, each with a small hiccup mark, a note nearly every mammal",""),
 ("It even tracks with how we're related. The animals that share it are the animals that share our ancestor.",'none','wh','m',"a family tree where the branches carrying the hiccup mark are highlighted as the ones sharing the ancestor",""),
 ("This isn't a bug that happened to each of us separately.",'none','wh','m',"several separate hiccup icons with a big red X over the idea of separate independent origins",""),
 ("It's a single, ancient inheritance, handed down the whole mammal family tree from the same creature that crawled out of the water.",'none','wh','m',"a single glowing inheritance line flowing down the whole mammal family tree from one fish at the root",""),
 ("When your dog hiccups in its sleep and its leg twitches, you're not watching a cute little accident.",'none','night','m',"a cute light-brown dog asleep at night, hiccuping, its leg twitching, tiny z's",""),
 ("You're watching the same three hundred and seventy million year old reflex you have, firing in a cousin.",'none','night','m',"the sleeping dog with the same ancient reflex glowing on it, a small label cousin",""),
 ("The whole family kept it.",'none','wh','m',"a group of animals and a person all holding the same hiccup icon together",""),
 ("And nobody in the family can turn it off.",'none','wh','m',"a locked off-switch toggle that none of them can reach","NO OFF SWITCH"),
 # CHUONG 7 — sao can khong duoc
 ("Which is the part everyone actually wants to know. How do you make it stop?",'you','wh','m',"the figure asking urgently, a big question mark","STOP?"),
 ("You already know the folk cures. Hold your breath. Drink water upside down. Swallow a spoon of sugar. Get someone to scare you.",'you','wh','m',"four small cure icons around the figure: puffed cheeks holding breath, an upside-down water glass, a spoon of sugar, a surprise scare",""),
 ("And sometimes they work. But not for the reason people think.",'none','wh','m',"some cure icons with green checks and a puzzled not-the-reason-you-think note",""),
 ("Remember what a hiccup responds to. Carbon dioxide.",'none','wh','m',"a reminder card with a small CO2 molecule icon","CO2"),
 ("When you hold your breath, carbon dioxide builds up in your blood, and that rising level quiets the reflex. The gill logic, used against itself.",'you','wh','m',"the figure holding its breath, a CO2 gauge rising, a hiccup icon quieting down",""),
 ("The other cures do something different. They hit a nerve.",'none','brain','m',"a small lightning bolt striking a nerve line",""),
 ("A big nerve called the vagus runs from your gut up to your brain, and you can jolt it. A spoon of sugar. A splash of cold water. A sudden fright.",'none','nerve','m',"the vagus nerve running from the gut up to the brain, jolted, with a sugar spoon, a cold splash and a fright icon","VAGUS"),
 ("That jolt basically interrupts the loop, like smacking a stuck machine.",'none','wh','m',"a hand smacking a small stuck machine, a looping arrow breaking apart",""),
 ("But notice something. None of it is reliable.",'none','wh','m',"several cure icons each stamped with an unreliable question mark, hit or miss",""),
 ("There is no button. No cure that works every time, for everyone.",'none','wh','m',"a big missing off-button spot with a red slash","NO BUTTON"),
 ("Because you are not fixing a modern problem. You are trying to argue with a reflex older than your ability to argue.",'you','wh','m',"the small modern figure arguing hopelessly with a giant ancient reflex creature",""),
 ("It doesn't listen to you. It never did.",'none','wh','m',"the giant reflex wearing earmuffs, ignoring the tiny figure",""),
 ("It runs on a circuit that was set, and locked, long before your species had a single thought in its head.",'none','wh','m',"an ancient circuit sealed with a padlock beside a dim empty thought bubble","LOCKED"),
 ("And once in a very long while, that circuit gets stuck, and does not come back.",'none','wh','m',"the reflex switch jammed in the on position, a small red warning mark",""),
 # CHUONG 8 — Osborne
 ("This is the part I saved for the end.",'none','wh','m',"a small saved box being opened for the finale","SAVED"),
 ("Because a reflex with no off switch has a worst case. And a man lived it.",'none','wh','m',"a jammed off-switch casting a long human-shaped shadow",""),
 ("His name was Charles Osborne. An American farmer.",'farmer','farm','m',"the farmer stickman standing in a simple farmyard, a small name tag","CHARLES OSBORNE"),
 ("In 1922, by one account, he was hoisting a hog to slaughter when he fell and hit the ground hard.",'farmer','farm','m',"the farmer lifting a cute pink hog, slipping and falling back, a motion arrow and a small impact star","1922"),
 ("Something deep in his brain, right around where this ancient reflex is wired, was knocked loose.",'farmer','farm','cu',"close on the farmer's head with a small spark near the lower brain area where the reflex lives",""),
 ("And Charles Osborne started to hiccup.",'farmer','farm','m',"the farmer starting to hiccup, a small hiccup mark","HIC"),
 ("He did not stop for sixty eight years.",'none','wh','cu',"a big bold text card","68 YEARS"),
 ("Every waking hour. Through his sleep. Through two marriages. Through decades of ordinary life.",'farmer','wh','m',"the farmer hiccuping through it all: a sleep z, two small wedding rings, a long calendar of decades",""),
 ("Twenty to forty times a minute, for most of a lifetime. By one estimate, around four hundred and thirty million hiccups.",'none','wh','m',"a counter ticking 20 to 40 per minute beside a huge total number","430 MILLION"),
 ("Doctors tried everything they had. Nothing reached it.",'none','wh','m',"a doctor stick figure surrounded by failed tools and pills, all with red X marks",""),
 ("And then in 1990, with no warning and no explanation anyone could give, it simply stopped.",'farmer','wh','m',"the farmer as the hiccups abruptly stop, a sudden quiet mark and a question mark","1990"),
 ("He lived one more quiet year, and then he died.",'farmer','wh','m',"the farmer resting peacefully in a calm quiet scene, a soft gentle fade, respectful",""),
 ("Sit with what that means. A reflex that does nothing, that you never chose, that helps you not at all, can switch on and run for the rest of your life.",'you','wh','m',"the modern figure sitting quietly beside a long lifeline with a small hiccup mark running its whole length",""),
 ("Because it was never yours to command. It is older than command.",'none','wh','m',"a small crown or command icon crossed out beside an ancient stamp",""),
 # KET
 ("So. Why do you hiccup?",'you','wh','m',"the figure standing under the big title question again","WHY?"),
 ("Not because anything is wrong with you.",'you','wh','m',"the figure reassured, a green check glowing over its chest",""),
 ("You hiccup because a very long time ago, something that was almost you lived in the water.",'none','water','m',"a faint almost-human fish silhouette living calmly in blue water",""),
 ("It gulped, and it shut a small flap, and that kept it alive.",'none','gilld','m',"the creature gulping and shutting a small flap, a little green survive check",""),
 ("Then it crawled onto land, and grew legs, and over an amount of time you cannot really feel, it became us.",'none','edge','w',"a morph line from a fish crawling out of water into a walking human across the riverbank",""),
 ("And it never let go of that one small move.",'none','wh','m',"a hand gently keeping hold of a small glowing gulp-and-snap icon",""),
 ("It's still here. In your chest. In your baby's. In your dog's. Waiting.",'you','wh','m',"the reflex glowing faintly in the modern figure's chest, in a tiny baby, and in a cute dog, all waiting",""),
 ("So the next time it happens, mid sentence, for no reason at all, don't be annoyed by it.",'you','home','m',"the figure hiccuping mid-sentence again, but this time smiling gently, not annoyed","HIC"),
 ("That's not a malfunction.",'none','wh','cu',"a bold text card on white","NOT A GLITCH"),
 ("That's three hundred and seventy million years old.",'none','wh','cu',"a big bold number card","370 MYA"),
 ("That's the tadpole. That's Tiktaalik. That's the fish that chose air.",'none','edge','m',"a small glowing lineup: a cute tadpole, a cute Tiktaalik fishapod, and a fish lifting its head to breathe air",""),
 ("That's the water you climbed out of, still moving inside you.",'you','wh','cu',"close on the modern figure's chest with a faint blue ripple of water still moving within",""),
 ("That's you.",'none','wh','cu',"a bold text card on white","THAT'S YOU"),
 ("So when your body interrupts you, and takes the wheel for half a second, just listen.",'you','home','m',"the figure pausing to listen, a hand resting gently on its own chest",""),
 ("It's the oldest word your body still knows how to say. Hic.",'you','wh','cu',"close on the figure with a soft small sound mark, a gentle warm hic","HIC"),
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

open(os.path.join(HERE,"Script_Video08_narration.txt"),"w").write("\n".join(l for (l,*_) in DATA))
open(os.path.join(HERE,"SHOTLINES_FULL.txt"),"w").write("\n".join(shot_lines))
open(os.path.join(HERE,"PROMPTS_FULL.txt"),"w").write("\n\n".join(prompts))
print("Shots:",len(DATA))
