# -*- coding: utf-8 -*-
"""Tools to build Columns HighCharts parameters."""
from . import HighchartsView


class HighchartsColumnView(HighchartsView):
    """Base Class to generate Column HighCharts configuration.

    Define at least title, y_unit, providers and get_data() to get started.
    """
    providers = {}
    chart_type = 'column'

    def get_y_axis(self):
        return {'min': getattr(self, 'yMin', 0),
                'title': self.get_y_title()}

    def get_y_title(self):
        """Return yAxis title."""
        subtitle = u'%s' % getattr(self, 'subtitle', '')
        return subtitle

    def get_y_unit(self):
        try:
            return self.y_unit
        except AttributeError:  # pragma: no cover
            raise NotImplementedError(  # pragma: no cover
                'Please define the yAxis unit (self.y_unit).')

    def get_tooltip(self):
        """Return tooltip configuration."""
        return {
            'headerFormat': '''
                <span style="font-size:10px">
                    {point.key}
                 </span>
                 <table>''',
            'pointFormat': '''
                     <tr>
                         <td style="color:{series.color};padding:0">
                             {series.name}:
                         </td>
                         <td style="padding:0">
                             <b>{point.y:.0f} %s</b>
                         </td>
                     </tr>''' % self.get_y_unit(),
            'footerFormat': '</table>',
            'shared': True,
            'useHTML': True
        }

    def get_plot_options(self):
        """Return plotOptions configuration."""
        options = super(HighchartsColumnView, self).get_plot_options()
        options.update({'column': {'pointPadding': 0.2, 'borderWidth': 0}})
        return options

    def get_series(self):
        """Generate HighCharts series from providers and data."""
        series = []
        data = self.get_data()
        providers = self.get_providers()
        for i, d in enumerate(data):
            series.append({'name': providers[i],
                           'data': d})
        return series

    def get_data(self):
        """Return a list of series [[25, 34, 0, 1, 50], ...]).

        In the same order as providers and with the same serie length
        of xAxis.
        """
        raise NotImplementedError(  # pragma: no cover
            'You should return a data list list. '
            '(i.e: [[25, 34, 0, 1, 50], ...]).')
