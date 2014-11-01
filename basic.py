import string
import random
import datetime

file_data_users = open('data/users','r')
file_data_team = open('data/team','r')
file_data_contests = open('data/team','r')
file_data_titles = open('data/titles','r')
file_data_problems = open('data/problems','r')
file_data_rules = open('data/rules','r')

file_schema = open('data/schema','r')

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
file_problems = open('problems','wr')





# 									_	D A T A _ T O _ P O P U L A T E _ T H E _ D . B . _ W I T H _





def normalize(datalist,size = 1000):
	'''Use this function always whenever feeding external data into the script. It ensures that the data doesnt break the SQL flow
		It requires however to be fed a list'''
	normalized = []
	for entry in datalist:
		if len(entry) > 0:
			normalized.append(entry.strip().replace("'","")[:size])
	return normalized


'''Make python lists of data read from files, all normalized and good to go'''
usernames =  normalize(file_data_users.read().split('\n'),20)
teamnames = normalize(file_data_team.read().split('\n'),50)
contestnames = normalize(file_data_contests.read().split('\n'))
titles = normalize(file_data_titles.read().split('\n'))
problems = normalize(file_data_problems.read().split('\n'))
rules = normalize(file_data_rules.read().split('\n'))

def password_generator(size = 10, chars = string.ascii_uppercase + string.digits + string.lowercase):
	password = []
	for i in range(size):
		password.append(random.choice(chars))
	return ''.join(password)

teamids = []
def teamid_generator(size = 10):
	for team in teamnames:
		id = []
		for i in range(size):
			num = ord(random.choice(team))
			id.append(str(num)[0])
		teamid = ''.join(id)
		while teamid in teamids:
			teamid = str(random.randint(0,5125435) + int(teamid))
		teamids.append(teamid)

active_contestnames = []

states = ['active','closed','open','early']

contestids = []
def contestid_generator(size = 10):
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

discussionids = []

programmingcontests = []





# 														_ S C H E M A _ 






def interpret( schemalist):
	
	for entry in schemalist:
		if len(entry) > len("create table ;"):
			attributes = []
			entry = entry.replace("\n","").lower().replace("create table ","")
			#CONFIRMED - entry is lowered, and stripped of initial create table statement print entry
			relation,attribute = entry.split('(',1)
			print "IN RELATION %s" % relation
			#CONFIRMED print relation
			#CONFIRMED print attribute.split(',')
			#for element in attribute.split(','):
			

interpret(file_schema.read().split(';'))

insert_user_acc = '''INSERT INTO user_acc VALUES ('%(username)s', '%(password)s');\n'''
insert_team = '''INSERT INTO team VALUES ('%(teamname)s', '%(teamid)s');\n '''
insert_contest = '''INSERT INTO contests VALUES ('%(contestid)s', '%(contestname)s', '%(prize)d', '%(rules)s', '%(state)s' , '%(guidelines)s');\n'''
insert_member = '''INSERT INTO members VALUES('%(username)s' , '%(teamid)s');\n'''
insert_submits_user = '''INSERT INTO submits_user VALUES('%(username)s', '%(submissionid)s');\n'''
insert_submits_team = '''INSERT INTO submits_team VALUES('%(teamid)s', '%(submissionid)s');\n'''
insert_submission = '''INSERT INTO submissions VALUES('%(submissionid)s', '%(score)d', '%(solutionpath)s', '%(visible)s', '%(contestid)s');\n'''
insert_judge = '''INSERT INTO judges VALUES('%(username)s', '%(contestid)s');\n'''
insert_sponsor = '''INSERT INTO sponsors VALUES('%(username)s', '%(contestid)s');\n'''
insert_programmingcontest = '''INSERT INTO programmingcontest VALUES('%(contestid)s');\n'''
insert_developingcontest = '''INSERT INTO developingcontest VALUES('%(contestid)s',	'%(theme)s');\n'''
insert_discussions = '''INSERT INTO discussions VALUES('%(discussionid)s', '%(username)s', '%(contestid)s', '%(title)s');\n'''
insert_comment = '''INSERT INTO comments VALUES('%(discussionid)s', '%(username)s', '%(timestamp)s', '%(text)s');\n'''
insert_problems = '''INSERT INTO problems VALUES('%(contestid)s', '%(problemname)s', '%(difficulty)s', '%(text)s', '%(testcase)s', '%(examples)s', '%(deadline)s');\n'''

def write_user_acc():
	for i in range(200):
		username = usernames[i]
		password = password_generator()
		query = insert_user_acc % { "username":username, "password":password }
		file_user_acc.write(query)
	file_user_acc.close()

def write_team():
	teamid_generator()
	for i in range(len(teamnames)):
		teamname = teamnames[i]
		teamid = teamids[i]
		query = insert_team % { "teamname":teamname, "teamid":teamid }
		file_team.write(query)
	file_team.close()

def write_contest():
	contestid_generator()
	for i in range(len(contestnames)):
		contestid = contestids[i]
		contestname = contestnames[i]
		rule_set = []
		prize = random.choice([0,0,0,0,1,2,5,10,20,50,0,0,0,0,0,0,0,0])*1000
		for i in range(4):
			chosen_rule = random.choice(rules)
			if not chosen_rule in rule_set:
				rule_set.append(chosen_rule)
		state = random.choice(states)
		if state == 'active' or state == 'closed':
			active_contestnames.append(contestname)
		query = insert_contest % { "contestid":contestid,"contestname":contestname,"rules":''.join(rule_set),"state":state,"guidelines":'Demo Guideline', "prize":prize}
		file_contests.write(query)
	file_contests.close()
	
def write_members():
	for id in teamids:
		users = []
		for i in range(3):
			chosen_user = random.choice(usernames)
			if not chosen_user in users:
				users.append(chosen_user)
				query = insert_member % { "username":chosen_user,"teamid":id }
				file_members.write(query)
	file_members.close()

def write_submits():
	total = 100
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
					query = insert_submits_user % { "username": username, "submissionid":submissionid}
					submissionids.append(submissionid)
					file_submits.write(query)
		else:
			team_index = random.randint(0,len(teamids)-1)
			teamid = teamids[team_index]
			teamname =  teamnames[team_index]
			submissionid = submissionid_generator(teamid,contestname)
			query = insert_submits_team % {"teamid": teamid, "submissionid":submissionid}
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
			programmingcontests.append(contestids[i])
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
			timestamp = str(datetime.datetime.now())
			text = "test comment text"
			query = insert_comment % { "discussionid": id, "username": user, "timestamp":timestamp, "text":text }
			file_comments.write(query)
	file_comments.close()

def write_problems():
	for id in programmingcontests:
		problemo = []
		for i in range(random.randint(0,6)):
			problemname =  random.choice(problems)
			if problemname in problemo:
				continue
			problemo.append(problemname)
			text = 'dummy text'
			testcase = 'dummy text'
			examples = 'The quick brown fox jumped over the lazy dog'
			deadline = str(datetime.datetime.now())[:-7]
			difficulty = random.choice(['easy','medium','hard','very easy', 'very hard'])
			query = insert_problems % {"contestid":id, "problemname":problemname, "difficulty":difficulty, "text":text, "testcase":testcase, "examples":examples,"deadline":deadline } 
			file_problems.write(query)
	file_problems.close()

write_user_acc()
write_team()
write_members()
write_contest()
write_developingcontest()
write_programmingcontest()
write_submits()
write_submission()
write_judge()
write_sponsor()
write_discussions()
write_problems()
write_comments()
