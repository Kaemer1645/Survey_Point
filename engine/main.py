#import qgis files
from qgis.PyQt.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
from qgis.PyQt import QtWidgets
from qgis.gui import QgsMapToolEmitPoint, QgsRubberBand
from qgis.core import QgsWkbTypes
from qgis.PyQt.QtGui import QColor

from SurveyPoint.ui.createPointsWindow import CreatePointsWindow
from SurveyPoint.ui.attributesWindow import AttributesWindow
from SurveyPoint.ui.databaseWindow import DatabaseWindow
        
class Create_points(QgsMapToolEmitPoint):
    def __init__(self, canvas):
        super(Create_points, self).__init__(canvas)
        self.points = QgsRubberBand(canvas, QgsWkbTypes.PointGeometry)
        

    def create_points_window(self):
        self.crt_pts_win = CreatePointsWindow()
        self.crt_pts_win.show()
    
    def canvasClicked(self,przycisk,punkt):
        print(przycisk,punkt)
        
    def deactivate(self):
        super(Create_points, self).deactivate()
        
    def canvasReleaseEvent(self, mouse_event):
        point = mouse_event.mapPoint()
        #print(point)
        dada = self.points.addPoint(point)
        #print(dada)
        self.points.setWidth(5)
        self.points.setIconSize(20)
        self.points.setIcon(QgsRubberBand.ICON_BOX)
        self.points.setColor(QColor('red'))
                

class Attributes:

    def __init__(self):
        pass
    def attributes_window(self):
        self.crt_attrs_win = AttributesWindow()
        self.crt_attrs_win.show()


class Database:

    def __init__(self):
        pass

    def database_window(self):
        self.crt_dtbs_win = DatabaseWindow()
        self.crt_dtbs_win.show()

    def create_database(self):
        pass
        
    def add_to_database(self):
        pass

    def delete_from_database(self):
        pass
    
