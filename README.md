TrafficCop WAT ad classifiers.

Philpot 29 May 2015

This Github repository project contains two independently developed
capabilities for classifying escort posts.

A. folder wat/escort implements a rule-based keyword scanner.  Derived
in large part from example data provided by FBI agents, it has been
hand-crafted to match many common examples and derives all its
capabilities from the knowledge encoded in the file by a human.  It
can indicate the part of a document that triggered the categorization.
However, it is likely brittle and difficult to extend.

B. folder wat/learn implements a machine-learning Naive Bayes
classifier.  There is no embedded knowledge, so the capabilities of
training new categories is much greater.  The results are noisy and
the system requires significant preparation including human annotation
and data tokenization decisions, before one can deal with new rule
classes or new sentences.
