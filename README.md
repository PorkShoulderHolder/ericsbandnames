# ericsbandnames
Pull the latest band names from http://ericsbandnames.com

## please use responsibly
This client pulls live from the site to ensure that we have all the latest bands. 
We dont want to inadvertently DDOS Eric's website, so please cache your results and limit the amount of traffic to the site

## installation
```
pip install ericsbandnames
```

## examples
#### Inline Usage
```
>>> from ericsbandnames import random_name
>>> band_names = random_name(n=10)
>>> print(band_names)
[u'New Man Rivers', u'Night Loop', u'Barbie Surgery', u'Adolph Nixon', u'The Last Yesterday', u'Alien vs Predator vs Brown vs The Board of Education', u'Glen Jeff Beck Hansen', u'Fake Cops', u'Abortion Magma', u'Goat Ghosts']
```

#### cli usage
the cli takes the same optional args as `random_name(n=<number of names>, sep=<word_serparator>, url=<alternative_url_in_case_he_changes_it?!?!>)` 
```
$ ericsbandnames
Louis Vuitton Colostomy Bag
$ ericsbandnames 5 _
[u'Pregnant_On_Purpose', u'Black_Smithers', u'Boring_Nightmare', u'Christmas_Cocaine_Showdown', u'Good_Feminist_Husband']
```


