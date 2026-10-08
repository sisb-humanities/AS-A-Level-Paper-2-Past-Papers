"""Batch 2 tags. Key: (series, year, variant, qid). AO3 marks come from a rule (verified against every MS):
2-mark 0, 4-mark 1, 6-mark 2, 8-mark 2, 12-mark 4."""


def t(topics, sub, cmd, cmd2, concepts, context=''):
    return dict(topics=topics, sub=sub, cmd=cmd, cmd2=cmd2, concepts=concepts, context=context)


PH = 'Philippines – onion prices'
MY = 'Malaysia – economic challenges'
EV = 'China/EU – exports of electric vehicles'
AR = 'Argentina – economic reform'
MYP = 'Malaysia – ageing population'
US = 'USA – growth and inflation'

T2 = {
    # ---------- June 2025, 9708/23 — How onions became a luxury good in the Philippines ----------
    ('June', 2025, '23', '1(a)'): t(['2.4', '2.1'], ['2.4.2', '2.1.6'], 'Demonstrate', '', ['supply shift', 'equilibrium price', 'natural disaster'], PH),
    ('June', 2025, '23', '1(b)'): t(['2.3'], ['2.3.3', '2.3.4'], 'Justify', '', ['PES', 'short run', 'agricultural supply'], PH),
    ('June', 2025, '23', '1(c)'): t(['1.5', '1.1'], ['1.5.1', '1.5.2', '1.1.3'], 'Consider', '', ['PPC', 'opportunity cost', 'increasing opportunity cost'], PH),
    ('June', 2025, '23', '1(d)'): t(['3.2', '3.1'], ['3.2.4', '3.2.5', '3.1.3'], 'Assess', '', ['maximum price', 'price stabilisation', 'buffer stocks', 'imports'], PH),
    ('June', 2025, '23', '1(e)'): t(['2.2', '3.3', '4.6'], ['2.2.6', '3.3.3', '4.6.5'], 'Assess', '', ['PED', 'proportion of income', 'low-income households', 'necessities'], PH),
    ('June', 2025, '23', '2(a)'): t(['2.3', '2.4'], ['2.3.1', '2.3.3', '2.3.5', '2.4.3'], 'Explain', 'Consider', ['PES', 'short run vs long run', 'derived demand', 'semi-conductors']),
    ('June', 2025, '23', '2(b)'): t(['2.4', '2.3', '1.4'], ['2.4.2', '2.4.4', '2.3.5', '1.4.2'], 'Assess', '', ['resource allocation', 'price mechanism', 'signalling', 'incentive', 'PES']),
    ('June', 2025, '23', '3(a)'): t(['1.6', '3.2', '3.1'], ['1.6.3', '3.2.3', '3.1.2'], 'Explain', 'Consider', ['merit good', 'imperfect information', 'direct provision', 'healthcare']),
    ('June', 2025, '23', '3(b)'): t(['3.2', '1.6', '3.3'], ['3.2.3', '1.6.3', '3.3.4'], 'Assess', '', ['user charges', 'free provision', 'rationing', 'equity', 'healthcare']),
    ('June', 2025, '23', '4(a)'): t(['4.4'], ['4.4.2', '4.4.4'], 'Explain', 'Consider', ['causes of economic growth', 'measuring growth']),
    ('June', 2025, '23', '4(b)'): t(['4.4', '5.2'], ['4.4.5', '5.2.4'], 'Assess', '', ['consequences of growth', 'tax revenue', 'inequality', 'environment', 'inflation']),
    ('June', 2025, '23', '5(a)'): t(['6.1', '6.3'], ['6.1.3', '6.3.3'], 'Explain', 'Consider', ['terms of trade', 'export prices', 'PED', 'current account']),
    ('June', 2025, '23', '5(b)'): t(['6.1', '5.4'], ['6.1.1', '6.1.4', '5.4.3'], 'Assess', '', ['comparative advantage', 'supply-side policy', 'education', 'infrastructure']),

    # ---------- June 2025, 9708/24 — Economic challenges in Malaysia ----------
    ('June', 2025, '24', '1(a)'): t(['4.4'], ['4.4.2'], 'Describe', '', ['economic growth rate', 'data trend'], MY),
    ('June', 2025, '24', '1(b)'): t(['4.4', '4.6'], ['4.4.3', '4.6.3'], 'Explain', '', ['real GDP', 'nominal vs real'], MY),
    ('June', 2025, '24', '1(c)'): t(['3.2'], ['3.2.2'], 'Consider', '', ['subsidy', 'government spending', 'opportunity cost'], MY),
    ('June', 2025, '24', '1(d)'): t(['4.4', '4.3'], ['4.4.4', '4.3.5'], 'Assess', '', ['causes of growth', 'external demand', 'net exports'], MY),
    ('June', 2025, '24', '1(e)'): t(['4.5', '4.6'], ['4.5.4', '4.6.4'], 'Assess', '', ['falling unemployment', 'demand-pull inflation', 'tax revenue'], MY),
    ('June', 2025, '24', '2(a)'): t(['2.2'], ['2.2.1', '2.2.2', '2.2.7', '2.2.8'], 'Explain', 'Consider', ['PED', 'PED formula', 'total revenue']),
    ('June', 2025, '24', '2(b)'): t(['3.1', '1.6', '3.2'], ['3.1.2', '1.6.3', '3.2.2', '3.2.3', '3.2.6'], 'Assess', '', ['merit good', 'subsidy', 'direct provision', 'education', 'health care']),
    ('June', 2025, '24', '3(a)'): t(['3.2', '2.5'], ['3.2.4', '2.5.1', '2.5.3'], 'Explain', 'Consider', ['minimum price', 'consumer surplus', 'excess supply']),
    ('June', 2025, '24', '3(b)'): t(['3.3'], ['3.3.4'], 'Assess', '', ['minimum wage', 'redistribution', 'transfer payments', 'progressive tax']),
    ('June', 2025, '24', '4(a)'): t(['5.4', '4.3'], ['5.4.1', '5.4.3', '5.4.4', '4.3.9'], 'Explain', 'Consider', ['supply-side policy', 'education and training', 'LRAS', 'price level', 'time lags']),
    ('June', 2025, '24', '4(b)'): t(['4.6'], ['4.6.5'], 'Assess', '', ['consequences of inflation', 'mild inflation', 'menu costs', 'competitiveness']),
    ('June', 2025, '24', '5(a)'): t(['6.1', '6.3'], ['6.1.3'], 'Explain', 'Consider', ['terms of trade formula', 'export prices', 'import prices']),
    ('June', 2025, '24', '5(b)'): t(['6.4', '6.3'], ['6.4.3', '6.4.5', '6.3.4'], 'Assess', '', ['depreciation', 'export competitiveness', 'imported inflation', 'current account']),

    # ---------- June 2026, 9708/23 — Exports of Chinese EVs ----------
    ('June', 2026, '23', '1(a)'): t(['2.1'], ['2.1.2'], 'Identify', '', ['data interpretation', 'market sales'], EV),
    ('June', 2026, '23', '1(b)'): t(['2.1', '6.2'], ['2.1.3', '6.2.2'], 'Give', '', ['determinants of demand', 'tariffs'], EV),
    ('June', 2026, '23', '1(c)'): t(['6.2', '3.2', '2.4'], ['6.2.2', '3.2.2', '2.4.2'], 'Explain', 'Consider', ['export subsidy', 'supply shift', 'PED', 'PES'], EV),
    ('June', 2026, '23', '1(d)'): t(['2.2'], ['2.2.1', '2.2.8'], 'Assess', '', ['XED', 'substitutes', 'business decisions'], EV),
    ('June', 2026, '23', '1(e)'): t(['6.3', '4.5', '4.3', '6.1'], ['6.3.3', '4.5.3', '4.3.5'], 'Assess', '', ['imports', 'current account', 'structural unemployment', 'consumer benefits'], EV),
    ('June', 2026, '23', '2(a)'): t(['2.1'], ['2.1.3', '2.1.5'], 'Explain', 'Consider', ['determinants of demand', 'tastes', 'income', 'substitutes']),
    ('June', 2026, '23', '2(b)'): t(['2.4', '2.2', '2.5'], ['2.4.2', '2.2.7', '2.5.2'], 'Assess', '', ['supply restriction', 'PED', 'total revenue', 'producer surplus']),
    ('June', 2026, '23', '3(a)'): t(['1.6'], ['1.6.1', '1.6.2'], 'Explain', 'Consider', ['public good', 'private good', 'non-rejectability', 'non-excludable']),
    ('June', 2026, '23', '3(b)'): t(['3.3', '3.2', '1.6'], ['3.3.4', '3.2.3', '1.6.2', '1.6.3'], 'Assess', '', ['income distribution', 'merit goods', 'public goods', 'state provision']),
    ('June', 2026, '23', '4(a)'): t(['4.3', '4.6'], ['4.3.12', '4.3.8', '4.6.4'], 'Explain', 'Consider', ['AD increase', 'real output', 'price level', 'demand-pull inflation']),
    ('June', 2026, '23', '4(b)'): t(['5.4', '4.5', '4.3'], ['5.4.4', '4.5.3', '4.3.9'], 'Assess', '', ['LRAS', 'supply-side policy', 'unemployment', 'demand-side alternatives']),
    ('June', 2026, '23', '5(a)'): t(['6.4', '6.1'], ['6.4.3', '6.1.3', '6.4.5'], 'Explain', 'Consider', ['depreciation', 'terms of trade', 'export prices', 'import prices']),
    ('June', 2026, '23', '5(b)'): t(['6.3'], ['6.3.4'], 'Assess', '', ['current account deficit', 'consumers', 'firms', 'imports']),

    # ---------- June 2026, 9708/24 — Economic problems in Argentina ----------
    ('June', 2026, '24', '1(a)'): t(['6.4'], ['6.4.3'], 'Describe', 'State', ['depreciation', 'exporters'], AR),
    ('June', 2026, '24', '1(b)'): t(['6.2', '2.2'], ['6.2.2', '2.2.7'], 'Explain', '', ['tariffs', 'value of imports', 'PED'], AR),
    ('June', 2026, '24', '1(c)'): t(['3.2', '4.6'], ['3.2.2', '4.6.4'], 'Explain', 'Consider', ['removal of subsidy', 'supply shift', 'cost-push inflation'], AR),
    ('June', 2026, '24', '1(d)'): t(['3.2', '2.4'], ['3.2.4', '2.4.4'], 'Assess', '', ['maximum price', 'shortages', 'price mechanism'], AR),
    ('June', 2026, '24', '1(e)'): t(['5.4', '3.3'], ['5.4.4', '3.3.3'], 'Assess', '', ['supply-side policy', 'winners and losers', 'inequality'], AR),
    ('June', 2026, '24', '2(a)'): t(['2.2'], ['2.2.6', '2.2.8'], 'Explain', 'Consider', ['XED', 'substitutes', 'complements', 'business decisions']),
    ('June', 2026, '24', '2(b)'): t(['2.2', '4.4'], ['2.2.3', '2.2.6', '2.2.8'], 'Assess', '', ['PED', 'YED', 'recession', 'normal and inferior goods']),
    ('June', 2026, '24', '3(a)'): t(['2.4', '1.6'], ['2.4.4', '1.6.4'], 'Explain', 'Consider', ['functions of price', 'rationing', 'signalling', 'incentivising', 'over-consumption']),
    ('June', 2026, '24', '3(b)'): t(['1.4', '3.1'], ['1.4.1', '1.4.2', '3.1.1'], 'Assess', '', ['mixed economy', 'state sector', 'private sector', 'public goods']),
    ('June', 2026, '24', '4(a)'): t(['4.2'], ['4.2.1', '4.2.2'], 'Explain', 'Consider', ['circular flow', 'closed vs open economy', 'government sector', 'injections and leakages']),
    ('June', 2026, '24', '4(b)'): t(['4.3', '5.2', '4.6'], ['4.3.8', '5.2.7', '4.6.4'], 'Assess', '', ['LRAS shape', 'fiscal policy', 'price stability', 'spare capacity']),
    ('June', 2026, '24', '5(a)'): t(['6.1', '1.3'], ['6.1.2', '6.1.4', '1.3.4'], 'Explain', 'Consider', ['specialisation', 'free trade', 'consumer choice', 'lower prices']),
    ('June', 2026, '24', '5(b)'): t(['6.3'], ['6.3.4'], 'Assess', '', ['current account surplus', 'exchange rate', 'inflation', 'living standards']),

    # ---------- November 2025, 9708/23 — Malaysia's uncertain economic prospects ----------
    ('November', 2025, '23', '1(a)'): t(['1.3'], ['1.3.1'], 'Compare', '', ['data interpretation', 'ageing population', 'labour force'], MYP),
    ('November', 2025, '23', '1(b)'): t(['1.1'], ['1.1.4'], 'Explain', '', ['what to produce', 'ageing population'], MYP),
    ('November', 2025, '23', '1(c)'): t(['1.5', '1.3'], ['1.5.3', '1.3.1'], 'Consider', '', ['PPC shift', 'productive capacity', 'labour force', 'productivity'], MYP),
    ('November', 2025, '23', '1(d)'): t(['3.2', '5.4', '5.2'], ['3.2.3', '5.4.3', '5.2.5'], 'Assess', '', ['direct provision', 'free childcare', 'labour force participation', 'opportunity cost'], MYP),
    ('November', 2025, '23', '1(e)'): t(['4.3'], ['4.3.2', '4.3.3', '4.3.5'], 'Assess', '', ['aggregate demand', 'consumption', 'investment', 'government spending', 'population'], MYP),
    ('November', 2025, '23', '2(a)'): t(['2.4', '2.1'], ['2.4.2', '2.1.5', '2.1.6'], 'Explain', 'Consider', ['market equilibrium', 'supply fall', 'demand increase', 'indeterminate outcome']),
    ('November', 2025, '23', '2(b)'): t(['3.2', '2.2', '2.3'], ['3.2.5', '2.2.7', '2.3.4'], 'Assess', '', ['buffer stock', 'income stabilisation', 'storage', 'diversification']),
    ('November', 2025, '23', '3(a)'): t(['3.3'], ['3.3.2'], 'Explain', 'Consider', ['Gini coefficient', 'income inequality', 'data usefulness']),
    ('November', 2025, '23', '3(b)'): t(['3.3'], ['3.3.1', '3.3.4'], 'Assess', '', ['income vs wealth', 'flow vs stock', 'inheritance tax', 'capital taxes']),
    ('November', 2025, '23', '4(a)'): t(['4.6'], ['4.6.4'], 'Explain', 'Consider', ['causes of inflation', 'cost-push', 'demand-pull', 'own economy']),
    ('November', 2025, '23', '4(b)'): t(['5.4', '5.3', '5.2', '4.6'], ['5.4.4', '5.3.4', '5.2.7'], 'Assess', '', ['supply-side policy', 'demand-side policy', 'inflation', 'time lags']),
    ('November', 2025, '23', '5(a)'): t(['6.3'], ['6.3.3', '6.3.4'], 'Explain', 'Consider', ['current account deficit', 'causes', 'government concern']),
    ('November', 2025, '23', '5(b)'): t(['6.5', '6.2'], ['6.5.2', '6.2.2'], 'Assess', '', ['protectionism', 'contractionary policy', 'current account deficit', 'retaliation']),

    # ---------- November 2025, 9708/24 — US growth and inflation ----------
    ('November', 2025, '24', '1(a)'): t(['4.4'], ['4.4.2'], 'Compare', '', ['economic growth forecasts', 'data comparison'], US),
    ('November', 2025, '24', '1(b)'): t(['4.4', '4.6'], ['4.4.3', '4.6.3'], 'Explain', '', ['real GDP', 'nominal GDP'], US),
    ('November', 2025, '24', '1(c)'): t(['2.4', '2.1'], ['2.1.6', '2.4.2'], 'Explain', 'Consider', ['productivity', 'supply shift', 'costs of production'], US),
    ('November', 2025, '24', '1(d)'): t(['4.6'], ['4.6.5'], 'Assess', '', ['costs of inflation', 'benefits of inflation'], US),
    ('November', 2025, '24', '1(e)'): t(['5.3', '4.6'], ['5.3.4', '4.6.4'], 'Assess', '', ['high interest rates', 'contractionary monetary policy', 'inflation control', 'alternative policies'], US),
    ('November', 2025, '24', '2(a)'): t(['3.2', '2.2', '2.3'], ['3.2.1'], 'Explain', 'Consider', ['tax incidence', 'indirect tax', 'PED', 'PES']),
    ('November', 2025, '24', '2(b)'): t(['3.2', '1.6', '3.1'], ['3.2.2', '1.6.3', '3.1.2'], 'Assess', '', ['subsidy', 'merit good', 'consumption', 'opportunity cost']),
    ('November', 2025, '24', '3(a)'): t(['2.3'], ['2.3.4'], 'Explain', 'Consider', ['PES determinants', 'agricultural goods', 'manufactured goods', 'time']),
    ('November', 2025, '24', '3(b)'): t(['2.2'], ['2.2.6', '2.2.8'], 'Assess', '', ['YED', 'XED', 'business decisions', 'sales revenue']),
    ('November', 2025, '24', '4(a)'): t(['6.2'], ['6.2.1', '6.2.2', '6.2.3'], 'Explain', 'Consider', ['protectionism', 'tariffs', 'quotas']),
    ('November', 2025, '24', '4(b)'): t(['6.1', '6.2'], ['6.1.1', '6.1.4', '6.2.3'], 'Assess', '', ['comparative advantage', 'trade decisions', 'strategic industries']),
    ('November', 2025, '24', '5(a)'): t(['4.5'], ['4.5.3', '4.5.4'], 'Explain', 'Consider', ['structural unemployment', 'cyclical unemployment', 'consequences']),
    ('November', 2025, '24', '5(b)'): t(['5.4', '4.5', '5.1'], ['5.4.4', '4.5.3', '5.1.1'], 'Assess', '', ['supply-side policy', 'low unemployment', 'demand-side alternatives']),
}

FLAGS2 = {}  # redaction flags are generated from the stimulus text in build.py

MX = 'Mexico – state-led energy policy'
CI = 'Ivory Coast – cocoa prices and farmer incomes'

T2.update({
    # ---------- November 2025, 9708/21 — Mexico's energy policy ----------
    ('November', 2025, '21', '1(a)'): t(['1.4'], ['1.4.1'], 'Explain', '', ['mixed economy', 'private sector', 'public sector'], MX),
    ('November', 2025, '21', '1(b)'): t(['1.1'], ['1.1.3'], 'Explain', '', ['opportunity cost'], MX),
    ('November', 2025, '21', '1(c)'): t(['3.2', '1.4'], ['3.2.3', '1.4.2'], 'Consider', '', ['direct provision', 'state-owned enterprise', 'consumers'], MX),
    ('November', 2025, '21', '1(d)'): t(['3.2'], ['3.2.2'], 'Assess', '', ['subsidy', 'price control', 'government spending', 'over-consumption'], MX),
    ('November', 2025, '21', '1(e)'): t(['6.1', '6.3', '1.1'], ['6.1.2', '6.3.3', '1.1.3'], 'Assess', '', ['self-sufficiency', 'specialisation', 'balance of trade', 'opportunity cost'], MX),
    ('November', 2025, '21', '2(a)'): t(['2.2'], ['2.2.1', '2.2.2', '2.2.6'], 'Explain', 'Consider', ['PED', 'PED formula', 'time period']),
    ('November', 2025, '21', '2(b)'): t(['2.2'], ['2.2.6', '2.2.8'], 'Assess', '', ['YED', 'XED', 'business decisions']),
    ('November', 2025, '21', '3(a)'): t(['1.6'], ['1.6.1'], 'Explain', 'Consider', ['free goods', 'private goods', 'scarcity', 'opportunity cost']),
    ('November', 2025, '21', '3(b)'): t(['1.6'], ['1.6.2', '1.6.3'], 'Assess', '', ['public good', 'merit good', 'education', 'excludability']),
    ('November', 2025, '21', '4(a)'): t(['4.5'], ['4.5.3'], 'Explain', 'Consider', ['frictional unemployment', 'technological unemployment', 'natural unemployment']),
    ('November', 2025, '21', '4(b)'): t(['4.5'], ['4.5.3', '4.5.4'], 'Assess', '', ['technological unemployment', 'cyclical unemployment', 'consequences']),
    ('November', 2025, '21', '5(a)'): t(['6.2'], ['6.2.2'], 'Explain', 'Consider', ['tools of protection', 'tariffs', 'quotas']),
    ('November', 2025, '21', '5(b)'): t(['6.2'], ['6.2.3'], 'Assess', '', ['protectionism', 'consumers', 'producers', 'government revenue']),

    # ---------- November 2025, 9708/22 — Cocoa farmers and a living wage ----------
    ('November', 2025, '22', '1(a)(i)'): t(['2.2'], ['2.2.6'], 'Identify', '', ['PED', 'determinants of PED'], CI),
    ('November', 2025, '22', '1(a)(ii)'): t(['2.1'], ['2.1.2'], 'Calculate', '', ['percentage change', 'data calculation'], CI),
    ('November', 2025, '22', '1(b)'): t(['2.4', '2.1'], ['2.4.2', '2.1.6'], 'Demonstrate', '', ['supply shift', 'falling price', 'commodity market'], CI),
    ('November', 2025, '22', '1(c)'): t(['3.2'], ['3.2.5'], 'Consider', '', ['buffer stock', 'price fluctuations', 'commodity prices'], CI),
    ('November', 2025, '22', '1(d)'): t(['3.2', '3.3'], ['3.2.4', '3.3.4'], 'Assess', '', ['minimum price', 'excess supply', 'farm incomes', 'living wage'], CI),
    ('November', 2025, '22', '1(e)'): t(['6.1', '1.3'], ['6.1.2', '6.1.4', '1.3.4'], 'Assess', '', ['specialisation', 'primary product dependence', 'diversification', 'export revenue'], CI),
    ('November', 2025, '22', '2(a)'): t(['2.5'], ['2.5.1', '2.5.2', '2.5.3', '2.5.4'], 'Explain', 'Consider', ['producer surplus', 'consumer surplus', 'cost increase', 'PED']),
    ('November', 2025, '22', '2(b)'): t(['2.2'], ['2.2.6', '2.2.8'], 'Assess', '', ['YED', 'XED', 'falling incomes', 'business decisions']),
    ('November', 2025, '22', '3(a)'): t(['1.5', '1.1'], ['1.5.2', '1.5.3', '1.5.4', '1.1.3'], 'Explain', 'Consider', ['PPC', 'movement vs shift', 'constant vs increasing opportunity cost']),
    ('November', 2025, '22', '3(b)'): t(['1.5', '1.3', '4.4'], ['1.5.3', '1.3.1', '1.3.2', '4.4.4'], 'Assess', '', ['PPC shift', 'labour', 'technology', 'quality of resources']),
    ('November', 2025, '22', '4(a)'): t(['6.3', '6.4'], ['6.3.1', '6.4.5'], 'Explain', 'Consider', ['current account components', 'depreciation', 'current account surplus']),
    ('November', 2025, '22', '4(b)'): t(['6.5', '5.4'], ['6.5.2', '5.4.3'], 'Assess', '', ['supply-side policy', 'current account deficit', 'competitiveness', 'time lags']),
    ('November', 2025, '22', '5(a)'): t(['4.3', '4.6'], ['4.3.5', '4.3.12', '4.6.4'], 'Explain', 'Consider', ['components of AD', 'AD/AS', 'demand-pull inflation', 'spare capacity']),
    ('November', 2025, '22', '5(b)'): t(['4.6'], ['4.6.5'], 'Assess', '', ['consequences of inflation', 'consumers', 'firms']),
})

ZA = 'South Africa – unemployment, the rand and AfCFTA'
AI = 'Japan/US – artificial intelligence'
ARG = 'Argentina – high inflation'
CL = 'Chile – growth, copper and inequality'
CF = 'Global coffee bean prices'

T2.update({
    # ---------- June 2025, 9708/22 — South Africa ----------
    ('June', 2025, '22', '1(a)(i)'): t(['4.5'], ['4.5.2'], 'Identify', '', ['unemployment rate', 'data interpretation'], ZA),
    ('June', 2025, '22', '1(a)(ii)'): t(['4.5'], ['4.5.2'], 'Compare', '', ['unemployment trend', 'data comparison'], ZA),
    ('June', 2025, '22', '1(b)'): t(['4.5'], ['4.5.4'], 'Identify', '', ['consequences of unemployment', 'firms', 'government'], ZA),
    ('June', 2025, '22', '1(c)'): t(['6.4', '6.3'], ['6.4.3', '6.4.5', '6.3.4'], 'Consider', '', ['depreciation', 'current account deficit', 'PED for exports and imports'], ZA),
    ('June', 2025, '22', '1(d)'): t(['6.1', '4.4'], ['6.1.2', '4.4.4'], 'Assess', '', ['free trade area', 'trade liberalisation', 'economic growth'], ZA),
    ('June', 2025, '22', '1(e)'): t(['3.3', '5.4', '4.5'], ['3.3.3', '5.4.3', '4.5.4'], 'Assess', '', ['income inequality', 'infrastructure', 'unemployment policy'], ZA),
    ('June', 2025, '22', '2(a)'): t(['1.6', '1.4'], ['1.6.1', '1.6.2', '1.4.2'], 'Explain', 'Consider', ['public goods', 'free goods', 'market economy', 'free-rider problem']),
    ('June', 2025, '22', '2(b)'): t(['3.1', '3.2', '1.6'], ['3.1.2', '3.2.1', '3.2.2', '3.2.6', '1.6.3', '1.6.4'], 'Assess', '', ['merit goods', 'demerit goods', 'taxes', 'subsidies', 'information']),
    ('June', 2025, '22', '3(a)'): t(['2.1', '3.2'], ['2.1.4', '2.1.6', '3.2.2'], 'Explain', 'Consider', ['determinants of supply', 'costs of production', 'subsidy', 'supply shift']),
    ('June', 2025, '22', '3(b)'): t(['2.3', '2.2'], ['2.3.5', '2.2.8'], 'Assess', '', ['PES', 'PED', 'YED', 'business decisions']),
    ('June', 2025, '22', '4(a)'): t(['4.6', '4.3'], ['4.6.1', '4.3.12'], 'Explain', 'Consider', ['deflation', 'AD/AS', 'demand-side cause', 'supply-side cause']),
    ('June', 2025, '22', '4(b)'): t(['5.2', '4.6', '5.3'], ['5.2.6', '5.2.7', '5.3.4'], 'Assess', '', ['contractionary fiscal policy', 'inflation', 'monetary alternative']),
    ('June', 2025, '22', '5(a)'): t(['6.4', '6.3'], ['6.4.4', '6.4.2'], 'Explain', 'Consider', ['floating exchange rate', 'balance of trade', 'interest rates', 'currency demand']),
    ('June', 2025, '22', '5(b)'): t(['6.1', '6.3'], ['6.1.3', '6.3.4'], 'Assess', '', ['terms of trade', 'current account surplus']),

    # ---------- March 2024, 9708/22 — Artificial Intelligence ----------
    ('March', 2024, '22', '1(a)'): t(['4.4'], ['4.4.2'], 'Compare', '', ['real GDP growth', 'data comparison'], AI),
    ('March', 2024, '22', '1(b)'): t(['1.5'], ['1.5.3'], 'Demonstrate', '', ['PPC shift', 'investment', 'technology'], AI),
    ('March', 2024, '22', '1(c)'): t(['2.4', '2.1'], ['2.1.6', '2.4.2'], 'Consider', '', ['supply shift', 'technology', 'costs of production'], AI),
    ('March', 2024, '22', '1(d)'): t(['4.5'], ['4.5.3', '4.5.4'], 'Assess', '', ['technological unemployment', 'structural unemployment', 'job creation'], AI),
    ('March', 2024, '22', '1(e)'): t(['6.1'], ['6.1.1', '6.1.2'], 'Assess', '', ['comparative advantage', 'specialisation', 'technology'], AI),
    ('March', 2024, '22', '2(a)'): t(['3.2', '2.4', '2.2'], ['3.2.1', '2.4.2'], 'Explain', 'Consider', ['indirect tax', 'tax incidence', 'PED']),
    ('March', 2024, '22', '2(b)'): t(['3.2', '1.6', '3.1'], ['3.2.6', '1.6.4', '3.1.2', '3.2.1'], 'Assess', '', ['provision of information', 'demerit good', 'indirect tax', 'regulation']),
    ('March', 2024, '22', '3(a)'): t(['2.2'], ['2.2.1', '2.2.2', '2.2.3'], 'Explain', 'Consider', ['YED', 'YED formula', 'normal goods', 'inferior goods']),
    ('March', 2024, '22', '3(b)'): t(['2.2', '2.3'], ['2.2.8', '2.3.5'], 'Assess', '', ['PED', 'PES', 'business decisions']),
    ('March', 2024, '22', '4(a)'): t(['6.4'], ['6.4.3', '6.4.5'], 'Explain', 'Consider', ['depreciation', 'AD', 'real output', 'net exports']),
    ('March', 2024, '22', '4(b)'): t(['6.5', '5.2'], ['6.5.2', '5.2.6'], 'Assess', '', ['contractionary fiscal policy', 'current account deficit', 'expenditure reduction']),
    ('March', 2024, '22', '5(a)'): t(['5.3', '4.4', '4.6'], ['5.3.4', '4.4.4', '4.6.4'], 'Explain', 'Consider', ['interest rates', 'AD/AS', 'economic growth', 'demand-pull inflation']),
    ('March', 2024, '22', '5(b)'): t(['4.4'], ['4.4.5'], 'Assess', '', ['consequences of growth', 'environment', 'inequality', 'inflation']),

    # ---------- November 2024, 9708/21 — Inflation in Argentina ----------
    ('November', 2024, '21', '1(a)'): t(['4.6'], ['4.6.2'], 'Describe', '', ['inflation trend', 'disinflation', 'data trend'], ARG),
    ('November', 2024, '21', '1(b)'): t(['4.6', '5.3'], ['4.6.3', '5.3.2'], 'Explain', '', ['real interest rate', 'nominal vs real'], ARG),
    ('November', 2024, '21', '1(c)'): t(['4.6'], ['4.6.5'], 'Consider', '', ['consequences of inflation', 'competitiveness', 'menu costs'], ARG),
    ('November', 2024, '21', '1(d)'): t(['3.2'], ['3.2.4'], 'Assess', '', ['maximum price', 'shortages', 'informal market'], ARG),
    ('November', 2024, '21', '1(e)'): t(['5.3', '4.6'], ['5.3.3', '5.3.4', '4.6.4'], 'Assess', '', ['contractionary monetary policy', 'interest rates', 'inflation control'], ARG),
    ('November', 2024, '21', '2(a)'): t(['2.1'], ['2.1.4'], 'Explain', 'Consider', ['determinants of supply', 'agricultural products', 'weather']),
    ('November', 2024, '21', '2(b)'): t(['2.3'], ['2.3.4'], 'Assess', '', ['PES', 'agricultural products', 'manufactured products', 'spare capacity']),
    ('November', 2024, '21', '3(a)'): t(['1.5'], ['1.5.4'], 'Explain', 'Consider', ['PPC', 'unemployed resources', 'inefficiency']),
    ('November', 2024, '21', '3(b)'): t(['1.4', '3.1', '3.2'], ['1.4.1', '1.4.2', '3.1.1'], 'Assess', '', ['mixed economy', 'market mechanism', 'government intervention', 'consumers']),
    ('November', 2024, '21', '4(a)'): t(['4.4'], ['4.4.4', '4.4.5'], 'Explain', 'Consider', ['causes of growth', 'consequences of growth']),
    ('November', 2024, '21', '4(b)'): t(['5.2'], ['5.2.6', '5.2.7'], 'Assess', '', ['expansionary fiscal policy', 'contractionary fiscal policy', 'inflation', 'national debt']),
    ('November', 2024, '21', '5(a)'): t(['6.1', '6.2'], ['6.1.2', '6.2.3'], 'Explain', 'Consider', ['free trade', 'specialisation', 'disadvantages of free trade']),
    ('November', 2024, '21', '5(b)'): t(['6.3'], ['6.3.4'], 'Assess', '', ['current account surplus', 'exchange rate', 'inflation']),

    # ---------- November 2024, 9708/22 — Chile ----------
    ('November', 2024, '22', '1(a)'): t(['6.3'], ['6.3.1'], 'Identify', '', ['current account components', 'primary income', 'trade in services'], CL),
    ('November', 2024, '22', '1(b)'): t(['6.5', '6.2'], ['6.5.2', '6.2.2'], 'Consider', '', ['import reduction', 'tariffs', 'current account policy'], CL),
    ('November', 2024, '22', '1(c)'): t(['3.3'], ['3.3.2'], 'Explain', '', ['Gini coefficient', 'income inequality'], CL),
    ('November', 2024, '22', '1(d)'): t(['3.3', '5.2'], ['3.3.4', '5.2.5'], 'Assess', '', ['education spending', 'human capital', 'poorer households'], CL),
    ('November', 2024, '22', '1(e)'): t(['4.4', '6.1'], ['4.4.4', '6.1.3'], 'Assess', '', ['commodity prices', 'export revenue', 'terms of trade', 'economic growth'], CL),
    ('November', 2024, '22', '2(a)'): t(['2.1', '2.4'], ['2.1.5', '2.1.7', '2.4.3'], 'Explain', 'Consider', ['movement vs shift', 'substitutes', 'complements']),
    ('November', 2024, '22', '2(b)'): t(['2.2', '4.4'], ['2.2.7', '2.2.8'], 'Assess', '', ['YED', 'PED', 'total expenditure', 'economic growth']),
    ('November', 2024, '22', '3(a)'): t(['1.5', '1.1', '4.4'], ['1.5.2', '1.1.3', '4.4.4'], 'Explain', 'Consider', ['constant opportunity cost', 'increasing opportunity cost', 'capital goods', 'future growth']),
    ('November', 2024, '22', '3(b)'): t(['1.4', '1.1'], ['1.4.1', '1.4.2', '1.1.4'], 'Assess', '', ['market economy', 'basic economic questions', 'economic systems']),
    ('November', 2024, '22', '4(a)'): t(['4.5'], ['4.5.2'], 'Explain', 'Consider', ['measuring unemployment', 'claimant count', 'labour force survey']),
    ('November', 2024, '22', '4(b)'): t(['5.4', '4.5'], ['5.4.4', '4.5.3'], 'Assess', '', ['supply-side policy', 'structural unemployment', 'cyclical unemployment']),
    ('November', 2024, '22', '5(a)'): t(['5.2'], ['5.2.4'], 'Explain', 'Consider', ['marginal rate of tax', 'average rate of tax', 'indirect tax', 'tax revenue']),
    ('November', 2024, '22', '5(b)'): t(['5.2', '5.1'], ['5.2.2', '5.2.3', '5.1.1'], 'Assess', '', ['balanced budget', 'budget deficit', 'macroeconomic objectives']),

    # ---------- November 2024, 9708/23 — Coffee bean prices ----------
    ('November', 2024, '23', '1(a)'): t(['2.4', '2.1'], ['2.4.2', '2.1.6'], 'Demonstrate', '', ['supply shift', 'weather', 'price increase'], CF),
    ('November', 2024, '23', '1(b)'): t(['2.3'], ['2.3.3', '2.3.4'], 'Justify', '', ['PES', 'agricultural supply', 'time period'], CF),
    ('November', 2024, '23', '1(c)'): t(['3.2'], ['3.2.5'], 'Consider', '', ['buffer stock', 'price fluctuations'], CF),
    ('November', 2024, '23', '1(d)'): t(['2.2', '2.5', '2.4'], ['2.2.7', '2.5.3'], 'Assess', '', ['PED', 'total revenue', 'producer surplus', 'output loss'], CF),
    ('November', 2024, '23', '1(e)'): t(['4.4', '6.1', '6.3'], ['4.4.4', '6.1.3', '6.3.3'], 'Assess', '', ['commodity price fluctuations', 'export revenue', 'primary product dependence'], CF),
    ('November', 2024, '23', '2(a)'): t(['1.6'], ['1.6.1', '1.6.2', '1.6.3'], 'Explain', 'Consider', ['public goods', 'free goods', 'vaccinations', 'opportunity cost']),
    ('November', 2024, '23', '2(b)'): t(['3.2', '1.6', '3.3'], ['3.2.3', '1.6.3', '3.3.4'], 'Assess', '', ['free healthcare', 'merit goods', 'opportunity cost', 'equity']),
    ('November', 2024, '23', '3(a)'): t(['3.3'], ['3.3.1', '3.3.2', '3.3.3'], 'Explain', 'Consider', ['income inequality', 'wealth inequality', 'measurement']),
    ('November', 2024, '23', '3(b)'): t(['3.3'], ['3.3.4'], 'Assess', '', ['redistribution policies', 'progressive tax', 'transfer payments', 'minimum wage']),
    ('November', 2024, '23', '4(a)'): t(['4.6', '4.3'], ['4.6.4', '4.3.9'], 'Explain', 'Consider', ['cost-push inflation', 'AD/AS', 'own economy']),
    ('November', 2024, '23', '4(b)'): t(['4.6'], ['4.6.5'], 'Assess', '', ['benefits of inflation', 'costs of inflation']),
    ('November', 2024, '23', '5(a)'): t(['6.2'], ['6.2.2'], 'Explain', 'Consider', ['tools of protection', 'employment', 'output']),
    ('November', 2024, '23', '5(b)'): t(['6.5', '6.2'], ['6.5.2', '6.2.3'], 'Assess', '', ['protectionism', 'current account deficit', 'alternative policies']),
})

SL = 'Sri Lanka – exports, depreciation and recovery'
EZ = 'Eurozone – inflation and the ECB'
TR = 'Turkey – unconventional monetary policy'

T2.update({
    # ---------- June 2024, 9708/21 — Sri Lanka ----------
    ('June', 2024, '21', '1(a)(i)'): t(['6.3'], ['6.3.2'], 'Identify', '', ['balance of trade', 'data trend'], SL),
    ('June', 2024, '21', '1(a)(ii)'): t(['6.3'], ['6.3.2'], 'Calculate', '', ['percentage change', 'balance of trade'], SL),
    ('June', 2024, '21', '1(b)'): t(['6.1'], ['6.1.1'], 'Explain', '', ['comparative advantage', 'opportunity cost'], SL),
    ('June', 2024, '21', '1(c)'): t(['6.4', '6.3'], ['6.4.3', '6.4.5', '6.3.4'], 'Consider', '', ['depreciation', 'balance of trade', 'PED for exports and imports'], SL),
    ('June', 2024, '21', '1(d)'): t(['6.2', '6.5'], ['6.2.3', '6.5.2'], 'Assess', '', ['removal of protectionism', 'trade deficit', 'imports'], SL),
    ('June', 2024, '21', '1(e)'): t(['5.4', '4.4'], ['5.4.3', '5.4.4', '4.4.4'], 'Assess', '', ['supply-side policy', 'economic growth', 'time lags'], SL),
    ('June', 2024, '21', '2(a)'): t(['1.6', '3.1'], ['1.6.2', '1.6.3', '3.1.1', '3.1.2'], 'Explain', 'Consider', ['public goods', 'merit goods', 'market failure', 'under-provision']),
    ('June', 2024, '21', '2(b)'): t(['1.4'], ['1.4.1', '1.4.2'], 'Assess', '', ['planned economy', 'mixed economy', 'transition']),
    ('June', 2024, '21', '3(a)'): t(['2.2'], ['2.2.1', '2.2.2', '2.2.3'], 'Explain', 'Consider', ['YED', 'YED formula', 'normal goods', 'inferior goods']),
    ('June', 2024, '21', '3(b)'): t(['2.3', '2.2'], ['2.3.5', '2.2.8'], 'Assess', '', ['PES', 'XED', 'business decisions']),
    ('June', 2024, '21', '4(a)'): t(['4.3', '4.6'], ['4.3.2', '4.3.3', '4.6.4'], 'Explain', 'Consider', ['components of AD', 'demand-pull inflation', 'spare capacity']),
    ('June', 2024, '21', '4(b)'): t(['5.2', '4.3'], ['5.2.4', '5.2.5', '5.2.7', '4.3.3'], 'Assess', '', ['fiscal policy', 'rebalancing', 'consumption', 'China']),
    ('June', 2024, '21', '5(a)'): t(['4.5'], ['4.5.3', '4.5.4'], 'Explain', 'Consider', ['causes of unemployment', 'high-income economy']),
    ('June', 2024, '21', '5(b)'): t(['5.2', '5.3', '5.4', '4.5'], ['5.2.7', '5.3.4', '5.4.4', '5.1.1'], 'Assess', '', ['expansionary policy', 'low unemployment', 'policy comparison']),

    # ---------- June 2024, 9708/22 — Dilemma for the ECB ----------
    ('June', 2024, '22', '1(a)'): t(['4.6'], ['4.6.2'], 'Describe', '', ['consumer prices', 'data trend'], EZ),
    ('June', 2024, '22', '1(b)'): t(['4.6', '4.3'], ['4.6.4', '4.3.12'], 'Identify', '', ['cost-push inflation', 'AD/AS diagram'], EZ),
    ('June', 2024, '22', '1(c)'): t(['4.6', '4.5'], ['4.6.4'], 'Consider', '', ['labour shortage', 'wage costs', 'cost-push inflation'], EZ),
    ('June', 2024, '22', '1(d)'): t(['2.2', '3.3', '4.6'], ['2.2.6', '2.2.7', '4.6.5'], 'Assess', '', ['PED', 'necessities', 'poorer households', 'fixed incomes'], EZ),
    ('June', 2024, '22', '1(e)'): t(['5.3', '4.6'], ['5.3.3', '5.3.4'], 'Assess', '', ['contractionary monetary policy', 'interest rates', 'recession risk'], EZ),
    ('June', 2024, '22', '2(a)'): t(['3.3'], ['3.3.2', '3.3.3'], 'Explain', 'Consider', ['Gini coefficient', 'causes of inequality', 'low-income country']),
    ('June', 2024, '22', '2(b)'): t(['3.3'], ['3.3.4'], 'Assess', '', ['redistribution policies', 'progressive tax', 'transfer payments', 'disincentives']),
    ('June', 2024, '22', '3(a)'): t(['1.6', '3.2'], ['1.6.3', '1.6.4', '3.2.2'], 'Explain', 'Consider', ['merit good', 'demerit good', 'subsidy']),
    ('June', 2024, '22', '3(b)'): t(['3.2', '1.6'], ['3.2.4', '3.2.1', '3.2.6', '1.6.4'], 'Assess', '', ['minimum price', 'demerit good', 'indirect tax', 'information']),
    ('June', 2024, '22', '4(a)'): t(['4.2', '4.4'], ['4.2.1', '4.2.2', '4.4.4'], 'Explain', 'Consider', ['circular flow', 'open economy', 'injections', 'economic growth']),
    ('June', 2024, '22', '4(b)'): t(['5.4', '4.4'], ['5.4.2', '5.4.4', '4.4.4'], 'Assess', '', ['supply-side policy', 'long-run growth', 'productive capacity']),
    ('June', 2024, '22', '5(a)'): t(['6.2'], ['6.2.1', '6.2.2'], 'Explain', 'Consider', ['protectionism', 'tariffs', 'effectiveness']),
    ('June', 2024, '22', '5(b)'): t(['6.2', '6.1'], ['6.2.3', '6.1.2'], 'Assess', '', ['free trade', 'protectionism', 'developing economy', 'infant industry']),

    # ---------- June 2024, 9708/23 — Turkey ----------
    ('June', 2024, '23', '1(a)'): t(['4.6', '5.3'], ['4.6.3', '5.3.2'], 'Calculate', '', ['real interest rate', 'nominal vs real'], TR),
    ('June', 2024, '23', '1(b)(i)'): t(['6.4'], ['6.4.3', '6.4.4'], 'Explain', '', ['depreciation', 'interest rates', 'currency demand'], TR),
    ('June', 2024, '23', '1(b)(ii)'): t(['6.4'], ['6.4.5'], 'Consider', '', ['depreciation', 'exporters', 'imported raw materials'], TR),
    ('June', 2024, '23', '1(c)'): t(['5.3', '4.6', '4.4'], ['5.3.3', '5.3.4', '4.6.5'], 'Assess', '', ['expansionary monetary policy', 'inflation', 'growth', 'exports'], TR),
    ('June', 2024, '23', '1(d)'): t(['5.2', '5.4', '4.6'], ['5.2.6', '5.4.4', '4.6.4'], 'Assess', '', ['contractionary fiscal policy', 'supply-side policy', 'inflation control'], TR),
    ('June', 2024, '23', '2(a)'): t(['2.1'], ['2.1.3'], 'Explain', 'Consider', ['determinants of demand', 'electric cars', 'government policy']),
    ('June', 2024, '23', '2(b)'): t(['2.2'], ['2.2.6', '2.2.8'], 'Assess', '', ['XED', 'YED', 'electric cars']),
    ('June', 2024, '23', '3(a)'): t(['1.5', '1.4'], ['1.5.1', '1.5.3', '1.4.1'], 'Explain', 'Consider', ['PPC', 'consumer vs capital goods', 'mixed economy']),
    ('June', 2024, '23', '3(b)'): t(['1.5', '4.4'], ['1.5.3', '4.4.4', '4.4.5'], 'Assess', '', ['investment', 'capital goods', 'future growth', 'opportunity cost']),
    ('June', 2024, '23', '4(a)'): t(['4.3', '4.6'], ['4.3.12', '4.3.8', '4.6.4'], 'Explain', 'Consider', ['AD increase', 'real output', 'price level', 'demand-pull inflation']),
    ('June', 2024, '23', '4(b)'): t(['4.5', '4.3', '5.4'], ['4.5.3', '4.3.12', '5.4.4'], 'Assess', '', ['aggregate demand', 'unemployment', 'supply-side alternatives', 'high-income country']),
    ('June', 2024, '23', '5(a)'): t(['6.1'], ['6.1.3'], 'Explain', 'Consider', ['terms of trade', 'export prices', 'low-income countries']),
    ('June', 2024, '23', '5(b)'): t(['6.2', '6.1'], ['6.2.2', '6.1.3'], 'Assess', '', ['tools of protection', 'terms of trade']),
})
