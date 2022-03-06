# pySymbols

An easy class for getting symbols and their values from common storage.

Only run this on z/OS (obviously)...


    
## Methods

Even though 'in memory' the symbols are stored as `&SYSPLEX.` this modules uses `SYSPLEX`

### symbol(symbolName)
Returns the value for the symbol, or False if symbol not present.

    s = SYMBOLS()
    sysplex = s.symbol('SYSPLEX')
    >> ADCD

### symlist()
Returns a full list of all symbol names.

    s.symlist()
    >> ['ADCDLVL', 'CNMDOMN', 'CNMNETID', ..., 'UNIXVER']

### Usage video :)

![Usage](https://github.com/wizardofzos/pysymbols/raw/main/symbols.gif)

## TODO

- make 'setup.py' installable?
