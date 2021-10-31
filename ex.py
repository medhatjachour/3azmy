"""PySide6 port of the line/bar example from Qt v5.x"""
"""
import sys
from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import (QBarCategoryAxis, QBarSeries, QBarSet, QChart,
                              QChartView, QLineSeries, QValueAxis)


class TestChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.set0 = QBarSet("Jane")
        self.set1 = QBarSet("John")
        self.set2 = QBarSet("Axel")
        self.set3 = QBarSet("Mary")
        self.set4 = QBarSet("Sam")

        self.set0.append([1, 2, 3, 4, 5, 6])
        self.set1.append([5, 0, 0, 4, 0, 7])
        self.set2.append([3, 5, 8, 13, 8, 5])
        self.set3.append([5, 6, 7, 3, 4, 5])
        self.set4.append([9, 7, 5, 3, 1, 2])

        self._bar_series = QBarSeries()
        self._bar_series.append(self.set0)
        self._bar_series.append(self.set1)
        self._bar_series.append(self.set2)
        self._bar_series.append(self.set3)
        self._bar_series.append(self.set4)

        #self._line_series = QLineSeries()
        #self._line_series.setName("trend")
        #self._line_series.append(QPoint(0, 4))
        #self._line_series.append(QPoint(1, 15))
        #self._line_series.append(QPoint(2, 20))
        #self._line_series.append(QPoint(3, 4))
        #self._line_series.append(QPoint(4, 12))
        #self._line_series.append(QPoint(5, 17))

        self.chart = QChart()
        self.chart.addSeries(self._bar_series)
        #self.chart.addSeries(self._line_series)
        #self.chart.setTitle("Line and barchart example")

        self.categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        self._axis_x = QBarCategoryAxis()
        self._axis_x.append(self.categories)
        #self.chart.setAxisX(self._axis_x, self._line_series)
        self.chart.setAxisX(self._axis_x, self._bar_series)
        self._axis_x.setRange("Jan", "Jun")

        self._axis_y = QValueAxis()
        #self.chart.setAxisY(self._axis_y, self._line_series)
        self.chart.setAxisY(self._axis_y, self._bar_series)
        self._axis_y.setRange(0, 20)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self._chart_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TestChart()
    window.show()
    window.resize(440, 300)

    sys.exit(app.exec())

import sys
from PySide6.QtCore import QPointF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import QChart, QChartView, QLineSeries


class TestChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.series = QLineSeries()
        self.series.append(0, 6)
        self.series.append(2, 4)
        self.series.append(3, 8)
        self.series.append(7, 4)
        self.series.append(10, 5)
        self.series.append(12, 6)
        self.series.append(14, 8)
        self.series.append(15, 6)
        self.series.append(16, 6)
        self.series.append(17, 5)
        #self.series.append(QPointF(11, 1))
        #self.series.append(QPointF(13, 3))
        #self.series.append(QPointF(17, 6))
        #self.series.append(QPointF(18, 3))
        #self.series.append(QPointF(20, 2))
        #self.series.append(QPointF(11, 1))
        #self.series.append(QPointF(13, 3))
        #self.series.append(QPointF(17, 6))
        #self.series.append(QPointF(18, 3))
        #self.series.append(QPointF(20, 2))

        self.chart = QChart()
        #self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Simple line chart example")

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self._chart_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TestChart()
    window.show()
    window.resize(440, 300)
    sys.exit(app.exec())

import sys
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QBrush, QColor, QPainter, QPen
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox,
    QFormLayout, QGridLayout, QGroupBox, QPushButton, QWidget)
from PySide6.QtCharts import QBarSeries, QBarSet, QChart, QChartView


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.chart = QChart()
        self.series = QBarSeries()

        self.main_layout = QGridLayout()
     
        # Create chart view with the chart
        self.chart_view = QChartView(self.chart, self)

        # Create layout for grid and detached legend
        self.main_layout.addWidget(self.chart_view, 0, 1, 3, 1)
        self.setLayout(self.main_layout)

        self.create_series()

    def create_series(self):
        self.add_barset()
        self.add_barset()
        self.add_barset()
        self.add_barset()
        self.add_barset()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Legend detach example")
        self.chart.createDefaultAxes()

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chart_view.setRenderHint(QPainter.Antialiasing)

    def show_legend_spinbox(self):
        self.legend_settings.setVisible(True)
        chart_viewrect = self.chart_view.rect()

        self.legend_posx.setMinimum(0)
        self.legend_posx.setMaximum(chart_viewrect.width())
        self.legend_posx.setValue(150)

        self.legend_posy.setMinimum(0)
        self.legend_posy.setMaximum(chart_viewrect.height())
        self.legend_posy.setValue(150)

        self.legend_width.setMinimum(0)
        self.legend_width.setMaximum(chart_viewrect.width())
        self.legend_width.setValue(150)

        self.legend_height.setMinimum(0)
        self.legend_height.setMaximum(chart_viewrect.height())
        self.legend_height.setValue(75)

    def hide_legend_spinbox(self):
        self.legend_settings.setVisible(False)

    def toggle_attached(self):
        legend = self.chart.legend()
        if legend.isAttachedToChart():
            legend.detachFromChart()
            legend.setBackgroundVisible(True)
            legend.setBrush(QBrush(QColor(128, 128, 128, 128)))
            legend.setPen(QPen(QColor(192, 192, 192, 192)))

            self.show_legend_spinbox()
            self.update_legend_layout()
        else:
            legend.attachToChart()
            legend.setBackgroundVisible(False)
            self.hide_legend_spinbox()
        self.update()

    def add_barset(self):
        series_count = self.series.count()
        bar_set = QBarSet(f"set {series_count}")
        delta = series_count * 0.1
        bar_set.append([1 + delta, 2 + delta, 3 + delta, 4 + delta])
        self.series.append(bar_set)

    def remove_barset(self):
        sets = self.series.barSets()
        len_sets = len(sets)
        if len_sets > 0:
            self.series.remove(sets[len_sets - 1])

    def set_legend_alignment(self):
        button = self.sender()
        legend = self.chart.legend()
        alignment = legend.alignment()

        if alignment == Qt.AlignTop:
            legend.setAlignment(Qt.AlignLeft)
            if button:
                button.setText("Align (Left)")
        elif alignment == Qt.AlignLeft:
            legend.setAlignment(Qt.AlignBottom)
            if button:
                button.setText("Align (Bottom)")
        elif alignment == Qt.AlignBottom:
            legend.setAlignment(Qt.AlignRight)
            if button:
                button.setText("Align (Right)")
        else:
            if button:
                button.setText("Align (Top)")
            legend.setAlignment(Qt.AlignTop)

    def toggle_bold(self):
        legend = self.chart.legend()
        font = legend.font()
        font.setBold(not font.bold())
        legend.setFont(font)

    def toggle_italic(self):
        legend = self.chart.legend()
        font = legend.font()
        font.setItalic(not font.italic())
        legend.setFont(font)

    def font_size_changed(self):
        legend = self.chart.legend()
        font = legend.font()
        font_size = self.font_size.value()
        if font_size < 1:
            font_size = 1
        font.setPointSizeF(font_size)
        legend.setFont(font)

    def update_legend_layout(self):
        legend = self.chart.legend()

        rect = QRectF(self.legend_posx.value(),
            self.legend_posy.value(),
            self.legend_width.value(),
            self.legend_height.value())
        legend.setGeometry(rect)

        legend.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWidget()
    available_geometry = w.screen().availableGeometry()
    size = available_geometry.height() * 0.75
    w.setFixedSize(size, size)
    w.show()
    sys.exit(app.exec())
    """
    #!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019/10/2
@author: Irony
@site: https://pyqt5.com , https://github.com/892768447
@email: 892768447@qq.com
@file: ChartThemes
@description: 图表主题动画等
"""
#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2012 Digia Plc
## All rights reserved.
##
## This file is part of the PyQtChart examples.
##
## $QT_BEGIN_LICENSE$
## Licensees holding valid Qt Commercial licenses may use this file in
## accordance with the Qt Commercial License Agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and Digia.
## $QT_END_LICENSE$
##
#############################################################################
"""

import random
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

from PySide6.QtCharts import *
import sys




class ThemeWidget(QWidget):

    def __init__(self, parent=None):
        super(ThemeWidget, self).__init__(parent)

        self.m_charts = []
        self.m_listCount = 3
        self.m_valueMax = 10
        self.m_valueCount = 7
        self.m_dataTable = self.generateRandomData(self.m_listCount,
                                                   self.m_valueMax, self.m_valueCount)
        self.m_themeComboBox = self.createThemeBox()
        self.m_antialiasCheckBox = QCheckBox("Anti-aliasing")
        self.m_animatedComboBox = self.createAnimationBox()
        self.m_legendComboBox = self.createLegendBox()

        self.connectSignals()

        # Create the layout.
        baseLayout = QGridLayout()
        settingsLayout = QHBoxLayout()
        settingsLayout.addWidget(QLabel("Theme:"))
        settingsLayout.addWidget(self.m_themeComboBox)
        settingsLayout.addWidget(QLabel("Animation:"))
        settingsLayout.addWidget(self.m_animatedComboBox)
        settingsLayout.addWidget(QLabel("Legend:"))
        settingsLayout.addWidget(self.m_legendComboBox)
        settingsLayout.addWidget(self.m_antialiasCheckBox)
        settingsLayout.addStretch()
        baseLayout.addLayout(settingsLayout, 0, 0, 1, 3)

        # Create the charts.
        chartView = QChartView(self.createAreaChart())
        baseLayout.addWidget(chartView, 1, 0)
        self.m_charts.append(chartView)

        chartView = QChartView(self.createBarChart(self.m_valueCount))
        baseLayout.addWidget(chartView, 1, 1)
        self.m_charts.append(chartView)

        chartView = QChartView(self.createLineChart())
        baseLayout.addWidget(chartView, 1, 2)
        self.m_charts.append(chartView)

        chartView = QChartView(self.createPieChart())
        # Funny things happen if the pie slice labels no not fit the screen...
        chartView.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        baseLayout.addWidget(chartView, 2, 0)
        self.m_charts.append(chartView)

        chartView = QChartView(self.createSplineChart())
        baseLayout.addWidget(chartView, 2, 1)
        self.m_charts.append(chartView)

        chartView = QChartView(self.createScatterChart())
        baseLayout.addWidget(chartView, 2, 2)
        self.m_charts.append(chartView)

        self.setLayout(baseLayout)

        # Set the defaults.
        self.m_antialiasCheckBox.setChecked(True)
        self.updateUI()

    def connectSignals(self):
        self.m_themeComboBox.currentIndexChanged.connect(self.updateUI)
        self.m_antialiasCheckBox.toggled.connect(self.updateUI)
        self.m_animatedComboBox.currentIndexChanged.connect(self.updateUI)
        self.m_legendComboBox.currentIndexChanged.connect(self.updateUI)

    def generateRandomData(self, listCount, valueMax, valueCount):
        random.seed()

        dataTable = []

        for i in range(listCount):
            dataList = []
            yValue = 0.0
            f_valueCount = float(valueCount)

            for j in range(valueCount):
                yValue += random.uniform(0, valueMax) / f_valueCount
                value = QPointF(
                    j + random.random() * self.m_valueMax / f_valueCount,
                    yValue)
                label = "Slice " + str(i) + ":" + str(j)
                dataList.append((value, label))

            dataTable.append(dataList)

        return dataTable

    def createThemeBox(self):
        themeComboBox = QComboBox()

        themeComboBox.addItem("Light", QChart.ChartThemeLight)
        themeComboBox.addItem("Blue Cerulean", QChart.ChartThemeBlueCerulean)
        themeComboBox.addItem("Dark", QChart.ChartThemeDark)
        themeComboBox.addItem("Brown Sand", QChart.ChartThemeBrownSand)
        themeComboBox.addItem("Blue NCS", QChart.ChartThemeBlueNcs)
        themeComboBox.addItem("High Contrast", QChart.ChartThemeHighContrast)
        themeComboBox.addItem("Blue Icy", QChart.ChartThemeBlueIcy)

        return themeComboBox

    def createAnimationBox(self):
        animationComboBox = QComboBox()

        animationComboBox.addItem("No Animations", QChart.NoAnimation)
        animationComboBox.addItem("GridAxis Animations", QChart.GridAxisAnimations)
        animationComboBox.addItem("Series Animations", QChart.SeriesAnimations)
        animationComboBox.addItem("All Animations", QChart.AllAnimations)

        return animationComboBox

    def createLegendBox(self):
        legendComboBox = QComboBox()

        legendComboBox.addItem("No Legend ", 0)
        legendComboBox.addItem("Legend Top", Qt.AlignTop)
        legendComboBox.addItem("Legend Bottom", Qt.AlignBottom)
        legendComboBox.addItem("Legend Left", Qt.AlignLeft)
        legendComboBox.addItem("Legend Right", Qt.AlignRight)

        return legendComboBox

    def createAreaChart(self):
        chart = QChart()
        chart.setTitle("Area chart")

        # The lower series is initialized to zero values.
        lowerSeries = None
        y_points = []

        for i, data_list in enumerate(self.m_dataTable):
            upperSeries = QLineSeries(chart)
            for j, (value, _) in enumerate(data_list):
                y = value.y()

                if lowerSeries is None:
                    upperSeries.append(QPointF(j, y))
                    y_points.append(y)
                else:
                    new_y = y_points[i] + y
                    upperSeries.append(QPointF(j, new_y))
                    y_points[j] += new_y

            area = QAreaSeries(upperSeries, lowerSeries)
            area.setName("Series " + str(i))
            chart.addSeries(area)
            lowerSeries = upperSeries

        chart.createDefaultAxes()

        return chart

    def createBarChart(self, valueCount):
        chart = QChart()
        chart.setTitle("Bar chart")

        series = QStackedBarSeries(chart)

        for i, data_list in enumerate(self.m_dataTable):
            set = QBarSet("Bar set " + str(i))
            for value, _ in data_list:
                set << value.y()

            series.append(set)

        chart.addSeries(series)
        chart.createDefaultAxes()

        return chart

    def createLineChart(self):
        chart = QChart()
        chart.setTitle("Line chart")

        for i, data_list in enumerate(self.m_dataTable):
            series = QLineSeries(chart)
            for value, _ in data_list:
                series.append(value)

            series.setName("Series " + str(i))
            chart.addSeries(series)

        chart.createDefaultAxes()

        return chart

    def createPieChart(self):
        chart = QChart()
        chart.setTitle("Pie chart")

        pieSize = 1.0 / len(self.m_dataTable)

        for i, data_list in enumerate(self.m_dataTable):
            series = QPieSeries(chart)
            for value, label in data_list:
                slice = series.append(label, value.y())
                if len(series) == 1:
                    slice.setLabelVisible()
                    slice.setExploded()

            hPos = (pieSize / 2) + (i / float(len(self.m_dataTable)))
            series.setPieSize(pieSize)
            series.setHorizontalPosition(hPos)
            series.setVerticalPosition(0.5)

            chart.addSeries(series)

        return chart

    def createSplineChart(self):
        chart = QChart()
        chart.setTitle("Spline chart")

        for i, data_list in enumerate(self.m_dataTable):
            series = QSplineSeries(chart)
            for value, _ in data_list:
                series.append(value)

            series.setName("Series " + str(i))
            chart.addSeries(series)

        chart.createDefaultAxes()

        return chart

    def createScatterChart(self):
        chart = QChart()
        chart.setTitle("Scatter chart")

        for i, data_list in enumerate(self.m_dataTable):
            series = QScatterSeries(chart)
            for value, _ in data_list:
                series.append(value)

            series.setName("Series " + str(i))
            chart.addSeries(series)

        chart.createDefaultAxes()

        return chart

    @pyqtSlot()
    def updateUI(self):
        theme = self.m_themeComboBox.itemData(
            self.m_themeComboBox.currentIndex())

        if self.m_charts[0].chart().theme() != theme:
            for chartView in self.m_charts:
                chartView.chart().setTheme(theme)

            pal = self.window().palette()

            if theme == QChart.ChartThemeLight:
                pal.setColor(QPalette.Window, QColor(0xf0f0f0))
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif theme == QChart.ChartThemeDark:
                pal.setColor(QPalette.Window, QColor(0x121218))
                pal.setColor(QPalette.WindowText, QColor(0xd6d6d6))
            elif theme == QChart.ChartThemeBlueCerulean:
                pal.setColor(QPalette.Window, QColor(0x40434a))
                pal.setColor(QPalette.WindowText, QColor(0xd6d6d6))
            elif theme == QChart.ChartThemeBrownSand:
                pal.setColor(QPalette.Window, QColor(0x9e8965))
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif theme == QChart.ChartThemeBlueNcs:
                pal.setColor(QPalette.Window, QColor(0x018bba))
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif theme == QChart.ChartThemeHighContrast:
                pal.setColor(QPalette.Window, QColor(0xffab03))
                pal.setColor(QPalette.WindowText, QColor(0x181818))
            elif theme == QChart.ChartThemeBlueIcy:
                pal.setColor(QPalette.Window, QColor(0xcee7f0))
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            else:
                pal.setColor(QPalette.Window, QColor(0xf0f0f0))
                pal.setColor(QPalette.WindowText, QColor(0x404044))

            self.window().setPalette(pal)

        checked = self.m_antialiasCheckBox.isChecked()
        for chartView in self.m_charts:
            chartView.setRenderHint(QPainter.Antialiasing, checked)

        options = QChart.AnimationOptions(
            self.m_animatedComboBox.itemData(
                self.m_animatedComboBox.currentIndex()))

        if self.m_charts[0].chart().animationOptions() != options:
            for chartView in self.m_charts:
                chartView.chart().setAnimationOptions(options)

        alignment = self.m_legendComboBox.itemData(
            self.m_legendComboBox.currentIndex())

        for chartView in self.m_charts:
            legend = chartView.chart().legend()

            if alignment == 0:
                legend.hide()
            else:
                legend.setAlignment(Qt.Alignment(alignment))
                legend.show()


if __name__ == '__main__':
    import sys

    from PyQt5.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)

    window = QMainWindow()
    widget = ThemeWidget()
    window.setCentralWidget(widget)
    window.resize(900, 600)
    window.show()

    sys.exit(app.exec_())
    """
    #!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017年12月23日
@author: Irony."[讽刺]
@site: https://pyqt5.com , https://github.com/892768447
@email: 892768447@qq.com
@file: ToolTip
@description: 
'''
import sys

# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

from PySide6.QtCharts import *
import sys
__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2017 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

'''
class CircleWidget(QGraphicsProxyWidget):

    def __init__(self, color, *args, **kwargs):
        super(CircleWidget, self).__init__(*args, **kwargs)
        label = QLabel()
        label.setMinimumSize(12, 12)
        label.setMaximumSize(12, 12)
        label.setStyleSheet(
            "border:1px solid green;border-radius:6px;background: %s;" % color)
        self.setWidget(label)


class TextWidget(QGraphicsProxyWidget):

    def __init__(self, text, *args, **kwargs):
        super(TextWidget, self).__init__(*args, **kwargs)
        self.setWidget(QLabel(text, styleSheet="color:white;"))


class GraphicsWidget(QGraphicsWidget):

    def __init__(self, *args, **kwargs):
        super(GraphicsWidget, self).__init__(*args, **kwargs)
        self.setFlags(self.ItemClipsChildrenToShape)
        self.setZValue(999)
        layout = QGraphicsGridLayout(self)
        for row in range(6):
            layout.addItem(CircleWidget("red"), row, 0)
            layout.addItem(TextWidget("red"), row, 1)
        self.hide()

    def show(self, pos):
        self.setGeometry(pos.x(), pos.y(), self.size().width(),
                         self.size().height())
        super(GraphicsWidget, self).show()
'''


#class ToolTipItem(QWidget):

    #def __init__(self, color, text, parent=None):
        #super(ToolTipItem, self).__init__(parent)
        #layout = QHBoxLayout(self)
        #layout.setContentsMargins(0, 0, 0, 0)
        #clabel = QLabel(self)
        #clabel.setMinimumSize(12, 12)
        #clabel.setMaximumSize(12, 12)
        #clabel.setStyleSheet("border-radius:6px;background: rgba(%s,%s,%s,%s);" % (
            #color.red(), color.green(), color.blue(), color.alpha()))
        #layout.addWidget(clabel)
        #self.textLabel = QLabel(text, self, styleSheet="color:white;")
        #layout.addWidget(self.textLabel)

    #def setText(self, text):
        #self.textLabel.setText(text)

"""
class ToolTipWidget(QWidget):
    Cache = {}

    def __init__(self, *args, **kwargs):
        super(ToolTipWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            "ToolTipWidget{background: rgba(50,50,50,70);}")
        layout = QVBoxLayout(self)
        self.titleLabel = QLabel(self, styleSheet="color:white;")
        layout.addWidget(self.titleLabel)

    #def updateUi(self, title, points):
        #self.titleLabel.setText(title)
        #for serie, point in points:
            #self.Cache[serie].setText(
                #(serie.name() or "-") + ":" + str(point.y()))
            #if serie not in self.Cache:
                #pass
                #item = ToolTipItem(
                    #serie.color(),
                    #(serie.name() or "-") + ":" + str(point.y()), self)
                #self.layout().addWidget(item)
                #self.Cache[serie] = item
            #else:
                #pass
                #self.Cache[serie].setText(
                    #(serie.name() or "-") + ":" + str(point.y()))

"""
#class GraphicsProxyWidget(QGraphicsProxyWidget):

    #def __init__(self, *args, **kwargs):
        #super(GraphicsProxyWidget, self).__init__(*args, **kwargs)
        #self.setZValue(999)
        #self.tipWidget = ToolTipWidget()
        #self.setWidget(self.tipWidget)
        #self.hide()

    #def show(self, title, points, pos):
        #self.setGeometry(QRectF(pos, self.size()))
        #self.tipWidget.updateUi(title, points)
        #super(GraphicsProxyWidget, self).show()


class ChartView(QChartView):

    def __init__(self, *args, **kwargs):
        super(ChartView, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.initChart()

        #self.toolTipWidget = GraphicsProxyWidget(self._chart)

        # line
        #self.lineItem = QGraphicsLineItem(self._chart)
        #self.lineItem.setZValue(998)
        #self.lineItem.hide()

        # 一些固定计算，减少mouseMoveEvent中的计算量
        # 获取x和y轴的最小最大值
        axisX, axisY = self._chart.axisX(), self._chart.axisY()
        self.min_x, self.max_x = axisX.min(), axisX.max()
        self.min_y, self.max_y = axisY.min(), axisY.max()
        # 坐标系中左上角顶点
        self.point_top = self._chart.mapToPosition(
            QPointF(self.min_x, self.max_y))
        # 坐标原点坐标
        self.point_bottom = self._chart.mapToPosition(
            QPointF(self.min_x, self.min_y))
        self.step_x = (self.max_x - self.min_x) / (axisX.tickCount() - 1)

    #         self.step_y = (self.max_y - self.min_y) / (axisY.tickCount() - 1)

    def mouseMoveEvent(self, event):
        super(ChartView, self).mouseMoveEvent(event)
        # 把鼠标位置所在点转换为对应的xy值
        x = self._chart.mapToValue(event.pos()).x()
        y = self._chart.mapToValue(event.pos()).y()
        index = round((x - self.min_x) / self.step_x)
        pos_x = self._chart.mapToPosition(
            QPointF(index * self.step_x + self.min_x, self.min_y))
        #         print(x, pos_x, index, index * self.step_x + self.min_x)
        # 得到在坐标系中的所有series的类型和点
        points = [(serie, serie.at(index))
                  for serie in self._chart.series() if self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y]
        if points:
            pass
            # 永远在轴上的黑线条
            #self.lineItem.setLine(pos_x.x(), self.point_top.y(),
            #                      pos_x.x(), self.point_bottom.y())
            #self.lineItem.show()
            #self.toolTipWidget.show("", points, event.pos() + QPoint(20, 20))
        else:
            pass
            #self.toolTipWidget.hide()
            #self.lineItem.hide()

    def onSeriesHoverd(self, point, state):
        if state:
            try:
                name = self.sender().name()
            except:
                name = ""
            QToolTip.showText(QCursor.pos(), "%s\nx: %s\ny: %s" %
                              (name, point.x(), point.y()))

    def initChart(self):
        self._chart = QChart(title="Line Chart")
        self._chart.setAcceptHoverEvents(True)
        dataTable = [
            [120, 132, 101, 134, 90, 230, 210],
            [220, 182, 191, 234, 290, 330, 310],
            [150, 232, 201, 154, 190, 330, 410],
            [320, 332, 301, 334, 390, 330, 320],
            [820, 932, 901, 934, 1290, 1330, 1320]
        ]
        for i, data_list in enumerate(dataTable):
            series = QLineSeries(self._chart)
            for j, v in enumerate(data_list):
                series.append(j, v)
            series.setName("Series " + str(i))
            series.setPointsVisible(True)  # 显示原点
            series.hovered.connect(self.onSeriesHoverd)
            self._chart.addSeries(series)
        self._chart.createDefaultAxes()  # 创建默认的轴
        self._chart.axisX().setTickCount(7)  # x轴设置7个刻度
        self._chart.axisY().setTickCount(7)  # y轴设置7个刻度
        self._chart.axisY().setRange(0, 1500)  # 设置y轴范围
        self.setChart(self._chart)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""QToolTip {
        border: none;
        padding: 5px;
        color: white;
        background: rgb(50,50,50);
        opacity: 100;
            }""")
    view = ChartView()
    view.show()
    sys.exit(app.exec_())

"""

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QChart {{
    border: none;
    color: {_color};
    background-color: {_bg_color};
}}
QLineSeries {{
    border: none;
    color: {_color};
    background-color: {_bg_color};
}}
'''

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyLineChart(QWidget):
    def __init__(
        self, 
        color= "#343b48",
        bg_color = "#343b48",
        line_color = "#cd1234"
    ):
        super().__init__()
        self.chart = QChart()
        self.series = QSplineSeries()
        
        
        self.main_layout = QGridLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        # Create chart view with the chart
        self.chart_view = QChartView(self.chart, self)
        self.chart_view.setContentsMargins(0,0,0,0)
        self.chart_view.setStyleSheet("background-color: transparent;\n")
        self.chart.setBackgroundBrush(QBrush(QColor("transparent"))) 
        
        self.series.setColor(QColor(line_color))
        self.main_layout.addWidget(self.chart_view, 0, 1, 3, 1)
        self.setLayout(self.main_layout)

        self.create_series(line_color)
        # SET STYLESHEET
        self.set_stylesheet(
            color,
            bg_color,
        )


    def create_series(self,line_color):
        self.add_barset()
        self.chart.addSeries(self.series)
        #self.chart.setTitle("Legend detach example")
        self.chart.createDefaultAxes()
        self.setStyleSheet("background-color: transparent;\n")

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        brush = QBrush(QColor(line_color))
        pen = QPen(brush,2)
        pen.setWidth(3);
        self.series.setPen(pen);
        #self.chart_view.setRenderHint(QPainter.Antialiasing)

    def add_barset(self):

        self.series.append(0, 1)
        self.series.append(2, 4)
        self.series.append(3, 2)
        self.series.append(5, 5)
        self.series.append(6, 3)
        

    # SET STYLESHEET
    def set_stylesheet(
        self,
        color,
        bg_color,
    ):
        # APPLY STYLESHEET
        style_format = style.format(    
            _color = color,
            _bg_color = bg_color,
        )
        self.setStyleSheet(style_format)
"""
