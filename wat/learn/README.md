			 LEARNED CLASSIFIERS

Andrew Philpot 
29 May 2015
philpot@isi.edu

DATA

For experiment wat_annot_escort_01, I annotated 1000 backpage posts
from about 2/1/2015 (distributed from entire US).  Each post was
assigned one or more of the following labels.  Each is listed with the
number of times label was used.
  age (34) expressed specific restriction on age of client
  agency (33) post appears to be escort agency
  dance (2) provider primarily offering dance services
  employment (5) post offers employment
  healthspa (139) post advertises incall spa/massage location
  multi (129) post offers two providers for simultaneous session
  party (4)  post offers a buy-in/stripper party
  race (116) expressed (positive or negative) restriction on race of
             client, including references to thugs, pimp 
  spam (22) off-topic post; includes transvestite, clickbait, "get
            out"/anti-trafficking ads, strip club, other services 
  typical (558) escort ad with no other characteristic

Because category labels dance, employment, and party are so infrequent
and are also basically off-topic, I have combined those with the spam
category, and called the result offtopc.  this yields

  age (34) expressed specific restriction on age of client
  agency (33) post appears to be escort agency
  healthspa (139) post advertises incall spa/massage location
  multi (129) post offers two providers for simultaneous session
  race (116) expressed (positive or negative) restriction on race of
             client, including references to thugs, pimp 
  typical (558) escort ad with no other characteristic
  offtopic (33) all off-topic: dance/employment/party/spam

==================================================================

LEARNING:

Given these 1000 annotated samples, we use simple NaiveBayes learning
on unigram tokens (isolated words) to predict the label from the text.
These are binary classifiers, so they only try to identify things
which are in the single category; everthing else is a negative
example.  We use the standard Python NLTK learning module via the
TextBlob API (also available as a standard Python library).

DOCUMENT FEATURES FOR LEARNING:

We have three strategies for converting a text into unigram tokens.
These strategies are indicated using the input -i with values ci, cs
and default, respectively.

Top illustrate the difference , suppose we have only three documents:

Document A: "CALL me Sandy"
Document B: "Call me Rhonda"
Document C: "New in town 555-1212"

1. 'ci' means case-insensitive, which means that all letters are
treated as if they are lower case.  Our case-insensitive tokenizer
only generates tokens for seen items.  So the 'ci' tokens for Document
A would be 'call', 'me', 'sandy'

2 'cs' means case-sensitive, so all values are treated as is.  The
'cs' tokens for Document A would be 'CALL', 'me', 'Sandy'

3. 'default' is the default tokenizer implemented by the learning
module.  It is case-sensitive and it also uses both positive ("seen")
and negative ("unseen") words as tokens.  What this means is that
words not seen in a document are used as features that
counter-indicate the document label.  The 'default' tokens for
Document A would be: 'positive:CALL', 'positive:me', 'positive:Sandy',
'negative:Call', 'negative:Rhonda', 'negative:New', 'negative:in',
'negative:town', 'negative:555-1212'

MAIN CAPABILITIES SUPPORTED BY THIS LEARNING MODULE:

There is a single entry point for training, testing, and applying
    learning.  The choice of which operation(s) to do is controlled by
    command line arguments.

    usage: postclassifier.py [-h] -n NAME [-l] [-s] [-v] [-i INDICATOR]
			     [-t {text,html}] [--train TRAIN] [--test TEST]
			     [--validate VALIDATE] [--apply APPLY]

    optional arguments:
      -h, --help            show this help message and exit
      -n NAME, --name NAME, --positive NAME
			    name, tag of positive class
      -l, --load            load
      -s, --save            save
      -v, --verbose         verbose
      -i INDICATOR, --indicator INDICATOR
			    indicator/featureset/tokenizer
      -t {text,html}, --type {text,html}
			    input file type
      --train TRAIN         training size
      --test TEST           test set size
      --validate VALIDATE   validation set size
      --apply APPLY         apply

GENERAL MODEL ARGUMENTS:

-h/--help: don't do anything, only display the help (optional)
-v/--verbose: if supplied print lots of debug output (optional)
-n/--positive/--name: the name of the label category, e.g., one of 
    {age, agency, healthspa, multi, race, typical, offtopic}
    (required)
-i/--indicator/--featureset/--tokenizer: one of {cs, ci, default}

1. Loading model: use --load

python postclassifier.py -n <positiveClass> -i <tokenization> -l

2. Training model: use --train <trainingSize>

If --train 0 is passed, training is skipped

3. Saving model: use --save  

Models are saved into data/classifier in a file named after the
positive class and the feature tokenization

4. Applying the model to input data: use --apply

python postclassifier.py -n <positiveClass> -i <tokenization> -l --apply <input>

5. Testing the learner: --test

If --test 0 is passed, no testing is done

6. Validating: --validate is not implemented yet

Good machine learning practice is to train your data on 80% of the
labeled examples, test it on 10%, and hold out 10% for validation.

See also the scripts apply_all.sh, test_all.sh, and train_all.sh
See also some test cases in data/test which are used in test_all.sh
