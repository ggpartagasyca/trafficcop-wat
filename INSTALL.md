trafficcop-wat is a python application to classify escort advertisements using two complementary methods: keyword-based rules and learned classifiers.

LEARNED CLASSIFIERS
We have created seven classifier learning experiments ("classes"):

age: posts where the provider expresses a preference for/against clients of a specific age range
agency: indicates posts which suggest the escort provider(s) are affiliated with an escort agency
healthspa: indicates posts which suggest the services advertised are coming from an incall spa establishment.  Includes Asian and general spa establishments
multi: indicates posts which suggest multiple providers advertised in the same ad.  Includes ads with a single provider who indicates she works with a second person.
offtopic: posts which are considered not relevant in this domain.  Includes among other things buy-in parties, offers of employment (escort and conventional), exotic dancers, male and transsexual providers, ads for other adultl services (adult friend finder, ashleymadison, etc.), anti-trafficking ads, and spam.
race: posts where the provider expresses a preference for/against a specific racial or ethnic group.  Includes 'thug' and 'pimp'.
typical: posts deemed to be typical escort ads not otherwise classified.  In short, a single independent escort provider (incall or outcall) with no specific restrictions 
These categories were chosen to try to find cases useful for FBI analysis but also with sufficient frequency and distribution to allow learning.

Training classifiers into these categories has been carried out with three different feature approaches.  These are:

ci: case-insensitive "seen" (positive) tokens
cs: case-sensitive "seen" tokens
NLTK default feature method: all tokens, includes seen tokens and all unseen tokens

Training and reloading classifiers with only "seen" tokens results in much smaller and quicker classifiers, with much less accuracy.

PATTERN SCANNING RULES:
We have created about 100 rules which can classify input text or html files which match subsequences of terms within the document.  This capability includes identifying categories deemed important by FBI, without too much regard for frequency and variability.  Categories of rules include: provider youth indications, provider movement indications, evidence of race/ethnic preference, etc. which could indicate underage/trafficked persons.

INSTALLATION

To install, you will need python 2.7.

Checkout the application from github into an appropriate directory:

git clone https://github.com/philpot/trafficcop-wat.git

Enter that directory

cd trafficcop-wat

You will need to install a few libraries.  I recommend using pip, virtualenv, and virtualenvwrapper to manage these.

python setup.py develop
pip install -r requirements.txt 

To run:

cd wat/escort

[consult README.md in wat/escort for more]

or

cd wat/learn

[consult README.md in wat/learn for more]

