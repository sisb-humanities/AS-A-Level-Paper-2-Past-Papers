"""Tags for 2023 papers (batch7). Key: (series, year, variant, qid). Same shape as tags2.T2; build.py merges T3 into T2.
2023 is the first year of the 2023–25 syllabus; AS topic numbering 1.1–6.5 is the same as 2026–28."""


def t(topics, sub, cmd, cmd2, concepts, context=''):
    return dict(topics=topics, sub=sub, cmd=cmd, cmd2=cmd2, concepts=concepts, context=context)


IN = 'India – seasonal and frictional unemployment'
NG = 'Nigeria – dependence on oil and gas'
DN = 'USA/UK – doughnuts and sugary foods'
USI = 'USA – rising inflation and stimulus'
TW = 'Taiwan – export-led growth and an appreciating currency'
EO = 'Oil producers – electric cars and diversification'
CV = 'China/US/UK – recovery from the COVID-19 recession'

T3 = {
    # ---------- June 2023, 9708/21 — Unemployment in India ----------
    ('June', 2023, '21', '1(a)'): t(['4.5'], ['4.5.2'], 'Calculate', '', ['unemployment rate', 'data calculation'], IN),
    ('June', 2023, '21', '1(b)'): t(['4.5'], ['4.5.3'], 'Explain', '', ['seasonal unemployment', 'agriculture'], IN),
    ('June', 2023, '21', '1(c)'): t(['4.5'], ['4.5.2'], 'Consider', '', ['measuring unemployment', 'hidden unemployment', 'informal economy'], IN),
    ('June', 2023, '21', '1(d)'): t(['4.5'], ['4.5.3', '4.5.4'], 'Assess', '', ['seasonal unemployment', 'frictional unemployment', 'consequences of unemployment'], IN),
    ('June', 2023, '21', '1(e)'): t(['5.4', '5.2', '4.5'], ['5.4.3', '5.4.4', '5.2.7'], 'Assess', '', ['supply-side policy', 'expansionary fiscal policy', 'employment'], IN),
    ('June', 2023, '21', '2(a)'): t(['1.5'], ['1.5.3', '1.5.4'], 'Explain', 'Consider', ['PPC', 'movement vs shift', 'unemployed resources']),
    ('June', 2023, '21', '2(b)'): t(['1.6'], ['1.6.2', '1.6.3'], 'Assess', '', ['public good', 'merit good', 'education', 'excludability']),
    ('June', 2023, '21', '3(a)'): t(['2.2'], ['2.2.1', '2.2.2', '2.2.3', '2.2.6'], 'Explain', 'Consider', ['XED', 'XED formula', 'substitutes', 'complements']),
    ('June', 2023, '21', '3(b)'): t(['3.2'], ['3.2.5'], 'Assess', '', ['buffer stock', 'price stabilisation', 'agricultural products', 'storage costs']),
    ('June', 2023, '21', '4(a)'): t(['4.6', '4.3'], ['4.6.4', '4.3.12'], 'Explain', 'Consider', ['cost-push inflation', 'demand-pull inflation', 'AD/AS']),
    ('June', 2023, '21', '4(b)'): t(['5.3', '5.4', '4.6'], ['5.3.4', '5.4.4', '4.6.4'], 'Assess', '', ['monetary policy', 'supply-side policy', 'inflation control', 'time lags']),
    ('June', 2023, '21', '5(a)'): t(['6.4'], ['6.4.2', '6.4.4', '6.4.5'], 'Explain', 'Consider', ['floating exchange rate', 'depreciation', 'currency demand and supply']),
    ('June', 2023, '21', '5(b)'): t(['6.2', '6.1'], ['6.2.3', '6.1.2'], 'Assess', '', ['protectionism', 'free trade', 'infant industry', 'retaliation']),

    # ---------- June 2023, 9708/22 — Nigeria's dependence on oil and gas ----------
    ('June', 2023, '22', '1(a)'): t(['5.2'], ['5.2.1'], 'Compare', '', ['budget deficit', 'data comparison'], NG),
    ('June', 2023, '22', '1(b)'): t(['1.5', '4.5'], ['1.5.4'], 'Demonstrate', '', ['PPC', 'unemployed resources'], NG),
    ('June', 2023, '22', '1(c)'): t(['4.6', '3.2'], ['4.6.4', '3.2.2'], 'Consider', '', ['removal of subsidy', 'cost-push inflation', 'PED'], NG),
    ('June', 2023, '22', '1(d)'): t(['5.4', '6.1'], ['5.4.3', '5.4.4', '6.1.4'], 'Assess', '', ['supply-side policy', 'diversification', 'primary product dependence', 'export-oriented manufacturing'], NG),
    ('June', 2023, '22', '1(e)'): t(['5.2'], ['5.2.4'], 'Assess', '', ['direct tax', 'indirect tax', 'tax base', 'tax evasion', 'informal economy'], NG),
    ('June', 2023, '22', '2(a)'): t(['2.5', '2.4'], ['2.5.1', '2.5.2', '2.5.3', '2.5.4'], 'Explain', 'Consider', ['consumer surplus', 'producer surplus', 'cost increase', 'PED']),
    ('June', 2023, '22', '2(b)'): t(['3.2', '3.3'], ['3.2.4', '3.3.4'], 'Assess', '', ['maximum price', 'transfer payments', 'essential food', 'low-income households']),
    ('June', 2023, '22', '3(a)'): t(['2.4', '2.1'], ['2.4.1', '2.4.2', '2.1.6'], 'Explain', 'Consider', ['market equilibrium', 'costs of production', 'wages', 'income effect on demand']),
    ('June', 2023, '22', '3(b)'): t(['1.3', '4.4'], ['1.3.1', '1.3.2', '4.4.4'], 'Assess', '', ['entrepreneurship', 'factors of production', 'long-run growth']),
    ('June', 2023, '22', '4(a)'): t(['6.1'], ['6.1.1'], 'Explain', 'Consider', ['absolute advantage', 'comparative advantage', 'opportunity cost']),
    ('June', 2023, '22', '4(b)'): t(['6.5', '6.2'], ['6.5.2', '6.2.2'], 'Assess', '', ['protectionism', 'current account deficit', 'expenditure switching', 'retaliation']),
    ('June', 2023, '22', '5(a)'): t(['4.6', '6.4'], ['4.6.4', '6.4.5'], 'Explain', 'Consider', ['cost-push inflation', 'demand-pull inflation', 'depreciation', 'imported inflation']),
    ('June', 2023, '22', '5(b)'): t(['5.3', '5.2', '5.4', '4.6'], ['5.3.4', '5.2.7', '5.4.4'], 'Assess', '', ['monetary policy', 'fiscal policy', 'supply-side policy', 'inflation control']),

    # ---------- June 2023, 9708/23 — Are doughnuts demerit goods? (only paper with a 1(f)) ----------
    ('June', 2023, '23', '1(a)'): t(['2.1'], ['2.1.2'], 'Calculate', '', ['percentage change', 'data calculation', 'market size'], DN),
    ('June', 2023, '23', '1(b)'): t(['2.1'], ['2.1.3'], 'Explain', '', ['determinants of demand', 'working from home'], DN),
    ('June', 2023, '23', '1(c)'): t(['2.2'], ['2.2.3'], 'Comment', '', ['YED', 'income inelastic'], DN),
    ('June', 2023, '23', '1(d)'): t(['1.6'], ['1.6.4'], 'Explain', '', ['demerit good', 'information failure'], DN),
    ('June', 2023, '23', '1(e)'): t(['2.4', '2.1', '3.2'], ['2.4.2', '2.1.5', '3.2.6'], 'Assess', '', ['demand shift', 'advertising ban', 'PED', 'regulation'], DN),
    ('June', 2023, '23', '1(f)'): t(['3.2', '3.1'], ['3.2.6', '3.1.2'], 'Assess', '', ['regulation', 'demerit good', 'information failure', 'healthcare costs'], DN),
    ('June', 2023, '23', '2(a)'): t(['2.2'], ['2.2.1', '2.2.3'], 'Explain', 'Consider', ['YED', 'normal goods', 'inferior goods', 'luxury goods']),
    ('June', 2023, '23', '2(b)'): t(['2.5', '2.2'], ['2.5.1', '2.5.3', '2.2.7'], 'Assess', '', ['consumer surplus', 'PED', 'price change']),
    ('June', 2023, '23', '3(a)'): t(['3.1', '1.6', '3.2'], ['3.1.2', '1.6.3', '3.2.2', '3.2.3'], 'Explain', 'Consider', ['merit good', 'under-consumption', 'information failure', 'government failure']),
    ('June', 2023, '23', '3(b)'): t(['3.2'], ['3.2.5'], 'Assess', '', ['buffer stock', 'agricultural markets', 'price stabilisation']),
    ('June', 2023, '23', '4(a)'): t(['4.2'], ['4.2.1', '4.2.2', '4.2.3'], 'Explain', 'Consider', ['circular flow', 'open economy', 'injections', 'leakages', 'equilibrium']),
    ('June', 2023, '23', '4(b)'): t(['4.2', '4.3'], ['4.2.2', '4.3.3'], 'Assess', '', ['investment', 'injections', 'multiplier effect', 'infrastructure']),
    ('June', 2023, '23', '5(a)'): t(['5.3', '4.6'], ['5.3.3', '5.3.4', '4.6.4'], 'Explain', 'Consider', ['interest rates', 'contractionary monetary policy', 'inflation control']),
    ('June', 2023, '23', '5(b)'): t(['5.1', '5.2', '5.3', '5.4'], ['5.1.1', '5.2.7', '5.3.4', '5.4.4'], 'Assess', '', ['macroeconomic objectives', 'fiscal policy', 'monetary policy', 'supply-side policy', 'policy conflicts']),

    # ---------- March 2023, 9708/22 — Inflation in the United States ----------
    ('March', 2023, '22', '1(a)'): t(['4.6'], ['4.6.2'], 'Compare', '', ['inflation trend', 'data comparison'], USI),
    ('March', 2023, '22', '1(b)'): t(['5.2'], ['5.2.6', '5.2.7'], 'Explain', '', ['expansionary fiscal policy', 'stimulus package'], USI),
    ('March', 2023, '22', '1(c)'): t(['5.3', '4.6'], ['5.3.4', '4.6.4'], 'Consider', '', ['interest rates', 'contractionary monetary policy', 'aggregate demand'], USI),
    ('March', 2023, '22', '1(d)'): t(['4.6', '4.3'], ['4.6.4', '4.3.12'], 'Assess', '', ['demand-pull inflation', 'cost-push inflation', 'AD/AS'], USI),
    ('March', 2023, '22', '1(e)'): t(['4.6'], ['4.6.5'], 'Assess', '', ['consequences of inflation', 'competitiveness', 'real incomes'], USI),
    ('March', 2023, '22', '2(a)'): t(['2.4', '1.4'], ['2.4.4', '1.4.2'], 'Explain', 'Consider', ['functions of price', 'rationing', 'signalling', 'incentivising', 'market economy']),
    ('March', 2023, '22', '2(b)'): t(['1.4', '3.1'], ['1.4.1', '1.4.2', '3.1.1'], 'Assess', '', ['market economy', 'mixed economy', 'market failure']),
    ('March', 2023, '22', '3(a)'): t(['3.3'], ['3.3.3'], 'Explain', 'Consider', ['causes of inequality', 'income inequality', 'incentives']),
    ('March', 2023, '22', '3(b)'): t(['3.2'], ['3.2.4'], 'Assess', '', ['minimum price', 'excess supply', 'demerit goods', 'producer incomes']),
    ('March', 2023, '22', '4(a)'): t(['4.2'], ['4.2.1', '4.2.2'], 'Explain', 'Consider', ['circular flow', 'closed vs open economy', 'injections and leakages']),
    ('March', 2023, '22', '4(b)'): t(['4.4'], ['4.4.5'], 'Assess', '', ['consequences of growth', 'environment', 'inequality', 'inflation']),
    ('March', 2023, '22', '5(a)'): t(['6.4'], ['6.4.2', '6.4.3', '6.4.5'], 'Explain', 'Consider', ['appreciation', 'floating exchange rate', 'export competitiveness', 'import prices']),
    ('March', 2023, '22', '5(b)'): t(['6.5', '5.4'], ['6.5.2', '5.4.3'], 'Assess', '', ['supply-side policy', 'current account deficit', 'competitiveness', 'time lags']),

    # ---------- November 2023, 9708/21 — Economic growth in Taiwan ----------
    ('November', 2023, '21', '1(a)'): t(['4.4', '4.6'], ['4.4.3', '4.6.3'], 'Calculate', '', ['real GDP', 'nominal vs real'], TW),
    ('November', 2023, '21', '1(b)'): t(['4.4', '4.3'], ['4.4.4', '4.3.5'], 'State', 'Consider', ['causes of growth', 'investment', 'consumption'], TW),
    ('November', 2023, '21', '1(c)'): t(['6.4'], ['6.4.2', '6.4.4'], 'Explain', '', ['appreciation', 'currency demand', 'export demand'], TW),
    ('November', 2023, '21', '1(d)'): t(['6.1', '6.4'], ['6.1.3', '6.4.5'], 'Assess', '', ['terms of trade', 'appreciation', 'export competitiveness', 'imported inputs'], TW),
    ('November', 2023, '21', '1(e)'): t(['4.4'], ['4.4.5'], 'Assess', '', ['consequences of growth', 'inflation', 'environment', 'living standards'], TW),
    ('November', 2023, '21', '2(a)'): t(['2.1', '2.4', '2.3'], ['2.1.3', '2.1.5', '2.4.2', '2.3.3'], 'Explain', 'Consider', ['determinants of demand', 'demand shift', 'PES', 'short run vs long run']),
    ('November', 2023, '21', '2(b)'): t(['2.2'], ['2.2.8'], 'Assess', '', ['PED', 'YED', 'business decisions', 'cars']),
    ('November', 2023, '21', '3(a)'): t(['3.2', '1.6'], ['3.2.3', '1.6.3'], 'Explain', 'Consider', ['direct provision', 'merit goods', 'government failure']),
    ('November', 2023, '21', '3(b)'): t(['3.2'], ['3.2.4'], 'Assess', '', ['maximum price', 'shortages', 'informal market']),
    ('November', 2023, '21', '4(a)'): t(['5.2', '3.3'], ['5.2.4', '3.3.4'], 'Explain', 'Consider', ['reasons for taxation', 'progressive tax', 'regressive tax', 'equity']),
    ('November', 2023, '21', '4(b)'): t(['5.2'], ['5.2.2', '5.2.3', '5.2.6'], 'Assess', '', ['balanced budget', 'budget deficit', 'budget surplus']),
    ('November', 2023, '21', '5(a)'): t(['6.2'], ['6.2.2'], 'Explain', 'Consider', ['tariffs', 'quotas', 'government revenue']),
    ('November', 2023, '21', '5(b)'): t(['6.1'], ['6.1.1', '6.1.2'], 'Assess', '', ['absolute advantage', 'comparative advantage', 'limitations of the theory', 'transport costs']),

    # ---------- November 2023, 9708/22 — Electric cars create challenges for oil producers ----------
    ('November', 2023, '22', '1(a)'): t(['2.1'], ['2.1.2'], 'Calculate', '', ['percentage change', 'data calculation', 'real price'], EO),
    ('November', 2023, '22', '1(b)'): t(['2.4', '2.1'], ['2.4.2', '2.1.5'], 'Explain', '', ['demand shift', 'fall in demand', 'price fall'], EO),
    ('November', 2023, '22', '1(c)'): t(['2.4', '2.1'], ['2.4.2', '2.1.6'], 'Explain', 'Consider', ['supply shortage', 'costs of production', 'price increase', 'supply-side policy'], EO),
    ('November', 2023, '22', '1(d)'): t(['4.5'], ['4.5.3', '4.5.4'], 'Explain', 'Consider', ['structural unemployment', 'cyclical unemployment', 'diversification'], EO),
    ('November', 2023, '22', '1(e)'): t(['4.4', '6.1', '1.3'], ['4.4.4', '6.1.4', '1.3.4'], 'Assess', '', ['diversification', 'primary product dependence', 'investment', 'capital'], EO),
    ('November', 2023, '22', '2(a)'): t(['2.2'], ['2.2.1', '2.2.2', '2.2.7'], 'Explain', 'Consider', ['PED', 'PED formula', 'total expenditure']),
    ('November', 2023, '22', '2(b)'): t(['2.3', '2.2'], ['2.3.5', '2.2.8'], 'Assess', '', ['PES', 'XED', 'business decisions', 'growing economy']),
    ('November', 2023, '22', '3(a)'): t(['1.6', '1.4'], ['1.6.1', '1.6.2', '1.4.2'], 'Explain', 'Consider', ['free goods', 'public goods', 'free-rider problem']),
    ('November', 2023, '22', '3(b)'): t(['3.1', '1.6', '1.4'], ['3.1.2', '1.6.3', '1.6.4', '1.4.1'], 'Assess', '', ['imperfect information', 'merit goods', 'demerit goods', 'market economy', 'mixed economy']),
    ('November', 2023, '22', '4(a)'): t(['6.1', '6.3'], ['6.1.3', '6.3.1'], 'Explain', 'Consider', ['terms of trade', 'balance of trade']),
    ('November', 2023, '22', '4(b)'): t(['6.1', '6.3'], ['6.1.3', '6.3.4'], 'Assess', '', ['terms of trade', 'macroeconomic performance', 'PED for exports and imports']),
    ('November', 2023, '22', '5(a)'): t(['4.3', '4.6'], ['4.3.5', '4.3.9', '4.3.12', '4.6.4'], 'Explain', 'Consider', ['AD shift', 'AS shift', 'demand-pull inflation', 'spare capacity']),
    ('November', 2023, '22', '5(b)'): t(['4.6', '6.3'], ['4.6.5'], 'Assess', '', ['consequences of inflation', 'international competitiveness', 'current account']),

    # ---------- November 2023, 9708/23 — Varied responses to the COVID-19 pandemic ----------
    ('November', 2023, '23', '1(a)'): t(['4.4'], ['4.4.2'], 'Explain', '', ['negative economic growth', 'recession'], CV),
    ('November', 2023, '23', '1(b)'): t(['4.4'], ['4.4.2'], 'Identify', 'Justify', ['recession', 'data interpretation'], CV),
    ('November', 2023, '23', '1(c)'): t(['4.4', '4.3'], ['4.4.4', '4.3.5'], 'State', 'Consider', ['causes of growth', 'export demand', 'government policy'], CV),
    ('November', 2023, '23', '1(d)'): t(['4.5', '4.6', '4.4'], ['4.5.4', '4.6.4', '4.4.5'], 'Assess', '', ['economic recovery', 'employment', 'demand-pull inflation'], CV),
    ('November', 2023, '23', '1(e)'): t(['5.3', '5.2', '4.4'], ['5.3.3', '5.3.4', '5.2.7'], 'Assess', '', ['expansionary monetary policy', 'fiscal policy', 'economic recovery'], CV),
    ('November', 2023, '23', '2(a)'): t(['2.3'], ['2.3.1', '2.3.3', '2.3.4'], 'Explain', 'Consider', ['PES', 'short run vs long run', 'smartphones']),
    ('November', 2023, '23', '2(b)'): t(['2.2'], ['2.2.6', '2.2.8'], 'Assess', '', ['PED', 'XED', 'business decisions', 'smartphones']),
    ('November', 2023, '23', '3(a)'): t(['1.6', '1.4'], ['1.6.1', '1.6.2', '1.4.2'], 'Explain', 'Consider', ['private good', 'public good', 'excludability', 'mass transit']),
    ('November', 2023, '23', '3(b)'): t(['3.2', '3.1'], ['3.2.2', '3.1.2'], 'Assess', '', ['subsidy', 'merit goods', 'opportunity cost', 'mass transit']),
    ('November', 2023, '23', '4(a)'): t(['4.5'], ['4.5.3'], 'Explain', 'Consider', ['causes of unemployment', 'structural unemployment', 'cyclical unemployment', 'own economy']),
    ('November', 2023, '23', '4(b)'): t(['5.4', '4.5', '5.2'], ['5.4.4', '4.5.3', '5.2.7'], 'Assess', '', ['supply-side policy', 'long-term unemployment', 'demand-side policy']),
    ('November', 2023, '23', '5(a)'): t(['6.5', '6.2'], ['6.5.2', '6.2.2'], 'Explain', 'Consider', ['tariffs', 'current account deficit', 'expenditure switching', 'retaliation']),
    ('November', 2023, '23', '5(b)'): t(['6.3'], ['6.3.4'], 'Assess', '', ['current account deficit', 'exchange rate', 'external debt']),
}
