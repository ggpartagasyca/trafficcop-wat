For experiment wat_annot_escort_01, I annotated 1000 backpage posts from about 2/1/2015 (drawn from entire US)
Each post was assigned one or more of the following tags.  Each is listed with the number of times tag was used.
age (34) expressed specific restriction on age of client
agency (33) post appears to be escort agency
dance (2) provider primarily offering dance services
employment (5) post offers employment
healthspa (139) post advertises incall spa/massage location
multi (129) post offers two providers for simultaneous session
party (4)  post offers a buy-in/stripper party
race (116) expressed (positive or negative) restriction on race of client, including references to thugs, pimp
spam (22) off-topic post; includes transvestite, clickbait, "get out"/anti-trafficking ads, strip club, other services
typical (558) escort ad with no other characteristic

Because categories dance, employment, and party are so infrequent and are also basically off-topic, I will combine those into the spam category, hoping we can learn something.  this yields

dance/employment/party/spam (33) all off-topic ads

race vs non-race: learning using 500 training took 492 seconds


==================================================================

python learnblob.py -v -l age --train 800 --test 100 --validate 100 > age.test
