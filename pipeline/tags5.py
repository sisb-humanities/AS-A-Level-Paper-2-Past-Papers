"""Tags for 2021 papers (batch10). Key: (series, year, variant, qid). build.py merges T5 into T2.

Same rules as tags4 (2020–22 syllabus): point-based mark schemes, so each part's evaluation marks ('ao3') are read from
its mark scheme; 8-mark (a) essay parts have none, 12-mark (b) parts 4. Topics use the current (2023+) AS codes."""


def t(topics, sub, cmd, cmd2, concepts, ao3=0, context=''):
    return dict(topics=topics, sub=sub, cmd=cmd, cmd2=cmd2, concepts=concepts, context=context, ao3=ao3)


VN = 'Vietnam – fruit and vegetable exports to China'
MC = 'Myanmar/Cambodia – EU tariffs on rice'
LU = 'Great Britain/Luxembourg – transport and free public transport'
JP = 'Japan – deflation and monetary policy'
HI = 'Zimbabwe/Venezuela – hyperinflation'
IN = 'India – slowing growth'
CN = 'China – growth, consumption and the US trade war'

OFF_SYLLABUS5 = {
    '9708_w21_21_Q1c': 'Functions of money: not in the 2023+ AS syllabus (now A Level).',
}

T5 = {
    # ---------- June 2021, 9708/21 — Vietnam ----------
    ('June', 2021, '21', '1(a)(i)'): t(['6.3'], ['6.3.2'], 'Describe', '', ['current account balance', 'data trend'], 0, VN),
    ('June', 2021, '21', '1(a)(ii)'): t(['6.3'], ['6.3.2'], 'Calculate', '', ['exports', 'data calculation'], 0, VN),
    ('June', 2021, '21', '1(b)'): t(['2.4', '2.1'], ['2.1.3', '2.1.4', '2.4.2'], 'Explain', '', ['determinants of demand', 'determinants of supply', 'exports'], 0, VN),
    ('June', 2021, '21', '1(c)'): t(['2.1', '6.2'], ['2.1.6', '6.2.2'], 'Explain', '', ['administrative barriers', 'costs of production', 'supply shift'], 0, VN),
    ('June', 2021, '21', '1(d)'): t(['6.1', '6.3'], ['6.1.2', '6.1.4', '6.3.3'], 'Discuss', '', ['dependence on one export market', 'specialisation', 'risk'], 1, VN),
    ('June', 2021, '21', '1(e)'): t(['4.3', '6.3'], ['4.3.5', '4.3.12'], 'Discuss', '', ['net exports', 'aggregate demand', 'AD/AS', 'inflation'], 1, VN),
    ('June', 2021, '21', '2(a)'): t(['1.6', '1.4'], ['1.6.1', '1.6.2', '1.4.2'], 'Explain', '', ['private goods', 'free goods', 'public goods', 'market economy']),
    ('June', 2021, '21', '2(b)'): t(['3.2', '2.4', '1.4'], ['3.2.3', '2.4.4'], 'Discuss', '', ['direct provision', 'price mechanism', 'resource allocation'], 4),
    ('June', 2021, '21', '3(a)'): t(['2.5', '2.2'], ['2.5.1', '2.5.3', '2.2.6'], 'Explain', '', ['consumer surplus', 'price fall', 'PED', 'luxury vs necessity']),
    ('June', 2021, '21', '3(b)'): t(['2.2'], ['2.2.8'], 'Discuss', '', ['YED', 'XED', 'business decisions'], 4),
    ('June', 2021, '21', '4(a)'): t(['6.4'], ['6.4.2', '6.4.4'], 'Explain', '', ['floating exchange rate', 'depreciation', 'currency demand and supply']),
    ('June', 2021, '21', '4(b)'): t(['5.3', '6.4', '4.6'], ['5.3.4', '6.4.5', '4.6.4'], 'Discuss', '', ['monetary policy', 'inflation control', 'floating exchange rate', 'appreciation'], 4),

    # ---------- June 2021, 9708/22 — Rice farmers in Cambodia and Myanmar ----------
    ('June', 2021, '22', '1(a)'): t(['4.6'], ['4.6.2'], 'Compare', '', ['price level', 'data comparison'], 0, MC),
    ('June', 2021, '22', '1(b)'): t(['6.3'], ['6.3.2'], 'Compare', '', ['current account balance', 'data comparison'], 0, MC),
    ('June', 2021, '22', '1(c)'): t(['5.4', '6.1'], ['5.4.3', '6.1.4'], 'Explain', '', ['international competitiveness', 'supply-side policy', 'devaluation'], 0, MC),
    ('June', 2021, '22', '1(d)'): t(['6.2', '2.2'], ['6.2.2', '2.2.7'], 'Discuss', '', ['tariffs', 'PED', 'XED', 'alternative markets'], 0, MC),
    ('June', 2021, '22', '1(e)'): t(['6.2', '6.1'], ['6.2.3', '6.1.2'], 'Discuss', '', ['free trade', 'tariffs', 'EU', 'domestic producers'], 2, MC),
    ('June', 2021, '22', '2(a)'): t(['3.2', '1.6', '3.1'], ['3.2.1', '1.6.4', '3.1.2'], 'Explain', 'State', ['demerit good', 'indirect tax', 'resource allocation', 'sugar tax']),
    ('June', 2021, '22', '2(b)'): t(['3.2', '1.6'], ['3.2.4', '3.2.1', '3.2.6', '1.6.4'], 'Compare', 'Consider', ['minimum price', 'demerit goods', 'public health', 'alternative policies'], 4),
    ('June', 2021, '22', '3(a)'): t(['2.2'], ['2.2.1', '2.2.3'], 'Explain', '', ['XED', 'substitutes', 'complements', 'unrelated goods']),
    ('June', 2021, '22', '3(b)'): t(['2.2'], ['2.2.8'], 'Discuss', 'Consider', ['YED', 'PED', 'recession', 'business decisions'], 4),
    ('June', 2021, '22', '4(a)'): t(['4.6', '4.3'], ['4.6.1', '4.3.12'], 'Explain', '', ['deflation', 'AD/AS', 'causes of deflation']),
    ('June', 2021, '22', '4(b)'): t(['5.3', '5.2', '4.6'], ['5.3.3', '5.2.6', '4.6.1'], 'Discuss', '', ['monetary policy', 'fiscal policy', 'deflation'], 4),

    # ---------- June 2021, 9708/23 — Transport in Great Britain and Luxembourg ----------
    ('June', 2021, '23', '1(a)(i)'): t(['2.1'], ['2.1.2'], 'Describe', '', ['data trend', 'bus journeys'], 0, LU),
    ('June', 2021, '23', '1(a)(ii)'): t(['2.1', '4.6'], ['2.1.3', '4.6.2'], 'Explain', '', ['price changes', 'determinants of demand', 'index numbers'], 0, LU),
    ('June', 2021, '23', '1(b)'): t(['1.1', '3.2'], ['1.1.3', '3.2.2'], 'Explain', '', ['opportunity cost', 'subsidy'], 0, LU),
    ('June', 2021, '23', '1(c)'): t(['1.6'], ['1.6.1'], 'Explain', '', ['free goods', 'zero price', 'opportunity cost'], 0, LU),
    ('June', 2021, '23', '1(d)'): t(['3.2', '2.2'], ['3.2.4', '2.2.6'], 'Discuss', '', ['minimum price', 'congestion', 'PED for fuel'], 1, LU),
    ('June', 2021, '23', '1(e)'): t(['3.2', '1.4', '2.4'], ['3.2.3', '2.4.4'], 'Discuss', '', ['free provision', 'resource allocation', 'public transport'], 1, LU),
    ('June', 2021, '23', '2(a)'): t(['2.2'], ['2.2.1', '2.2.3'], 'Explain', '', ['XED', 'complements', 'substitutes', 'tourism']),
    ('June', 2021, '23', '2(b)'): t(['3.2', '2.2'], ['3.2.1', '2.2.7'], 'Discuss', '', ['indirect tax', 'tax revenue', 'PED', 'tourism'], 4),
    ('June', 2021, '23', '3(a)'): t(['4.3'], ['4.3.6', '4.3.7', '4.3.9'], 'Explain', '', ['aggregate supply', 'SRAS', 'LRAS', 'AS shift']),
    ('June', 2021, '23', '3(b)'): t(['4.3', '4.4', '4.6'], ['4.3.12', '4.4.5', '4.6.4'], 'Discuss', '', ['aggregate demand increase', 'growth', 'inflation', 'employment'], 4),
    ('June', 2021, '23', '4(a)'): t(['6.2', '6.1'], ['6.2.1', '6.1.2'], 'Explain', '', ['free trade area', 'customs union', 'trade agreements']),
    ('June', 2021, '23', '4(b)'): t(['6.1', '6.2'], ['6.1.2', '6.2.3'], 'Discuss', '', ['free trade', 'net importers', 'net exporters'], 4),

    # ---------- March 2021, 9708/22 — Challenges for the Japanese economy ----------
    ('March', 2021, '22', '1(a)'): t(['4.6'], ['4.6.2'], 'Calculate', '', ['inflation rate', 'price index', 'data calculation'], 0, JP),
    ('March', 2021, '22', '1(b)'): t(['5.2'], ['5.2.6'], 'Identify', '', ['fiscal stance', 'budget deficit', 'data interpretation'], 0, JP),
    ('March', 2021, '22', '1(c)'): t(['4.6'], ['4.6.1', '4.6.5'], 'Explain', '', ['deflation', 'consumption', 'delayed spending'], 0, JP),
    ('March', 2021, '22', '1(d)'): t(['6.4', '5.3'], ['6.4.2', '6.4.4'], 'Explain', '', ['exchange rate', 'interest rate differentials', 'depreciation'], 0, JP),
    ('March', 2021, '22', '1(e)'): t(['5.3', '4.6', '4.3'], ['5.3.3', '5.3.4', '4.6.4'], 'Discuss', 'Consider', ['expansionary monetary policy', 'deflation', 'aggregate demand'], 2, JP),
    ('March', 2021, '22', '1(f)'): t(['5.2', '4.3', '6.3'], ['5.2.6', '5.2.7', '4.3.5'], 'Discuss', '', ['government spending', 'expansionary fiscal policy', 'external demand'], 2, JP),
    ('March', 2021, '22', '2(a)'): t(['1.5', '1.3'], ['1.5.3', '1.5.4', '1.3.1'], 'Explain', '', ['PPC', 'unused labour', 'natural resources', 'PPC shift']),
    ('March', 2021, '22', '2(b)'): t(['5.4', '1.3'], ['5.4.3', '1.3.1'], 'Discuss', '', ['supply-side policy', 'labour supply', 'enterprise'], 4),
    ('March', 2021, '22', '3(a)'): t(['2.2'], ['2.2.1', '2.2.3'], 'Explain', '', ['XED', 'complements', 'substitutes', 'cars']),
    ('March', 2021, '22', '3(b)'): t(['6.2'], ['6.2.2', '6.2.3'], 'Discuss', '', ['import controls', 'protectionism', 'car industry', 'retaliation'], 4),
    ('March', 2021, '22', '4(a)'): t(['2.4', '2.1'], ['2.4.1', '2.4.2', '2.1.6'], 'Explain', '', ['market equilibrium', 'wages', 'costs of production', 'income effect on demand']),
    ('March', 2021, '22', '4(b)'): t(['3.2', '3.1'], ['3.2.1', '3.2.2', '3.2.4', '3.1.1'], 'Discuss', '', ['government intervention', 'price controls', 'taxes and subsidies', 'resource allocation'], 4),

    # ---------- November 2021, 9708/21 — What is the 'right' level of inflation? ----------
    ('November', 2021, '21', '1(a)'): t(['4.6'], ['4.6.3', '4.6.5'], 'Explain', '', ['real value of money', 'inflation'], 0, HI),
    ('November', 2021, '21', '1(b)'): t(['4.6', '2.4'], ['4.6.4', '2.4.2'], 'Explain', '', ['expectations', 'panic buying', 'demand shift', 'shortages'], 0, HI),
    ('November', 2021, '21', '1(c)'): t(['4.6', '5.3'], ['4.6.5'], 'Explain', '', ['functions of money', 'hyperinflation'], 0, HI),
    ('November', 2021, '21', '1(d)'): t(['5.3', '4.3', '4.6'], ['5.3.4', '4.3.12'], 'Discuss', '', ['monetary policy', 'investment', 'inflation', 'policy conflict'], 1, HI),
    ('November', 2021, '21', '1(e)'): t(['4.6', '3.3'], ['4.6.5'], 'Discuss', '', ['consequences of hyperinflation', 'winners and losers', 'debtors and creditors'], 1, HI),
    ('November', 2021, '21', '2(a)'): t(['1.5'], ['1.5.3', '1.5.4'], 'Compare', '', ['PPC', 'movement vs shift', 'resources']),
    ('November', 2021, '21', '2(b)'): t(['1.4'], ['1.4.1', '1.4.2'], 'Discuss', '', ['planned economy', 'market economy', 'transition'], 4),
    ('November', 2021, '21', '3(a)'): t(['3.2', '2.5'], ['3.2.4', '2.5.1'], 'Explain', '', ['minimum price', 'excess supply', 'consumers and producers']),
    ('November', 2021, '21', '3(b)'): t(['2.2', '2.3'], ['2.2.8', '2.3.5'], 'Discuss', '', ['PED', 'PES', 'business decisions'], 4),
    ('November', 2021, '21', '4(a)'): t(['6.4', '6.3'], ['6.4.1', '6.3.3'], 'Explain', '', ['fixed exchange rate', 'central bank intervention', 'foreign currency reserves', 'current account deficit']),
    ('November', 2021, '21', '4(b)'): t(['6.5'], ['6.5.1', '6.5.2'], 'Discuss', '', ['expenditure-reducing policy', 'current account deficit', 'floating exchange rate'], 4),

    # ---------- November 2021, 9708/22 — India's slowing growth ----------
    ('November', 2021, '22', '1(a)'): t(['4.3', '6.3'], ['4.3.2'], 'Calculate', '', ['imports', 'aggregate demand', 'data calculation'], 0, IN),
    ('November', 2021, '22', '1(b)(i)'): t(['2.2'], ['2.2.1', '2.2.2'], 'Explain', '', ['YED', 'income tax cut'], 0, IN),
    ('November', 2021, '22', '1(b)(ii)'): t(['2.2'], ['2.2.3'], 'Explain', '', ['YED', 'normal goods', 'luxury goods'], 0, IN),
    ('November', 2021, '22', '1(c)'): t(['5.4'], ['5.4.3'], 'Identify', 'Explain', ['supply-side policy', 'competitiveness'], 0, IN),
    ('November', 2021, '22', '1(d)'): t(['5.3', '4.3'], ['5.3.3', '5.3.4'], 'Discuss', '', ['interest rate cut', 'aggregate demand', 'inflation risk'], 1, IN),
    ('November', 2021, '22', '1(e)'): t(['1.6', '3.2', '1.4'], ['1.6.2', '3.2.3', '1.4.1'], 'Consider', '', ['infrastructure', 'public goods', 'private vs public provision'], 1, IN),
    ('November', 2021, '22', '2(a)'): t(['1.5', '1.1'], ['1.5.1', '1.5.2', '1.1.3'], 'Explain', '', ['PPC', 'opportunity cost', 'increasing opportunity cost']),
    ('November', 2021, '22', '2(b)'): t(['6.1'], ['6.1.1', '6.1.2'], 'Discuss', '', ['comparative advantage', 'free trade', 'limitations of the theory'], 4),
    ('November', 2021, '22', '3(a)'): t(['2.5', '3.2', '2.2'], ['2.5.1', '2.5.3', '3.2.1'], 'Explain', '', ['consumer surplus', 'indirect tax', 'PED']),
    ('November', 2021, '22', '3(b)'): t(['3.2', '3.3'], ['3.2.4', '3.2.2', '3.3.4'], 'Discuss', '', ['maximum price', 'food subsidies', 'food shortages'], 4),
    ('November', 2021, '22', '4(a)'): t(['4.6', '4.3'], ['4.6.1', '4.6.4', '4.3.12'], 'Explain', '', ['inflation', 'demand-pull', 'cost-push', 'AD/AS']),
    ('November', 2021, '22', '4(b)'): t(['4.6'], ['4.6.5'], 'Discuss', '', ['consequences of inflation', 'domestic effects', 'external effects'], 4),

    # ---------- November 2021, 9708/23 — China's uncertain economic prospects ----------
    ('November', 2021, '23', '1(a)'): t(['4.3', '4.4'], ['4.3.2', '4.4.2'], 'Describe', '', ['components of AD', 'real output growth', 'data trend'], 0, CN),
    ('November', 2021, '23', '1(b)(i)'): t(['2.2', '4.4'], ['2.2.3'], 'Identify', '', ['YED', 'income and car sales'], 0, CN),
    ('November', 2021, '23', '1(b)(ii)'): t(['2.2', '4.4'], ['2.2.3'], 'Consider', '', ['data interpretation', 'car sales', 'real output growth'], 0, CN),
    ('November', 2021, '23', '1(c)'): t(['6.2'], ['6.2.2', '6.2.3'], 'State', 'Explain', ['tools of protection', 'trade war', 'consumers and producers'], 0, CN),
    ('November', 2021, '23', '1(d)'): t(['5.2', '2.2'], ['5.2.4', '2.2.3'], 'Discuss', '', ['direct tax cut', 'YED', 'normal and inferior goods'], 1, CN),
    ('November', 2021, '23', '1(e)'): t(['4.4', '4.3'], ['4.4.4', '4.3.5'], 'Discuss', '', ['consumption-led growth', 'investment', 'exports'], 1, CN),
    ('November', 2021, '23', '2(a)'): t(['1.1', '1.4'], ['1.1.1', '1.1.4', '1.4.1'], 'Explain', '', ['economic problem', 'planned economy', 'market economy']),
    ('November', 2021, '23', '2(b)'): t(['1.6', '1.4', '3.2'], ['1.6.2', '1.6.3', '1.4.1', '3.2.3'], 'Discuss', '', ['mixed economy', 'public goods', 'merit goods', 'role of government'], 4),
    ('November', 2021, '23', '3(a)'): t(['2.2'], ['2.2.6', '2.2.7'], 'Explain', '', ['PED', 'proportion of income', 'total revenue']),
    ('November', 2021, '23', '3(b)'): t(['2.2'], ['2.2.8'], 'Discuss', '', ['XED', 'YED', 'pricing decisions'], 4),
    ('November', 2021, '23', '4(a)'): t(['4.6'], ['4.6.2', '4.6.5'], 'Explain', '', ['measuring inflation', 'CPI', 'consequences of inflation']),
    ('November', 2021, '23', '4(b)'): t(['5.3', '4.6', '5.2'], ['5.3.4', '4.6.4'], 'Discuss', '', ['interest rates', 'inflation control', 'alternative policies'], 4),
}
