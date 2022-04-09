from ctypes import string_at


class SYMBOLS:
  def __init__(self):

    self._symbols = {}

    CVT      = string_at(0x10,4).hex()
    pLoc     = int(CVT,16) - 40
    PRODNAME = string_at(pLoc,7).decode('cp500')
    ecvtLoc  = int(CVT,16) + 140
    ECVT     = string_at(ecvtLoc,4).hex()

    eSYMTLoc = int(ECVT,16) + 296
    ECVTSYMT = string_at(eSYMTLoc,4).hex()
    numLoc   = int(ECVTSYMT,16) + 2
    NUMSYMBS = int(string_at(numLoc,2).hex(),16)
    for i in range(NUMSYMBS):
      soff = i * 16
      namoffloc  = int(ECVTSYMT,16) +  4 + soff
      namlenloc  = int(ECVTSYMT,16) +  8 + soff
      valoffloc  = int(ECVTSYMT,16) + 12 + soff
      vallenloc  = int(ECVTSYMT,16) + 16 + soff
      namoff     = string_at(namoffloc,4).hex()
      namlen     = int(string_at(namlenloc,4).hex(),16)
      valoff     = string_at(valoffloc,4).hex()
      vallen     = int(string_at(vallenloc,4).hex(),16)
      symnameoff = int(ECVTSYMT,16) + 4 + int(namoff,16)
      valnameoff = int(ECVTSYMT,16) + 4 + int(valoff,16)
      symname    = string_at(symnameoff,namlen).decode('cp500')
      valname    = string_at(valnameoff,vallen).decode('cp500')
      self._symbols[symname] = valname

  def symbol(self, symbol):
     """Will return the value of a SYSTEM SYMBOL. Returns "False" if SYMBOL not present

    Args:
        symbol (str): The symbol name you want to query (e.g. SYSPLEX)

    Returns:
        str: The symbol value. False if symbol not defined

    """
    if symbol[0] != '&' and symbol[-1] != '.':
      symbol = '&' + symbol + '.'
    if symbol in self._symbols:
      return self._symbols[symbol]
    else:
      return False

  def symlist(self):
    symlist = []
    for sym in self._symbols:
      symlist.append(sym.replace('&','').replace('.',''))
    return symlist
