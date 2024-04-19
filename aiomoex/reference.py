"""Функции для получения справочной информации."""
from collections.abc import Iterable
from typing import Literal

import aiohttp

from aiomoex import client, request_helpers
from aiomoex.constants import C, Engines, Markets


async def get_reference(session: aiohttp.ClientSession, placeholder: str = "boards") -> client.Table:
    """Получить перечень доступных значений плейсхолдера в адресе запроса.

    Например в описание запроса https://iss.moex.com/iss/reference/32 присутствует следующий адрес
    /iss/engines/[engine]/markets/[market]/boards/[board]/securities с плейсхолдерами engines, markets и
    boards.

    Описание запроса - https://iss.moex.com/iss/reference/28

    :param session:
        Сессия http соединения.
    :param placeholder:
        Наименование плейсхолдера в адресе запроса: engines, markets, boards, boardgroups, durations,
        securitytypes, securitygroups, securitycollections.

    :return:
        Список словарей, которые напрямую конвертируется в pandas.DataFrame.
    """
    url = request_helpers.make_url(ending="index")
    return await request_helpers.get_short_data(session=session, url=url, table_name=placeholder)


async def get_security(session: aiohttp.ClientSession, string: str, primary_board: bool = False) -> client.Table:
    url = request_helpers.make_url(security=string)
    query = request_helpers.make_query(question=string)
    if primary_board:
        query['primary_board'] = int(primary_board)
    return await request_helpers.get_short_data(session=session, url=url, table_name=C.description, query=query)


async def find_securities(
    session: aiohttp.ClientSession,
    string: str,
    columns: Iterable[str] | None = ("secid", "regnumber"),
    engine: str | None = None,
    is_trading: bool | None = None,
    market: str | None = None,
    group_by: Literal['group', 'type'] | None = None,
    group_by_filter: bool | None = None,
) -> client.Table:
    """Найти инструменты по части Кода, Названию, ISIN, Идентификатору Эмитента, Номеру гос.регистрации.

    Один из вариантов использования - по регистрационному номеру узнать предыдущие тикеры эмитента, и с
    помощью нескольких запросов об истории котировок собрать длинную историю с использованием всех
    предыдущих тикеров.

    Описание запроса - https://iss.moex.com/iss/reference/5

    :param session:
        Сессия http соединения.
    :param string:
        Часть Кода, Названия, ISIN, Идентификатора Эмитента, Номера гос.регистрации.
    :param columns:
        Кортеж столбцов, которые нужно загрузить - по умолчанию тикер и номер государственно регистрации.
        Если пустой или None, то загружаются все столбцы.
    :param engine:
        Выдать бумаги торгуемые на engine.
    :param is_trading:
        Выводить только торгуемые is_trading=True или только не торгуемые бумаги - is_trading=False
    :param market:
        Выдать бумаги торгуемые на рынке (market).
    :param group_by:
        Группировать выводимый результат по полю. Доступны значения group и type.
    :param group_by_filter:
        Фильтровать по типам group или type.
        Зависит от значения фильтра group_by

    :return: Список словарей, которые напрямую конвертируется в pandas.DataFrame.
    """
    table = C.securities
    url = request_helpers.make_url(ending=table)
    query = request_helpers.make_query(question=string, table=table, columns=columns)
    if engine:
        query['engine'] = engine
    if is_trading:
        query['is_trading'] = int(is_trading)
    if market:
        query['market'] = market
    if group_by:
        query['group_by'] = group_by
    if group_by_filter:
        query['group_by_filter'] = int(group_by_filter)
    return await request_helpers.get_short_data(session=session, url=url, table_name=table, query=query)


async def get_futures(session: aiohttp.ClientSession, asset_code: str = '', show_expired: bool = False) -> client.Table:
    """ Получить список фьючерсов.

    Описание запроса - https://iss.moex.com/iss/reference/999

    :param session:
        Сессия http соединения
    :param asset_code:
        Код базового актива
    :param show_expired:
        Показывать уже не торгующиеся опционные серии

    :return: Список словарей, которые напрямую конвертируется в pandas.DataFrame.
    """

    url = request_helpers.make_url(statistics=True, engine=Engines.futures, market=Markets.forts, ending=C.series)
    query = request_helpers.make_query()
    if asset_code:
        query['asset_code'] = asset_code
    if show_expired:
        query['show_expired'] = int(show_expired)
    return await request_helpers.get_short_data(session=session, url=url, table_name=C.series, query=query)
