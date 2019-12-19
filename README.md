### Material
- [The *psycopg2* tutorial I'm reading right now](http://initd.org/psycopg/docs/usage.html)
- [TOC of Official documentation of *psycopg2*](http://initd.org/psycopg/docs/index.html)
- [*psycopg2* documentation PDF](http://initd.org/psycopg/docs/index.html) <small>(`2.7.6`, June 2019)</small>

### Read soure code

- Get it
  - `git clone https://github.com/psycopg/psycopg2 && cd psycopg2`
- Search _methods_, _functions_ etc.

  ```bash
  grep -inr 'KEYWORD' SEARCH_PATH \
    | grep -vi "test\|NEWS\|pep\|rst\|psycopg/\|errorcode" \
    | grep -i "KEYWORD"

  # OPTIONAL pipes
    | wc -l             # how many search results
    >| OUTPUT_FILE      # export search results to a text file

  # test\|NEWS\|pep\|rst\|psycopg/\|errorcode
  # test        typically we don't need it
  # pep, rst    you may add this if you just wanna see the code
  # psycopg     no C code
  # errorcode   typically we don't need it
  ```
