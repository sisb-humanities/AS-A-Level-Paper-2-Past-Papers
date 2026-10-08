"""Tags for 2022 papers (batch9). Key: (series, year, variant, qid). build.py merges T4 into T2.

2022 papers follow the 2020–22 syllabus: Q1 data response + ONE essay from Q2–Q4; the mark schemes award marks by
point, not by AO1/AO2/AO3 levels. So each part carries its own evaluation marks ('ao3'), read from its mark scheme:
8-mark (a) parts have none; 12-mark (b) parts have 4 (evaluation incl. a reserved conclusion mark).
Topics use the current (2023+) AS codes so 2022 questions sit in the same heatmap rows."""


def t(topics, sub, cmd, cmd2, concepts, ao3=0, context=''):
    return dict(topics=topics, sub=sub, cmd=cmd, cmd2=cmd2, concepts=concepts, context=context, ao3=ao3)


BD = 'Bangladesh – inflation'
RU = 'Russia – inflation, oil prices and the rouble'
AV = 'Avocado market – US imports, Mexico and New Zealand'
TK = 'Turkey – current account, inflation and interest rate cuts'
GM = 'Governments and markets – price controls and buffer stocks'
MZ = 'Malawi/Zimbabwe – maize prices'
PK = 'Pakistan – agricultural subsidies'

# Parts on content that is no longer in the AS syllabus (2023+): flagged in build.py
OFF_SYLLABUS = {
    '9708_m22_22_Q1di': 'Functions of money: not in the 2023+ AS syllabus (now A Level).',
    '9708_m22_22_Q1dii': 'Functions of money: not in the 2023+ AS syllabus (now A Level).',
    '9708_w22_22_Q2a': 'Money and its functions: not in the 2023+ AS syllabus (now A Level).',
}

T4 = {
    # ---------- June 2022, 9708/21 — Inflation in Bangladesh ----------
    ('June', 2022, '21', '1(a)'): t(['4.6'], ['4.6.2'], 'Describe', '', ['inflation trend', 'data trend'], 0, BD),
    ('June', 2022, '21', '1(b)'): t(['4.6'], ['4.6.2'], 'Explain', '', ['consumer price index', 'weights'], 0, BD),
    ('June', 2022, '21', '1(c)'): t(['4.6'], ['4.6.5'], 'Explain', '', ['consequences of inflation', 'international competitiveness'], 0, BD),
    ('June', 2022, '21', '1(d)'): t(['4.6', '4.3'], ['4.6.4', '4.3.12'], 'Analyse', '', ['demand-pull inflation', 'cost-push inflation', 'wages', 'AD/AS'], 0, BD),
    ('June', 2022, '21', '1(e)'): t(['5.3', '5.2', '4.6'], ['5.3.4', '5.2.7'], 'Discuss', '', ['monetary policy', 'fiscal policy', 'inflation control'], 1, BD),
    ('June', 2022, '21', '2(a)'): t(['1.6'], ['1.6.2', '1.6.3'], 'Explain', '', ['merit goods', 'private goods', 'public goods', 'rivalry', 'excludability'], 0),
    ('June', 2022, '21', '2(b)'): t(['1.4'], ['1.4.1', '1.4.2'], 'Discuss', '', ['mixed economy', 'planned economy'], 4),
    ('June', 2022, '21', '3(a)'): t(['2.3'], ['2.3.4'], 'Explain', '', ['PES determinants', 'manufactured products', 'spare capacity', 'stocks']),
    ('June', 2022, '21', '3(b)'): t(['3.2', '2.2', '2.3'], ['3.2.1'], 'Discuss', '', ['tax incidence', 'indirect tax', 'PED', 'PES'], 4),
    ('June', 2022, '21', '4(a)'): t(['6.4'], ['6.4.1'], 'Explain', '', ['fixed exchange rate', 'foreign currency reserves'], 0),
    ('June', 2022, '21', '4(b)'): t(['6.2'], ['6.2.2', '6.2.3'], 'Discuss', '', ['export subsidies', 'tariffs', 'tools of protection'], 4),

    # ---------- June 2022, 9708/22 — Russia ----------
    ('June', 2022, '22', '1(a)(i)'): t(['4.6'], ['4.6.2'], 'Compare', '', ['inflation rate', 'data comparison'], 0, RU),
    ('June', 2022, '22', '1(a)(ii)'): t(['4.6'], ['4.6.1'], 'Identify', '', ['price level', 'inflation vs price level'], 0, RU),
    ('June', 2022, '22', '1(a)(iii)'): t(['4.6'], ['4.6.3'], 'Explain', '', ['real wages', 'nominal vs real'], 0, RU),
    ('June', 2022, '22', '1(b)'): t(['1.6'], ['1.6.2', '1.6.3'], 'Explain', '', ['private goods', 'public goods', 'rivalry', 'excludability', 'free school meals'], 0, RU),
    ('June', 2022, '22', '1(c)'): t(['5.2', '4.3', '4.6'], ['5.2.3', '5.2.6', '4.3.12'], 'Assess', '', ['budget surplus', 'aggregate demand', 'inflation'], 1, RU),
    ('June', 2022, '22', '1(d)'): t(['6.4', '6.3', '6.1'], ['6.4.5', '6.3.4', '6.1.3'], 'Discuss', '', ['oil prices', 'depreciation', 'export revenue', 'primary product dependence'], 1, RU),
    ('June', 2022, '22', '2(a)'): t(['1.5', '4.4'], ['1.5.3', '1.5.4', '4.4.4'], 'Explain', '', ['PPC shift', 'unused resources', 'productive capacity', 'actual vs potential growth'], 0),
    ('June', 2022, '22', '2(b)'): t(['1.4'], ['1.4.1', '1.4.2'], 'Discuss', 'Consider', ['planned economy', 'market economy', 'transition'], 4),
    ('June', 2022, '22', '3(a)'): t(['2.2', '2.4'], ['2.2.3', '2.4.2'], 'Explain', '', ['YED', 'normal goods', 'inferior goods', 'fall in income', 'equilibrium']),
    ('June', 2022, '22', '3(b)'): t(['2.2'], ['2.2.6', '2.2.8'], 'Discuss', 'Consider', ['PED determinants', 'business decisions', 'branding', 'substitutes'], 4),
    ('June', 2022, '22', '4(a)'): t(['6.3', '4.3'], ['6.3.1', '6.3.4'], 'Explain', 'Consider', ['current account surplus', 'employment', 'price level'], 0),
    ('June', 2022, '22', '4(b)'): t(['6.5'], ['6.5.1', '6.5.2'], 'Discuss', '', ['expenditure-reducing policy', 'expenditure-switching policy', 'current account deficit'], 4),

    # ---------- June 2022, 9708/23 — The changing market for avocados ----------
    ('June', 2022, '23', '1(a)'): t(['6.1'], ['6.1.2'], 'Describe', '', ['imports', 'data trend'], 0, AV),
    ('June', 2022, '23', '1(b)(i)'): t(['2.1'], ['2.1.2'], 'Calculate', '', ['percentage change', 'data calculation'], 0, AV),
    ('June', 2022, '23', '1(b)(ii)'): t(['2.4', '2.1'], ['2.4.2', '2.1.5', '2.1.6'], 'Explain', '', ['demand shift', 'supply shift', 'price change'], 0, AV),
    ('June', 2022, '23', '1(c)'): t(['2.3'], ['2.3.3', '2.3.4'], 'Consider', '', ['PES', 'short run vs long run', 'agricultural supply'], 0, AV),
    ('June', 2022, '23', '1(d)'): t(['1.5', '1.1'], ['1.5.1', '1.1.3'], 'Explain', '', ['PPC', 'opportunity cost'], 0, AV),
    ('June', 2022, '23', '1(e)'): t(['2.4', '1.4'], ['2.4.4', '1.4.2'], 'Discuss', '', ['price mechanism', 'resource allocation', 'signalling'], 1, AV),
    ('June', 2022, '23', '2(a)'): t(['1.6'], ['1.6.2'], 'Explain', '', ['public good', 'non-rival', 'non-excludable', 'flood defences'], 0),
    ('June', 2022, '23', '2(b)'): t(['1.6', '3.2', '1.4'], ['1.6.3', '3.2.3', '1.4.1'], 'Discuss', '', ['merit goods', 'private sector', 'public sector', 'education', 'healthcare'], 4),
    ('June', 2022, '23', '3(a)'): t(['4.6', '4.3'], ['4.6.4', '4.3.12'], 'Explain', '', ['cost-push inflation', 'demand-pull inflation'], 0),
    ('June', 2022, '23', '3(b)'): t(['5.3', '4.6', '5.2', '5.4'], ['5.3.3', '5.3.4', '4.6.4'], 'Discuss', '', ['contractionary monetary policy', 'interest rates', 'inflation control', 'alternative policies'], 4),
    ('June', 2022, '23', '4(a)'): t(['6.3'], ['6.3.3', '6.3.4'], 'Explain', '', ['current account deficit', 'causes', 'competitiveness'], 0),
    ('June', 2022, '23', '4(b)'): t(['6.5'], ['6.5.1', '6.5.2'], 'Discuss', '', ['expenditure-switching policy', 'expenditure-reducing policy', 'current account deficit'], 4),

    # ---------- March 2022, 9708/22 — Turkey ----------
    ('March', 2022, '22', '1(a)'): t(['6.3'], ['6.3.2'], 'Describe', '', ['current account balance', 'data trend'], 0, TK),
    ('March', 2022, '22', '1(b)'): t(['6.1'], ['6.1.3'], 'Explain', '', ['terms of trade', 'export and import prices', 'data interpretation'], 0, TK),
    ('March', 2022, '22', '1(c)'): t(['6.3', '2.2', '4.6'], ['6.3.4', '2.2.7', '4.6.5'], 'Explain', '', ['inflation', 'international competitiveness', 'PED for exports and imports', 'current account'], 0, TK),
    ('March', 2022, '22', '1(d)(i)'): t(['5.3', '4.6'], ['4.6.3'], 'Explain', '', ['functions of money', 'standard of deferred payment', 'real interest rate'], 0, TK),
    ('March', 2022, '22', '1(d)(ii)'): t(['5.3', '4.6'], ['4.6.3'], 'Explain', '', ['functions of money', 'store of value', 'real interest rate'], 0, TK),
    ('March', 2022, '22', '1(e)'): t(['5.3', '4.3', '4.6'], ['5.3.4', '4.3.12'], 'Discuss', '', ['interest rate cut', 'aggregate demand', 'inflation', 'economic recovery'], 2, TK),
    ('March', 2022, '22', '2(a)'): t(['1.5', '1.1'], ['1.5.1', '1.5.3', '1.1.3'], 'Explain', '', ['PPC', 'capital vs consumer goods', 'short run vs long run'], 0),
    ('March', 2022, '22', '2(b)'): t(['1.4'], ['1.4.1', '1.4.2'], 'Discuss', '', ['planned economy', 'market economy', 'transition', 'consumers'], 4),
    ('March', 2022, '22', '3(a)'): t(['2.3'], ['2.3.4'], 'Explain', '', ['PES', 'determinants of PES', 'examples']),
    ('March', 2022, '22', '3(b)'): t(['5.2', '5.4'], ['5.2.4', '5.2.5', '5.4.3'], 'Discuss', 'Consider', ['fiscal policy', 'aggregate supply', 'supply-side effects of fiscal policy'], 4),
    ('March', 2022, '22', '4(a)'): t(['6.2'], ['6.2.1', '6.2.2'], 'Explain', 'Describe', ['protectionism', 'tools of protection', 'steel industry'], 0),
    ('March', 2022, '22', '4(b)'): t(['6.2'], ['6.2.3'], 'Discuss', 'Consider', ['protectionism', 'strategic industry', 'retaliation', 'consumers'], 4),

    # ---------- November 2022, 9708/21 — Governments and markets ----------
    ('November', 2022, '21', '1(a)'): t(['2.4'], ['2.4.4'], 'Explain', '', ['functions of price', 'signalling', 'scarcity'], 0, GM),
    ('November', 2022, '21', '1(b)'): t(['3.2'], ['3.2.4'], 'Explain', '', ['minimum price', 'fuel'], 0, GM),
    ('November', 2022, '21', '1(c)'): t(['3.2'], ['3.2.4'], 'Explain', '', ['minimum price', 'excess supply', 'basic food'], 0, GM),
    ('November', 2022, '21', '1(d)'): t(['3.2', '2.4'], ['3.2.5', '2.4.4'], 'Consider', '', ['buffer stock', 'price mechanism', 'commodity prices'], 1, GM),
    ('November', 2022, '21', '1(e)'): t(['3.2', '4.6'], ['3.2.4', '4.6.4'], 'Discuss', '', ['maximum price', 'inflation control', 'shortages'], 1, GM),
    ('November', 2022, '21', '2(a)'): t(['2.2'], ['2.2.6'], 'Explain', '', ['PED determinants', 'branding', 'time period'], 0),
    ('November', 2022, '21', '2(b)'): t(['2.2'], ['2.2.8'], 'Discuss', '', ['PED', 'YED', 'business decisions', 'cars'], 4),
    ('November', 2022, '21', '3(a)'): t(['1.5', '1.3'], ['1.5.3', '1.3.1'], 'Explain', '', ['PPC shift', 'quantity of labour', 'quality of labour'], 0),
    ('November', 2022, '21', '3(b)'): t(['5.4', '1.3'], ['5.4.3', '1.3.1'], 'Discuss', '', ['supply-side policy', 'enterprise', 'entrepreneurship'], 4),
    ('November', 2022, '21', '4(a)'): t(['6.4'], ['6.4.2', '6.4.4'], 'Explain', '', ['floating exchange rate', 'depreciation', 'currency demand and supply'], 0),
    ('November', 2022, '21', '4(b)'): t(['6.5', '6.2'], ['6.5.2', '6.2.2'], 'Discuss', '', ['protectionism', 'current account deficit', 'retaliation'], 4),

    # ---------- November 2022, 9708/22 — Variations in the price of maize ----------
    ('November', 2022, '22', '1(a)'): t(['2.4', '2.1'], ['2.4.2'], 'Identify', '', ['price fall', 'supply increase'], 0, MZ),
    ('November', 2022, '22', '1(b)'): t(['2.1', '2.4'], ['2.1.3', '2.4.2'], 'Explain', '', ['determinants of demand', 'demand shift'], 0, MZ),
    ('November', 2022, '22', '1(c)'): t(['2.4', '2.1'], ['2.4.2', '2.1.6'], 'Explain', '', ['supply and demand', 'price rise', 'data interpretation'], 0, MZ),
    ('November', 2022, '22', '1(d)'): t(['3.2'], ['3.2.4'], 'Explain', '', ['minimum price', 'incentive to produce'], 0, MZ),
    ('November', 2022, '22', '1(e)'): t(['3.2', '2.2', '2.3'], ['3.2.2', '2.2.7'], 'Consider', '', ['subsidy', 'subsidy incidence', 'PED', 'PES'], 2, MZ),
    ('November', 2022, '22', '1(f)'): t(['3.2', '3.3'], ['3.2.4', '3.3.4'], 'Discuss', '', ['maximum price', 'shortages', 'poorer households', 'staple food'], 2, MZ),
    ('November', 2022, '22', '2(a)'): t(['5.3'], ['5.3.2'], 'Explain', '', ['money', 'functions of money', 'contactless payments'], 0),
    ('November', 2022, '22', '2(b)'): t(['5.3', '4.6'], ['5.3.3', '5.3.4', '4.6.1'], 'Discuss', '', ['expansionary monetary policy', 'deflation', 'interest rates'], 4),
    ('November', 2022, '22', '3(a)'): t(['1.5', '1.1'], ['1.5.1', '1.1.1', '1.1.3'], 'Explain', '', ['PPC', 'scarcity', 'choice', 'opportunity cost'], 0),
    ('November', 2022, '22', '3(b)'): t(['5.4'], ['5.4.3', '5.4.4'], 'Discuss', 'Consider', ['supply-side policy', 'productive capacity', 'time lags', 'cost'], 4),
    ('November', 2022, '22', '4(a)'): t(['6.4', '4.6'], ['6.4.4', '6.4.3'], 'Explain', '', ['floating exchange rate', 'relative inflation', 'depreciation'], 0),
    ('November', 2022, '22', '4(b)'): t(['6.1'], ['6.1.3'], 'Discuss', 'Consider', ['terms of trade', 'export prices', 'competitiveness'], 4),

    # ---------- November 2022, 9708/23 — Pakistan's agricultural subsidies ----------
    ('November', 2022, '23', '1(a)'): t(['1.1', '3.2'], ['1.1.3', '3.2.2'], 'Explain', '', ['opportunity cost', 'subsidy', 'government spending'], 0, PK),
    ('November', 2022, '23', '1(b)(i)'): t(['3.2'], ['3.2.2'], 'State', '', ['subsidy', 'data interpretation'], 0, PK),
    ('November', 2022, '23', '1(b)(ii)'): t(['3.2', '6.1'], ['3.2.2', '6.1.1'], 'Explain', '', ['subsidy', 'international competitiveness', 'exports'], 0, PK),
    ('November', 2022, '23', '1(c)'): t(['3.2', '2.2'], ['3.2.1', '2.2.7'], 'Analyse', '', ['indirect tax', 'supply shift', 'PED'], 0, PK),
    ('November', 2022, '23', '1(d)'): t(['3.2'], ['3.2.3', '3.2.5'], 'Explain', '', ['government intervention', 'buffer stock', 'minimum price', 'direct provision'], 0, PK),
    ('November', 2022, '23', '1(e)'): t(['6.1', '3.2', '1.1'], ['6.1.1', '6.1.4', '3.2.2'], 'Discuss', '', ['comparative advantage', 'opportunity cost', 'agricultural subsidies'], 3, PK),
    ('November', 2022, '23', '2(a)'): t(['1.6', '3.1'], ['1.6.3', '1.6.4', '3.1.2'], 'Explain', '', ['merit goods', 'demerit goods', 'information failure']),
    ('November', 2022, '23', '2(b)'): t(['3.2'], ['3.2.4'], 'Discuss', '', ['maximum price', 'consumers', 'shortages', 'informal market'], 4),
    ('November', 2022, '23', '3(a)'): t(['5.2', '3.3'], ['5.2.4', '3.3.4'], 'Explain', '', ['progressive tax', 'regressive tax', 'direct tax', 'indirect tax']),
    ('November', 2022, '23', '3(b)'): t(['5.2', '5.3', '4.6'], ['5.2.6', '5.3.4', '4.6.4'], 'Discuss', '', ['direct taxes', 'interest rates', 'inflation control'], 4),
    ('November', 2022, '23', '4(a)'): t(['6.1', '6.4', '4.6'], ['6.1.3', '6.4.5'], 'Explain', '', ['terms of trade', 'relative inflation', 'depreciation'], 0),
    ('November', 2022, '23', '4(b)'): t(['6.2'], ['6.2.3'], 'Discuss', '', ['tariffs', 'trade war', 'winners and losers', 'retaliation'], 4),
}
