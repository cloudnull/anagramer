Anagramer the anagram finder
############################
:date: 2013-09-05 09:51
:tags: tools, text, processing, food for thought
:category: \*nix


General Overview
----------------

This is a very simple tool that will parse a list of known words from a
dictionary file and find all of the given anagrams based on a defined
constraint. The tool is compatible with Python 2.6, 2.7, and 3.4.


About the constraint:
  The constrain limits results to a given number of letters in a word.
  All of the anagrams which meet the the constrained number of
  letters and also have at least the same number of anagrams as there
  are letters will be printed.


About the word file:
  The file containing the words should have **ONLY** one word per line.  On
  most *\nix systems a common dictionary can be found at ``/usr/dict/words``
  or ``/usr/share/dict/words``.


.. code-block:: bash

    usage: anagramer

    From a given list of words or a file containing a list of words find and print
    out all of the anagrams possible for a given word.

    optional arguments:
      -h, --help            show this help message and exit
      --system-config [FILE]
                            Path to your Configuration file. This is an optional
                            argument used to specify config. available as:
                            env[ANAGRAM_CONFIG]
      --value-constraint [INT]
                            Constrain the results to a given number of anagrams
                            for a given word. This will find all of the anagrams
                            which there are at least the constrained letters in
                            the word and that also have at least as many anagrams
                            as there are letters. Default: 4
      --words-files [PATH] [[PATH] ...]
                            Path to a dictionary file. The file should contain one
                            word per line. Default: ['/usr/share/dict/words']

    Licensed Apache2
