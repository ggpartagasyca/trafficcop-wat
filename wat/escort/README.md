	      PATSCAN KEYWORD RULE BASED CLASSIFICATION

Andrew Philpot 
29 May 2015
philpot@isi.edu

Pattern ("keyword") rules were developed by hand to using sequences of
terms within a document.  The document text is split into words using
a more complex tokenizer than is used in the unigram learning models.
The main differences and complexity comes from treating punctuation,
digits, and unicode characters specially.  The tokenizer is
implemented in tools/wattok as a specialization of the NLTK-supplied
sentence and word tokenizers.

MAIN CAPABILITIES SUPPORTED BY THIS MODULE:

There is a single entry point for applying rules to a document.  One
can apply all rules, a single rule, or a given subset of rules.  The
rules are grouped into a two-level hierarchy.  The first level is
called category.  The top-level categories are:

multiProvider: indicates more than one provider in the same ad
providerYouth: language in the indicates the provider is younger than
    average
ageSelect: indicates the provider expresses preference for/against
    specific ages of the client  
raceEthnicSelect: indicates the provider preference for/against
    specific races or ethnicities of the client.  As with the learned
    model, "thug" and "pimp" are included.  Note: racist epithets if
    matched will also indicate this category 
briefDuration: indicates the provider has just arrived in town, will
    be leaving soon, or similar
ethnicityNationality: provider's ethnicity, nationality, language
    and/or race is mentioned
incall: suggests the provider is offering to perform incall services
notincall: suggests the provider is NOT offering to perform incall
outcall: suggests the provider is offering to perform outcall services
notoutcall: suggests the provider is NOT offering to perform outcall
incalloutcall: suggest the provider is offering to perform both incall
               and outcall
agency: may suggest the provider works with an agency.  May also
    indicate mentions of a phrase such as "law enforcement agency"
spa: suggest services being offered in a spa/massage parlor setting
notagency: suggests the provider denies being with an agency.  May
    also indicate mentions of a phrase such as "not law enforcement
    agency"
names: this pattern finds locations in the text that indicate a
    provider name or working name or other designation.  These names
    are not looked up in a dictionary
NBA: this pattern attempted to indicate posts that mentioned the NBA
    all-star game
superbowl: this pattern attempted to indicate posts that mentioned the
    2014 Super Bowl in Meadowlands, NJ

The second level categorization is called 'family'.  A rule category
might have several different rule families.  If a category is a broad
topic/modality, the family attempts to group similar expressions of
that idea.  For example, the idea of multiple providers in a single ad
(category 'multiProvider' above): includes the following families:

    "ask about my friend" and similar expressions
    "i have a girlfriend" and similiar
    "me and my girlfriend"
    "with my friend"
    "my friend's name is"
    "two-girl show"
    "both girls"
    "double your pleasure"
    etc.

Note that the family name string is just a typical way to refer to
this kind of expression.  The family "with my friend" also includes
things like "with my sexy friend" and "with my girlfriends".

Finally, each rule has a unique identifier.  For brevity, these are
triples of numbers, where the first number corresponds to the
category, the second the family, and the third the rule within the
family.  For example, the "briefDuration" category includes the "two
days only" rule, indicated uniquely as (3,4,1).  It is not expected
that typical use of the module will be to specify rules uniquely; but
this is useful when testing new rules.

USE OF THE MODULE:

    usage: patscan.py [-h] [-c CATEGORY] [-f FAMILY] [-i INDICATOR]
		      [-t {text,html}] [-v]
		      input

    positional arguments:
      input

    optional arguments:
      -h, --help            show this help message and exit
      -c CATEGORY, --category CATEGORY
			    major category of rules to apply (default: use all)
      -f FAMILY, --family FAMILY
			    minor category of rules to apply (default: use all)
      -i INDICATOR, --indicator INDICATOR
			    Indicate precise rule as X.Y.Z
      -t {text,html}, --type {text,html}
			    input file type
      -v, --verbose         verbose

GENERAL ARGUMENTS:

-h/--help: don't do anything, only display the help (optional)
-v/--verbose: if supplied print lots of debug output (optional)

RULE SELECTION:
-c/--category: category to use
-f/--family: rule family, within category to use
-i/--indicator: precise rule.  Should be specified as I.J.K where
    I,J,and K are numbers

DOCUMENT TYPE:
-t/--type should be 'text' or 'html'

DOCUMENT to be examined is passed in as the last argument

The result is written to standard output in JSON format.  Since
multiple matches could apply in a single document, the result is a
JSON array.  Each element within the array contains the following
fields:

    category: the category of the successfully applied rule
    family: the family of the rule
    indicator: an array of 3 integers, the unique ID indicator of the rule
    weight: how informative this rule is for its category and
        family.  A value of 1 indicates the rule is believed to be a
	good indicator; a value of 0.5 indicates a weak indicator
    pattern: is the Python regular expression used to implement this
        rule
    matches: is an array of arrays.  Each inner array corresponds to
        one sequence of tokens.  There could be more than one match of
        a given rule, so there could be more than one subarray of
       tokens, although this is quite rare

Example:

  python patscan.py -c briefDuration data/test/tokens009.txt 

specifies (any rules) in category "briefDuration" be applied to the sentence from that file:

    Hi!  I'm brand new in this area.

The result shows that "new in this area" was found as a match instance
for the briefDuration/"new in town" rule family.

[
    {
        "category": "briefDuration", 
        "indicator": [
            3, 
            1, 
            1
        ], 
        "family": "new in town", 
        "weight": 1, 
        "matches": [
            [
                "new", 
                "in", 
                "this", 
                "area"
            ]
        ], 
        "pattern": "(?V1)<(?i)NEW|NU> <(?i)IN|N|TO> <(?i)THE|THIS>? <(?i)TOWN|AREA|CITY|NEIGHBORHOOD>"
    }
]
