import string
import random
import datetime

file_user_acc = open('user_acc','wr')
file_team = open('team','wr')
file_contests = open('contests','wr')
file_members = open('members','wr')
file_submits = open('submits', 'wr')
file_submissions = open('submissions','wr')
file_judges = open('judges','wr')
file_sponsers = open('sponsors','wr')
file_programmingcontest = open('programmingcontest','wr')
file_developingcontest = open('developingcontest','wr')
file_discussions = open('discussions','wr')
file_comments = open('comments','wr')

usernames = '''brringstreets tennisvagary abackfink dogreceive brouhaharhyming deadbeatpheasant pridefulfish sobwrathful marrybog hootenanydock extrasmallobeisant
headedvillainous stinkyhills danishracket concretebranch numbstrung scrubtoes narroweat selfishoceanic armtoothsome politewoozy jumpingdray verdantpoised loftyhomely 
waisttrent imminentswimming panpushy prisonerbellow strainedacrobat pigstandard divulgeflue mouldybazaar mumgoal surgeonlook petitestray whiteblow toastedbumper 
laminatehart faithlessleopard immodestnegative fetchmumpsimus forthrightclasses shootingdark methodicaltape bahnambypamby closeamazed filletgeek homelynecked 
surfingroofer puffspiggy gamepanicky snapirritate whoresonmuffins hoopreverse flightsnowy rootssurprise shotpututilized abundantrug sowcold agressiveexclusive 
roundrealtor casejabber protectulna launchingviolent glugaccepting pickleballstoppers smackbunch unequalimpressive mushroomhug pickyiraqi ladycontinue yeomanpicky
originalincisive peacocklove flabbyhowl gaudygurgle shinyfawning notablehopes allegedhandy cyclistcrushing trimrigmarole blueberryclass bobbinpermit phalanxcomment
introducewarming mutationwhimper niftyslip doughnutjovial glitchesweasel zealoussweet farrowtemporary deboshedthrowing slabsredstone gripingfoot rugbygraze
spiritsrafter buckcut fakeskip brandpushing wingfearful deanunreal torpidadamant finchnapkin spencersspider thoumugging notesknight moprecord dumpbloviate esteemedleg
sledgibbon dualextralarge croatiantoss raspsausage tucktesting steelguineafowl greytry doubtfulsnout dwindleabsent tremblehunter waddlerequest subsequenthateful
helpfulunequaled slashhornbill whammurmer paunchymoonbeam dimwittedblackbird admonishnice shamefuldragging skarkprofitable silverspade premiumdeformed impresswarren
illfateddean walkerwrack bolivianhastiness childlikegush artistebugbear evasivebum finicalsparkling israelisaber angelicpoppycock baldyimplore dunnockfallen
crumbletriathlon modestfanny cleverundress uppityintend netcompetitor rejectyodel abalonemuddy wornoutduster masticatemilitary noticepoo smashfruit nappiessaucy 
arraymother groinabashed hooverviolet makingdemanding professwoebegone boomerangsober followmeasly notedpecan bruisefunctional ownhyena shutbaggage pingpongpedlar
protectivespew eyeballsthrust buyerromantic needledebate bindbaffled adevilish polepad chompsamovar havingbowling zaftiglearned anarchistclassic whiningbaa
turkeygluttonous cartoonadmonish gapingmoon labouraccused purseimply scoldlobe specificpuddles dependentactor doodlewhipper secretiveflyingfish abashedlush
soullessspiky cappeddroning highjumpwhirl ratbumpy pillowchickens impetuouscrayon applestottering thundersmack luxuriousbeautiful traumaticfragile'''.split()

def password_generator(size = 10, chars = string.ascii_uppercase + string.digits + string.lowercase):
	password = []
	for i in range(size):
		password.append(random.choice(chars))
	return ''.join(password)
	
teamnames = "The Walkie Talkies;The Sons of Pitches;Holy Walkamolies;Rubber Puckies;French Toast Mafia;Bloodbath and Beyond;Coast Busters;The Beer View Mirrors;The Abusement Park;" 
teamnames = teamnames + '''Paintball Wizards;Wii Not Fit;Scared Hitless;Toxic Tigers;Reptile Crunchers;Reptile Wild;Pink Miners;Poison Ivy;Strike This;American Lightning;Flying Sharks;Cyborg Hawks;'''
teamnames = teamnames + '''Hot Xpress;Killer Stars;The Assassins;The Creed;The Croods;McQueen Lightning;Carnivore Miners;American Wasps;Awesome Slammers;Fierce Predators;Amazing Slayers;Midnight Ninjas;''' 
teamnames = teamnames + '''Rocky Secret Agents;Shockwave Slammers;Butterfly Piledrivers;Nunchuk Dynamos;Killer Crunchers;Red Flyers;The Sharks;Smart Alecs;Split Personalities;Moon Walkers;Diamond Divas;'''  
teamnames = teamnames + '''The Y-Nots!;Fargo Wood Chippers;Pink Soldiers;Shockwave Warriors;Basket Brawlers;Pigs Might Fly;Pigs Will Fly; So will Pings; Will you will?;Slapnut Magoos;Intoxicated;Timon & Pumba;''' 
teamnames = teamnames + '''Hansel and Gretel;Fire Breathing Kittens;Mind Bogglers;Fire Kittens Breathers;The Mighty Morphin;Mighty Sledgehammers;Tenacious Turtles;Mighty Midget Kickers;''' 
teamnames = teamnames + '''Grim Reapers;Wood Chuckers!;Smooth Operators;Unfrozen Caveman Lawyers;Eleven Wise Monkeys;The Tuna Tasters;Smooth Operators;Anti Armed Flying Mortal Penguins;Aidans Apotheoses;''' 
teamnames = teamnames + '''The Riders of Gauthus;The Angels of Airis;Toks Rebels;UpdarDwarfs;Demons of Mylo;The Rebels of Eckard;The Warriors of Minox;Senics Demons;Apotheoses of Bazol;Drit Friends;''' 
teamnames = teamnames + '''Tybell of the Limbo;Devils of Wroogny;The Guardians of Odeir;The Masters of Sermak;Renegades of Bredin;Tespan Trolls;Conquerors from Gosform;ModricAngels;Naterish beneath the Saints;''' 
teamnames = teamnames + '''Creators from Haston;Markard Falcons;The Friends of Eckard;Cipyar Angels;The Falcons of Peitar;Maevi above the Daemons;Sinners of Tespan;Calebaas Knights;Slayers of Reaper;''' 
teamnames = teamnames + '''Savages of Vacon;Horde of Telpur;Yakkitys Villains;Alliance of Ackmard;The Order of Aslan;Hildar of the Eagles;Loons of Haiduc;The Parents from Holypetra;Monsters out of Abardon;''' 
teamnames = teamnames + '''Daemons from Elthen;UhrdWolves;The Brutes from Pingala;Heart of Dawood;The Villains of Eythil;The Wolves from Cibrock;The Ancestor of Naterish;The Rebels from Sojiro;Slayers of Onimia;''' 
teamnames = teamnames + '''Friends out of Sildo;The Wolves of Purhara;Dismers Hordes;Efars Loons;Ryodan Masters;Light of Mylo;The Conquerors of Bredock;The Sons of Falcord;Devils from Merdon;Yerpal of the Daemons;''' 
teamnames = teamnames + '''Knights of Efar;The Gods from Leeuwin;SamotRunners;Tiamath above the Villains;The Slayers of Lolimgolas;Veldars Horde;Daburn Riders;The Children of Reaper;Tybells Knights;The Slayers of Okuni;''' 
teamnames = teamnames + '''Overlords of Modric;Palpur beneath the Riders;Parents of Darmor;Palids Daemons;Trolls of Valtaur;Lights of Badek;Heart from Cevelt;The Protector of Alkirk;Laracal Angels;The Knights from Etran;''' 
teamnames = teamnames + '''Heart of Tiamath;Nildale of the Wolves;EckardSons;Overlords of Naterish;Lurd Fiends;Warriors of Rahe;The Beasts from Penduhl;Loons of Matsa;The Protectors of Galin;Cordale of the Creatures;''' 
teamnames = teamnames + '''Lords out of Bernout;Loons of Xandar;Daimons from Fibroe;Kaldar Alliance;Protector of Etar;Gehardts Sphinx;Gods from Lidorn;Bedic Order;The Order of Meldin;Survivors of Yakkity;''' 
teamnames = teamnames + '''The Wolves from Zerin;Latzafs Limbo;Jared Leto;Ielis Ancestor;Monsters of Aslan;The Sinners from Suktar;Loons of Jiger;Omgicrit Slayers;Haiducs Savages;Fathers of Hubok;The Apotheoses of Quid;''' 
teamnames = teamnames + '''The Runners of Ixen;The Slayers of Shane;The Apotheoses of Modum;Jihnj Fathers;The Daimons of Dismer;Lords of Koldof;The Falcons of Etran;Amerdan Hordes;Masters out of Santhil;Deathmars Protectors;''' 
teamnames = teamnames + '''Daimons of Driz;RiandurDaemons;The Spirits from Nathon;The Sinners of Latzaf;Riders of Eloon;Masses of Achard;Horde of Keran;Darg beneath the Loons;Riders of Mezo;Ghosts of Sermak;ErikHorde;''' 
teamnames = teamnames + '''Light of Xithyl;Dask Ancestor;Eloons Dwarfs;Loons of Rythen;The Creatures from Orin;The Riders of Wortel;The Order of Achard;Mylo Brutes;Jelli of the Riders;Mitars Riders;Temils Riders;Qtiss Horde;Overlords of Meldin;''' 
teamnames = teamnames + '''The Apotheoses of Pluitti;Bealx Dwarfs;Voltains Warriors;Lobans Runners;Ohmars Parents;The Riders of Sucz;Wortels Rollers;The Hordes of Belep;The Saints of Zak;Fronars Hordes;The Masters of Valker'''
teamnames = teamnames.split(';')

teamid = '''8785152096 9034104039 1160772600 2262920213 3165366496 2235649560 5672387389 0998819553 9704272912 0583935249 8466840159 0703033972 6806050825 3383631794 2295094391 9906013629 2444898618 9547842863 9626756866 '''
teamid += '''4006858955 6534001092 3610889280 5686906800 8696744817 1917569603 4358195154 3291431960 1377643515 1789702890 9965508163 4802212162 9846774845 4781151319 3229277214 0752188436 0347924696 5814762405 0877745580 8349882487 '''
teamid += '''9425673839 5349349378 0273138794 0886116730 5763576526 6261629950 4487461328 8615291326 2420138667 0631686195 0720756839 9002122429 1061030938 1347842163 7868060908 6166734118 5884749709 3605666925 9253351426 5610327921 '''
teamid += '''9820068333 8700344588 7438825400 3995436302 3018400558 0152587819 7171596158 3516884208 6057024980 7587846734 2209583158 7346097206 2786444893 8253039666 2001090494 1585241341 5826176153 7635617334 1540369005 2688021684 '''
teamid += '''9285820704 7882259003 1762660134 4051721078 1623211414 5213635678 5233756609 9048312103 0817975331 9267425139 3608814032 0156171130 0465886413 7208126040 0088502921 9280853973 0413604775 3870324843 2466152427 2840202252 '''
teamid += '''9405335033'''
teamid = teamid.split()

contestnames = ''' ProjectEuler+ , October Gamathon , Let's Bash! , 101hack18 , Lambda Calculi , Code Sprint , Evernote Coding Challenge , Code Masters , TechFest , '''
contestnames = contestnames + '''Insomnia , Clash Credenz , Procon , Prometheus , Game of Codes , Bit Battle , abacus , Codelt , Byte Code , Dementia , Ignus , '''
contestnames = contestnames + '''Trinity , Cranium , Shaastra , Ode2Code , Code Czar , Pravega , Inscription , Cryptoss , Bit Freak , IOPC , Epiphany , Conscientia,'''
contestnames = contestnames + '''10-70 REPEATER ASSN , ABB RADIO AMATEURS , ARAUCARIA DX GROUP, July Cook-off 2011 , J.N.E.C. - Dialect , Code Mutants, Code Turtles, Turtles, TNMT of Tomorrow','''
contestnames = contestnames + '''	NIT - Kurukshetra , 101hack18 , July Gamathon , Addepar Hackathon , 101 Hack May , Guess the rating , MGM - Tech Arete , 	ACM Trial,'''
contestnames = contestnames + '''Limit-de-Plazo, ICPC Warmup 1,EMA,CE,Icoder, Dreamspark, Google Code In, Google Code Out, Google Code Up, Google Code Down, Google Code Left, Google Code Right,'''
contestnames = contestnames + '''CTRLF1,CTRLF2,CTRLF3,CTRLF4,CTRLF5,CTRLF6,CTRLF7,CTRLF8,CTRLF9,CTRLF10,CTRLF11,CTRLF12,Rubix, Tz Test, Code Buzz, Code Aldrin, Quark, Quake, Technovanza, '''
contestnames = contestnames + '''Snack Down, Smack Down, Raw, Wrestlemania, Summer Slam, Cyber Sunday, No Holes Barred, Resnack Down, Royal Rumble, Backlash, Backslash, Code Baker, Code Baker Street,'''
contestnames = contestnames + '''Inscription, iDecipher, Inception, Insomnia, Fight Club, The Rooks, Most Wanted,'''
contestnames = contestnames + '''Top Coder, Go! Code, Django Unchained, Google App Challenge, Code Spill'''
contestnames = contestnames.split(',')
active_contestnames = []

rules = []
rules.append("All decisions of the contest officials are final.\n")
rules.append("Style of the solution will not be considered in the judging.\n")
rules.append("All sponsors will remain in the observing area and may not communicate with the team during the rounds.\n")
rules.append("Use of internet is allowed\n")
rules.append("All programs are text based. Programs must read input from a designated input file with a given filename and write output to stdout.\n")
rules.append("Both input and output format are crucial. Adhere to them precisely to avoid getting solutions judged as wrong.\n")
rules.append("You may update the submission even after uploading it already, till the timer goes off.\n")
rules.append("Competitors should not log out of their computer for the duration of the contest.\n")
rules.append("Your mentor must not have written any part of the code\n")
rules.append("Plagarism is a bad habit and any forms of it will lead to a direct, non negotiabel disqualification\n")

states = ['active','closed','open','early']

contestids = []
def attach_contestid(size = 10):
	for contestname in contestnames:
		name = []
		for text in contestname:
			name.append(text.lower().strip())
		names = ''.join(name)
		
		contestid = []
		for i in range(size):
			contestid.append(random.choice(names))
		contestid_ = ''.join(contestid)
		contestids.append(contestid_)

submissionids = []
def submissionid_generator(id,contestname):
	name = contestname.lower().strip().split()
	contestname = ''
	for text in name:
		contestname += text.strip()

	submissionid = ''
	for i in range(10):
		submissionid += random.choice(contestname+id)
	return submissionid

titles = []
titles.append(" A workload warrants the electorate inside the practicable potato. ")
titles.append(" A resident drains a home. ")
titles.append(" Without a species orbits a regulation wonder. ")
titles.append(" Does another package stumble underneath a sunny specimen? ")
titles.append(" Why does the standpoint try a guided motive? ")
titles.append(" A reasonable bulb argues an eventual manifesto. ")
titles.append(" Into a telescope noses the hooked cuckoo. ")
titles.append(" A lighted chocolate boggles behind a true refund. ")
titles.append(" A boiled consequence scores. ")
titles.append(" Over our ass spits the enlightened outcome. ")
titles.append(" The virgin studies the bread within the flash impulse. ")
titles.append(" The conjecture racks the tremendous chain on top of a bugger. ")
titles.append(" On top of a button trips a resemblance. ")
titles.append(" Next to a tribe fudges the sod. ")
titles.append(" When can the divine minister to an even prostitute? ")
titles.append(" The microcomputer quibbles. ")
titles.append(" An inexperienced twist succeeds into a purple brush. ")
titles.append(" An expressway scans a reign. ")
titles.append(" How will the negative academic degenerate into the chestnut relief? ")
titles.append(" The worse violence reaches the killing lady. ")
titles.append(" Does the theme adjust the plaster? ")
titles.append(" His anticipated worker leaks opposite the reflex badge. ")
titles.append(" Why can't the slippery seat escape after the soul? ")
titles.append(" An afraid caffeine expires. ")
titles.append(" A tight vein plays after a spoof. ")

discussionids = []



insert_user_acc = '''INSERT INTO user_acc VALUES ('%(username)s', '%(password)s');\n'''
insert_team = '''INSERT INTO team VALUES ('%(teamname)s', '%(teamid)s');\n '''
insert_contest = '''INSERT INTO contests VALUES ('%(contestid)s', '%(contestname)s', '%(rules)s', '%(state)s' , '%(guidelines)s');\n'''
insert_member = '''INSERT INTO members VALUES('%(username)s' , '%(teamid)s');\n'''
insert_submits = '''INSERT INTO submits VALUES('%(username)s', '%(teamid)s', '%(submissionid)s');\n'''
insert_submission = '''INSERT INTO submissions VALUES('%(submissionid)s', '%(score)d', '%(solutionpath)s', '%(visible)s', '%(contestid)s');\n'''
insert_judge = '''INSERT INTO judges VALUES('%(username)s', '%(contestid)s');\n'''
insert_sponsor = '''INSERT INTO sponsors VALUES('%(username)s', '%(contestid)s');\n'''
insert_programmingcontest = '''INSERT INTO programmingcontest VALUES('%(contestid)s')\n'''
insert_developingcontest = '''INSERT INTO developingcontest VALUES('%(contestid)s',	'%(theme)s')\n'''
insert_discussions = '''INSERT INTO discussions VALUE('%(discussionid)s', '%(username)s', '%(contestid)s', '%(title)s')\n'''
insert_comment = '''INSERT INTO comments VALUE('%(discussionid)s', '%(username)s', '%(timestamp)s', '%(text)s')\n'''

def write_user_acc():
	for i in range(200):
		username = usernames[i]
		password = password_generator()
		query = insert_user_acc % { "username":username, "password":password }
		file_user_acc.write(query)
	file_user_acc.close()

def write_team():
	for i in range(100):
		teamname = teamnames[i][:19]
		team_id = teamid[i]
		query = insert_team % { "teamname":teamname, "teamid":team_id }
		file_team.write(query)
	file_team.close()

def write_contest():
	attach_contestid()
	for i in range(100):
		contestid = contestids[i]
		contestname = contestnames[i]
		rule_set = []
		for i in range(4):
			chosen_rule = random.choice(rules)
			if not chosen_rule in rule_set:
				rule_set.append(chosen_rule)
		state = random.choice(states)
		if state == 'active' or state == 'closed':
			active_contestnames.append(contestname)
		query = insert_contest % { "contestid":contestid,"contestname":contestname,"rules":''.join(rule_set),"state":state,"guidelines":'Demo Guideline'}
		file_contests.write(query)
	file_contests.close()
	
def write_members():
	for id in teamid:
		users = []
		for i in range(3):
			chosen_user = random.choice(usernames)
			if not chosen_user in users:
				users.append(chosen_user)
				query = insert_member % { "username":chosen_user,"teamid":id }
				file_members.write(query)
	file_members.close()

def write_submits():
	total = 50
	for i in range(total):
		contestname = random.choice(active_contestnames)
		is_team = random.randint(0,3) > 2
		if not is_team:
			participants = []
			for j in range(random.randint(0,5)):
				username = random.choice(usernames)
				if not username in participants:
					participants.append(username)
					submissionid = submissionid_generator(username,contestname)
					query = insert_submits % { "username": username, "teamid": ' ', "submissionid":submissionid}
					submissionids.append(submissionid)
					file_submits.write(query)
		else:
			team_index = random.randint(0,len(teamid)-1)
			team_id = teamid[team_index]
			teamname =  teamnames[team_index]
			submissionid = submissionid_generator(team_id,contestname)
			query = insert_submits % { "username": ' ', "teamid": team_id, "submissionid":submissionid}
			submissionids.append(submissionid)
			file_submits.write(query)
	file_submits.close()

def write_submission():
	counter = 0
	for submissionid in submissionids:
		contestid = random.choice(contestids)
		score = random.randint(0,100)
		solutionpath = 'root/contests/%(contestid)s/v%(a)d.%(b)d/final' % { "contestid":contestid, "a":random.randint(0,4), "b":random.randint(01,14) }
		counter += 1
		if counter%3 == 0:
			visible = 'True'
		else:
			visible = 'False'
		query = insert_submission % { "submissionid": submissionid, "score":score, "solutionpath":solutionpath, "visible":visible, "contestid":contestid }
		file_submissions.write(query)
	file_submissions.close()

def write_judge():
	for contestid in contestids:
		for i in range(random.randint(1,2)):
			user = random.choice(usernames)
			query = insert_judge % { "username":user, "contestid":contestid }
			file_judges.write(query)
	file_judges.close()

def write_sponsor():
	for contestid in contestids:
		for i in range(random.randint(1,2)):
			user = random.choice(usernames)
			query = insert_sponsor % { "username":user, "contestid":contestid }
			file_sponsers.write(query)
	file_sponsers.close()

def write_programmingcontest():
	for i in range(len(contestids)):
		if not i % 3 == 0:
			query = insert_programmingcontest % { "contestid": contestids[i] }
			file_programmingcontest.write(query)
	file_programmingcontest.close()

def write_developingcontest():
	for i in range(len(contestids)):
		if not i % 3 == 0:
			query = insert_developingcontest % { "contestid": contestids[i] , "theme":'TestTheme'}
			file_developingcontest.write(query)
	file_developingcontest.close()

def write_discussions():
	for i in range(80):
		username = random.choice(usernames)
		contestid = random.choice(contestids)
		title = random.choice(titles)
		discussionid = ''.join(random.choice(username+contestid+title.replace(' ','')) for _ in range(10))
		discussionids.append(discussionid)
		print discussionid
		query = insert_discussions % { "username":username,"contestid":contestid,"title":title,"discussionid":discussionid }
		file_discussions.write(query)
	file_discussions.close()

def write_comments():
	for id in discussionids:
		for i in range(random.randint(0,5)):
			user = random.choice(usernames)
			timestamp = str(datetime.datetime.now())[:-7]
			text = "test comment text"
			query = insert_comment % { "discussionid": id, "username": user, "timestamp":timestamp, "text":text }
			file_comments.write(query)
	file_comments.close()


write_user_acc()
write_team()
write_contest()
write_members()
write_submits()
write_submission()
write_judge()
write_sponsor()
write_programmingcontest()
write_developingcontest()
write_discussions()
write_comments()