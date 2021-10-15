def lastNames(L):
    if not L:
        return None
    else:
        return list(map(lambda name: name[-1], L))

def citations(L):
    if not L:
        return None
    else:
        return list(map(lambda name: name[0][0].capitalize() + ". " + name[-1], L))

def fullCitations(L):
    def fullCitationsAux(full_name):
        x = 0
        citation = ""
        for name in full_name:
            while x < len(full_name) - 1:
                citation += full_name[x][0].capitalize() + ". "
                x += 1
        citation += full_name[-1]
        return citation
    
    if not L:
        return None
    else:
        return list(map(fullCitationsAux, L))
        