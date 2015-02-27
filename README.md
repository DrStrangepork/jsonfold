# jsonfold
A JSON pretty print script that displays JSON with multiple levels of minimization

## Want to pretty print JSON with multiple levels of minimization?
We have standard pretty printed JSON:
```
{
  "results": {
    "groups": {
      "alpha": {
        "items": {
          "apple": {
            "attributes": {
              "class": "fruit"
            }
          },
          "pear": {
            "attributes": {
              "class": "fruit"
            }
          },
          "dog": {
            "attributes": {
              "class": null
            }
          }
        }
      },
      "beta": {
        "items": {
          "banana": {
            "attributes": {
              "class": "fruit"
            }
          }
        }
      }
    }
  }
}
```

And we have JMin (minimized json):
```
{"results":{"groups":{"alpha":{"items":{"apple":{"attributes":{"class":"fruit"}},"pear":{"attributes":{"class":"fruit"}},"dog":{"attributes":{"class":null}}}},"beta":{"items":{"banana":{"attributes":{"class":"fruit"}}}}}}}
```

But if you want to collapse JSON down to a certain level, your options were limited. Well, before I wrote this script, as far as I found, there were NO options. But with **jsonfold**, you can now do something like this:
```
{
    "results": {
        "groups": {
            "alpha": {
                "items": {
                    "pear": {"attributes":{"class":"fruit"}},
                    "apple": {"attributes":{"class":"fruit"}},
                    "dog": {"attributes":{"class":null}}
                }
            },
            "beta": {
                "items": {
                    "banana": {"attributes":{"class":"fruit"}}
                }
            }
        }
    }
}
```

The above is "pretty-print JSON, minimized at level 5", or ```jsonfold.py test.json -f 5```. Every level of JSON from the 5th indent and deeper is minimized to the 5th indent level.

## Installation
Just install it and run it.

## Requirements
python >=2.6

## Usage
```
$ jsonfold.py -h
Usage: jsonfold.py json_file [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -f FOLD_LEVEL, --fold-level=FOLD_LEVEL
                        int (all json is minimized to this level)
  -i INDENT, --indent=INDENT
                        int (spaces of indentation, default is 4)
  -o filename, --outfile=filename
                        write output to a file
```

## TODO
1. I'd like to rely heavier on the [json module](https://docs.python.org/2.6/library/json.html) rather than use my own print method.
2. I'd like to add an option to print in sorted/alphabetical order.

## License
GNU GPL v3<br>
You like it? You can use it, play with it, adapt it. I'd prefer if you recommend updates here, so I can improve it for everyone.
