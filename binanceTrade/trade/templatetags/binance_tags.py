from django import template
from trade.binanceExch.SymbolsData import SymbolsTFData


register = template.Library()

@register.inclusion_tag('trade/_include/_indexes_table.html')
def index_table():
    m15 = SymbolsTFData('15m').get_indexcoin_data('idxusdt')
    h1 = SymbolsTFData('1h').get_indexcoin_data('idxusdt')
    h4 = SymbolsTFData('4h').get_indexcoin_data('idxusdt')
    d1 = SymbolsTFData('1d').get_indexcoin_data('idxusdt')



    return {'idxusdt': {'m15': m15.get('idxusdt'),
                        'h1': h1.get('idxusdt'),
                        'h4': h4.get('idxusdt'),
                        'd1': d1.get('idxusdt')}}