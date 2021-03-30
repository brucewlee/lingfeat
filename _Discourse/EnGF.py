# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: EnGF.py (Entity Grid Features)
License: CC-BY-SA 4.0

Original Author: Diego Palma @dpalmasan
Affiliation: Evernote
Contributing Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA

References:
>>> Original Python Code from TRUNAJOD2.0, modified by Bruce W. Lee
Publication 1: Palma, Diego, and John Atkinson. "Coherence-based automatic essay assessment." IEEE Intelligent Systems 33.5 (2018): 26-36.
Repository: <https://github.com/dpalmasan/TRUNAJOD2.0>

>>> S-V-O extraction inspired by an algorithm from
Publication 1: Rusu, Delia, et al. "Triplet extraction from sentences." Proceedings of the 10th International Multiconference” Information Society-IS. 2007.

>>> 16 transition patterns approach obtained from 
Publication 1: Barzilay, Regina, and Mirella Lapata. "Modeling local coherence: An entity-based approach." Computational Linguistics 34.1 (2008): 1-34.
Publication 2: Pitler, Emily, and Ani Nenkova. "Revisiting readability: A unified framework for predicting text quality." Proceedings of the 2008 conference on empirical methods in natural language processing. 2008.

>>> Notations in Dependency Mapping
Publication 1: Barzilay, Regina, and Mirella Lapata. "Modeling local coherence: An entity-based approach." Computational Linguistics 34.1 (2008): 1-34.

>>> Local Coherence (graph-based)
Publication 1: Guinaudeau, Camille, and Michael Strube. "Graph-based local coherence modeling." Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 2013.
"""

from lingfeat.utils import division

NOUNS = set(['NOUN', 'PRON', 'PROPN'])

ordered_transitions = [
    'SS', 'SO', 'SX', 'S-', 'OS', 'OO', 'OX', 'O-', 'XS', 'XO',
    'XX', 'X-', '-S', '-O', '-X', '--'
]

def dependency_mapping(dep):
    """
    +-----------+-----------------------------------+
    | EGrid Tag | Dependency Tag                    |
    +===========+===================================+
    | S         | nsub, csubj, csubjpass, dsubjpass |
    +-----------+-----------------------------------+
    | O         | iobj, obj, pobj, dobj             |
    +-----------+-----------------------------------+
    | X         | For any other dependency tag      |
    +-----------+-----------------------------------+
    """
    S = ['nsubj', 'csubj', 'csubjpass', 'dsubjpass']
    O = ['iobj', 'obj', 'pobj', 'dobj']
    if S.count(dep) == 1:
        return 'S'
    if O.count(dep) == 1:
        return 'O'
    return 'X'


class EntityGrid:

    def __init__(self, NLP_doc, n_sent):
        """Construct EntityGrid object."""
        # Initialization
        entity_map = dict()
        entity_grid = dict()
        i = 1
        entity_map['s%d' % i] = []
        entity_features = {
            'SS': 0,
            'SO': 0,
            'SX': 0,
            'S-': 0,
            'OS': 0,
            'OO': 0,
            'OX': 0,
            'O-': 0,
            'XS': 0,
            'XO': 0,
            'XX': 0,
            'X-': 0,
            '-S': 0,
            '-O': 0,
            '-X': 0,
            '--': 0
        }

        # For each sentence, get dependencies and its grammatical role
        for token in NLP_doc:
            if token.pos_ in NOUNS:
                entity_map['s%d' % i].append((token.text.upper(),
                                                token.dep_))
                if token.text.upper() not in entity_grid:
                    entity_grid[token.text.upper()] = ['-'] * n_sent
            i += 1
            entity_map['s%d' % i] = []

        # Last iteration will create an extra element, so I remove it.
        entity_map.pop('s%d' % i)

        # Fill entity grid
        for i in range(n_sent):
            sentence = "s%d" % (i + 1)
            for entity, dep in entity_map[sentence]:
                if entity_grid[entity][i] == '-':
                    entity_grid[entity][i] = dependency_mapping(dep)
                elif dependency_mapping(dep) == 'S':
                    entity_grid[entity][i] = dependency_mapping(dep)
                elif (dependency_mapping(dep) == 'O'
                      and entity_grid[entity][i] == 'X'):
                    entity_grid[entity][i] = dependency_mapping(dep)

        # Compute feature vector, we consider transitions of length 2
        total_transitions = (n_sent - 1) * len(entity_grid.keys())

        for entity in entity_grid:
            for i in range(n_sent - 1):
                # Transition type found (e.g. S-)
                transition = (
                    entity_grid[entity][i] + entity_grid[entity][i + 1])

                # Adding 1 to transition count
                entity_features[transition] += 1

        for prob in entity_features:
            if total_transitions != 0:
                entity_features[prob] /= float(total_transitions)
            else:
                entity_features[prob] = 0.0

        self.grid = entity_grid
        self.n_sent = n_sent
        self.prob = entity_features

    def retrieve(self):
        """
        Retrieve All
        """
        result = {}
        result['ra_SSTo_C'] = self.prob['SS']
        result['ra_SOTo_C'] = self.prob['SO']
        result['ra_SXTo_C'] = self.prob['SX']
        result['ra_SNTo_C'] = self.prob['S-']
        result['ra_OSTo_C'] = self.prob['OS']
        result['ra_OOTo_C'] = self.prob['OO']
        result['ra_OXTo_C'] = self.prob['OX']
        result['ra_ONTo_C'] = self.prob['O-']
        result['ra_XSTo_C'] = self.prob['XS']
        result['ra_XOTo_C'] = self.prob['XO']
        result['ra_XXTo_C'] = self.prob['XX']
        result['ra_XNTo_C'] = self.prob['X-']
        result['ra_NSTo_C'] = self.prob['-S']
        result['ra_NOTo_C'] = self.prob['-O']
        result['ra_NXTo_C'] = self.prob['-X']
        result['ra_NNTo_C'] = self.prob['--']
        lcresult = get_local_coherence(self)
        return {**result, **lcresult}

def weighting_syntactic_role(entity_role):
    """
    Return weight given an entity grammatical role.
    +-----------+--------+
    | EGrid Tag | Weight |
    +===========+========+
    | S         | 3      |
    +-----------+--------+
    | O         | 2      |
    +-----------+--------+
    | X         | 1      |
    +-----------+--------+
    | dash      | 0      |
    +-----------+--------+
    """
    if entity_role == u"S":
        return 3
    elif entity_role == u"O":
        return 2
    elif entity_role == u"X":
        return 1

    return 0

def get_local_coherence(EntityGrid):
    local_coherence_PU = 0.0        #lcPA
    local_coherence_PW = 0.0        #lcPW
    local_coherence_PA = 0.0        #lcPU
    local_coherence_PU_dist = 0.0   #lcdPA
    local_coherence_PW_dist = 0.0   #lcdPW
    local_coherence_PA_dist = 0.0   #lcdPU

    n_sent = EntityGrid.n_sent
    grid = EntityGrid.grid

    PW = [[0] * n_sent for i in range(n_sent)]

    # Weight Matrix for PACC, syntactic information is accounted for by
    # integrating the edges of the bipartite graph
    W = [[0] * n_sent for i in range(n_sent)]

    for entity in grid:
        for i in range(n_sent):
            for j in range(i + 1, n_sent):
                if grid[entity][i] != u"-" and grid[entity][j] != u"-":
                    PW[i][j] += 1
                    W[i][j] += (weighting_syntactic_role(grid[entity][i]) *
                                weighting_syntactic_role(grid[entity][j]))

    PU = [list(map(lambda x: x != 0, PWi)) for PWi in PW]

    for i in range(n_sent):
        local_coherence_PW += sum(PW[i])
        local_coherence_PU += sum(PU[i])
        local_coherence_PA += sum(W[i])

    local_coherence_PW /= n_sent
    local_coherence_PU /= n_sent
    local_coherence_PA /= n_sent

    # Weighting projection graphs
    PU_weighted = list(PU)
    PW_weighted = list(PW)
    PA_weighted = list(W)
    for i in range(n_sent):
        for j in range(i + 1, n_sent):
            PU_weighted[i][j] = division(PU[i][j],float(j - i))
            PW_weighted[i][j] = division(PW[i][j],float(j - i))
            PA_weighted[i][j] = division(W[i][j],float(j - i))

    for i in range(n_sent):
        local_coherence_PW_dist += sum(PW_weighted[i])
        local_coherence_PU_dist += sum(PU_weighted[i])
        local_coherence_PA_dist += sum(PA_weighted[i])

    local_coherence_PW_dist /= n_sent
    local_coherence_PU_dist /= n_sent
    local_coherence_PA_dist /= n_sent

    result = {
        'LoCohPA_S':local_coherence_PU,        
        'LoCohPW_S':local_coherence_PW,
        'LoCohPU_S':local_coherence_PA,
        'LoCoDPA_S':local_coherence_PU_dist,
        'LoCoDPW_S':local_coherence_PW_dist,
        'LoCoDPU_S':local_coherence_PA_dist,
    }
    return result