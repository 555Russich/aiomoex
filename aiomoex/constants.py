from typing import Final
from enum import StrEnum, IntEnum


class C(StrEnum):
    description = 'description'
    securities = 'securities'
    candle_borders = "candleborders"
    candles = "candles"
    board = 'boards'
    engines = 'engines'
    series = 'series'


class CandleInterval(IntEnum):
    MIN_1 = 1
    MIN_10 = 10
    HOUR = 60
    DAY = 24
    WEEK = 7
    MONTH = 31
    QUARTER = 4


class Engines(StrEnum):
    stock = 'stock'  # Фондовый рынок и рынок депозитов
    state = 'state'  # Рынок ГЦБ (размещение)
    currency = 'currency'  # Валютный рынок
    futures = 'futures'  # Срочный рынок
    commodity = 'commodity'  # Товарный рынок
    interventions = 'interventions'  # Товарные интервенции
    offboard = 'offboard'  # ОТС-система
    agro = 'agro'  # Агро
    otc = 'otc'  # ОТС с ЦК
    quotes = 'quotes'  # Квоты


class Markets(StrEnum):
    index = 'index'  # Индексы фондового рынка
    shares = 'shares'  # Рынок акций
    bonds = 'bonds'  # Рынок облигаций
    ndm = 'ndm'  # Режим переговорных сделок
    otc = 'otc'  # ОТС
    ccp = 'ccp'  # РЕПО с ЦК
    deposit = 'deposit'  # Депозиты с ЦК
    repo = 'repo'  # Рынок сделок РЕПО
    qnv = 'qnv'  # Квал. инвесторы
    mamc = 'mamc'  # Мультивалютный рынок смешанных активов
    foreignshares = 'foreignshares'  # Иностранные ц.б.
    foreignndm = 'foreignndm'  # Иностранные ц.б. РПС
    moexboard = 'moexboard'  # MOEX Board
    gcc = 'gcc'  # РЕПО с ЦК с КСУ
    credit = 'credit'  # Рынок кредитов
    selt = 'selt'  # Биржевые сделки с ЦК
    futures = 'futures'  # Поставочные фьючерсы
    main = 'main'  # Срочные инструменты
    forts = 'forts'  # ФОРТС
    options = 'options'  # Опционы ФОРТС
    fortsiqs = 'fortsiqs'  # Фьючерсы IQS
    optionsiqs = 'optionsiqs'  # Опционы IQS
    sharesndm = 'sharesndm'  # Акции с ЦК
    nonresndm = 'nonresndm'  # Режим переговорных сделок (нерезиденты)
    nonresrepo = 'nonresrepo'  # Рынок РЕПО (нерезиденты)
    nonresccp = 'nonresccp'  # Рынок РЕПО с ЦК (нерезиденты)
    grain = 'grain'  # Интервенции по зерну
    sugar = 'sugar'  # Торги сахаром
    auctions = 'auctions'  # Аукционы НТБ
    buyauctions = 'buyauctions'  # Закупочные аукционы НТБ
    standard = 'standard'  # Standard
    classica = 'classica'  # Classica


class Boards(StrEnum):
    TQIF = 'TQIF'  # Т+: Паи - безадрес.
    TQTF = 'TQTF'  # Т+: ETF - безадрес.
    TQBR = 'TQBR'  # Т+: Акции и ДР - безадрес.
    TQBS = 'TQBS'  # Т+: А2-Акции и паи - безадрес.
    TQNL = 'TQNL'  # Т+: Б-Акции и паи - безадрес.
    TQLV = 'TQLV'  # Т+: В-Акции и ДР - безадрес.
    TQLI = 'TQLI'  # Т+: И-Акции - безадрес.
    TQNE = 'TQNE'  # Т+: Акции, паи и ДР внесписочные - безадрес.
    TQDE = 'TQDE'  # Т+: Акции Д - безадрес.
    TQPI = 'TQPI'  # Т+: Акции ПИР - безадрес.
    TQTD = 'TQTD'  # Т+: ETF (USD) - безадрес.
    TQFD = 'TQFD'  # Т+: ПАИ (USD) - безадрес.
    TQPD = 'TQPD'  # Т+: Акции ПИР (USD) - безадрес.
    EQBR = 'EQBR'  # Основной режим: А1-Акции и паи - безадрес.
    EQBS = 'EQBS'  # Основной режим: А2-Акции и паи - безадрес.
    EQNL = 'EQNL'  # Основной режим: Б-Акции и паи - безадрес.
    EQLV = 'EQLV'  # Основной режим: В-Акции и РДР - безадрес.
    EQDE = 'EQDE'  # Основной режим: Акции Д - безадрес.
    EQLI = 'EQLI'  # Основной режим: И-Акции - безадрес.
    EQNE = 'EQNE'  # Основной режим: Акции и паи внесписочные - безадрес.
    SPEQ = 'SPEQ'  # Поставка по СК (акции)
    SMAL = 'SMAL'  # Т+: Неполные лоты (акции) - безадрес.
    TQDP = 'TQDP'  # Крупные пакеты - Акции - безадрес.
    EQDP = 'EQDP'  # Крупные пакеты - Акции - безадрес.
    EQTD = 'EQTD'  # Т0: ETF (USD) - безадрес.
    TQBE = 'TQBE'  # Т+: Акции и ДР (EUR) - безадрес.
    TQTE = 'TQTE'  # Т+: ETF (EUR) - безадрес.
    TQFE = 'TQFE'  # Т+: ПАИ (EUR) - безадрес.
    TQPE = 'TQPE'  # Т+: Акции ПИР (EUR) - безадрес.
    TQTY = 'TQTY'  # Т+: ПАИ (CNY) - безадрес.
    TQPY = 'TQPY'  # Т+: Акции ПИР (CNY) - безадрес.
    EQTU = 'EQTU'  # Т0: ETF (EUR) - безадрес.
    TQTH = 'TQTH'  # Т+: ПАИ (HKD) - безадрес.
    TQPH = 'TQPH'  # Т+: Акции ПИР (HKD) - безадрес.
    EQCC = 'EQCC'  # ЦК - режим основных торгов - безадрес.
    TQOB = 'TQOB'  # Т+: Гособлигации - безадрес.
    TQOS = 'TQOS'  # Т+: А2-Облигации - безадрес.
    TQNO = 'TQNO'  # Т+: Б-Облигации - безадрес.
    TQOV = 'TQOV'  # Т+: В-Облигации - безадрес.
    TQNB = 'TQNB'  # Т+: Облигации внесписочные - безадрес.
    TQUS = 'TQUS'  # Т+: Облигации внеспис. в ин.валюте - безадрес.
    TQCB = 'TQCB'  # Т+: Облигации - безадрес.
    TQRD = 'TQRD'  # Т+: Облигации Д - безадрес.
    TQIR = 'TQIR'  # Т+ Облигации ПИР - безадрес.
    TQOD = 'TQOD'  # Т+: Облигации (USD) - безадрес.
    TQUD = 'TQUD'  # Т+: Облигации Д (USD) - безадрес.
    TQIU = 'TQIU'  # Т+: Облигации ПИР (USD) - безадрес.
    TQTC = 'TQTC'  # T+: ETC - безадрес.
    EQOB = 'EQOB'  # Т0 Облигации - безадрес.
    EQOS = 'EQOS'  # Основной режим: А2-Облигации - безадрес.
    EQNO = 'EQNO'  # Основной режим: Б-Облигации - безадрес.
    EQOV = 'EQOV'  # Основной режим: В-Облигации - безадрес.
    EQDB = 'EQDB'  # Основной режим: Облигации Д - безадрес.
    EQNB = 'EQNB'  # Основной режим: Облигации внесписочные - безадрес.
    EQUS = 'EQUS'  # Основной режим: Облигации внеспис. в ин.валюте - безадрес.
    EQEO = 'EQEO'  # Основной режим: Облигации (EUR) - безадрес.
    SPOB = 'SPOB'  # Поставка по ОФЗ
    EQTC = 'EQTC'  # T0 ETC - безадрес.
    EQEU = 'EQEU'  # Облигации (USD) - безадрес.
    EQGO = 'EQGO'  # Облигации (GBP) - безадрес.
    EQYO = 'EQYO'  # Облигации (CNY) - безадрес.
    AUBB = 'AUBB'  # Выкуп: Аукцион - безадрес.
    AUCT = 'AUCT'  # Размещение: Аукцион - безадрес.
    TQDB = 'TQDB'  # Крупные пакеты: Облигации - безадрес.
    TQOE = 'TQOE'  # Т+: Облигации (EUR) - безадрес.
    TQED = 'TQED'  # Т+: Облигации Д (EUR) - безадрес
    TQIE = 'TQIE'  # Т+: Облигации ПИР (EUR) - безадрес.
    TQDU = 'TQDU'  # Крупные пакеты – Облигации (USD) - безадрес.
    TQOY = 'TQOY'  # Т+: Облигации (CNY) - безадрес.
    TQIY = 'TQIY'  # Т+: Облигации ПИР (CNY) - безадрес.
    PACT = 'PACT'  # Аукцион: адресные заявки
    RPMO = 'RPMO'  # РЕПО-М - адрес.
    RPEQ = 'RPEQ'  # РЕПО: Акции и паи - адрес.
    RPMA = 'RPMA'  # РЕПО c акциями - адрес.
    RPEU = 'RPEU'  # РЕПО в ин. валюте (USD) - адрес.
    RPUA = 'RPUA'  # РЕПО c акциями (USD) - адрес.
    RPUO = 'RPUO'  # РЕПО c облигациями (USD) - адрес.
    RPEO = 'RPEO'  # РЕПО в ин. валюте (EUR) - адрес.
    RPEY = 'RPEY'  # РЕПО в ин.валюте (CNY) - адрес.
    RPGO = 'RPGO'  # РЕПО c облигациями (GBP) - адрес.
    RPCC = 'RPCC'  # РЕПО с ЦК - адрес.
    PTEU = 'PTEU'  # РПС с ЦК: Облигации (USD) - адрес.
    PTIF = 'PTIF'  # РПС с ЦК: Паи - адрес.
    PTTC = 'PTTC'  # РПС с ЦК: ETC - адрес.
    PTTF = 'PTTF'  # РПС с ЦК: ETF - адрес.
    PTEQ = 'PTEQ'  # РПС с ЦК: Акции и ДР - адрес.
    PTES = 'PTES'  # РПС С ЦК: А2-Акции и паи - адрес.
    PTNL = 'PTNL'  # РПС С ЦК: Б-Акции и паи - адрес.
    PTLV = 'PTLV'  # РПС С ЦК: В-Акции и ДР - адрес.
    PTLI = 'PTLI'  # РПС С ЦК: И-Акции - адрес.
    PTNE = 'PTNE'  # РПС С ЦК: Акции, паи и ДР внесписочные - адрес.
    PTNO = 'PTNO'  # РПС С ЦК: Б-Облигации - адрес.
    PTUS = 'PTUS'  # РПС С ЦК: Облигации в ин.валюте - адрес.
    PTDE = 'PTDE'  # РПС с ЦК: Акции Д - адрес.
    PTPI = 'PTPI'  # РПС с ЦК: Акции ПИР - адрес.
    PSTD = 'PSTD'  # РПС: ETF (USD) - адрес.
    PSFD = 'PSFD'  # РПС: ПАИ (USD) - адресн.
    PSPD = 'PSPD'  # РПС: Акции ПИР (USD) - адресн.
    PSIF = 'PSIF'  # РПС: Паи - адрес.
    PSTC = 'PSTC'  # РПС: ETC - адрес.
    PSTF = 'PSTF'  # РПС: ETF - адрес.
    PSEQ = 'PSEQ'  # РПС: Акции - адрес.
    PSES = 'PSES'  # РПС: А2-Акции и паи - адрес.
    PSNL = 'PSNL'  # РПС: Б-Акции и паи - адрес.
    PSLV = 'PSLV'  # РПС: В-Акции и ДР - адрес.
    PSDE = 'PSDE'  # РПС: Акции Д - адрес.
    PSLI = 'PSLI'  # РПС: И-Акции - адрес.
    PSNE = 'PSNE'  # РПС: Акции, паи и ДР внесписочные - адрес.
    PSOS = 'PSOS'  # РПС: А2-Облигации - адрес.
    PSNO = 'PSNO'  # РПС: Б-Облигации - адрес.
    PSOV = 'PSOV'  # РПС: В-Облигации - адрес.
    PSNB = 'PSNB'  # РПС: Облигации внесписочные - адрес.
    PSUS = 'PSUS'  # РПС: Облигации в ин.валюте - адрес.
    PSPI = 'PSPI'  # РПС: Акции ПИР - адрес.
    PSGO = 'PSGO'  # РПС: Облигации (GBP) - адрес.
    PSAU = 'PSAU'  # Размещение - адрес.
    PAUS = 'PAUS'  # Размещение (USD) - адрес.
    PAEU = 'PAEU'  # Размещение (EUR) - адрес.
    PACY = 'PACY'  # Размещение (CNY) - адрес.
    PAGB = 'PAGB'  # Размещение (GBP) - адрес.
    PSBB = 'PSBB'  # Выкуп - адрес.
    PSBE = 'PSBE'  # Выкуп (EUR) - адрес.
    OTCB = 'OTCB'  # Анонимный РПС - адрес.
    OTCU = 'OTCU'  # Анонимный РПС (USD) - адрес.
    OTCE = 'OTCE'  # Анонимный РПС (EUR) - адрес.
    PTTD = 'PTTD'  # РПС с ЦК: ETF (USD) - адрес.
    PTFD = 'PTFD'  # РПС с ЦК: Паи (USD) - адресн.
    PTPD = 'PTPD'  # РПС с ЦК: Акции ПИР (USD) - адресн.
    PSBU = 'PSBU'  # Выкуп (USD) - адрес.
    PSBY = 'PSBY'  # Выкуп (CNY) - адрес.
    PTOE = 'PTOE'  # РПС с ЦК: Облигации (EUR) - адрес.
    PTED = 'PTED'  # РПС с ЦК: Д Облигации (EUR) - адрес.
    PTIE = 'PTIE'  # РПС с ЦК: Облигации ПИР (EUR) - адрес.
    PSSE = 'PSSE'  # РПС: Акции и ДР (расч. в EUR) - адрес.
    PSTE = 'PSTE'  # РПС: ETF (расч. в EUR) - адрес.
    PSFE = 'PSFE'  # РПС: ПАИ (EUR) - адрес.
    PSPE = 'PSPE'  # РПС: Акции ПИР (EUR) - адрес.
    PTSE = 'PTSE'  # РПС с ЦК: Акции и ДР (EUR) - адрес.
    PTTE = 'PTTE'  # РПС с ЦК: ETF (EUR) - адрес.
    PTFE = 'PTFE'  # РПС с ЦК: Паи (EUR) - адрес.
    PTPE = 'PTPE'  # РПС с ЦК: Акции ПИР (EUR) - адрес.
    PTOB = 'PTOB'  # РПС с ЦК: Облигации - адрес.
    PTOS = 'PTOS'  # РПС С ЦК: А2-Облигации - адрес.
    PTOV = 'PTOV'  # РПС С ЦК: В-Облигации - адрес.
    PTNB = 'PTNB'  # РПС С ЦК: Облигации внесписочные - адрес.
    PTDB = 'PTDB'  # РПС с ЦК: Д Облигации - адрес.
    PTIR = 'PTIR'  # РПС с ЦК: Облигации ПИР - адрес.
    PTOD = 'PTOD'  # РПС с ЦК: Облигации (USD) - адрес.
    PTUD = 'PTUD'  # РПС с ЦК: Д Облигации (USD) - адрес.
    PTIU = 'PTIU'  # РПС с ЦК: Облигации ПИР (USD) - адрес.
    PSOB = 'PSOB'  # РПС: Облигации - адрес.
    PSDB = 'PSDB'  # РПС: Облигации Д - адрес.
    PSIR = 'PSIR'  # РПС: Облигации ПИР - адрес.
    PSEU = 'PSEU'  # РПС: Облигации (USD) - адрес.
    PSUD = 'PSUD'  # РПС: Облигации Д (USD) - адрес.
    PSIU = 'PSIU'  # РПС: Облигации ПИР (USD) - адрес.
    PSEO = 'PSEO'  # РПС: Облигации (EUR) - адрес.
    PSED = 'PSED'  # РПС: Облигации Д (EUR) - адрес.
    PSIE = 'PSIE'  # РПС: Облигации ПИР (EUR) - адрес.
    PSYO = 'PSYO'  # РПС: Облигации (CNY) - адрес.
    PSIY = 'PSIY'  # РПС: Облигации ПИР (CNY) - адрес.
    PTIY = 'PTIY'  # РПС с ЦК: Облигации ПИР (CNY) - адрес.
    PTOY = 'PTOY'  # РПС с ЦК: Облигации (CNY) - адрес.
    PSTY = 'PSTY'  # РПС: ПАИ (CNY) - адрес.
    PSPY = 'PSPY'  # РПС: Акции ПИР (CNY) - адрес.
    PTTY = 'PTTY'  # РПС с ЦК: Паи (CNY) - адрес.
    PTPY = 'PTPY'  # РПС с ЦК: Акции ПИР (CNY) - адрес.
    PSTH = 'PSTH'  # РПС: ПАИ (HKD) - адресн.
    PSPH = 'PSPH'  # РПС: Акции ПИР (HKD) - адресн.
    PTTH = 'PTTH'  # РПС с ЦК: Паи (HKD) - адресн.
    PTPH = 'PTPH'  # РПС с ЦК: Акции ПИР (HKD) - адресн.
    PSCC = 'PSCC'  # РПС с ЦК - адрес.
    SNDX = 'SNDX'  # Индексы фондового рынка
    RTSI = 'RTSI'  # Индексы РТС
    INAV = 'INAV'  # INAV
    MMIX = 'MMIX'  # Money Market IndeX
    AGRO = 'AGRO'  # Индексы НТБ
    INPF = 'INPF'  # Ценовой фиксинг
    SDII = 'SDII'  # Индексы СПФИ
    STMR = 'STMR'  # Standard: дневная сессия - безадрес.
    SDMR = 'SDMR'  # Standard: вечерняя сессия - безадрес.
    STAD = 'STAD'  # Standard: дневная сессия - адрес.
    SDAD = 'SDAD'  # Standard: вечерняя сессия - адрес.
    STRP = 'STRP'  # Standard: сделки репо, дневная сессия - адрес.
    SDRP = 'SDRP'  # Standard: сделки репо, вечерняя сессия - адрес.
    CLMR = 'CLMR'  # Classica - безадрес.
    CLAD = 'CLAD'  # Classica - адрес.
    EQRD = 'EQRD'  # РЕПО с ЦК 1 день (USD) - безадрес.
    EQRE = 'EQRE'  # РЕПО с ЦК 1 день (EUR) - безадрес.
    EQWP = 'EQWP'  # РЕПО с ЦК 7 дн. - безадрес.
    EQWD = 'EQWD'  # РЕПО с ЦК 7 дней (USD) - безадрес.
    EQWE = 'EQWE'  # РЕПО с ЦК 7 дней (EUR) - безадрес.
    EQRP = 'EQRP'  # РЕПО с ЦК 1 день - безадрес.
    EQMP = 'EQMP'  # РЕПО с ЦК 1 мес.(RUB) - безадрес.
    EQMD = 'EQMD'  # РЕПО с ЦК 1 мес. (USD) - безадрес.
    EQME = 'EQME'  # РЕПО с ЦК 1 мес. (EUR) - безадрес.
    EQTP = 'EQTP'  # РЕПО с ЦК 3 мес. (RUB) - безадрес.
    ETQD = 'ETQD'  # РЕПО с ЦК 3 мес. (USD) - безадрес.
    EQTE = 'EQTE'  # РЕПО с ЦК 3 мес. (EUR) - безадрес.
    LIQR = 'LIQR'  # РЕПО с ЦК: Урегулирование - безадрес.
    EQRY = 'EQRY'  # РЕПО с ЦК 1 день (CNY) - безадрес.
    PSRY = 'PSRY'  # РЕПО с ЦК (CNY) - адрес.
    EQWY = 'EQWY'  # РЕПО с ЦК 7 дней (CNY) - безадрес.
    EQMY = 'EQMY'  # РЕПО с ЦК 1 мес. (CNY) - безадрес.
    EQTY = 'EQTY'  # РЕПО с ЦК 3 мес. (CNY) - безадрес
    PSRP = 'PSRP'  # РЕПО с ЦК - адрес.
    PSRD = 'PSRD'  # РЕПО с ЦК (USD) - адрес.
    PSRE = 'PSRE'  # РЕПО с ЦК (EUR) - адрес.
    FKRP = 'FKRP'  # Аукцион с ЦК 1 день - безадрес.
    FKOW = 'FKOW'  # Аукцион с ЦК 1 неделя - безадрес.
    FKSW = 'FKSW'  # Аукцион с ЦК 2 недели - безадрес.
    FKFW = 'FKFW'  # Аукцион с ЦК 5 недель - безадрес.
    FKOM = 'FKOM'  # Аукцион с ЦК 1 месяц - безадрес.
    FKSM = 'FKSM'  # Аукцион с ЦК 2 месяца - безадрес.
    FKTM = 'FKTM'  # Аукцион с ЦК 3 месяца - безадрес.
    FKUM = 'FKUM'  # Аукцион с ЦК 6 месяцев - безадрес.
    FKOY = 'FKOY'  # Аукцион с ЦК 1 год - безадрес.
    FRRP = 'FRRP'  # Аукцион РЕПО с ЦК 1 день - безадрес.
    FROW = 'FROW'  # Аукцион РЕПО с ЦК 1 неделя - безадрес.
    FRSW = 'FRSW'  # Аукцион РЕПО с ЦК 2 недели - безадрес.
    FRFW = 'FRFW'  # Аукцион РЕПО с ЦК 5 недель - безадрес.
    FROM = 'FROM'  # Аукцион РЕПО с ЦК 1 месяц - безадрес.
    FRTM = 'FRTM'  # Аукцион РЕПО с ЦК 3 месяца - безадрес.
    FSRP = 'FSRP'  # Аукцион обр.РЕПО с ЦК 1 день - безадрес.
    FSOW = 'FSOW'  # Аукцион обр.РЕПО с ЦК 1 неделя - безадрес.
    FSSW = 'FSSW'  # Аукцион обр.РЕПО с ЦК 2 недели - безадрес.
    FSOM = 'FSOM'  # Аукцион обр.РЕПО с ЦК 1 месяц - безадрес.
    FSFW = 'FSFW'  # Аукцион обр.РЕПО с ЦК 5 недель - безадрес.
    TQQI = 'TQQI'  # Т+: Для квал. инвесторов - безадрес.
    EQQI = 'EQQI'  # Основной режим: Для квал. инвесторов - безадрес.
    PSQI = 'PSQI'  # РПС: Для квал. инвесторов - адрес.
    PTQI = 'PTQI'  # РПС с ЦК: Для квал. инвесторов - адрес.
    RPQI = 'RPQI'  # РЕПО: Для квал. инвесторов - адрес.
    RPUQ = 'RPUQ'  # РЕПО: Для квал. инвесторов (USD) - адрес.
    TQQD = 'TQQD'  # Т+: Для квал. инвесторов (USD) - безадрес.
    SOTC = 'SOTC'  # Репортинг внебиржевых сделок (6264-У)
    MXBD = 'MXBD'  # MOEX Board
    TDEP = 'TDEP'  # Депозиты с ЦК - безадрес.
    NDEP = 'NDEP'  # Депозиты с ЦК - адрес.
    NDPU = 'NDPU'  # Депозиты с ЦК (USD) - адрес.
    NDPE = 'NDPE'  # Депозиты с ЦК (EUR) - адрес.
    TDPU = 'TDPU'  # Депозиты с ЦК (USD) - безадрес.
    TDPE = 'TDPE'  # Депозиты с ЦК (EUR) - безадрес.
    TDPY = 'TDPY'  # Депозиты с ЦК (CNY) - безадрес.
    NDPY = 'NDPY'  # Депозиты с ЦК (CNY) - адрес.
    ADEP = 'ADEP'  # Депозиты с ЦК - Аукцион
    LIQB = 'LIQB'  # Продажа обеспечения бирж.рынок - безадрес.
    CIQB = 'CIQB'  # Урегулирование с ЦК Нерезиденты - безадрес.
    GCRP = 'GCRP'  # РЕПО с ЦК с КСУ 1 день - безадрес.
    GCOW = 'GCOW'  # РЕПО с ЦК с КСУ 7 дн. - безадрес.
    GCSW = 'GCSW'  # РЕПО с ЦК с КСУ 14 дн. - безадрес.
    GCOM = 'GCOM'  # РЕПО с ЦК с КСУ 1 месяц - безадрес.
    GCSM = 'GCSM'  # РЕПО с ЦК с КСУ 2 месяца - безадрес.
    GCTM = 'GCTM'  # РЕПО с ЦК с КСУ 3 месяца - безадрес.
    GCUM = 'GCUM'  # РЕПО с ЦК с КСУ 6 мес. - безадрес.
    GCOY = 'GCOY'  # РЕПО с ЦК с КСУ 1 год - безадрес.
    PSGC = 'PSGC'  # РЕПО с ЦК с КСУ - адрес.
    GURP = 'GURP'  # РЕПО с ЦК с КСУ 1 день (USD) - безадрес.
    GUOW = 'GUOW'  # РЕПО с ЦК с КСУ 7 дн. (USD) - безадрес.
    GUSW = 'GUSW'  # РЕПО с ЦК с КСУ 14 дн. (USD) - безадрес.
    GUOM = 'GUOM'  # РЕПО с ЦК с КСУ 1 месяц (USD) - безадрес.
    GUSM = 'GUSM'  # РЕПО с ЦК с КСУ 2 месяца (USD) - безадрес.
    GUTM = 'GUTM'  # РЕПО с ЦК с КСУ 3 месяца (USD) - безадрес.
    GUUM = 'GUUM'  # РЕПО с ЦК с КСУ 6 месяцев (USD) - безадрес.
    GUOY = 'GUOY'  # РЕПО с ЦК с КСУ 1 год (USD) - безадрес.
    PUGC = 'PUGC'  # РЕПО с ЦК с КСУ (USD) - адрес.
    GERP = 'GERP'  # РЕПО с ЦК с КСУ 1 день (EUR) - безадрес.
    GEOW = 'GEOW'  # РЕПО с ЦК с КСУ 7 дн. (EUR) - безадрес.
    GESW = 'GESW'  # РЕПО с ЦК с КСУ 14 дн. (EUR) - безадрес.
    GEOM = 'GEOM'  # РЕПО с ЦК с КСУ 1 месяц (EUR) - безадрес.
    GESM = 'GESM'  # РЕПО с ЦК с КСУ 2 месяца (EUR) - безадрес.
    GETM = 'GETM'  # РЕПО с ЦК с КСУ 3 месяца (EUR) - безадрес.
    GEUM = 'GEUM'  # РЕПО с ЦК с КСУ 6 месяцев (EUR) - безадрес.
    GEOY = 'GEOY'  # РЕПО с ЦК с КСУ 1 год (EUR) - безадрес.
    PEGC = 'PEGC'  # РЕПО с ЦК с КСУ (EUR) - адрес.
    GCNM = 'GCNM'  # РЕПО с ЦК с КСУ 9 месяцев - безадрес.
    GUNM = 'GUNM'  # РЕПО с ЦК с КСУ 9 мес. (USD) - безадрес.
    GENM = 'GENM'  # РЕПО с ЦК с КСУ 9 мес. (EUR) - безадрес.
    GYRP = 'GYRP'  # РЕПО с ЦК с КСУ 1 день (CNY) - безадрес.
    GYOW = 'GYOW'  # РЕПО с ЦК с КСУ 7 дней (CNY) - безадрес.
    GYSW = 'GYSW'  # РЕПО с ЦК с КСУ 14 дней (CNY) - безадрес.
    GYOM = 'GYOM'  # РЕПО с ЦК с КСУ 1 месяц (CNY) - безадрес.
    GYSM = 'GYSM'  # РЕПО с ЦК с КСУ 2 месяца (CNY) - безадрес.
    GYTM = 'GYTM'  # РЕПО с ЦК с КСУ 3 месяца (CNY) - безадрес.
    GYUM = 'GYUM'  # РЕПО с ЦК с КСУ 6 месяцев (CNY) - безадрес.
    GYNM = 'GYNM'  # РЕПО с ЦК с КСУ 9 месяцев (CNY) - безадрес.
    GYOY = 'GYOY'  # РЕПО с ЦК с КСУ 1 год (CNY) - безадрес.
    PYGC = 'PYGC'  # РЕПО с ЦК с КСУ (CNY) - адрес.
    FCOW = 'FCOW'  # РЕПО с ЦК с КСУ пл. 7 дней - безадрес. (RUSFAR)
    FCSW = 'FCSW'  # РЕПО с ЦК с КСУ пл. 14 дней - безадрес. (RUSFAR)
    FCOM = 'FCOM'  # РЕПО с ЦК с КСУ пл. 1 месяц - безадрес. (RUSFAR)
    FCSM = 'FCSM'  # РЕПО с ЦК с КСУ пл. 2 месяца - безадрес. (RUSFAR)
    FCTM = 'FCTM'  # РЕПО с ЦК с КСУ пл. 3 месяца - безадрес. (RUSFAR)
    FCUM = 'FCUM'  # РЕПО с ЦК с КСУ пл. 6 месяца - безадрес. (RUSFAR)
    FCNM = 'FCNM'  # РЕПО с ЦК с КСУ пл. 9 месяца - безадрес. (RUSFAR)
    FCOY = 'FCOY'  # РЕПО с ЦК с КСУ пл. 1 год - безадрес. (RUSFAR)
    FYOW = 'FYOW'  # РЕПО с ЦК с КСУ пл. 7 дней (CNY) - безадрес. (RUSFARCNY)
    FYSW = 'FYSW'  # РЕПО с ЦК с КСУ пл. 14 дней (CNY) - безадрес. (RUSFARCNY)
    FYOM = 'FYOM'  # РЕПО с ЦК с КСУ пл. 1 месяц (CNY) - безадрес. (RUSFARCNY)
    FYSM = 'FYSM'  # РЕПО с ЦК с КСУ пл. 2 месяца (CNY) - безадрес. (RUSFARCNY)
    FYTM = 'FYTM'  # РЕПО с ЦК с КСУ пл. 3 месяца (CNY) - безадрес. (RUSFARCNY)
    FYUM = 'FYUM'  # РЕПО с ЦК с КСУ пл. 6 месяца (CNY) - безадрес. (RUSFARCNY)
    FYNM = 'FYNM'  # РЕПО с ЦК с КСУ пл. 9 месяца (CNY) - безадрес. (RUSFARCNY)
    FYOY = 'FYOY'  # РЕПО с ЦК с КСУ пл. 1 год (CNY) - безадрес. (RUSFARCNY)
    FAOM = 'FAOM'  # РЕПО с ЦК с КСУ пл. КлСт 1 мес. - безадрес. (RREFKEYR)
    FATM = 'FATM'  # РЕПО с ЦК с КСУ пл. КлСт 3 мес. - безадрес. (RREFKEYR)
    FQBH = 'FQBH'  # Т+: Ин.Акции и ДР (HKD) - безадрес.
    FQDH = 'FQDH'  # Т+: Ин.Акции ПИР (HKD) - безадрес.
    FQBR = 'FQBR'  # Т+ Ин.Акции и ДР - безадрес.
    FQDE = 'FQDE'  # Т+ Ин.Акции ПИР - безадрес.
    TQBD = 'TQBD'  # Т+: Ин.Акции и ДР (USD) - безадрес.
    TQDD = 'TQDD'  # Т+: Ин.Акции ПИР (USD) - безадрес.
    FQBY = 'FQBY'  # Т+: Ин.Акции и ДР (CNY) - безадрес.
    FQDY = 'FQDY'  # Т+: Ин.Акции ПИР (CNY) - безадрес.
    FTSH = 'FTSH'  # РПС с ЦК: Ин.Акции и ДР (HKD) - адрес.
    FTDH = 'FTDH'  # РПС с ЦК: Ин.Акции ПИР (HKD) - адрес.
    FSSH = 'FSSH'  # РПС: Ин.Акции (HKD) - адрес.
    FSDH = 'FSDH'  # РПС: Ин.Акции ПИР (HKD) - адрес.
    FTEQ = 'FTEQ'  # РПС с ЦК: Ин.Акции и ДР - адрес.
    FTDE = 'FTDE'  # РПС с ЦК: Ин.Акции ПИР - адрес.
    PSSD = 'PSSD'  # РПС: Ин.Акции (USD) - адрес.
    PSDD = 'PSDD'  # РПС: Ин.Акции ПИР (USD) - адрес.
    FTSY = 'FTSY'  # РПС с ЦК: Ин.Акции и ДР (CNY) - адрес.
    FTDY = 'FTDY'  # РПС с ЦК: Ин.Акции ПИР (CNY) - адрес.
    FSSY = 'FSSY'  # РПС: Ин.Акции (CNY) - адрес.
    FSDY = 'FSDY'  # РПС: Ин.Акции ПИР (CNY) - адрес.
    FSEQ = 'FSEQ'  # РПС: Ин.Акции - адрес.
    FSDE = 'FSDE'  # Ин.Акции ПИР - РПС - адрес.
    PTSD = 'PTSD'  # РПС с ЦК: Ин.Акции и ДР (USD) - адрес.
    PTDD = 'PTDD'  # РПС с ЦК: Ин.Акции ПИР (USD) - адрес.
    CRER = 'CRER'  # Кредиты RUB - адрес.
    CREU = 'CREU'  # Кредиты USD - адрес.
    CREE = 'CREE'  # Кредиты EUR - адрес.
    CREY = 'CREY'  # Кредиты CNY - адрес.
    CTEQ = 'CTEQ'  # РПС с ЦК Нерезиденты: Акции и ДР - адрес.
    CTSD = 'CTSD'  # РПС с ЦК Нерезиденты: Акции и ДР (USD) - адрес.
    CTSE = 'CTSE'  # РПС с ЦК Нерезиденты: Акции и ДР (EUR) - адрес.
    CTOB = 'CTOB'  # РПС с ЦК Нерезиденты: Облигации - адрес.
    CTOY = 'CTOY'  # РПС с ЦК Нерезиденты: Облигации (CNY) - адрес.
    CTOD = 'CTOD'  # РПС с ЦК Нерезиденты: Облигации (USD) - адрес.
    CTOE = 'CTOE'  # РПС с ЦК Нерезиденты: Облигации (EUR) - адрес.
    CPMO = 'CPMO'  # РЕПО-M Нерезиденты - адрес.
    CPEU = 'CPEU'  # РЕПО-M Нерезиденты (USD) - адрес.
    CPEO = 'CPEO'  # РЕПО-M Нерезиденты (EUR) - адрес.
    CPEY = 'CPEY'  # РЕПО-M Нерезиденты (CNY) - адрес.
    CIQR = 'CIQR'  # Урегулирование РЕПО с ЦК Нерезиденты - безадрес.
    MAIN = 'MAIN'  # ГЦБ
    RPDD = 'RPDD'  # Сделки междилерского РЕПО
    NEGD = 'NEGD'  # ГЦБ: Внесистемные сделки
    GNDX = 'GNDX'  # Индексы ГЦБ
    CETS = 'CETS'  # Системные сделки - безадрес.
    SDBP = 'SDBP'  # Крупные сделки - безадрес.
    CURR = 'CURR'  # Дневная сессия
    CNGD = 'CNGD'  # Внесистемные сделки- адрес.
    LICU = 'LICU'  # Внесистемные сделки урегулирования - безадрес.
    FIXS = 'FIXS'  # Фиксинг системный - безадрес.
    FIXN = 'FIXN'  # Фиксинг внесистемный- адрес.
    WAPS = 'WAPS'  # Системные средневзвешенные - безадрес.
    WAPN = 'WAPN'  # Внесистемные средневзвешенные - адрес.
    AUCB = 'AUCB'  # Аукцион ЦБР - адрес.
    SPEC = 'SPEC'  # Поставка - безадресные
    FUTS = 'FUTS'  # Фьючерсы системные - безадрес.
    FUTN = 'FUTN'  # Фьючерсы внесистемные- адрес.
    FIXI = 'FIXI'  # Валютный фиксинг
    OTCT = 'OTCT'  # Рынок OTC
    OTCF = 'OTCF'  # Рынок OTC крупные сделки
    FOB = 'FOB'  # Фьючерсы и Опционы
    RFUD = 'RFUD'  # Фьючерсы
    ROPD = 'ROPD'  # Опционы
    FIQS = 'FIQS'  # Фьючерсы IQS
    OIQS = 'OIQS'  # Опционы IQS
    FOCM = 'FOCM'  # Фьючерсы на товарные активы
    GSEL = 'GSEL'  # Интервенции по продаже зерна
    OBBO = 'OBBO'  # ОТС-система: облигации
    SUGR = 'SUGR'  # Агро: Сахар
    AIGR = 'AIGR'  # Агро: Аукционы НТБ
    ABGR = 'ABGR'  # Агро: Закупочные аукционы НТБ
    OCTR = 'OCTR'  # ОТС: Облигации Т+ - безадресные
    OCTU = 'OCTU'  # ОТС: Облигации Т+ (USD) - безадресные
    OCBR = 'OCBR'  # OTC: Облигации с ЦК - двусторонние
    OCBY = 'OCBY'  # OTC: Облигации с ЦК (CNY) - двусторонние
    OCBU = 'OCBU'  # OTC: Облигации с ЦК (USD) - двусторонние
    OCAR = 'OCAR'  # OTC: Облигации с ЦК адрес. - двусторонние
    OCAY = 'OCAY'  # OTC: Облигации с ЦК адрес. (CNY) - двусторонние
    OCAU = 'OCAU'  # OTC: Облигации с ЦК адрес. (USD) - двусторонние
    MTQR = 'MTQR'  # ОТС: Акции Т+ - безадресные
    MPTR = 'MPTR'  # ОТС: Акции РПС с ЦК - адресные
    MPAU = 'MPAU'  # OTC Размещение: Адресный
    MPBB = 'MPBB'  # OTC Выкуп: Адресный
    QBND = 'QBND'  # Квоты


# Режимы по умолчанию для запросов
DEFAULT_ENGINE: Final = Engines.stock
DEFAULT_MARKET: Final = Markets.shares
DEFAULT_BOARD: Final = Boards.TQBR
